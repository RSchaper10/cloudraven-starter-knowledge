---
title: gap - Flexbox & Grid - Tailwind CSS | CloudRaven Enrichment
source_url: https://tailwindcss.com/docs/gap
target_id: tailwind-css
dependency: Tailwind CSS
collected_at: 2026-04-16T03:22:00.878731+00:00
kind: enriched-doc
tags: tailwind, styling, frontend
---

# gap - Flexbox & Grid - Tailwind CSS | CloudRaven Enrichment

Source URL:

- https://tailwindcss.com/docs/gap

Dependency:

- Tailwind CSS

Collection scope:

- Collect the Next.js setup path and core utility styling guidance.

What this page is useful for:

- gap - Flexbox & Grid - Tailwind CSS v 4.2 ⌘K Ctrl K Docs Blog Showcase Sponsor Plus Flexbox & Grid gap Flexbox & Grid gap Utilities for controlling gutters between grid and flexbox items.
- Class Styles gap- <number> gap: calc(var(--spacing) * <value> ); gap-( <custom-property> ) gap: var( <custom-property> ); gap-[ <value> ] gap: <value> ; gap-x- <number> column-gap: calc(var(--spacing) * <value> ); gap-x-( <custom-property> ) column-gap: var( <custom-property> ); gap-x-[ <value> ] column-gap: <value> ; gap-y- <number> row-gap: calc(var(--spacing) * <value> ); gap-y-( <custom-property> ) row-gap: var( <custom-property> ); gap-y-[ <value> ] row-gap: <value> ; Examples Basic example Use gap- <number> utilities like gap-2 and gap-4 to change the gap between both rows and columns in grid and flexbox layouts: 01 02 03 04 < div class = "grid grid-cols-2 gap-4 " > < div > 01 </ div > < div > 02 </ div > < div > 03 </ div > < div > 04 </ div > </ div > Changing row and column gaps independently Use gap-x- <number> or gap-y- <number> utilities like gap-x-8 and gap-y-4 to change the gap between columns and rows independently: 01 02 03 04 05 06 < div class = "grid grid-cols-3 gap-x-8 gap-y-4 " > < div > 01 </ div > < div > 02 </ div > < div > 03 </ div > < div > 04 </ div > < div > 05 </ div > < div > 06 </ div > </ div > Using a custom value Use utilities like gap -[ <value> ] , gap-x -[ <value> ] , and gap-y -[ <value> ] to set the gap based on a completely custom value: < div class = " gap-[10vw] ..." > <!-- ...
- --> </ div > For CSS variables, you can also use the gap -( <custom-property> ) syntax: < div class = " gap-(--my-gap) ..." > <!-- ...
- --> </ div > This is just a shorthand for gap -[ var( <custom-property> )] that adds the var() function for you automatically.

CloudRaven applicability:

- Use this material when fast layout iteration and custom interface composition matter.

Prototype-to-production review:

- High fit for rapid iteration and unusual UI compositions.
- Create conventions early so utility usage does not become unstructured.

CloudRaven example paths:

- Build a branded portal shell with responsive utility classes.
- Layer custom presentation or dashboard layouts over a component system.

Suggested retrieval tags:

- `tailwind`
- `styling`
- `frontend`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/tailwind-css/docs-gap-107a1898ed.md`
- Raw source: `knowledgebase/store/raw_html/tailwind-css/docs-gap-107a1898ed.html`
