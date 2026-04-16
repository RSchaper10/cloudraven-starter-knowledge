# CloudRaven Starter Knowledge

This repository is now scaffolded as a docs-first knowledgebase for CloudRaven Labs rapid prototyping-to-production work.

The current version does not add runtime code, package installs, or implementation scaffolding. It focuses on:

- collecting official documentation entry points for core dependencies
- curating that material into reusable dependency briefs
- defining how knowledge should be persisted in the repo
- outlining a semantic retrieval layer for agentic development workflows
- providing starter templates for future doc intake and enrichment

Start here:

- [Knowledgebase Index](./knowledgebase/README.md)
- [Collection Workflow](./knowledgebase/collection-workflow.md)
- [Dependency Manifest](./knowledgebase/dependency-manifest.md)
- [Agentic Doing Playbook](./knowledgebase/agentic-doing-playbook.md)

Repo status:

- The original project brief remains in [SUMMARY.md](./SUMMARY.md).
- The repo currently contains knowledge assets only.

Publishing this repo:

1. Create a new GitHub repository for this starter.
2. Initialize git locally and add the remote.
3. Commit the scaffold, manifests, scripts, and shared Markdown knowledge.
4. Push to GitHub and use the repo as a starter to copy into application repos.

Suggested commands:

```bash
git init
git branch -M main
git add .
git commit -m "Initial knowledgebase starter"
git remote add origin git@github.com:YOUR_ORG/YOUR_REPO.git
git push -u origin main
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

Before publishing to GitHub:

- choose a license
- confirm whether you want to keep the sample collected docs and indexes in the public starter
- update the repo name and README language if this will become a reusable scaffold outside CloudRaven Labs
