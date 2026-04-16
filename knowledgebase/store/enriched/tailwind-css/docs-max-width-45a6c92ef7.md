# max-width - Sizing - Tailwind CSS | CloudRaven Enrichment

Source URL:

- https://tailwindcss.com/docs/max-width

Dependency:

- Tailwind CSS

Collection scope:

- Collect the Next.js setup path and core utility styling guidance.

What this page is useful for:

- max-width - Sizing - Tailwind CSS v 4.2 ⌘K Ctrl K Docs Blog Showcase Sponsor Plus Sizing max-width Sizing max-width Utilities for setting the maximum width of an element.
- Class Styles max-w- <number> max-width: calc(var(--spacing) * <number> ); max-w- <fraction> max-width: calc( <fraction> * 100%); max-w-3xs max-width: var(--container-3xs); /* 16rem (256px) */ max-w-2xs max-width: var(--container-2xs); /* 18rem (288px) */ max-w-xs max-width: var(--container-xs); /* 20rem (320px) */ max-w-sm max-width: var(--container-sm); /* 24rem (384px) */ max-w-md max-width: var(--container-md); /* 28rem (448px) */ max-w-lg max-width: var(--container-lg); /* 32rem (512px) */ max-w-xl max-width: var(--container-xl); /* 36rem (576px) */ max-w-2xl max-width: var(--container-2xl); /* 42rem (672px) */ max-w-3xl max-width: var(--container-3xl); /* 48rem (768px) */ max-w-4xl max-width: var(--container-4xl); /* 56rem (896px) */ max-w-5xl max-width: var(--container-5xl); /* 64rem (1024px) */ max-w-6xl max-width: var(--container-6xl); /* 72rem (1152px) */ max-w-7xl max-width: var(--container-7xl); /* 80rem (1280px) */ max-w-none max-width: none; max-w-px max-width: 1px; max-w-full max-width: 100%; max-w-dvw max-width: 100dvw; max-w-dvh max-width: 100dvh; max-w-lvw max-width: 100lvw; max-w-lvh max-width: 100lvh; max-w-svw max-width: 100svw; max-w-svh max-width: 100svh; max-w-screen max-width: 100vw; max-w-min max-width: min-content; max-w-max max-width: max-content; max-w-fit max-width: fit-content; container width: 100%; @media (width >= 40rem) { max-width: 40rem; } @media (width >= 48rem) { max-width: 48rem; } @media (width >= 64rem) { max-width: 64rem; } @media (width >= 80rem) { max-width: 80rem; } @media (width >= 96rem) { max-width: 96rem; } max-w-( <custom-property> ) max-width: var( <custom-property> ); max-w-[ <value> ] max-width: <value> ; Show more Examples Basic example Use max-w- <number> utilities like max-w-24 and max-w-64 to set an element to a fixed maximum width based on the spacing scale: Resize the example to see the expected behavior max-w-96 max-w-80 max-w-64 max-w-48 max-w-40 max-w-32 max-w-24 < div class = "w-full max-w-96 ..." > max-w-96 </ div > < div class = "w-full max-w-80 ..." > max-w-80 </ div > < div class = "w-full max-w-64 ..." > max-w-64 </ div > < div class = "w-full max-w-48 ..." > max-w-48 </ div > < div class = "w-full max-w-40 ..." > max-w-40 </ div > < div class = "w-full max-w-32 ..." > max-w-32 </ div > < div class = "w-full max-w-24 ..." > max-w-24 </ div > Using a percentage Use max-w-full or max-w- <fraction> utilities like max-w-1/2 and max-w-2/5 to give an element a percentage-based maximum width: Resize the example to see the expected behavior max-w-9/10 max-w-3/4 max-w-1/2 max-w-1/3 < div class = "w-full max-w-9/10 ..." > max-w-9/10 </ div > < div class = "w-full max-w-3/4 ..." > max-w-3/4 </ div > < div class = "w-full max-w-1/2 ..." > max-w-1/2 </ div > < div class = "w-full max-w-1/3 ..." > max-w-1/3 </ div > Using the container scale Use utilities like max-w-sm and max-w-xl to set an element to a fixed maximum width based on the container scale: Resize the example to see the expected behavior Andrew Alfred Assistant to the Traveling Secretary < div class = " max-w-md ..." > <!-- ...
- --> </ div > Using breakpoints container Use the container utility to set the maximum width of an element to match the min-width of the current breakpoint.
- This is useful if you'd prefer to design for a fixed set of screen sizes instead of trying to accommodate a fully fluid viewport: < div class = " container " > <!-- ...

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

- Extracted page: `knowledgebase/store/extracted/tailwind-css/docs-max-width-45a6c92ef7.md`
- Raw HTML: `knowledgebase/store/raw_html/tailwind-css/docs-max-width-45a6c92ef7.html`
