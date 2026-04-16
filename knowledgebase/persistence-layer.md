# Persistence Layer

The persistence layer defines how knowledge should live in this repository over time.

Persistence model:

- root-level manifests for discovery
- grouped dependency briefs for fast scanning
- templates for new intake
- retrieval cards for high-value patterns and decisions

Recommended durable artifact types:

1. Manifest
2. Dependency brief
3. Curated note
4. Retrieval card
5. Decision note

Implemented local store:

- `knowledgebase/manifests/collection-targets.json`
  Seed collection rules, URL allowlists, and CloudRaven enrichment context.
- `knowledgebase/manifests/url-manifest.json`
  Machine-readable record of visited pages in the last collection run.
- `knowledgebase/manifests/url-manifest.md`
  Human-readable record of visited pages and local output paths.
- `knowledgebase/store/raw_html/`
  Raw HTML copies of collected pages.
- `knowledgebase/store/extracted/`
  Local markdown copies of collected page text plus direct links.
- `knowledgebase/store/enriched/`
  CloudRaven-focused applicability and example notes per collected page.
- `knowledgebase/index/`
  Local retrieval index artifacts.

Suggested folder behavior:

- `knowledgebase/dependency-manifest.md`
  Central index of dependencies, sources, collection status, and priority.
- `knowledgebase/dependencies/`
  Curated grouped briefs by domain.
- `knowledgebase/templates/`
  Reusable authoring formats for future additions.

Persistence conventions:

- keep one canonical entry per dependency in the manifest
- prefer updating an existing brief over creating near-duplicates
- preserve source URLs when paraphrasing
- separate source facts from CloudRaven interpretation
- add retrieval tags at the end of each brief or note

Status model:

- `seeded`
  Root docs and starter brief captured
- `curated`
  Concepts distilled and tagged
- `ready-for-agent-use`
  Retrieval hints and caveats included
- `needs-refresh`
  Docs shifted or assumptions may be stale

Refresh triggers:

- major product renames
- framework version shifts
- auth flow changes
- API deprecations
- pricing or capability changes that alter architecture choices
