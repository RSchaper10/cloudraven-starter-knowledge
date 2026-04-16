---
title: Bar Racing - Bar - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/bar/bar-race
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:54.680651+00:00
kind: extracted-doc
---

# Bar Racing - Bar - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/bar/bar-race

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:54.680651+00:00

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

- Bar Racing - Bar - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Dynamic Sorting Bar Chart Related Options Bar race is a chart that shows changes in the ranking of data over time and it is supported by default since ECharts 5.
- Bar race charts usually use horizontal bars.
- If you want to use vertical bars, just take the X axis and Y axis in this tutorial to the opposite.
- Set realtimeSort of the bar series to be true to enable bar race Set yAxis.inverse to be true to display longer bars at top yAxis.animationDuration is suggested to be set to be 300 for bar reordering animation for the first time yAxis.animationDurationUpdate is suggested to be set to be 300 for bar reordering animation for later times Set yAxis.max to be n - 1 where n is the number of bars to be displayed; otherwise, all bars are displayed xAxis.max is suggested to be set to be 'dataMax' so that the maximum of data is used as X maximum.

Extracted text:

Bar Racing - Bar - Common Charts - How To Guides - Handbook - Apache ECharts

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

Dynamic Sorting Bar Chart

Related Options

Bar race is a chart that shows changes in the ranking of data over time and it is supported by default since ECharts 5.

Bar race charts usually use horizontal bars. If you want to use vertical bars, just take the X axis and Y axis in this tutorial to the opposite.

Set

realtimeSort

of the bar series to be

true

to enable bar race

Set

yAxis.inverse

to be

true

to display longer bars at top

yAxis.animationDuration

is suggested to be set to be

300

for bar reordering animation for the first time

yAxis.animationDurationUpdate

is suggested to be set to be

300

for bar reordering animation for later times

Set

yAxis.max

to be

n - 1

where

n

is the number of bars to be displayed; otherwise, all bars are displayed

xAxis.max

is suggested to be set to be

'dataMax'

so that the maximum of data is used as X maximum.

If realtime label changing is required, set

series.label.valueAnimation

to be

true

Set

animationDuration

to be

0

so that the first animation doesn't start from 0; if you wish otherwise, set it to be the same value as

animationDurationUpdate

animationDurationUpdate

is suggested to be set to be

3000

for animation update duration, which should be the same as the frequency of calling

setOption

Call

setOption

to update data to be of next time with

setInterval

at the frequency of

animationDurationUpdate

Demo

A complete demo:

var data = []; for (let i = 0; i < 5; ++i) { data.push(Math.round(Math.random() * 200)); } option = { xAxis: { max: 'dataMax' }, yAxis: { type: 'category', data: ['A', 'B', 'C', 'D', 'E'], inverse: true, animationDuration: 300, animationDurationUpdate: 300, max: 2 // only the largest 3 bars will be displayed }, series: [ { realtimeSort: true, name: 'X', type: 'bar', data: data, label: { show: true, position: 'right', valueAnimation: true } } ], legend: { show: true }, animationDuration: 0, animationDurationUpdate: 3000, animationEasing: 'linear', animationEasingUpdate: 'linear' }; function run() { var data = option.series[0].data; for (var i = 0; i < data.length; ++i) { if (Math.random() > 0.9) { data[i] += Math.round(Math.random() * 2000); } else { data[i] += Math.round(Math.random() * 200); } } myChart.setOption(option); } setTimeout(function() { run(); }, 0); setInterval(function() { run(); }, 3000);

var

data

=

[

]

;

for

(

let

i

=

0

;

i

<

5

;

++

i

)

{

data

.

push

(

Math

.

round

(

Math

.

random

(

)

*

200

)

)

;

}

option

=

{

xAxis

:

{

max

:

'dataMax'

}

,

yAxis

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

,

'D'

,

'E'

]

,

inverse

:

true

,

animationDuration

:

300

,

animationDurationUpdate

:

300

,

max

:

2

// only the largest 3 bars will be displayed

}

,

series

:

[

{

realtimeSort

:

true

,

name

:

'X'

,

type

:

'bar'

,

data

:

data

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

'right'

,

valueAnimation

:

true

}

}

]

,

legend

:

{

show

:

true

}

,

animationDuration

:

0

,

animationDurationUpdate

:

3000

,

animationEasing

:

'linear'

,

animationEasingUpdate

:

'linear'

}

;

function

run

(

)

{

var

data

=

option

.

series

[

0

]

.

data

;

for

(

var

i

=

0

;

i

<

data

.

length

;

++

i

)

{

if

(

Math

.

random

(

)

>

0.9

)

{

data

[

i

]

+=

Math

.

round

(

Math

.

random

(

)

*

2000

)

;

}

else

{

data

[

i

]

+=

Math

.

round

(

Math

.

random

(

)

*

200

)

;

}

}

myChart

.

setOption

(

option

)

;

}

setTimeout

(

function

(

)

{

run

(

)

;

}

,

0

)

;

setInterval

(

function

(

)

{

run

(

)

;

}

,

3000

)

;

live

Contributors

Edit this page on GitHub

Ovilia

pissang

Shofol
