---
title: Basic Scatter - Scatter - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/scatter/basic-scatter
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:02.396671+00:00
kind: extracted-doc
---

# Basic Scatter - Scatter - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/scatter/basic-scatter

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:23:02.396671+00:00

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

- Basic Scatter - Scatter - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Basic Scatter Chart Scatter Chart, a frequently used chart type, was constructed with several "points".
- These points sometimes represent the position of the value in the coordinate system (cartesian coordinate system, geo coordinate system, etc.), sometimes the size and color of items can be mapped to the value, represent high-dimensional data.
- Simple Example The following example is a basic scatter chart configuration with the x-axis as category and the y-axis as value: option = { xAxis: { data: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] }, yAxis: {}, series: [ { type: 'scatter', data: [220, 182, 191, 234, 290, 330, 310] } ] }; option = { xAxis : { data : [ 'Sun' , 'Mon' , 'Tue' , 'Wed' , 'Thu' , 'Fri' , 'Sat' ] } , yAxis : { } , series : [ { type : 'scatter' , data : [ 220 , 182 , 191 , 234 , 290 , 330 , 310 ] } ] } ; live Scatter Chart in Cartesian Coordinate System In the previous case, the x-axis of the scatter chart is a discrete category axis and the y-axis is a continuous value axis.
- However, the normal scene for the scatter chart is to have 2 continuous value axis (also called the cartesian coordinate system).

Extracted text:

Basic Scatter - Scatter - Common Charts - How To Guides - Handbook - Apache ECharts

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

Basic Scatter Chart

Scatter Chart, a frequently used chart type, was constructed with several "points". These points sometimes represent the position of the value in the coordinate system (cartesian coordinate system, geo coordinate system, etc.), sometimes the size and color of items can be mapped to the value, represent high-dimensional data.

Simple Example

The following example is a basic scatter chart configuration with the x-axis as category and the y-axis as value:

option = { xAxis: { data: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] }, yAxis: {}, series: [ { type: 'scatter', data: [220, 182, 191, 234, 290, 330, 310] } ] };

option

=

{

xAxis

:

{

data

:

[

'Sun'

,

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

'scatter'

,

data

:

[

220

,

182

,

191

,

234

,

290

,

330

,

310

]

}

]

}

;

live

Scatter Chart in Cartesian Coordinate System

In the previous case, the x-axis of the scatter chart is a discrete category axis and the y-axis is a continuous value axis. However, the normal scene for the scatter chart is to have 2 continuous value axis (also called the cartesian coordinate system). The series type is different in that both x-axis and y-axis value are included in

data

, but not in

xAxis

and

yAxis

.

option = { xAxis: {}, yAxis: {}, series: [ { type: 'scatter', data: [ [10, 5], [0, 8], [6, 10], [2, 12], [8, 9] ] } ] };

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

type

:

'scatter'

,

data

:

[

[

10

,

5

]

,

[

0

,

8

]

,

[

6

,

10

]

,

[

2

,

12

]

,

[

8

,

9

]

]

}

]

}

;

live

Customized Scatter Chart

Symbol Style

Symbol refers to the item shape in a scatter chart. There are three types of config available. The first is ECharts built-in shape, the second is image, the last is the SVG path.

The built-in shape in ECharts included:

'circle'

,

'rect'

(rectangle),

'roundRect'

(rounded rectangle),

'triangle'

,

'diamond'

,

'pin'

and

'arrow'

. To use built-in shapes, you need to state the

symbol

to the corresponding string.

If you want to define the shape as any image, try to use

'image'

following by the path, eg.

'image://http://example.com/xxx.png'

or

'image://./xxx.png'

.

ECharts

symbol

also supports SVG vector graphics. You can define

symbol

as an SVG file path that starts with

'path://'

to locate the vector graphics. The advantages of vector graphics are smaller size and no jagged or blurred.

Method to find the SVG path: Open an

SVG

path; Find the path similar as

<path d="M… L…"></path>

