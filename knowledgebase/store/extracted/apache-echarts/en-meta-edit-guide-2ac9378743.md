---
title: Edit Guide - Edit Handbook - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/meta/edit-guide
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:12.378230+00:00
kind: extracted-doc
---

# Edit Guide - Edit Handbook - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/meta/edit-guide

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:23:12.378230+00:00

Direct links in scope:

- https://echarts.apache.org/handbook/en/get-started
- https://echarts.apache.org/handbook/en/basics/download
- https://echarts.apache.org/handbook/en/basics/import
- https://echarts.apache.org/handbook/en/basics/help
- https://echarts.apache.org/handbook/en/basics/release-note/v6-feature
- https://echarts.apache.org/handbook/en/basics/release-note/v6-upgrade-guide
- https://echarts.apache.org/handbook/en/basics/release-note/v5-feature
- https://echarts.apache.org/handbook/en/basics/release-note/v5-upgrade-guide
- https://echarts.apache.org/handbook/en/basics/release-note/5-2-0
- https://echarts.apache.org/handbook/en/basics/release-note/5-3-0
- https://echarts.apache.org/handbook/en/basics/release-note/5-4-0
- https://echarts.apache.org/handbook/en/basics/release-note/5-5-0
- https://echarts.apache.org/handbook/en/basics/release-note/5-6-0
- https://echarts.apache.org/handbook/en/concepts/chart-size
- https://echarts.apache.org/handbook/en/concepts/style
- https://echarts.apache.org/handbook/en/concepts/dataset
- https://echarts.apache.org/handbook/en/concepts/data-transform
- https://echarts.apache.org/handbook/en/concepts/axis
- https://echarts.apache.org/handbook/en/concepts/visual-map
- https://echarts.apache.org/handbook/en/concepts/legend

Captured summary:

- Edit Guide - Edit Handbook - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Document Editing Guidelines Adding a Markdown File Add a markdown file to the contents/zh/ (Chinese posts) or contents/en/ (English posts) directories, up to three levels.
- Update the path and title information in contents/zh/posts.yml or contents/en/posts.yml .
- Add the corresponding contributor information in components/helper/contributors.ts .
- (Notice, en and zh are separate entries in that file.) Lowercase markdown file names.

Extracted text:

Edit Guide - Edit Handbook - Handbook - Apache ECharts

Get Started

Basics

Download ECharts

Import ECharts

Get Help

What's New

ECharts 6 Features

Migration from v5 to v6

5.0

Migration from v4 to v5

5.2

5.3

5.4

5.5

5.6

Concepts

Chart Container

Style

Dataset

Data Transform

Axis

Visual Mapping

Legend

Event and Action

How To Guides

Common Charts

Bar

Basic Bar

Stacked Bar

Bar Racing

Waterfall

Line

Basic Line

Stacked Line

Area Chart

Smoothed Line

Step Line

Pie

Basic Pie

Ring Style

Rose Style

Scatter

Basic Scatter

Custom Series

Common Components

Geo

SVG Base Map

Cross Platform

Server Side Rendering

Data

Dynamic Data

Label

Rich Text

Animation

Data Transition

Interaction

Drag

Intelligent Pointer Snapping

Best Practices

Canvas vs. SVG

Aria

Security Guidelines

Edit Handbook

Edit Guide

Document Editing Guidelines

Adding a Markdown File

Add a markdown file to the

contents/zh/

(Chinese posts) or

contents/en/

(English posts) directories, up to three levels. Update the path and title information in

contents/zh/posts.yml

or

contents/en/posts.yml

. Add the corresponding contributor information in

components/helper/contributors.ts

. (Notice,

en

and

zh

are separate entries in that file.)

Lowercase markdown file names.

Using Prettier to Automatically Format Code

Before you start, we recommend installing the

prettier VSCode plugin

, which will automatically format the code for you when you save it.

If you feel that the automatic formatting is breaking your code block, you can add the following comment to prevent

prettier

from formatting the code inside the block

<!-- prettier-ignore-start -->

<!-- prettier-ignore-end -->

If you find blocks of code that are not formatted, check first for syntax errors in the code.

Built-in Variables

optionPath

: For example, the source code of

xAxis.type

is:

[xAxis.type](${optionPath}xAxis.type)

apiPath

: For example, the source code of

echarts.init

is:

[echarts.init](${apiPath}echarts.init)

mainSitePath

: For example, the source code of

echarts.init

is:

