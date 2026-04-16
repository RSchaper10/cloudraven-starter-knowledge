---
title: Drag - Interaction - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/interaction/drag
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:08.123833+00:00
kind: extracted-doc
---

# Drag - Interaction - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/interaction/drag

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:23:08.123833+00:00

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

- Drag - Interaction - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide An Example: Implement Dragging This is a tiny example, introducing how to implement dragging of graphic elements in Apache ECharts TM .
- From this example, we will see how to make an application with rich intractivity based on echarts API.
- This example mainly implements that dragging points of a curve and by which the curve is modified.
- Although it is simple example, but we can do more based on that, like edit charts viually.

Extracted text:

Drag - Interaction - How To Guides - Handbook - Apache ECharts

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

An Example: Implement Dragging

This is a tiny example, introducing how to implement dragging of graphic elements in Apache ECharts

TM

. From this example, we will see how to make an application with rich intractivity based on echarts API.

This example mainly implements that dragging points of a curve and by which the curve is modified. Although it is simple example, but we can do more based on that, like edit charts viually. So let's get started from this simple example.

Implement basic dragging

First of all, we create a basic

line chart (line series)

:

var

symbolSize

=

20

;

var

data

=

[

[

15

,

0

]

,

[

-

50

,

10

]

,

[

-

56.5

,

20

]

,

[

-

46.5

,

30

]

,

[

-

22.1

,

40

]

]

;

myChart

.

setOption

(

{

xAxis

:

{

min

:

-

100

,

max

:

80

,

type

:

'value'

,

axisLine

:

{

onZero

:

false

}

}

,

yAxis

:

{

min

:

-

30

,

max

:

60

,

type

:

'value'

,

axisLine

:

{

onZero

:

false

}

}

,

series

:

[

{

id

:

'a'

,

type

:

'line'

,

smooth

:

true

,

// Set a big symbolSize for dragging convenience.

symbolSize

:

symbolSize

,

data

:

data

}

]

}

)

;

Since the symbols in line is not draggable, we make them draggable by using

graphic component

to add draggable circular elements to symbols respectively.

myChart

.

setOption

(

{

// Declare a graphic component, which contains some graphic elements

// with the type of 'circle'.

// Here we have used the method `echarts.util.map`, which has the same

// behavior as Array.prototype.map, and is compatible with ES5-.

graphic

:

echarts

.

util

.

map

(

data

,

function

(

dataItem

,

dataIndex

)

{

return

{

// 'circle' means this graphic element is a shape of circle.

type

:

'circle'

,

shape

:

{

// The radius of the circle.

r

:

symbolSize

/

2

}

,

// Transform is used to located the circle. position:

// [x, y] means translate the circle to the position [x, y].

// The API `convertToPixel` is used to get the position of

// the circle, which will introduced later.

position

:

myChart

.

convertToPixel

(

'grid'

,

dataItem

)

,

// Make the circle invisible (but mouse event works as normal).

invisible

:

true

,

// Make the circle draggable.

draggable

:

true

,

// Give a big z value, which makes the circle cover the symbol

// in line series.

z

:

100

,

// This is the event handler of dragging, which will be triggered

// repeatly while dragging. See more details below.

// A util method `echarts.util.curry` is used here to generate a

// new function the same as `onPointDragging`, except that the

// first parameter is fixed to be the `dataIndex` here.

ondrag

:

echarts

.

util

.

curry

(

onPointDragging

,

dataIndex

)

}

;

}

)

}

)

;

In the code above, API

convertToPixel

is used to convert data to its "pixel coodinate", based on which each graphic elements can be rendered on canvas. The term "pixel coodinate" means the coordinate is in canvas pixel, whose origin is the top-left of the canvas. In the sentence

myChart.convertToPixel('grid', dataItem)

, the first parameter

'grid'

indicates that

dataItem

should be converted in the first

grid component (cartesian)

.

Notice:

convertToPixel

should not be called before the first time that

setOption

called. Namely, it can only be used after coordinate systems (grid/polar/...) initialized.

Now points have been made draggable. Then we will bind event listeners on dragging to those points.

// This function will be called repeatly while dragging.

// The mission of this function is to update `series.data` based on

// the new points updated by dragging, and to re-render the line

// series based on the new data, by which the graphic elements of the

// line series can be synchronized with dragging.

function

onPointDragging

(

dataIndex

)

{

// Here the `data` is declared in the code block in the beginning

// of this article. The `this` refers to the dragged circle.

// `this.position` is the current position of the circle.

data

[

dataIndex

]

=

myChart

.

convertFromPixel

(

'grid'

,

this

.

position

)

;

// Re-render the chart based on the updated `data`.

myChart

.

setOption

(

{

series

:

[

{

id

:

'a'

,

data

:

data

}

]

}

)

;

}

In the code above, API

convertFromPixel

is used, which is the reversed process of

convertToPixel

.

myChart.convertFromPixel('grid', this.position)

converts a pixel coordinate to data item in

grid (cartesian)

.

Finally, add those code to make graphic elements responsive to change of canvas size.

window

.

addEventListener

