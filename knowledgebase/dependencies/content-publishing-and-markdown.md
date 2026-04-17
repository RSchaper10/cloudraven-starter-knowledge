# Content Publishing And Markdown

This brief covers the repo-local markdown publishing stack that powers the public blog and other markdown-backed content patterns.

## Where It Shows Up

- `content/blog/*.md`
- `lib/blog.ts`
- `app/lib/blog.ts`
- `app/blog/[slug]/page.tsx`

## Key Dependencies

- `gray-matter` for frontmatter parsing
- `remark` plus `remark-gfm` and `remark-rehype` for markdown parsing and conversion
- `rehype-slug`, `rehype-autolink-headings`, and `rehype-highlight` for heading IDs, anchor links, and code highlighting
- `rehype-stringify` for HTML output
- `github-slugger` and `unist-util-visit` for TOC and heading helpers

## Why It Belongs In The Knowledgebase

- This stack shapes the blog rendering contract, not just a one-off utility.
- Heading IDs, table-of-contents behavior, and HTML safety choices affect stable URLs and content behavior.
- The repo currently has parallel blog helper modules, which raises drift risk when markdown behavior changes in one path and not the other.

## CloudRaven Guidance

- Treat markdown rendering as a product surface, not a disposable content helper.
- Keep frontmatter expectations explicit when adding new content types or post metadata.
- When changing remark or rehype plugins, verify:
  - heading anchors remain stable
  - syntax highlighting still renders
  - any HTML passthrough stays intentional
- Prefer one canonical markdown-processing pipeline over parallel near-duplicates unless the outputs genuinely differ.

## Review Questions

- Are we changing rendering behavior or just content formatting?
- Does the change affect URL anchors or search indexing?
- Are we introducing another markdown transformation path instead of reusing the current one?
