#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from collections import deque
from dataclasses import dataclass
from datetime import UTC, datetime
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen


USER_AGENT = "CloudRavenKnowledgeCollector/0.1 (+https://cloudraven.io)"
ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "knowledgebase" / "manifests" / "collection-targets.json"
STORE_ROOT = ROOT / "knowledgebase" / "store"
URL_MANIFEST_JSON = ROOT / "knowledgebase" / "manifests" / "url-manifest.json"
URL_MANIFEST_MD = ROOT / "knowledgebase" / "manifests" / "url-manifest.md"
SECRET_PATTERNS = (
    re.compile(r"\b(?:sk|pk|rk)_(?:test|live)_[A-Za-z0-9.]+\b"),
    re.compile(r"\b(?:sk|pk|rk)_(?:test|live)_"),
)


@dataclass
class PageResult:
    url: str
    title: str
    text: str
    links: list[str]
    slug: str
    status: int
    fetched_at: str
    raw_html_path: str
    extracted_path: str
    enriched_path: str


class DocHTMLParser(HTMLParser):
    SKIP_TAGS = {"script", "style", "noscript", "svg", "nav", "header", "footer", "aside"}
    BLOCK_TAGS = {
        "article",
        "section",
        "div",
        "p",
        "ul",
        "ol",
        "li",
        "main",
        "br",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "pre",
        "code",
    }

    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.links: list[str] = []
        self.skip_depth = 0
        self.current_tag_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.current_tag_stack.append(tag)
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
        if tag == "a" and not self.skip_depth:
            href = dict(attrs).get("href")
            if href:
                absolute = normalize_url(urljoin(self.base_url, href))
                if absolute:
                    self.links.append(absolute)
        if tag in self.BLOCK_TAGS and not self.skip_depth:
            self.text_parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
        if self.current_tag_stack:
            self.current_tag_stack.pop()
        if tag in self.BLOCK_TAGS and not self.skip_depth:
            self.text_parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = collapse_whitespace(unescape(data))
        if not text:
            return
        if self.current_tag_stack and self.current_tag_stack[-1] == "title":
            self.title_parts.append(text)
        self.text_parts.append(text)


def collapse_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def redact_secrets(value: str) -> str:
    redacted = value
    for pattern in SECRET_PATTERNS:
        redacted = pattern.sub("[REDACTED_SECRET]", redacted)
    return redacted


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return ""
    cleaned = parsed._replace(fragment="")
    path = re.sub(r"/{2,}", "/", cleaned.path or "/")
    return urlunparse((cleaned.scheme, cleaned.netloc, path, "", cleaned.query, ""))


