---
title: Legend - Concepts - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/concepts/legend
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:51.573348+00:00
kind: extracted-doc
---

# Legend - Concepts - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/concepts/legend

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:51.573348+00:00

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

- Legend - Concepts - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Legend Legends are used to annotate the content in the chart using different colors, shapes and texts to indicate different categories.
- By clicking the legends, the user can show or hide the corresponding categories.
- Legend is one of the key to understand the chart.
- Layout Legend is always placed at the upper right corner of the chart.

Extracted text:

Legend - Concepts - Handbook - Apache ECharts

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

Legend

Legends are used to annotate the content in the chart using different colors, shapes and texts to indicate different categories. By clicking the legends, the user can show or hide the corresponding categories. Legend is one of the key to understand the chart.

Layout

Legend is always placed at the upper right corner of the chart. All legends in the same page need to be consistent, align horizontally or vertically by considering the layout of the overall chart space. When the chart has little vertical space or the content area is crowded, it is also a good choice to put the legend on the bottom of the chart. Here are some layouts of legend:

option = { legend: { // Try 'horizontal' orient: 'vertical', right: 10, top: 'center' }, dataset: { source: [ ['product', '2015', '2016', '2017'], ['Matcha Latte', 43.3, 85.8, 93.7], ['Milk Tea', 83.1, 73.4, 55.1], ['Cheese Cocoa', 86.4, 65.2, 82.5], ['Walnut Brownie', 72.4, 53.9, 39.1] ] }, xAxis: { type: 'category' }, yAxis: {}, series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }] };

option

=

{

legend

:

{

// Try 'horizontal'

orient

:

'vertical'

,

right

:

10

,

top

:

'center'

}

,

dataset

:

{

source

:

[

[

'product'

,

'2015'

,

'2016'

,

'2017'

]

,

[

'Matcha Latte'

,

43.3

,

85.8

,

93.7

]

,

[

'Milk Tea'

,

83.1

,

73.4

,

55.1

]

,

[

'Cheese Cocoa'

,

86.4

,

65.2

,

82.5

]

,

[

'Walnut Brownie'

,

72.4

,

53.9

,

39.1

]

]

}

,

xAxis

:

{

type

:

'category'

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

}

,

{

type

:

'bar'

}

,

{

type

:

'bar'

}

]

}

;

live

Use scrollable control if there are many legends.

option

=

{

legend

:

{

type

:

'scroll'

,

orient

:

'vertical'

,

right

:

10

,

top

:

20

,

bottom

:

20

,

data

:

[

'Legend A'

,

'Legend B'

,

'Legend C'

/* ... */

,

,

'Legend x'

]

// ...

}

// ...

}

;

Style

For dark color background, use a light color for the background layer and text while changing the background to translucent.

option

=

{

legend

:

{

data

:

[

'Legend A'

,

'Legend B'

,

'Legend C'

]

,

backgroundColor

:

'#ccc'

,

textStyle

:

{

color

:

'#ccc'

// ...

}

// ...

}

// ...

}

;

The color of legend has many ways to design. For different charts, the legend style can be different.

option

=

{

legend

:

{

data

:

[

'Legend A'

,

'Legend B'

,

'Legend C'

]

,

icon

:

'rect'

// ...

}

// ...

}

;

Interactive

Depend on the environmental demand, the legend can support interactive operation. Click the legend to show or hide corresponding categories:

option

=

{

legend

:

{

data

:

[

'Legend A'

,

'Legend B'

,

'Legend C'

]

,

selected

:

{

'Legend A'

:

true

,

'Legend B'

:

true

,

'Legend C'

:

false

}

// ...

}

// ...

}

;

Tips

The legend should be used according to the situation. Some dual-axis charts include multiple chart types. Different kinds of legend stypes should be distinguished.

option

=

{

legend

:

{

data

:

[

{

name

:

'Legend A'

,

icon

:

'rect'

}

,

{

name

:

'Legend B'

,

icon

:

'circle'

}

,

{

name

:

'Legend C'

,

icon

:

'pin'

}

]

// ...

}

,

series

:

[

{

name

:

'Legend A'

// ...

}

,

{

name

:

'Legend B'

// ...

}

,

{

name

:

'Legend C'

// ...

}

]

// ...

}

;

While there is only one kind of data in the chart, use the chart title rather than the legend to explain it.

Contributors

Edit this page on GitHub

pissang
