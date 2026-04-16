#!/usr/bin/env python3

from __future__ import annotations

import json
import math
import re
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGEBASE = ROOT / "knowledgebase"
INDEX_DB = KNOWLEDGEBASE / "index" / "knowledge.db"
TFIDF_INDEX = KNOWLEDGEBASE / "index" / "tfidf-index.json"
SECRET_PATTERNS = (
    re.compile(r"\b(?:sk|pk|rk)_(?:test|live)_[A-Za-z0-9.]+\b"),
    re.compile(r"\b(?:sk|pk|rk)_(?:test|live)_"),
    re.compile(r"\beyJ[A-Za-z0-9+/_=-]{10,}\.[A-Za-z0-9+/_=-]{10,}\.[A-Za-z0-9+/_=-]{10,}\b"),
)

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "use",
    "with",
    "you",
    "your",
}


def read_frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    metadata = {}
    body_start = 1
    for index in range(1, len(lines)):
        line = lines[index]
        if line.strip() == "---":
            body_start = index + 1
            break
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()
    return metadata, "\n".join(lines[body_start:])


def redact_secrets(value: str) -> str:
    redacted = value
    for pattern in SECRET_PATTERNS:
        redacted = pattern.sub("[REDACTED_SECRET]", redacted)
    return redacted


def markdown_files() -> list[Path]:
    files = []
    for path in KNOWLEDGEBASE.rglob("*.md"):
        if "/templates/" in path.as_posix():
            continue
        files.append(path)
    return sorted(files)


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9][a-z0-9_-]{1,}", text.lower())
    return [token for token in tokens if token not in STOPWORDS]


def chunk_markdown(path: Path, text: str) -> list[dict]:
    metadata, body = read_frontmatter(text)
    title = metadata.get("title") or path.stem.replace("-", " ").title()
    sections = []
    current_heading = title
    buffer: list[str] = []

    def flush() -> None:
        if not buffer:
            return
        content = "\n".join(buffer).strip()
        if content:
            sections.append(
                {
                    "heading": current_heading,
                    "content": content,
                    "metadata": metadata,
                }
            )
        buffer.clear()

    for line in body.splitlines():
        if line.startswith("#"):
            flush()
            current_heading = line.lstrip("#").strip() or current_heading
            continue
        buffer.append(line)
        if sum(len(item) for item in buffer) > 1600:
            flush()
    flush()
    if not sections:
        sections.append({"heading": title, "content": body, "metadata": metadata})
    return sections


def kind_for_path(path: Path) -> str:
    posix = path.as_posix()
    if "/store/extracted/" in posix:
        return "extracted-doc"
    if "/store/enriched/" in posix:
        return "enriched-doc"
    if "/dependencies/" in posix:
        return "dependency-brief"
    if path.name == "dependency-manifest.md":
        return "manifest"
    return "knowledge-note"


def init_db(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        DROP TABLE IF EXISTS documents;
        DROP TABLE IF EXISTS chunks;
        DROP TABLE IF EXISTS chunk_fts;

        CREATE TABLE documents (
            id INTEGER PRIMARY KEY,
            path TEXT UNIQUE NOT NULL,
            title TEXT,
            kind TEXT,
            source_url TEXT
        );

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            document_id INTEGER NOT NULL,
            chunk_index INTEGER NOT NULL,
            heading TEXT,
            content TEXT,
            path TEXT,
            source_url TEXT,
            FOREIGN KEY(document_id) REFERENCES documents(id)
        );

        CREATE VIRTUAL TABLE chunk_fts USING fts5(
            chunk_id UNINDEXED,
            title,
            heading,
            content,
            path
        );
        """
    )


def build() -> None:
    INDEX_DB.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(INDEX_DB)
    init_db(connection)

    chunk_rows = []
    tf_chunks = []

    for path in markdown_files():
        text = redact_secrets(path.read_text(encoding="utf-8"))
        sections = chunk_markdown(path, text)
        source_url = sections[0]["metadata"].get("source_url", "") if sections else ""
        document_title = sections[0]["metadata"].get("title") or (sections[0]["heading"] if sections else path.stem)

        cursor = connection.execute(
            "INSERT INTO documents(path, title, kind, source_url) VALUES (?, ?, ?, ?)",
            (str(path.relative_to(ROOT)), document_title, kind_for_path(path), source_url),
        )
        document_id = cursor.lastrowid

        for index, section in enumerate(sections):
            content = section["content"].strip()
            if not content:
                continue
            cursor = connection.execute(
                """
                INSERT INTO chunks(document_id, chunk_index, heading, content, path, source_url)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    document_id,
                    index,
                    section["heading"],
                    content,
                    str(path.relative_to(ROOT)),
                    source_url,
                ),
            )
            chunk_id = cursor.lastrowid
            connection.execute(
                "INSERT INTO chunk_fts(chunk_id, title, heading, content, path) VALUES (?, ?, ?, ?, ?)",
                (chunk_id, document_title, section["heading"], content, str(path.relative_to(ROOT))),
            )
            chunk_rows.append(
                {
                    "chunk_id": chunk_id,
                    "path": str(path.relative_to(ROOT)),
                    "title": document_title,
                    "heading": section["heading"],
                    "content": content,
                }
            )

    connection.commit()
    connection.close()

    document_frequency = Counter()
    term_frequencies = []
    for row in chunk_rows:
        tokens = tokenize(f"{row['title']} {row['heading']} {row['content']}")
        counts = Counter(tokens)
        term_frequencies.append(counts)
        document_frequency.update(counts.keys())

    total_chunks = len(chunk_rows) or 1
    idf = {
        term: math.log((1 + total_chunks) / (1 + frequency)) + 1.0
        for term, frequency in document_frequency.items()
        if frequency < total_chunks
    }

    for row, counts in zip(chunk_rows, term_frequencies):
        weighted = {term: counts[term] * idf[term] for term in counts if term in idf}
        norm = math.sqrt(sum(value * value for value in weighted.values())) or 1.0
        top_terms = sorted(weighted.items(), key=lambda item: item[1], reverse=True)[:64]
        row["vector"] = {term: round(value / norm, 6) for term, value in top_terms}
        row["preview"] = row["content"][:240].strip().replace("\n", " ")
        row.pop("content")

    TFIDF_INDEX.write_text(
        json.dumps({"chunk_count": len(chunk_rows), "idf": idf, "chunks": chunk_rows}, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    build()
