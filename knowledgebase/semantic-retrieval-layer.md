# Semantic Retrieval Layer

The semantic retrieval layer describes how agents should find the right knowledge quickly in the local repo.

Primary retrieval targets:

- dependency selection
- setup guidance
- auth and identity flows
- event-driven integration patterns
- UI and visualization choices
- media and AI service choices
- production risk checks

Recommended retrieval dimensions:

- dependency
- capability
- artifact type
- lifecycle stage
- surface area
- risk
- adjacent systems

Starter metadata schema for notes:

- `Dependency`
- `Category`
- `Use When`
- `Avoid When`
- `Key Concepts`
- `Integration Edges`
- `Production Risks`
- `Related Docs`
- `Tags`

Suggested semantic tags:

- `auth`
- `api`
- `agentic-doing`
- `nextjs`
- `aws`
- `ui-system`
- `voice`
- `media`
- `maps`
- `charts`
- `3d`
- `billing`
- `webhooks`
- `notifications`
- `calendar`
- `email`

Suggested query patterns:

- "Which dependency should handle this capability?"
- "What is the fastest prototype path for this feature?"
- "What changes when moving to production?"
- "What are the auth or webhook constraints?"
- "Which docs should be opened first before coding?"

Retrieval strategy for agents:

1. Search manifest by dependency or capability.
2. Open the grouped dependency brief.
3. Pull the official URLs listed under priority docs.
4. Use retrieval tags to expand into adjacent dependencies.
5. Escalate to primary docs before implementation if the task is version-sensitive or operationally risky.

Implemented local retrieval:

- `scripts/build_search_index.py` builds a local SQLite FTS5 index plus a TF-IDF similarity index.
- `scripts/search_knowledge.py` runs hybrid local retrieval across collected docs and curated notes.
- The current system is zero-install and local-first.

Future-ready path:

- The current markdown store can later back a chunked embeddings corpus or a Chroma adapter.
- The file and metadata layout was chosen so a stronger vector retrieval layer can be added without restructuring the repo.
