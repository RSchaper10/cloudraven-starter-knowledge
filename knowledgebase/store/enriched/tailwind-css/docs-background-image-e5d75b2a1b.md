---
title: background-image - Backgrounds - Tailwind CSS | CloudRaven Enrichment
source_url: https://tailwindcss.com/docs/background-image
target_id: tailwind-css
dependency: Tailwind CSS
collected_at: 2026-04-16T03:22:04.699241+00:00
kind: enriched-doc
tags: tailwind, styling, frontend
---

# background-image - Backgrounds - Tailwind CSS | CloudRaven Enrichment

Source URL:

- https://tailwindcss.com/docs/background-image

Dependency:

- Tailwind CSS

Collection scope:

- Collect the Next.js setup path and core utility styling guidance.

What this page is useful for:

- background-image - Backgrounds - Tailwind CSS v 4.2 ⌘K Ctrl K Docs Blog Showcase Sponsor Plus Backgrounds background-image Backgrounds background-image Utilities for controlling an element's background image.
- Class Styles bg-[ <value> ] background-image: <value> ; bg-(image: <custom-property> ) background-image: var( <custom-property> ); bg-none background-image: none; bg-linear-to-t background-image: linear-gradient(to top, var(--tw-gradient-stops)); bg-linear-to-tr background-image: linear-gradient(to top right, var(--tw-gradient-stops)); bg-linear-to-r background-image: linear-gradient(to right, var(--tw-gradient-stops)); bg-linear-to-br background-image: linear-gradient(to bottom right, var(--tw-gradient-stops)); bg-linear-to-b background-image: linear-gradient(to bottom, var(--tw-gradient-stops)); bg-linear-to-bl background-image: linear-gradient(to bottom left, var(--tw-gradient-stops)); bg-linear-to-l background-image: linear-gradient(to left, var(--tw-gradient-stops)); bg-linear-to-tl background-image: linear-gradient(to top left, var(--tw-gradient-stops)); bg-linear- <angle> background-image: linear-gradient( <angle> in oklab, var(--tw-gradient-stops)); -bg-linear- <angle> background-image: linear-gradient(- <angle> in oklab, var(--tw-gradient-stops)); bg-linear-( <custom-property> ) background-image: linear-gradient(var(--tw-gradient-stops, var( <custom-property> ))); bg-linear-[ <value> ] background-image: linear-gradient(var(--tw-gradient-stops, <value> )); bg-radial background-image: radial-gradient(in oklab, var(--tw-gradient-stops)); bg-radial-( <custom-property> ) background-image: radial-gradient(var(--tw-gradient-stops, var( <custom-property> ))); bg-radial-[ <value> ] background-image: radial-gradient(var(--tw-gradient-stops, <value> )); bg-conic- <angle> background-image: conic-gradient(from <angle> in oklab, var(--tw-gradient-stops)); -bg-conic- <angle> background-image: conic-gradient(from - <angle> in oklab, var(--tw-gradient-stops)); bg-conic-( <custom-property> ) background-image: var( <custom-property> ); bg-conic-[ <value> ] background-image: <value> ; from- <color> --tw-gradient-from: <color> ; from- <percentage> --tw-gradient-from-position: <percentage> ; from-( <custom-property> ) --tw-gradient-from: var( <custom-property> ); from-[ <value> ] --tw-gradient-from: <value> ; via- <color> --tw-gradient-via: <color> ; via- <percentage> --tw-gradient-via-position: <percentage> ; via-( <custom-property> ) --tw-gradient-via: var( <custom-property> ); via-[ <value> ] --tw-gradient-via: <value> ; to- <color> --tw-gradient-to: <color> ; to- <percentage> --tw-gradient-to-position: <percentage> ; to-( <custom-property> ) --tw-gradient-to: var( <custom-property> ); to-[ <value> ] --tw-gradient-to: <value> ; Show more Examples Basic example Use the bg-[ <value> ] syntax to set the background image of an element: < div class = " bg-[url(/img/mountains.jpg)] ..." ></ div > Adding a linear gradient Use utilities like bg-linear-to-r and bg-linear- <angle> with the color stop utilities to add a linear gradient to an element: < div class = "h-14 bg-linear-to-r from-cyan-500 to-blue-500" ></ div > < div class = "h-14 bg-linear-to-t from-sky-500 to-indigo-500" ></ div > < div class = "h-14 bg-linear-to-bl from-violet-500 to-fuchsia-500" ></ div > < div class = "h-14 bg-linear-65 from-purple-500 to-pink-500" ></ div > Adding a radial gradient Use the bg-radial and bg-radial-[ <position> ] utilities with the color stop utilities to add a radial gradient to an element: < div class = "size-18 rounded-full bg-radial from-pink-400 from-40% to-fuchsia-700" ></ div > < div class = "size-18 rounded-full bg-radial-[at_50%_75%] from-sky-200 via-blue-400 to-indigo-900 to-90%" ></ div > < div class = "size-18 rounded-full bg-radial-[at_25%_25%] from-white to-zinc-900 to-75%" ></ div > Adding a conic gradient Use the bg-conic and bg-conic- <angle> utilities with the color stop utilities to add a conic gradient to an element: < div class = "size-24 rounded-full bg-conic from-blue-600 to-sky-400 to-50%" ></ div > < div class = "size-24 rounded-full bg-conic-180 from-indigo-600 via-indigo-50 to-indigo-600" ></ div > < div class = "size-24 rounded-full bg-conic/decreasing from-violet-700 via-lime-300 to-violet-700" ></ div > Setting gradient color stops Use utilities like from-indigo-500 , via-purple-500 , and to-pink-500 to set the colors of the gradient stops: < div class = "bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 ..." ></ div > Setting gradient stop positions Use utilities like from-10% , via-30% , and to-90% to set more precise positions for the gradient color stops: 10% 30% 90% < div class = "bg-gradient-to-r from-indigo-500 from-10% via-sky-500 via-30% to-emerald-500 to-90% ..." ></ div > Changing interpolation mode Use the interpolation modifier to control the interpolation mode of a gradient: srgb hsl oklab oklch longer shorter increasing decreasing < div class = "bg-linear-to-r /srgb from-indigo-500 to-teal-400" ></ div > < div class = "bg-linear-to-r /hsl from-indigo-500 to-teal-400" ></ div > < div class = "bg-linear-to-r /oklab from-indigo-500 to-teal-400" ></ div > < div class = "bg-linear-to-r /oklch from-indigo-500 to-teal-400" ></ div > < div class = "bg-linear-to-r /longer from-indigo-500 to-teal-400" ></ div > < div class = "bg-linear-to-r /shorter from-indigo-500 to-teal-400" ></ div > < div class = "bg-linear-to-r /increasing from-indigo-500 to-teal-400" ></ div > < div class = "bg-linear-to-r /decreasing from-indigo-500 to-teal-400" ></ div > By default gradients are interpolated in the oklab color space.
- Removing background images Use the bg-none utility to remove an existing background image from an element: < div class = " bg-none " ></ div > Using a custom value Use utilities like bg-linear -[ <value> ] and from -[ <value> ] to set the gradient based on a completely custom value: < div class = " bg-linear-[25deg,red_5%,yellow_60%,lime_90%,teal] ..." > <!-- ...
- --> </ div > For CSS variables, you can also use the bg-linear -( <custom-property> ) syntax: < div class = " bg-linear-(--my-gradient) ..." > <!-- ...

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

- Extracted page: `knowledgebase/store/extracted/tailwind-css/docs-background-image-e5d75b2a1b.md`
- Raw source: `knowledgebase/store/raw_html/tailwind-css/docs-background-image-e5d75b2a1b.html`
