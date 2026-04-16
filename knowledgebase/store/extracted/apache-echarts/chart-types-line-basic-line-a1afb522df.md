---
title: Basic Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/line/basic-line
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:56.152745+00:00
kind: extracted-doc
---

# Basic Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/line/basic-line

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:56.152745+00:00

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

- Basic Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Basic Line Chart Simple Example We can use the following code to build a line chart which has x-axis as category , y-axis as value : option = { xAxis: { type: 'category', data: ['A', 'B', 'C'] }, yAxis: { type: 'value' }, series: [ { data: [120, 200, 150], type: 'line' } ] }; option = { xAxis : { type : 'category' , data : [ 'A' , 'B' , 'C' ] } , yAxis : { type : 'value' } , series : [ { data : [ 120 , 200 , 150 ] , type : 'line' } ] } ; live In this case, we set the type of axis to category and value under xAxis and yAxis .
- We also clarified the content on the x-axis through data .
- In series , we set the type to line , and specify the values of three points through data .
- In this way, we got a simple line chart.

Extracted text:

Basic Line - Line - Common Charts - How To Guides - Handbook - Apache ECharts

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

Basic Line Chart

Simple Example

We can use the following code to build a line chart which has x-axis as

category

, y-axis as

value

:

option = { xAxis: { type: 'category', data: ['A', 'B', 'C'] }, yAxis: { type: 'value' }, series: [ { data: [120, 200, 150], type: 'line' } ] };

option

=

{

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

'A'

,

'B'

,

'C'

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

data

:

[

120

,

200

,

150

]

,

type

:

'line'

}

]

}

;

live

In this case, we set the type of axis to

category

and

value

under

xAxis

and

yAxis

. We also clarified the content on the x-axis through

data

. In

series

, we set the type to

line

, and specify the values of three points through

data

. In this way, we got a simple line chart.

The

type

here can be omitted because the defaults of the axis are

value

while

xAxis

has specified the category's

data

. In this case,

ECharts

can recognize that this is a category axis.

Line Chart in Cartesian Coordinate System

How to implement if we want the line chart to be continuous? The answer is simple, as long as every value in

data

of the

series

is represented by an array containing two elements.

option = { xAxis: {}, yAxis: {}, series: [ { data: [ [20, 120], [50, 200], [40, 50] ], type: 'line' } ] };

option

=

{

xAxis

:

{

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

[

20

,

120

]

,

[

50

,

200

]

,

[

40

,

50

]

]

,

type

:

'line'

}

]

}

;

live

Customized Line Chart

Line Style

Line style can be changed by

lineStyle

setting. You can specify color, line width, polyline type and opacity etc.. For details, please see the handbook

series.lineStyle

to figure out.

Here is an example of setting color, line width and type.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 23, 19], type: 'line', lineStyle: { normal: { color: 'green', width: 4, type: 'dashed' } } } ] };

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

lineStyle

:

{

normal

:

{

color

:

'green'

,

width

:

4

,

type

:

'dashed'

}

}

}

]

}

;

live

When we set the line width here, the line width of items will not change. The line style of items needs to be set separately.

Item Style

Item style can be change by

series.itemStyle

. It included

color

,

borderColor

,

borderStyle

,

borderWidth

,

borderType

,

shadowColor

,

opacity

and so on. It works the same as the

lineType

, so we will not do further discuss.

Display Value on Items.

In the series, the label of the item was specified by

series.label

. If we change the

show

under

label

to

true

, the value will be displayed by default. Otherwise, if

series.emphasis.label.show

is

true

, the label will show only if the mouse moved across the item.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 23, 19], type: 'line', label: { show: true, position: 'bottom', textStyle: { fontSize: 20 } } } ] };

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

label

:

{

show

:

true

,

position

:

'bottom'

,

textStyle

:

{

fontSize

:

20

}

}

}

]

}

;

live

Empty Data

In a

series

, there are empty data. It has some difference with

0

. While there are empty elements, the lines chart will ignore that point without pass through it----empty elements will not be connected by the points next by.

In ECharts, we use

'-'

to represent null data, It is applicable for data in other series.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [0, 22, '-', 23, 19], type: 'line' } ] };

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

0

,

22

,

'-'

,

23

,

19

]

,

type

:

'line'

}

]

}

;

live

Please note the difference between the empty data and 0.

Contributors

Edit this page on GitHub

pissang
