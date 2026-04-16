---
title: Stacked Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/line/stacked-line
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:56.886817+00:00
kind: extracted-doc
---

# Stacked Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/line/stacked-line

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:56.886817+00:00

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

- Stacked Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Stacked Line Chart Similar to the Stacked Bar Chart , Stacked Line Chart use the 'stack' in series to decide which series should be stacked together.
- option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 43, 49], type: 'line', stack: 'x' }, { data: [5, 4, 3, 5, 10], type: 'line', stack: 'x' } ] }; option = { xAxis : { data : [ 'A' , 'B' , 'C' , 'D' , 'E' ] } , yAxis : { } , series : [ { data : [ 10 , 22 , 28 , 43 , 49 ] , type : 'line' , stack : 'x' } , { data : [ 5 , 4 , 3 , 5 , 10 ] , type : 'line' , stack : 'x' } ] } ; live However, without clarification, it is hard for us to judge whether it is a stacked line chart or normal line chart.
- Therefore, filling color for the area under the line is recommended to indicate for a stacked line chart.
- option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 43, 49], type: 'line', stack: 'x', areaStyle: {} }, { data: [5, 4, 3, 5, 10], type: 'line', stack: 'x', areaStyle: {} } ] }; option = { xAxis : { data : [ 'A' , 'B' , 'C' , 'D' , 'E' ] } , yAxis : { } , series : [ { data : [ 10 , 22 , 28 , 43 , 49 ] , type : 'line' , stack : 'x' , areaStyle : { } } , { data : [ 5 , 4 , 3 , 5 , 10 ] , type : 'line' , stack : 'x' , areaStyle : { } } ] } ; live Contributors Edit this page on GitHub vincentbernat pissang omkar787

Extracted text:

Stacked Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts

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

Stacked Line Chart

Similar to the

Stacked Bar Chart

, Stacked Line Chart use the

'stack'

in

series

to decide which series should be stacked together.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 43, 49], type: 'line', stack: 'x' }, { data: [5, 4, 3, 5, 10], type: 'line', stack: 'x' } ] };

option

=

{

xAxis

:

{

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

yAxis

:

{

}

,

series

:

[

{

data

:

[

10

,

22

,

28

,

43

,

49

]

,

type

:

'line'

,

stack

:

'x'

}

,

{

data

:

[

5

,

4

,

3

,

5

,

10

]

,

type

:

'line'

,

stack

:

'x'

}

]

}

;

live

However, without clarification, it is hard for us to judge whether it is a stacked line chart or normal line chart. Therefore, filling color for the area under the line is recommended to indicate for a stacked line chart.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 43, 49], type: 'line', stack: 'x', areaStyle: {} }, { data: [5, 4, 3, 5, 10], type: 'line', stack: 'x', areaStyle: {} } ] };

option

=

{

xAxis

:

{

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

yAxis

:

{

}

,

series

:

[

{

data

:

[

10

,

22

,

28

,

43

,

49

]

,

type

:

'line'

,

stack

:

'x'

,

areaStyle

:

{

}

}

,

{

data

:

[

5

,

4

,

3

,

5

,

10

]

,

type

:

'line'

,

stack

:

'x'

,

areaStyle

:

{

}

}

]

}

;

live

Contributors

Edit this page on GitHub

vincentbernat

pissang

omkar787
