#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

import build_search_index


ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGEBASE = ROOT / "knowledgebase"
MANIFEST_PATH = KNOWLEDGEBASE / "manifests" / "collection-targets.json"
URL_MANIFEST_JSON = KNOWLEDGEBASE / "manifests" / "url-manifest.json"
URL_MANIFEST_MD = KNOWLEDGEBASE / "manifests" / "url-manifest.md"
STORE_EXTRACTED = KNOWLEDGEBASE / "store" / "extracted"
STORE_RAW = KNOWLEDGEBASE / "store" / "raw_html"
STORE_ENRICHED = KNOWLEDGEBASE / "store" / "enriched"


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|")


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


def read_targets() -> tuple[list[str], dict[str, str]]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    ordered_ids = [target["id"] for target in data["targets"]]
    names = {target["id"]: target["name"] for target in data["targets"]}
    return ordered_ids, names


def parse_extracted(path: Path) -> tuple[str, str, str, str]:
    title = ""
    source_url = ""
    collected_at = ""
    dependency = ""
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# ") and not title:
            title = line[2:].strip()
        if line.strip() == "Source URL:" and index + 2 < len(lines):
            source_url = lines[index + 2].removeprefix("- ").strip()
        if line.strip() == "Collected at:" and index + 2 < len(lines):
            collected_at = lines[index + 2].removeprefix("- ").strip()
        if line.strip() == "Dependency:" and index + 2 < len(lines):
            dependency = lines[index + 2].removeprefix("- ").strip()
    return title, source_url, collected_at, dependency


def collect_pages(target_id: str, default_name: str) -> list[dict]:
    target_dir = STORE_EXTRACTED / target_id
    if not target_dir.exists():
        return []

    pages = []
    for extracted in sorted(target_dir.glob("*.md")):
        title, source_url, collected_at, dependency = parse_extracted(extracted)
        slug = extracted.stem
        raw_candidates = sorted((STORE_RAW / target_id).glob(f"{slug}.*"))
        raw_rel = str(raw_candidates[0].relative_to(ROOT)) if raw_candidates else ""
        enriched_rel = str((STORE_ENRICHED / target_id / extracted.name).relative_to(ROOT))
        pages.append(
            {
                "url": source_url,
                "title": title or dependency or default_name,
                "slug": slug,
                "status": 200,
                "fetched_at": collected_at,
                "raw_html_path": raw_rel,
                "extracted_path": str(extracted.relative_to(ROOT)),
                "enriched_path": enriched_rel,
            }
        )
    return pages


def build_manifest() -> dict:
    ordered_ids, names = read_targets()
    manifest = {
        "generated_at": datetime.now(UTC).isoformat(),
        "targets": [],
    }

    discovered_ids = []
    if STORE_EXTRACTED.exists():
        discovered_ids = sorted(path.name for path in STORE_EXTRACTED.iterdir() if path.is_dir())

    seen = set()
    for target_id in ordered_ids + [item for item in discovered_ids if item not in ordered_ids]:
        seen.add(target_id)
        pages = collect_pages(target_id, names.get(target_id, target_id.replace("-", " ").title()))
        manifest["targets"].append(
            {
                "target_id": target_id,
                "name": names.get(target_id, target_id.replace("-", " ").title()),
                "collected_pages": len(pages),
                "pages": pages,
            }
        )

    for target_id in discovered_ids:
        if target_id in seen:
            continue
        pages = collect_pages(target_id, target_id.replace("-", " ").title())
        manifest["targets"].append(
            {
                "target_id": target_id,
                "name": target_id.replace("-", " ").title(),
                "collected_pages": len(pages),
                "pages": pages,
            }
        )

    return manifest


def write_manifest(manifest: dict) -> None:
    URL_MANIFEST_JSON.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    URL_MANIFEST_MD.write_text(manifest_markdown(manifest), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Refresh generated knowledgebase artifacts from committed markdown knowledge."
    )
    parser.add_argument("--skip-manifest", action="store_true", help="Skip rebuilding url-manifest files.")
    parser.add_argument("--skip-index", action="store_true", help="Skip rebuilding the local search index.")
    args = parser.parse_args()

    if not args.skip_manifest:
        manifest = build_manifest()
        write_manifest(manifest)
        print(f"[sync] wrote {URL_MANIFEST_JSON.relative_to(ROOT)} and {URL_MANIFEST_MD.relative_to(ROOT)}")

    if not args.skip_index:
        build_search_index.build()
        print("[sync] rebuilt knowledgebase/index")

    print("[done] knowledgebase sync complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