[echarts.init](${mainSitePath}api.html#echarts.init)

exampleEditorPath

: For example, the source code of

line-simple

is:

[line-simple](${exampleEditorPath}line-simple&edit=1&reset=1)

exampleViewPath

: For example, the source code of

line-simple

is:

[line-simple](${exampleViewPath}scatter-exponential-regression&edit=1&reset=1)

lang

: For example, the source code of

Get Started

is:

[Get Started](${lang}/get-started)

Headings

The syntax:

## Some Heading [[[#a-unique-id-for-link]]]

The id is used to link this heading from outside. It's strongly recommended to declare the id in each heading (e.g., [[[#a-unique-id-for-link]]]) and ensure it remains unchanged. Otherwise an id is auto-generated base on the title text, which may be unstable (changed when the heading text is changed), and varies across different languages.

Note: No need to declare id for the main title of an article, as the link for an article is the file path (declared in

posts.yml

).

Link to Other Articles

The syntax is:

[Get Apache ECharts](${lang}/basics/download)

The effect is:

Get Apache ECharts

Embedding Code

Basic Usage

The syntax is:

```js option = { series: [{ type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] }] }; ```

The effect is:

option

=

{

series

:

[

{

type

:

'bar'

,

data

:

[

23

,

24

,

18

,

25

,

27

,

28

,

25

]

}

]

}

;

Recommended Way of Writing Code

In order to allow the tool to help us format the code, we should try to avoid syntactically problematic writing styles.

For example, the comment

...

option

=

{

series

:

[

{

type

:

'bar'

// ...

}

]

}

;

Live Preview and Editing

Currently only preview (render the charts) of ECharts option code is supported

The syntax is:

```js live option = { xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] }; ```

The effect is:

option = { xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] };

option

=

{

xAxis

:

{

data

:

[

'Mon'

,

'Tue'

,

'Wed'

,

'Thu'

,

'Fri'

,

'Sat'

,

'Sun'

]

}

,

yAxis

:

{

}

,

series

:

[

{

type

:

'bar'

,

data

:

[

23

,

24

,

18

,

25

,

27

,

28

,

25

]

}

]

}

;

live

More Preview Layouts

Left to Right

The syntax is:

```js live {layout: 'lr'} option = { ... }; ```

The effect is:

option = { xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] };

option

=

{

xAxis

:

{

data

:

[

'Mon'

,

'Tue'

,

'Wed'

,

'Thu'

,

'Fri'

,

'Sat'

,

'Sun'

]

}

,

yAxis

:

{

}

,

series

:

[

{

type

:

'bar'

,

data

:

[

23

,

24

,

18

,

25

,

27

,

28

,

25

]

}

]

}

;

live

Right to left

The syntax is:

```js live {layout: 'rl'} option = { ... }; ```

The effect is:

option = { xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] };

option

=

{

xAxis

:

{

data

:

[

'Mon'

,

'Tue'

,

'Wed'

,

'Thu'

,

'Fri'

,

'Sat'

,

'Sun'

]

}

,

yAxis

:

{

}

,

series

:

[

{

type

:

'bar'

,

data

:

[

23

,

24

,

18

,

25

,

27

,

28

,

25

]

}

]

}

;

live

Down to Up

The syntax is:

```js live {layout: 'bt'} option = { ... };

The effect is:

option = { xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] };

option

=

{

xAxis

:

{

data

:

[

'Mon'

,

'Tue'

,

'Wed'

,

'Thu'

,

'Fri'

,

'Sat'

,

'Sun'

]

}

,

yAxis

:

{

}

,

series

:

[

{

type

:

'bar'

,

data

:

[

23

,

24

,

18

,

25

,

27

,

28

,

25

]

}

]

}

;

live

Highlighting Lines of Code and Adding Filenames

The syntax is:

```js{1,3-5}[option.js] option = { series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] }; ```

The effect is:

option = { series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] };

Embedding Images

Source images are stored under

static/images/

.

The syntax is:

![image description](images/demo.png)

Set the Image Height and Width

For the temporary style of the current page, you can just write html.

<img data-src="images/demo.png" style="width: 50px" />

Embedding Examples (Iframe)

The syntax is:

<md-example src="doc-example/getting-started" width="100%" height="300"></md-example>

src

is the string after

?c=

in the

https://echarts.apache.org/examples/en/editor.html?c=line-simple

address.

The effect is:

Link to Examples

The syntax is:

[line-simple](${exampleEditorPath}line-simple&edit=1&reset=1)

The effect is:

line-simple

Link to ECharts Option Items

The syntax is:

[xAxis.type](${optionPath}xAxis.type)

The effect is:

xAxis.type

The syntax is:

[echarts.init](${apiPath}echarts.init)

The effect is:

echarts.init

More Component Usage

The documentation supports the use of globally registered

markdown

components. In addition to the

md-example

component just described, the following components are also available

md-alert

Prompt components

<md-alert type="info"> This is an info alert. </md-alert>

This is an info alert.

<md-alert type="success"> This is a success alert. </md-alert>

This is a success alert.

<md-alert type="warning"> This is a warning alert. </md-alert>

This is a warning alert.

<md-alert type="danger"> This is a danger alert. </md-alert>

This is a danger alert.

Contributors

Edit this page on GitHub

pissang

100pah

plainheart