(

'resize'

,

function

(

)

{

// Re-calculate the position of each circle and update chart using `setOption`.

myChart

.

setOption

(

{

graphic

:

echarts

.

util

.

map

(

data

,

function

(

item

,

dataIndex

)

{

return

{

position

:

myChart

.

convertToPixel

(

'grid'

,

item

)

}

;

}

)

}

)

;

}

)

;

Add tooltip component

Now basic functionality have been implemented by parte 1. If we need the data can be displayed realtime when dragging, we can use

tooltip component

to do that. Nevertheless, tooltip component has its default "show/hide rule", which is not applicable in this case. So we need to customize the "show/hide rule" for our case.

Add these snippets to the code block above:

myChart

.

setOption

(

{

// ...,

tooltip

:

{

// Means disable default "show/hide rule".

triggerOn

:

'none'

,

formatter

:

function

(

params

)

{

return

(

'X: '

+

params

.

data

[

0

]

.

toFixed

(

2

)

+

'<br>Y: '

+

params

.

data

[

1

]

.

toFixed

(

2

)

)

;

}

}

}

)

;

myChart

.

setOption

(

{

graphic

:

data

.

map

(

function

(

item

,

dataIndex

)

{

return

{

type

:

'circle'

,

// ...,

// Customize "show/hide rule", show when mouse over, hide when mouse out.

onmousemove

:

echarts

.

util

.

curry

(

showTooltip

,

dataIndex

)

,

onmouseout

:

echarts

.

util

.

curry

(

hideTooltip

,

dataIndex

)

}

;

}

)

}

)

;

function

showTooltip

(

dataIndex

)

{

myChart

.

dispatchAction

(

{

type

:

'showTip'

,

seriesIndex

:

0

,

dataIndex

:

dataIndex

}

)

;

}

function

hideTooltip

(

dataIndex

)

{

myChart

.

dispatchAction

(

{

type

:

'hideTip'

}

)

;

}

The API

dispatchAction

is used to show/hide tooltip content, where actions

showTip

and

hideTip

is dispatched.

Full code

Full code is shown as follow:

import

echarts

from

'echarts'

;

var

symbolSize

=

20

;

var

data

=

[

[

15

,

0

]

,

[

-

50

,

10

]

,

[

-

56.5

,

20

]

,

[

-

46.5

,

30

]

,

[

-

22.1

,

40

]

]

;

var

myChart

=

echarts

.

init

(

document

.

getElementById

(

'main'

)

)

;

myChart

.

setOption

(

{

tooltip

:

{

triggerOn

:

'none'

,

formatter

:

function

(

params

)

{

return

(

'X: '

+

params

.

data

[

0

]

.

toFixed

(

2

)

+

'<br />Y: '

+

params

.

data

[

1

]

.

toFixed

(

2

)

)

;

}

}

,

xAxis

:

{

min

:

-

100

,

max

:

80

,

type

:

'value'

,

axisLine

:

{

onZero

:

false

}

}

,

yAxis

:

{

min

:

-

30

,

max

:

60

,

type

:

'value'

,

axisLine

:

{

onZero

:

false

}

}

,

series

:

[

{

id

:

'a'

,

type

:

'line'

,

smooth

:

true

,

symbolSize

:

symbolSize

,

data

:

data

}

]

}

)

;

myChart

.

setOption

(

{

graphic

:

echarts

.

util

.

map

(

data

,

function

(

item

,

dataIndex

)

{

return

{

type

:

'circle'

,

position

:

myChart

.

convertToPixel

(

'grid'

,

item

)

,

shape

:

{

r

:

symbolSize

/

2

}

,

invisible

:

true

,

draggable

:

true

,

ondrag

:

echarts

.

util

.

curry

(

onPointDragging

,

dataIndex

)

,

onmousemove

:

echarts

.

util

.

curry

(

showTooltip

,

dataIndex

)

,

onmouseout

:

echarts

.

util

.

curry

(

hideTooltip

,

dataIndex

)

,

z

:

100

}

;

}

)

}

)

;

window

.

addEventListener

(

'resize'

,

function

(

)

{

myChart

.

setOption

(

{

graphic

:

echarts

.

util

.

map

(

data

,

function

(

item

,

dataIndex

)

{

return

{

position

:

myChart

.

convertToPixel

(

'grid'

,

item

)

}

;

}

)

}

)

;

}

)

;

function

showTooltip

(

dataIndex

)

{

myChart

.

dispatchAction

(

{

type

:

'showTip'

,

seriesIndex

:

0

,

dataIndex

:

dataIndex

}

)

;

}

function

hideTooltip

(

dataIndex

)

{

myChart

.

dispatchAction

(

{

type

:

'hideTip'

}

)

;

}

function

onPointDragging

(

dataIndex

,

dx

,

dy

)

{

data

[

dataIndex

]

=

myChart

.

convertFromPixel

(

'grid'

,

this

.

position

)

;

myChart

.

setOption

(

{

series

:

[

{

id

:

'a'

,

data

:

data

}

]

}

)

;

}

With knowledge introduced above, more feature can be implemented. For example,

dataZoom component

can be added to cooperate with the cartesian, or we can make a plotting board on coordinate systems. Use your imagination ~

Contributors

Edit this page on GitHub

Ovilia

pissang
