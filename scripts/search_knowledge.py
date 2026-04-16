#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import math
import re
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INDEX_DB = ROOT / "knowledgebase" / "index" / "knowledge.db"
TFIDF_INDEX = ROOT / "knowledgebase" / "index" / "tfidf-index.json"
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
    "with",
}


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9][a-z0-9_-]{1,}", text.lower())
    return [token for token in tokens if token not in STOPWORDS]


def build_query_vector(query: str, idf: dict[str, float]) -> dict[str, float]:
    counts = Counter(tokenize(query))
    weighted = {term: counts[term] * idf.get(term, 1.0) for term in counts}
    norm = math.sqrt(sum(value * value for value in weighted.values())) or 1.0
    return {term: value / norm for term, value in weighted.items()}


def cosine(left: dict[str, float], right: dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    if len(left) > len(right):
        left, right = right, left
    return sum(value * right.get(term, 0.0) for term, value in left.items())


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the local CloudRaven knowledge index.")
    parser.add_argument("query")
    parser.add_argument("--top-k", type=int, default=8)
    args = parser.parse_args()

    tfidf_index = json.loads(TFIDF_INDEX.read_text(encoding="utf-8"))
    query_vector = build_query_vector(args.query, tfidf_index["idf"])

    vector_scores = {}
    for chunk in tfidf_index["chunks"]:
        score = cosine(query_vector, chunk["vector"])
        if score > 0:
            vector_scores[chunk["chunk_id"]] = score

    connection = sqlite3.connect(INDEX_DB)
    terms = tokenize(args.query)
    match_query = " OR ".join(terms) if terms else args.query
    rows = connection.execute(
        """
        SELECT chunk_id, title, heading, path, snippet(chunk_fts, 2, '[', ']', '...', 18), bm25(chunk_fts)
        FROM chunk_fts
        WHERE chunk_fts MATCH ?
        LIMIT 25
        """,
        (match_query,),
    ).fetchall()
    connection.close()

    combined = {}
    for chunk_id, title, heading, path, snippet_text, bm25_score in rows:
        combined[chunk_id] = {
            "title": title,
            "heading": heading,
            "path": path,
            "snippet": snippet_text,
            "fts_score": 1.0 / (1.0 + max(bm25_score, 0.0)),
            "vector_score": vector_scores.get(chunk_id, 0.0),
        }

    for chunk in tfidf_index["chunks"]:
        chunk_id = chunk["chunk_id"]
        if chunk_id not in combined and chunk_id in vector_scores:
            combined[chunk_id] = {
                "title": chunk["title"],
                "heading": chunk["heading"],
                "path": chunk["path"],
                "snippet": chunk["preview"],
                "fts_score": 0.0,
                "vector_score": vector_scores[chunk_id],
            }

    ranked = sorted(
        combined.values(),
        key=lambda item: (item["vector_score"] * 0.65) + (item["fts_score"] * 0.35),
        reverse=True,
    )[: args.top_k]

    for index, item in enumerate(ranked, start=1):
        total_score = (item["vector_score"] * 0.65) + (item["fts_score"] * 0.35)
        print(f"{index}. {item['title']} :: {item['heading']}")
        print(f"   score={total_score:.4f} path={item['path']}")
        print(f"   {item['snippet']}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
