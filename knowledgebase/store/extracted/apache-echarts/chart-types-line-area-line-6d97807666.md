---
title: Area Chart - Line - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/line/area-line
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:57.598514+00:00
kind: extracted-doc
---

# Area Chart - Line - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/line/area-line

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:57.598514+00:00

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

- Area Chart - Line - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Area Chart The area chart fills the space between the line and axis with the background color, to express the data by the size of the area.
- Compared with the normal line chart, the area chart has more intuitive visual effects.
- It is especially suitable for the scenario with a few series.
- option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 23, 19], type: 'line', areaStyle: {} }, { data: [25, 14, 23, 35, 10], type: 'line', areaStyle: { color: '#ff0', opacity: 0.5 } } ] }; option = { xAxis : { data : [ 'A' , 'B' , 'C' , 'D' , 'E' ] } , yAxis : { } , series : [ { data : [ 10 , 22 , 28 , 23 , 19 ] , type : 'line' , areaStyle : { } } , { data : [ 25 , 14 , 23 , 35 , 10 ] , type : 'line' , areaStyle : { color : '#ff0' , opacity : 0.5 } } ] } ; live If you want to change the area style of the line chart, try to use areaStyle .

Extracted text:

Area Chart - Line - Common Charts - How To Guides - Handbook - Apache ECharts

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

Area Chart

The area chart fills the space between the line and axis with the background color, to express the data by the size of the area. Compared with the normal line chart, the area chart has more intuitive visual effects. It is especially suitable for the scenario with a few series.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 23, 19], type: 'line', areaStyle: {} }, { data: [25, 14, 23, 35, 10], type: 'line', areaStyle: { color: '#ff0', opacity: 0.5 } } ] };

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

23

,

19

]

,

type

:

'line'

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

25

,

14

,

23

,

35

,

10

]

,

type

:

'line'

,

areaStyle

:

{

color

:

'#ff0'

,

opacity

:

0.5

}

}

]

}

;

live

If you want to change the area style of the line chart, try to use

areaStyle

. Set

'areaStyle'

to

{}

to use the default type: use the color of series to fill the area in translucent. If you want to change the style, try to override the configuration items in

'areaStyle'

. For example, the color of the second series was changed to yellow with 50% opacity.

Contributors

Edit this page on GitHub

pissang
