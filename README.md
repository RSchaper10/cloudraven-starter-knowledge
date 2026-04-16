# Repo Knowledgebase Starter

This repository is a docs-first starter scaffold for building a shared, repo-local knowledgebase alongside an application codebase.

It does not add runtime code, package installs, or app scaffolding. It focuses on:

- collecting official documentation entry points for important dependencies
- capturing extracted markdown from those sources
- distilling that material into reusable enriched notes and dependency briefs
- defining how knowledge should be persisted in the repo
- providing a local retrieval workflow for collaborators and coding agents

Start here:

- [Knowledgebase Index](./knowledgebase/README.md)
- [Collection Workflow](./knowledgebase/collection-workflow.md)
- [Dependency Manifest](./knowledgebase/dependency-manifest.md)
- [Agentic Doing Playbook](./knowledgebase/agentic-doing-playbook.md)

Repo status:

- The original project brief for this starter remains in [SUMMARY.md](./SUMMARY.md).
- The repo contains knowledge assets and local tooling only.

Using this starter in another repo:

1. Copy the knowledgebase structure and scripts into your target repository.
2. Update the dependency targets in `knowledgebase/manifests/collection-targets.json`.
3. Collect and curate the docs that matter for that repo's architecture.
4. Commit the shared markdown knowledge so anyone with repo access can use it.

Suggested commands:

```bash
python3 scripts/collect_docs.py
python3 scripts/sync_knowledge.py
python3 scripts/build_search_index.py
python3 scripts/search_knowledge.py "your query"
```

Recommended tracked content:

- `knowledgebase/**/*.md`
- `knowledgebase/manifests/`
- `knowledgebase/store/extracted/`
- `knowledgebase/store/enriched/`
- `knowledgebase/dependencies/`
- `scripts/`

Local-only generated artifacts:

- `knowledgebase/store/raw_html/`
- `knowledgebase/index/`

Knowledge syncing policy:

- Treat shared Markdown as the canonical team knowledge.
- Commit manually collected notes, extracted markdown, enriched markdown, dependency briefs, templates, and manifests.
- Treat raw source snapshots and search indexes as rebuildable local artifacts.
- Rebuild the local retrieval index with `python3 scripts/build_search_index.py` after pulling new markdown knowledge.

Update workflow:

- If you add or edit markdown manually in `knowledgebase/`, run `python3 scripts/sync_knowledge.py`.
- If you collect new docs from URLs, run `python3 scripts/collect_docs.py` and then `python3 scripts/sync_knowledge.py`.
- If you want shorter commands, use `make kb-sync`, `make kb-collect targets=openai-api`, and `make kb-search q="your query"`.

Common adoption steps:

- add a license file before wider reuse or publication
- move the knowledgebase into `/docs/knowledgebase` when integrating it into an application repo
- replace the sample dependency briefs and manifests with the actual stack for the target repository
