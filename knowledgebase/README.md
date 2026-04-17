# Knowledgebase Index

This folder contains the starter knowledgebase structure for collecting, curating, and retrieving dependency and implementation knowledge inside a repository.

It is organized around four layers:

1. Collection
2. Curation
3. Persistence
4. Semantic retrieval

Core documents:

- [Repo Review](./repo-review.md)
- [Collection Workflow](./collection-workflow.md)
- [Collection Layer](./collection-layer.md)
- [Curation Layer](./curation-layer.md)
- [Persistence Layer](./persistence-layer.md)
- [Semantic Retrieval Layer](./semantic-retrieval-layer.md)
- [Dependency Manifest](./dependency-manifest.md)
- [Agentic Doing Playbook](./agentic-doing-playbook.md)

Dependency briefs:

- [Application Foundation](./dependencies/application-foundation.md)
- [AI and Media](./dependencies/ai-and-media.md)
- [Artifact Automation and Print](./dependencies/artifact-automation-and-print.md)
- [AWS SES Inbound Email And S3](./dependencies/aws-ses-inbound-email-and-s3.md)
- [Content Publishing and Markdown](./dependencies/content-publishing-and-markdown.md)
- [HeroUI to shadcn Migration Example](./dependencies/heroui-to-shadcn-migration-example.md)
- [Identity and Events](./dependencies/identity-and-events.md)
- [Important Outbound Email Considerations for Marketing Outreach Dynamics](./dependencies/important-outbound-email-considerations-for-marketing-outreach-dynamics.md)
- [Visualization and Spatial](./dependencies/visualization-and-spatial.md)

Starter templates:

- [Dependency Profile Template](./templates/dependency-profile-template.md)
- [Curated Note Template](./templates/curated-note-template.md)
- [Retrieval Card Template](./templates/retrieval-card-template.md)

Recommended working order:

1. Add or update dependency URLs in the manifest.
2. Capture raw notes from official docs only.
3. Distill those notes into dependency briefs and enriched notes.
4. Tag and persist the distilled notes using the retrieval schema.
5. Reference the knowledgebase during planning, implementation, and review.

Runnable tooling:

- `python3 scripts/collect_docs.py`
- `python3 scripts/build_search_index.py`
- `python3 scripts/search_knowledge.py "your query"`
