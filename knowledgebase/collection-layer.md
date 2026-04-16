# Collection Layer

The collection layer defines how new knowledge enters the repo.

Collection goals:

- prefer official documentation and primary references
- collect entry-point URLs before collecting details
- capture enough context for agent use without cloning entire doc sites
- separate raw source links from curated interpretation

Collection unit:

- one dependency
- one official documentation entry point
- a small set of priority pages
- one CloudRaven relevance statement

Minimum collection standard:

1. Official root URL
2. Priority quickstart or getting-started URL
3. Priority integration or architecture URL
4. Priority auth, data, events, or deployment URL when relevant
5. Notes on what the dependency is best used for
6. Notes on where the dependency should not be used

Source hierarchy:

1. Official docs
2. Official API references
3. Official examples and starter guides
4. Official product pages only when docs are thin

Collection rules:

- Do not rely on unofficial tutorials as source truth.
- Prefer narrow manifests over exhaustive crawls.
- Store source URLs in the dependency manifest first.
- Add update dates when official pages expose them.
- Flag unclear or outdated terminology instead of guessing.

CloudRaven bias for collection:

- prioritize material that supports rapid prototyping with a clean path to production
- prioritize APIs, auth flows, deployment constraints, eventing, and operational boundaries
- prioritize reusable patterns across web apps, content systems, automation flows, and artifact-as-code workflows
