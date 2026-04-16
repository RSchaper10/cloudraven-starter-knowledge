# Styling with utility classes - Core concepts - Tailwind CSS | CloudRaven Enrichment

Source URL:

- https://tailwindcss.com/docs/styling-with-utility-classes

Dependency:

- Tailwind CSS

Collection scope:

- Collect the Next.js setup path and core utility styling guidance.

What this page is useful for:

- Styling with utility classes - Core concepts - Tailwind CSS v 4.2 ⌘K Ctrl K Docs Blog Showcase Sponsor Plus Core concepts Styling with utility classes Core concepts Styling with utility classes Building complex components from a constrained set of primitive utilities.
- Overview You style things with Tailwind by combining many single-purpose presentational classes (utility classes) directly in your markup: ChitChat You have a new message!
- < div class = "mx-auto flex max-w-sm items-center gap-x-4 rounded-xl bg-white p-6 shadow-lg outline outline-black/5 dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10" > < img class = "size-12 shrink-0" src = "/img/logo.svg" alt = "ChitChat Logo" /> < div > < div class = "text-xl font-medium text-black dark:text-white" > ChitChat </ div > < p class = "text-gray-500 dark:text-gray-400" > You have a new message!
- </ p > </ div > </ div > For example, in the UI above we've used: The display and padding utilities ( flex , shrink-0 , and p-6 ) to control the overall layout The max-width and margin utilities ( max-w-sm and mx-auto ) to constrain the card width and center it horizontally The background-color , border-radius , and box-shadow utilities ( bg-white , rounded-xl , and shadow-lg ) to style the card's appearance The width and height utilities ( size-12 ) to set the width and height of the logo image The gap utilities ( gap-x-4 ) to handle the spacing between the logo and the text The font-size , color , and font-weight utilities ( text-xl , text-black , font-medium , etc.) to style the card text Styling things this way contradicts a lot of traditional best practices, but once you try it you'll quickly notice some really important benefits: You get things done faster — you don't spend any time coming up with class names, making decisions about selectors, or switching between HTML and CSS files, so your designs come together very fast.

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

- Extracted page: `knowledgebase/store/extracted/tailwind-css/docs-styling-with-utility-classes-90e7aa6bdf.md`
- Raw HTML: `knowledgebase/store/raw_html/tailwind-css/docs-styling-with-utility-classes-90e7aa6bdf.html`
