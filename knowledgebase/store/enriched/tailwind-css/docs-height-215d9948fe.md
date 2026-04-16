---
title: height - Sizing - Tailwind CSS | CloudRaven Enrichment
source_url: https://tailwindcss.com/docs/height
target_id: tailwind-css
dependency: Tailwind CSS
collected_at: 2026-04-16T03:22:00.468528+00:00
kind: enriched-doc
tags: tailwind, styling, frontend
---

# height - Sizing - Tailwind CSS | CloudRaven Enrichment

Source URL:

- https://tailwindcss.com/docs/height

Dependency:

- Tailwind CSS

Collection scope:

- Collect the Next.js setup path and core utility styling guidance.

What this page is useful for:

- height - Sizing - Tailwind CSS v 4.2 ⌘K Ctrl K Docs Blog Showcase Sponsor Plus Sizing height Sizing height Utilities for setting the height of an element.
- Class Styles h- <number> height: calc(var(--spacing) * <number> ); h- <fraction> height: calc( <fraction> * 100%); h-auto height: auto; h-px height: 1px; h-full height: 100%; h-screen height: 100vh; h-dvh height: 100dvh; h-dvw height: 100dvw; h-lvh height: 100lvh; h-lvw height: 100lvw; h-svh height: 100svh; h-svw height: 100svw; h-min height: min-content; h-max height: max-content; h-fit height: fit-content; h-lh height: 1lh; h-( <custom-property> ) height: var( <custom-property> ); h-[ <value> ] height: <value> ; size- <number> width: calc(var(--spacing) * <number> ); height: calc(var(--spacing) * <number> ); size- <fraction> width: calc( <fraction> * 100%); height: calc( <fraction> * 100%); size-auto width: auto; height: auto; size-px width: 1px; height: 1px; size-full width: 100%; height: 100%; size-dvw width: 100dvw; height: 100dvw; size-dvh width: 100dvh; height: 100dvh; size-lvw width: 100lvw; height: 100lvw; size-lvh width: 100lvh; height: 100lvh; size-svw width: 100svw; height: 100svw; size-svh width: 100svh; height: 100svh; size-min width: min-content; height: min-content; size-max width: max-content; height: max-content; size-fit width: fit-content; height: fit-content; size-( <custom-property> ) width: var( <custom-property> ); height: var( <custom-property> ); size-[ <value> ] width: <value> ; height: <value> ; Show more Examples Basic example Use h- <number> utilities like h-24 and h-64 to set an element to a fixed height based on the spacing scale: h-96 h-80 h-64 h-48 h-40 h-32 h-24 < div class = " h-96 ..." > h-96 </ div > < div class = " h-80 ..." > h-80 </ div > < div class = " h-64 ..." > h-64 </ div > < div class = " h-48 ..." > h-48 </ div > < div class = " h-40 ..." > h-40 </ div > < div class = " h-32 ..." > h-32 </ div > < div class = " h-24 ..." > h-24 </ div > Using a percentage Use h-full or h- <fraction> utilities like h-1/2 and h-2/5 to give an element a percentage-based height: h-full h-9/10 h-3/4 h-1/2 h-1/3 < div class = " h-full ..." > h-full </ div > < div class = " h-9/10 ..." > h-9/10 </ div > < div class = " h-3/4 ..." > h-3/4 </ div > < div class = " h-1/2 ..." > h-1/2 </ div > < div class = " h-1/3 ..." > h-1/3 </ div > Matching viewport Use the h-screen utility to make an element span the entire height of the viewport: < div class = " h-screen " > <!-- ...
- --> </ div > Matching dynamic viewport Use the h-dvh utility to make an element span the entire height of the viewport, which changes as the browser UI expands or contracts: Scroll the viewport to see the viewport height change tailwindcss.com h- dvh < div class = " h-dvh " > <!-- ...
- --> </ div > Matching large viewport Use the h-lvh utility to set an element's height to the largest possible height of the viewport: Scroll the viewport to see the viewport height change tailwindcss.com h- lvh < div class = " h-lvh " > <!-- ...

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

- Extracted page: `knowledgebase/store/extracted/tailwind-css/docs-height-215d9948fe.md`
- Raw source: `knowledgebase/store/raw_html/tailwind-css/docs-height-215d9948fe.html`
