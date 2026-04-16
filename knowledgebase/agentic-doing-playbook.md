# Agentic Doing Playbook

This playbook is the non-code operating guide for using the knowledgebase during project work.

Core intent:

- help an agent gather the right docs quickly
- reduce shallow pattern-matching against the wrong framework examples
- keep prototype velocity high without losing production awareness

Agent workflow:

1. Identify the dependency set involved in the task.
2. Read the corresponding grouped dependency brief.
3. Open only the priority official docs needed for the task.
4. Extract the smallest set of facts needed to proceed.
5. Create or update a curated note if new knowledge was required.
6. Add retrieval tags so future work can find it faster.

Use this repo for:

- project bootstrapping
- dependency comparisons
- auth and eventing design
- API integration planning
- implementation guardrails
- production-readiness checkpoints

Do not use this repo as:

- a replacement for version-sensitive primary docs
- a place to store copied documentation dumps
- a place to preserve stale code snippets without source links

CloudRaven framing:

- favor patterns that move cleanly from ideation to implementation
- document where shortcuts are acceptable in prototype mode
- document where shortcuts become liabilities in production mode
- relate technical choices back to reusable business workflows, not just app screens

Recommended agent prompts:

- "Summarize the production-safe path for this dependency using the knowledgebase and then check the official docs."
- "Find the likely integration edges between these dependencies before writing code."
- "List the quickstart path, the auth requirements, and the event model for this feature."
- "Convert this new learning into a curated note with tags and linked official sources."
