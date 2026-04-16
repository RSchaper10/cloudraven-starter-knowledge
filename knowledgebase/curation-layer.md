# Curation Layer

The curation layer turns raw documentation into reusable working knowledge.

Curation outputs:

- concise dependency briefs
- CloudRaven-specific fit notes
- implementation caveats
- retrieval tags and query hints

Curation questions:

1. What problem does this dependency solve?
2. Where does it sit in a starter stack?
3. What are its main primitives?
4. What integration edges usually create friction?
5. What production constraints matter early?
6. What would an agent need to know before writing code?

Curation rules:

- summarize concepts in plain language
- keep snippets conceptual unless an exact API detail is essential
- preserve product boundaries and naming as used in the official docs
- call out deprecated or misleading assumptions
- relate each dependency back to CloudRaven rapid prototyping-to-production paths

What to capture for every dependency:

- role in stack
- main concepts
- high-value docs to consult first
- production risks
- adjacent dependencies
- suggested retrieval tags

Review criteria:

- Is the brief actionable for an agent?
- Does it reduce common setup mistakes?
- Does it identify when to escalate to primary docs?
- Does it help choose between fast prototype and production-safe paths?
