---
title: Step Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/line/step-line
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:59.091148+00:00
kind: extracted-doc
---

# Step Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/line/step-line

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:59.091148+00:00

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

- Step Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Step Line Chart The normal line chart connects two points by straight line directly, while the step line chart, also known as square wave chart, uses only horizontal and vertical lines to connect the nearby items together.
- Compared with the normal line chart, the step line chart significantly shows the sudden changes of analyzed data.
- In ECharts, step is used to characterize the connection type of the step line chart.
- It has three available values: 'start' , 'end' , and 'middle' .

Extracted text:

Step Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts

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

Step Line Chart

The normal line chart connects two points by straight line directly, while the step line chart, also known as square wave chart, uses only horizontal and vertical lines to connect the nearby items together. Compared with the normal line chart, the step line chart significantly shows the sudden changes of analyzed data.

In ECharts,

step

is used to characterize the connection type of the step line chart. It has three available values:

'start'

,

'end'

, and

'middle'

. For item A and B, these values corresponded that the corner occurred at A, B, and mid-point between A and B.

option = { legend: {}, xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: { type: 'value' }, series: [ { name: 'Step Start', type: 'line', step: 'start', data: [120, 132, 101, 134, 90, 230, 210] }, { name: 'Step Middle', type: 'line', step: 'middle', data: [220, 282, 201, 234, 290, 430, 410] }, { name: 'Step End', type: 'line', step: 'end', data: [450, 432, 401, 454, 590, 530, 510] } ] };

option

=

{

legend

:

{

}

,

xAxis

:

{

type

:

'category'

,

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

type

:

'value'

}

,

series

:

[

{

name

:

'Step Start'

,

type

:

'line'

,

step

:

'start'

,

data

:

[

120

,

132

,

101

,

134

,

90

,

230

,

210

]

}

,

{

name

:

'Step Middle'

,

type

:

'line'

,

step

:

'middle'

,

data

:

[

220

,

282

,

201

,

234

,

290

,

430

,

410

]

}

,

{

name

:

'Step End'

,

type

:

'line'

,

step

:

'end'

,

data

:

[

450

,

432

,

401

,

454

,

590

,

530

,

510

]

}

]

}

;

live

Please focus on the difference of line between three separate types.

Contributors

Edit this page on GitHub

pissang
