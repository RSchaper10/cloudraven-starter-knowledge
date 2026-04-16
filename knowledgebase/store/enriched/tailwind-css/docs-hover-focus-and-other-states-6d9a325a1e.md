---
title: Hover, focus, and other states - Core concepts - Tailwind CSS | CloudRaven Enrichment
source_url: https://tailwindcss.com/docs/hover-focus-and-other-states
target_id: tailwind-css
dependency: Tailwind CSS
collected_at: 2026-04-16T03:22:03.300934+00:00
kind: enriched-doc
tags: tailwind, styling, frontend
---

# Hover, focus, and other states - Core concepts - Tailwind CSS | CloudRaven Enrichment

Source URL:

- https://tailwindcss.com/docs/hover-focus-and-other-states

Dependency:

- Tailwind CSS

Collection scope:

- Collect the Next.js setup path and core utility styling guidance.

What this page is useful for:

- Hover, focus, and other states - Core concepts - Tailwind CSS v 4.2 ⌘K Ctrl K Docs Blog Showcase Sponsor Plus Core concepts Hover, focus, and other states Core concepts Hover, focus, and other states Using utilities to style elements on hover, focus, and more.
- Every utility class in Tailwind can be applied conditionally by adding a variant to the beginning of the class name that describes the condition you want to target.
- For example, to apply the bg-sky-700 class on hover, use the hover:bg-sky-700 class: Hover over this button to see the background color change Save changes < button class = "bg-sky-500 hover:bg-sky-700 ..." > Save changes </ button > How does this compare to traditional CSS?
- When writing CSS the traditional way, a single class name would do different things based on the current state: Traditionally the same class name applies different styles on hover .btn-primary { background-color : #0ea5e9 ; } .btn-primary:hover { background-color : #0369a1 ; } In Tailwind, rather than adding the styles for a hover state to an existing class, you add another class to the element that only does something on hover: In Tailwind, separate classes are used for the default state and the hover state .bg-sky-500 { background-color : #0ea5e9 ; } .hover \: bg-sky-700:hover { background-color : #0369a1 ; } Notice how hover:bg-sky-700 only defines styles for the :hover state?

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

- Extracted page: `knowledgebase/store/extracted/tailwind-css/docs-hover-focus-and-other-states-6d9a325a1e.md`
- Raw source: `knowledgebase/store/raw_html/tailwind-css/docs-hover-focus-and-other-states-6d9a325a1e.html`
