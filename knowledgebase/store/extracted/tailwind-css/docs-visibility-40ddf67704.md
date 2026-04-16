---
title: visibility - Layout - Tailwind CSS
source_url: https://tailwindcss.com/docs/visibility
target_id: tailwind-css
dependency: Tailwind CSS
collected_at: 2026-04-16T03:22:06.406701+00:00
kind: extracted-doc
---

# visibility - Layout - Tailwind CSS

Source URL:

- https://tailwindcss.com/docs/visibility

Dependency:

- Tailwind CSS

Collected at:

- 2026-04-16T03:22:06.406701+00:00

Direct links in scope:

- https://tailwindcss.com/docs/visibility
- https://tailwindcss.com/docs/display
- https://tailwindcss.com/docs/hover-focus-and-other-states

Captured summary:

- visibility - Layout - Tailwind CSS v 4.2 ⌘K Ctrl K Docs Blog Showcase Sponsor Plus Layout visibility Layout visibility Utilities for controlling the visibility of an element.
- Class Styles visible visibility: visible; invisible visibility: hidden; collapse visibility: collapse; Examples Making elements invisible Use the invisible utility to hide an element, but still maintain its place in the document, affecting the layout of other elements: 01 02 03 < div class = "grid grid-cols-3 gap-4" > < div > 01 </ div > < div class = " invisible ..." > 02 </ div > < div > 03 </ div > </ div > To completely remove an element from the document, use the display property instead.
- Collapsing elements Use the collapse utility to hide table rows, row groups, columns, and column groups as if they were set to display: none , but without impacting the size of other rows and columns: Showing all rows Invoice # Client Amount #100 Pendant Publishing $2,000.00 #101 Kruger Industrial Smoothing $545.00 #102 J.
- Peterman $10,000.25 Hiding a row using `collapse` Invoice # Client Amount #100 Pendant Publishing $2,000.00 #101 Kruger Industrial Smoothing $545.00 #102 J.
- Peterman $10,000.25 Hiding a row using `hidden` Invoice # Client Amount #100 Pendant Publishing $2,000.00 #101 Kruger Industrial Smoothing $545.00 #102 J.

Extracted text:

visibility - Layout - Tailwind CSS

v

4.2

⌘K

Ctrl K

Docs

Blog

Showcase

Sponsor

Plus

Layout

visibility

Layout

visibility

Utilities for controlling the visibility of an element.

Class

Styles

visible

visibility: visible;

invisible

visibility: hidden;

collapse

visibility: collapse;

Examples

Making elements invisible

Use the

invisible

utility to hide an element, but still maintain its place in the document, affecting the layout of other elements:

01

02

03

<

div

class

=

"grid grid-cols-3 gap-4"

>

<

div

>

01

</

div

>

<

div

class

=

"

invisible

..."

>

02

</

div

>

<

div

>

03

</

div

>

</

div

>

To completely remove an element from the document, use the

display

property instead.

Collapsing elements

Use the

collapse

utility to hide table rows, row groups, columns, and column groups as if they were set to

display: none

, but without impacting the size of other rows and columns:

Showing all rows

Invoice #

Client

Amount

#100

Pendant Publishing

$2,000.00

#101

Kruger Industrial Smoothing

$545.00

#102

J. Peterman

$10,000.25

Hiding a row using

`collapse`

Invoice #

Client

Amount

#100

Pendant Publishing

$2,000.00

#101

Kruger Industrial Smoothing

$545.00

#102

J. Peterman

$10,000.25

Hiding a row using

`hidden`

Invoice #

Client

Amount

#100

Pendant Publishing

$2,000.00

#101

Kruger Industrial Smoothing

$545.00

#102

J. Peterman

$10,000.25

<

table

>

<

thead

>

<

tr

>

<

th

>

Invoice #

</

th

>

<

th

>

Client

</

th

>

<

th

>

Amount

</

th

>

</

tr

>

</

thead

>

<

tbody

>

<

tr

>

<

td

>

#100

</

td

>

<

td

>

Pendant Publishing

</

td

>

<

td

>

$2,000.00

</

td

>

</

tr

>

<

tr

class

=

"

collapse

"

>

<

td

>

#101

</

td

>

<

td

>

Kruger Industrial Smoothing

</

td

>

<

td

>

$545.00

</

td

>

</

tr

>

<

tr

>

<

td

>

#102

</

td

>

<

td

>

J. Peterman

</

td

>

<

td

>

$10,000.25

</

td

>

</

tr

>

</

tbody

>

</

table

>

This makes it possible to dynamically toggle rows and columns without affecting the table layout.

Making elements visible

Use the

visible

utility to make an element visible:

01

02

03

<

div

class

=

"grid grid-cols-3 gap-4"

>

<

div

>

01

</

div

>

<

div

class

=

"

visible

..."

>

02

</

div

>

<

div

>

03

</

div

>

</

div

>

This is mostly useful for undoing the

invisible

utility at different screen sizes.

Responsive design

Prefix

a

visibility

utility

with a breakpoint variant like

md

:

to only apply the utility at

medium

screen sizes and above:

<

div

class

=

"visible

md:invisible

..."

>

<!-- ... -->

</

div

>

Learn more about using variants in the

variants documentation

.

On this page

Quick reference

Examples

Making elements invisible

Collapsing elements

Making elements visible

Responsive design

Copyright ©

2026

Tailwind Labs Inc.

·

Trademark Policy