; Add

d

's value after

'path://'

. Let's check how to define an item to vector shape of heart.

Firstly, we need an

SVG

file of a heart. You can draw one by vector editing software, or download one from the internet. Here is the content:

<?xml version="1.0" encoding="iso-8859-1"?>

<

svg

version

=

"

1.1

"

xmlns

=

"

http://www.w3.org/2000/svg

"

xmlns:

xlink

=

"

http://www.w3.org/1999/xlink

"

x

=

"

0px

"

y

=

"

0px

"

viewBox

=

"

0 0 51.997 51.997

"

style

=

"

enable-background:new 0 0 51.997 51.997;

"

xml:

space

=

"

preserve

"

>

<

path

d

=

"

M51.911,16.242C51.152,7.888,45.239,1.827,37.839,1.827c-4.93,0-9.444,2.653-11.984,6.905 c-2.517-4.307-6.846-6.906-11.697-6.906c-7.399,0-13.313,6.061-14.071,14.415c-0.06,0.369-0.306,2.311,0.442,5.478 c1.078,4.568,3.568,8.723,7.199,12.013l18.115,16.439l18.426-16.438c3.631-3.291,6.121-7.445,7.199-12.014 C52.216,18.553,51.97,16.611,51.911,16.242z

"

/>

</

svg

>

In ECharts, define config

symbol

as a path of d:

option = { xAxis: { data: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] }, yAxis: {}, series: [ { type: 'scatter', data: [220, 182, 191, 234, 290, 330, 310], symbolSize: 20, symbol: 'path://M51.911,16.242C51.152,7.888,45.239,1.827,37.839,1.827c-4.93,0-9.444,2.653-11.984,6.905 c-2.517-4.307-6.846-6.906-11.697-6.906c-7.399,0-13.313,6.061-14.071,14.415c-0.06,0.369-0.306,2.311,0.442,5.478 c1.078,4.568,3.568,8.723,7.199,12.013l18.115,16.439l18.426-16.438c3.631-3.291,6.121-7.445,7.199-12.014 C52.216,18.553,51.97,16.611,51.911,16.242z' } ] };

option

=

{

xAxis

:

{

data

:

[

'Sun'

,

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

'scatter'

,

data

:

[

220

,

182

,

191

,

234

,

290

,

330

,

310

]

,

symbolSize

:

20

,

symbol

:

'path://M51.911,16.242C51.152,7.888,45.239,1.827,37.839,1.827c-4.93,0-9.444,2.653-11.984,6.905 c-2.517-4.307-6.846-6.906-11.697-6.906c-7.399,0-13.313,6.061-14.071,14.415c-0.06,0.369-0.306,2.311,0.442,5.478 c1.078,4.568,3.568,8.723,7.199,12.013l18.115,16.439l18.426-16.438c3.631-3.291,6.121-7.445,7.199-12.014 C52.216,18.553,51.97,16.611,51.911,16.242z'

}

]

}

;

live

In this way, we have a heart vector of the item.

Symbol Size

The size of symbol is defined by

series.symbolSize

. It can be s pixel value of the item size, or an array included two numbers, to define the width and height.

Besides, it can be defined as a call back function. Here is an example of the format:

(

value

:

Array

|

number

,

params

:

Object

)

=>

number

|

Array

;

The first argument is the data value, and the second argument included other arguments of the data item. In the following instance, we define the size of the item proportional related to the data value.

option = { xAxis: { data: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] }, yAxis: {}, series: [ { type: 'scatter', data: [220, 182, 191, 234, 290, 330, 310], symbolSize: function(value) { return value / 10; } } ] };

option

=

{

xAxis

:

{

data

:

[

'Sun'

,

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

'scatter'

,

data

:

[

220

,

182

,

191

,

234

,

290

,

330

,

310

]

,

symbolSize

:

function

(

value

)

{

return

value

/

10

;

}

}

]

}

;

live

Contributors

Edit this page on GitHub

pissang