def sanitize_name(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "page"


def slug_for_url(url: str) -> str:
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    core = "-".join(parts[-3:]) if parts else "index"
    if parsed.query:
        core = f"{core}-{sanitize_name(parsed.query)}"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{sanitize_name(core)}-{digest}"


def raw_extension(content_type: str, url: str) -> str:
    if content_type.startswith("text/plain") or urlparse(url).path.endswith(".txt"):
        return ".txt"
    return ".html"


def extract_links_from_text(base_url: str, text: str) -> list[str]:
    pattern = re.compile(r"https?://[^\s<>()]+")
    links = []
    seen = set()
    for match in pattern.findall(text):
        candidate = normalize_url(match.rstrip(".,;:!?"))
        if candidate and candidate not in seen:
            links.append(candidate)
            seen.add(candidate)
    return links


def title_from_text(text: str, fallback: str) -> str:
    for line in text.splitlines():
        cleaned = collapse_whitespace(line)
        if cleaned:
            return cleaned[:160]
    return fallback


def fetch_url(url: str, timeout: int) -> tuple[int, str, str]:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,text/plain,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        status = getattr(response, "status", 200)
        charset = response.headers.get_content_charset() or "utf-8"
        content_type = response.headers.get_content_type() or "text/html"
        payload = response.read().decode(charset, errors="replace")
        return status, payload, content_type


def parse_html(base_url: str, html_text: str) -> tuple[str, str, list[str]]:
    parser = DocHTMLParser(base_url)
    parser.feed(html_text)
    title = collapse_whitespace(" ".join(parser.title_parts))
    lines = []
    for line in "\n".join(parser.text_parts).splitlines():
        cleaned = collapse_whitespace(line)
        if cleaned:
            lines.append(cleaned)
    text = "\n\n".join(lines)
    links = []
    seen = set()
    for link in parser.links:
        if link not in seen:
            links.append(link)
            seen.add(link)
    return title, text, links


def parse_payload(base_url: str, payload: str, content_type: str, fallback_title: str) -> tuple[str, str, list[str]]:
    if content_type.startswith("text/plain") or urlparse(base_url).path.endswith(".txt"):
        lines = []
        for line in payload.splitlines():
            cleaned = collapse_whitespace(line)
            if cleaned:
                lines.append(cleaned)
        text = "\n\n".join(lines)
        title = title_from_text(text, fallback_title)
        links = extract_links_from_text(base_url, text)
        return title, text, links
    return parse_html(base_url, payload)


def allowed(url: str, target: dict) -> bool:
    parsed = urlparse(url)
    if not parsed.netloc:
        return False
    allowed_domains = target.get("allowed_domains", [])
    if allowed_domains and parsed.netloc not in allowed_domains:
        return False
    allow_prefixes = target.get("allow_prefixes", [])
    if allow_prefixes and not any(url.startswith(prefix) for prefix in allow_prefixes):
        return False
    deny_regexes = target.get("deny_regexes", [])
    if any(re.search(pattern, url) for pattern in deny_regexes):
        return False
    return True


def sentence_summary(text: str, limit: int = 5) -> list[str]:
    cleaned = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+", cleaned)
    bullets = []
    for part in parts:
        candidate = part.strip()
        if len(candidate) < 40:
            continue
        bullets.append(candidate)
        if len(bullets) >= limit:
            break
    return bullets


def excerpt(text: str, max_chars: int = 700) -> str:
    short = text[:max_chars].strip()
    if len(text) > max_chars:
        return f"{short}..."
    return short


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|")


def page_markdown(target: dict, page: PageResult) -> str:
    direct_links = "\n".join(f"- {link}" for link in page.links[:20]) or "- None discovered in scope."
    summary_points = sentence_summary(page.text) or [excerpt(page.text, 350)]
    summary = "\n".join(f"- {point}" for point in summary_points)
    title = page.title or target["name"]
    return f"""---
title: {title}
source_url: {page.url}
target_id: {target["id"]}
dependency: {target["name"]}
collected_at: {page.fetched_at}
kind: extracted-doc
---

# {title}

Source URL:

- {page.url}

Dependency:

- {target["name"]}

Collected at:

- {page.fetched_at}

Direct links in scope:

{direct_links}

Captured summary:

{summary}

Extracted text:

{page.text}
"""


def enriched_markdown(target: dict, page: PageResult) -> str:
    examples = "\n".join(f"- {item}" for item in target.get("cloudraven_examples", []))
    review = "\n".join(f"- {item}" for item in target.get("applicability_review", []))
    query_tags = "\n".join(f"- `{tag}`" for tag in target.get("tags", []))
    summary_points = sentence_summary(page.text, limit=4) or [excerpt(page.text, 350)]
    summary = "\n".join(f"- {point}" for point in summary_points)
    title = f"{page.title or target['name']} | CloudRaven Enrichment"
    tags = ", ".join(target.get("tags", []))
    return f"""---
title: {title}
source_url: {page.url}
target_id: {target["id"]}
dependency: {target["name"]}
collected_at: {page.fetched_at}
kind: enriched-doc
tags: {tags}
---

# {title}

Source URL:

- {page.url}

Dependency:

- {target["name"]}

Collection scope:

- {target.get("scope_note", "")}

What this page is useful for:

{summary}

CloudRaven applicability:

- {target.get("cloudraven_focus", "")}

Prototype-to-production review:

{review}

CloudRaven example paths:

{examples}

Suggested retrieval tags:

{query_tags}

Local artifact references:

- Extracted page: `{page.extracted_path}`
- Raw source: `{page.raw_html_path}`
"""


def manifest_markdown(manifest: dict) -> str:
    lines = [
        "# URL Manifest",
        "",
        f"Generated at: `{manifest['generated_at']}`",
        "",
    ]
    for target in manifest["targets"]:
        lines.extend(
            [
                f"## {target['name']}",
                "",
                f"- Target ID: `{target['target_id']}`",
                f"- Collected pages: `{target['collected_pages']}`",
                "",
                "| Title | URL | Extracted | Enriched |",
                "| --- | --- | --- | --- |",
            ]
        )
        for page in target["pages"]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        markdown_escape(page["title"] or target["name"]),
                        markdown_escape(page["url"]),
                        markdown_escape(page["extracted_path"]),
                        markdown_escape(page["enriched_path"]),
                    ]
                )
                + " |"
            )
        lines.append("")
    return "\n".join(lines)


