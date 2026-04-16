---
title: Waterfall - Bar - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/bar/waterfall
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:55.441578+00:00
kind: extracted-doc
---

# Waterfall - Bar - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/bar/waterfall

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:55.441578+00:00

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

- Waterfall - Bar - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Waterfall There is no waterfall series in Apache ECharts, but we can simulate the effect using a stacked bar chart.
- Assuming that the values in the data array represent an increase or decrease from the previous value.
- var data = [ 900 , 345 , 393 , - 108 , - 154 , 135 , 178 , 286 , - 119 , - 361 , - 203 ] ; That is, the first data is 900 and the second data 345 represents the addition of 345 to 900 , etc.
- When presenting this data as a stepped waterfall chart, we can use three series: the first is a non-interactive transparent series to implement the suspension bar effect, the second series is used to represent positive numbers, and the third series is used to represent negative numbers.

Extracted text:

Waterfall - Bar - Common Charts - How To Guides - Handbook - Apache ECharts

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

Waterfall

There is no waterfall series in Apache ECharts, but we can simulate the effect using a stacked bar chart.

Assuming that the values in the data array represent an increase or decrease from the previous value.

var

data

=

[

900

,

345

,

393

,

-

108

,

-

154

,

135

,

178

,

286

,

-

119

,

-

361

,

-

203

]

;

That is, the first data is

900

and the second data

345

represents the addition of

345

to

900

, etc. When presenting this data as a stepped waterfall chart, we can use three series: the first is a non-interactive transparent series to implement the suspension bar effect, the second series is used to represent positive numbers, and the third series is used to represent negative numbers.

var data = [900, 345, 393, -108, -154, 135, 178, 286, -119, -361, -203]; var help = []; var positive = []; var negative = []; for (var i = 0, sum = 0; i < data.length; ++i) { if (data[i] >= 0) { positive.push(data[i]); negative.push('-'); } else { positive.push('-'); negative.push(-data[i]); } if (i === 0) { help.push(0); } else { sum += data[i - 1]; if (data[i] < 0) { help.push(sum + data[i]); } else { help.push(sum); } } } option = { title: { text: 'Waterfall' }, grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true }, xAxis: { type: 'category', splitLine: { show: false }, data: (function() { var list = []; for (var i = 1; i <= 11; i++) { list.push('Oct/' + i); } return list; })() }, yAxis: { type: 'value' }, series: [ { type: 'bar', stack: 'all', itemStyle: { normal: { barBorderColor: 'rgba(0,0,0,0)', color: 'rgba(0,0,0,0)' }, emphasis: { barBorderColor: 'rgba(0,0,0,0)', color: 'rgba(0,0,0,0)' } }, data: help }, { name: 'positive', type: 'bar', stack: 'all', data: positive }, { name: 'negative', type: 'bar', stack: 'all', data: negative, itemStyle: { color: '#f33' } } ] };

var

data

=

[

900

,

345

,

393

,

-

108

,

-

154

,

135

,

178

,

286

,

-

119

,

-

361

,

-

203

]

;

var

help

=

[

]

;

var

positive

=

[

]

;

var

negative

=

[

]

;

for

(

var

i

=

0

,

sum

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

data

[

i

]

>=

0

)

{

positive

.

push

(

data

[

i

]

)

;

negative

.

push

(

'-'

)

;

}

else

{

positive

.

push

(

'-'

)

;

negative

.

push

(

-

data

[

i

]

)

;

}

if

(

i

===

0

)

{

help

.

push

(

0

)

;

}

else

{

sum

+=

data

[

i

-

1

]

;

if

(

data

[

i

]

<

0

)

{

help

.

push

(

sum

+

data

[

i

]

)

;

}

else

{

help

.

push

(

sum

)

;

}

}

}

option

=

{

title

:

{

text

:

'Waterfall'

}

,

grid

:

{

left

:

'3%'

,

right

:

'4%'

,

bottom

:

'3%'

,

containLabel

:

true

}

,

xAxis

:

{

type

:

'category'

,

splitLine

:

{

show

:

false

}

,

data

:

(

function

(

)

{

var

list

=

[

]

;

for

(

var

i

=

1

;

i

<=

11

;

i

++

)

{

list

.

push

(

'Oct/'

+

i

)

;

}

return

list

;

}

)

(

)

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

type

:

'bar'

,

stack

:

'all'

,

itemStyle

:

{

normal

:

{

barBorderColor

:

'rgba(0,0,0,0)'

,

color

:

'rgba(0,0,0,0)'

}

,

emphasis

:

{

barBorderColor

:

'rgba(0,0,0,0)'

,

color

:

'rgba(0,0,0,0)'

}

}

,

data

:

help

}

,

{

name

:

'positive'

,

type

:

'bar'

,

stack

:

'all'

,

data

:

positive

}

,

{

name

:

'negative'

,

type

:

'bar'

,

stack

:

'all'

,

data

:

negative

,

itemStyle

:

{

color

:

'#f33'

}

}

]

}

;

live

Contributors

Edit this page on GitHub

plainheart

pissang
