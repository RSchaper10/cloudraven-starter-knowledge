---
title: Ring Style - Pie - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/pie/doughnut
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:00.538104+00:00
kind: extracted-doc
---

# Ring Style - Pie - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/pie/doughnut

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:23:00.538104+00:00

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

- Ring Style - Pie - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Doughnut Chart Doughnut charts are also used to show the proportion of values compared with the total.
- Different from the pie chart, the blank in the middle of the chart can be used to provide some extra info.
- It makes a doughnut chart commonly used chart type.
- Basic Doughnut Chart In ECharts, the radius of the pie chart could also be an array with 2 elements.

Extracted text:

Ring Style - Pie - Common Charts - How To Guides - Handbook - Apache ECharts

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

Doughnut Chart

Doughnut charts are also used to show the proportion of values compared with the total. Different from the pie chart, the blank in the middle of the chart can be used to provide some extra info. It makes a doughnut chart commonly used chart type.

Basic Doughnut Chart

In ECharts, the radius of the pie chart could also be an array with 2 elements. Every element in the array could be string or value. The first element represents the inner radius while the second one is the outer radius.

The pie chart, from this perspective, is a subset of the doughnut chart that has inner radius equals to 0.

option = { title: { text: 'A Case of Doughnut Chart', left: 'center', top: 'center' }, series: [ { type: 'pie', data: [ { value: 335, name: 'A' }, { value: 234, name: 'B' }, { value: 1548, name: 'C' } ], radius: ['40%', '70%'] } ] };

option

=

{

title

:

{

text

:

'A Case of Doughnut Chart'

,

left

:

'center'

,

top

:

'center'

}

,

series

:

[

{

type

:

'pie'

,

data

:

[

{

value

:

335

,

name

:

'A'

}

,

{

value

:

234

,

name

:

'B'

}

,

{

value

:

1548

,

name

:

'C'

}

]

,

radius

:

[

'40%'

,

'70%'

]

}

]

}

;

live

If we set one radius to string of a percentage value, while the other to a value, the inner radius will be smaller than the outer radius in some resolution. ECharts will choose the smaller element for the inner radius automatically. However, it will still cause not an unexpected outcome.

Show Text In Middle Of Doughnut From Highlighted Sector

The previous case gives you a way to show fixed text in the middle of doughnut chart. The next case will show you how to display the corresponding text of the sector highlighted by the mouse. The general idea is to fix

label

in the middle of the chart while hiding

label

in default.

option = { legend: { orient: 'vertical', x: 'left', data: ['A', 'B', 'C', 'D', 'E'] }, series: [ { type: 'pie', radius: ['50%', '70%'], avoidLabelOverlap: false, label: { show: false, position: 'center' }, labelLine: { show: false }, emphasis: { label: { show: true, fontSize: '30', fontWeight: 'bold' } }, data: [ { value: 335, name: 'A' }, { value: 310, name: 'B' }, { value: 234, name: 'C' }, { value: 135, name: 'D' }, { value: 1548, name: 'E' } ] } ] };

option

=

{

legend

:

{

orient

:

'vertical'

,

x

:

'left'

,

data

:

[

'A'

,

'B'

,

'C'

,

'D'

,

'E'

]

}

,

series

:

[

{

type

:

'pie'

,

radius

:

[

'50%'

,

'70%'

]

,

avoidLabelOverlap

:

false

,

label

:

{

show

:

false

,

position

:

'center'

}

,

labelLine

:

{

show

:

false

}

,

emphasis

:

{

label

:

{

show

:

true

,

fontSize

:

'30'

,

fontWeight

:

'bold'

}

}

,

data

:

[

{

value

:

335

,

name

:

'A'

}

,

{

value

:

310

,

name

:

'B'

}

,

{

value

:

234

,

name

:

'C'

}

,

{

value

:

135

,

name

:

'D'

}

,

{

value

:

1548

,

name

:

'E'

}

]

}

]

}

;

live

In this case,

avoidLabelOverlap

is used to control whether ECharts adjust the position of label to avoid overlaps. Default value of

avoidLabelOverlap

is

true

. We want the label to be fixed in the middle so that we need to define it as

false

.

Therefore, the middle of doughnut chart will show the

name

of the highlighted sector.

Contributors

Edit this page on GitHub

plainheart

pissang

jnodorp