def collect_target(target: dict, timeout: int, sleep_seconds: float) -> dict:
    queue = deque((normalize_url(url), 0) for url in target["seed_urls"])
    seen = set()
    pages: list[PageResult] = []
    max_depth = int(target.get("max_depth", 1))
    max_pages = int(target.get("max_pages", 10))

    while queue and len(pages) < max_pages:
        url, depth = queue.popleft()
        if not url or url in seen or not allowed(url, target):
            continue
        seen.add(url)
        try:
            status, payload, content_type = fetch_url(url, timeout=timeout)
        except HTTPError as exc:
            print(f"[warn] {target['id']}: HTTP {exc.code} for {url}", file=sys.stderr)
            continue
        except URLError as exc:
            raise RuntimeError(f"Network error while fetching {url}: {exc}") from exc

        payload = redact_secrets(payload)
        title, text, links = parse_payload(url, payload, content_type, target["name"])
        title = redact_secrets(title)
        text = redact_secrets(text)
        slug = slug_for_url(url)
        fetched_at = datetime.now(UTC).isoformat()
        raw_suffix = raw_extension(content_type, url)

        raw_html_path = STORE_ROOT / "raw_html" / target["id"] / f"{slug}{raw_suffix}"
        extracted_path = STORE_ROOT / "extracted" / target["id"] / f"{slug}.md"
        enriched_path = STORE_ROOT / "enriched" / target["id"] / f"{slug}.md"

        page = PageResult(
            url=url,
            title=title,
            text=text,
            links=[link for link in links if allowed(link, target)],
            slug=slug,
            status=status,
            fetched_at=fetched_at,
            raw_html_path=str(raw_html_path.relative_to(ROOT)),
            extracted_path=str(extracted_path.relative_to(ROOT)),
            enriched_path=str(enriched_path.relative_to(ROOT)),
        )

        write_text(raw_html_path, payload)
        write_text(extracted_path, page_markdown(target, page))
        write_text(enriched_path, enriched_markdown(target, page))
        pages.append(page)

        if depth < max_depth:
            for link in page.links:
                if link not in seen:
                    queue.append((link, depth + 1))
        if sleep_seconds:
            time.sleep(sleep_seconds)

    return {
        "target_id": target["id"],
        "name": target["name"],
        "collected_pages": len(pages),
        "pages": [
            {
                "url": page.url,
                "title": page.title,
                "slug": page.slug,
                "status": page.status,
                "fetched_at": page.fetched_at,
                "raw_html_path": page.raw_html_path,
                "extracted_path": page.extracted_path,
                "enriched_path": page.enriched_path,
            }
            for page in pages
        ],
    }


def load_targets(selected: set[str] | None) -> list[dict]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    targets = data["targets"]
    if not selected:
        return targets
    return [target for target in targets if target["id"] in selected]


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect official docs into the local knowledge store.")
    parser.add_argument("--targets", help="Comma-separated target IDs to collect.")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--sleep-seconds", type=float, default=0.2)
    args = parser.parse_args()

    selected = {item.strip() for item in args.targets.split(",")} if args.targets else None
    targets = load_targets(selected)
    if not targets:
        print("No matching targets found.", file=sys.stderr)
        return 1

    manifest = {
        "generated_at": datetime.now(UTC).isoformat(),
        "targets": [],
    }

    for target in targets:
        print(f"[collect] {target['id']}")
        manifest["targets"].append(collect_target(target, timeout=args.timeout, sleep_seconds=args.sleep_seconds))

    write_text(URL_MANIFEST_JSON, json.dumps(manifest, indent=2))
    write_text(URL_MANIFEST_MD, manifest_markdown(manifest))
    print(f"[done] wrote {URL_MANIFEST_JSON.relative_to(ROOT)} and {URL_MANIFEST_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
