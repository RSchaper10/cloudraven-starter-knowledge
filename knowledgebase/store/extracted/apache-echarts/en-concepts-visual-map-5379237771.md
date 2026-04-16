---
title: Visual Mapping - Concepts - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/concepts/visual-map
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:50.695429+00:00
kind: extracted-doc
---

# Visual Mapping - Concepts - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/concepts/visual-map

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:50.695429+00:00

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

- Visual Mapping - Concepts - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Visual Map of Data Data visualization is a procedure of mapping data into visual elements.
- This procedure can also be called visual coding, and visual elements can also be called visual channels.
- Every type of charts in Apache ECharts TM has this built-in mapping procedure.
- For example, line chart map data into lines , bar chart map data into height .

Extracted text:

Visual Mapping - Concepts - Handbook - Apache ECharts

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

Visual Map of Data

Data visualization is a procedure of mapping data into visual elements. This procedure can also be called visual coding, and visual elements can also be called visual channels.

Every type of charts in Apache ECharts

TM

has this built-in mapping procedure. For example, line chart map data into

lines

, bar chart map data into

height

. Some more complicated charts, like

graph

,

themeRiver

, and

treemap

have their own built-in mapping.

Besides, ECharts provides

visualMap component

for general visual mapping. Visual elements allowed in

visualMap

component are:

symbol

,

symbolSize

color

,

opacity

,

colorAlpha

,

colorLightness

,

colorSaturation

,

colorHue

Next, we are going to introduce how to use

visualMap

component.

Data and Dimension

Data are usually stored in

series.data

in ECharts. Depending on chart types, like list, tree, graph, and so on, the form of data may vary somehow. But they have one common feature, that they are a collection of data items. Every data item contains data value, and other information if needed. Every data value can be a single value (one dimension) or an array (multiple dimensions).

For example,

series.data

is the most common form, which is a

list

, a common array:

series

:

{

data

:

[

{

// every item here is a dataItem

value

:

2323

,

// this is data value

itemStyle

:

{

}

}

,

1212

,

// it can also be a value of dataItem, which is a more common case

2323

,

// every data value here is one dimension

4343

,

3434

]

;

}

series

:

{

data

:

[

{

// every item here is a dataItem

value

:

[

3434

,

129

,

'San Marino'

]

,

// this is data value

itemStyle

:

{

}

}

,

[

1212

,

5454

,

'Vatican'

]

,

// it can also be a value of dataItem, which is a more common case

[

2323

,

3223

,

'Nauru'

]

,

// every data value here is three dimension

[

4343

,

23

,

'Tuvalu'

]

// If is scatter chart, usually map the first dimension to x axis,

// the second dimension to y axis,

// and the third dimension to symbolSize

]

;

}

Usually the first one or two dimensions are used for mapping. For example, map the first dimension to x axis, and the second dimension to y axis. If you want to represent more dimensions,

visualMap

is what you need. Most likely,

scatter charts

use radius to represent the third dimension.

The visualMap Component

visualMap component defines the mapping from

which dimension of data

to

what visual elements

.

The following two types of visualMap components are supported, identified with

visualMap.type

.

Its structure is defined as:

option

=

{

visualMap

:

[

// can define multiple visualMap components at the same time

{

// the first visualMap component

type

:

'continuous'

// defined as continuous visualMap

// ...

}

,

{

// the second visualMap component

type

:

'piecewise'

// defined as discrete visualMap

// ...

}

]

// ...

}

;

Continuous and Piecewise Visual Mapping Components

The visual mapping component of ECharts is divided into continuous (

visualMapContinuous

) and piecewise (

visualMapPiecewise

).

Continuous means that the data dimension for visual mapping is a continuous value, while piecewise means that the data is divided into multiple segments or discrete data.

Continuous Visual Mapping

Continuous type visual mapping can determine the range of visual mapping by specifying the maximum and minimum values.

option

=

{

visualMap

:

[

{

type

:

'continuous'

,

min

:

0

,

max

:

5000

,

dimension

:

3

,

// the fourth dimension of series.data (i.e. value[3]) is mapped

seriesIndex

:

4

,

// The fourth series is mapped.

inRange

:

{

// The visual configuration in the selected range

color

:

[

'blue'

,

'#121122'

,

'red'

]

,

// A list of colors that defines the graph color mapping

// the minimum value of the data is mapped to 'blue', and

// the maximum value is mapped to 'red', // the maximum value is mapped to 'red', // the maximum value is mapped to 'red'.

// The rest is automatically calculated linearly.

symbolSize

:

[

30

,

100

]

// Defines the mapping range for the graphic size.

// The minimum value of the data is mapped to 30, // and the maximum value is mapped to 100.

// The maximum value is mapped to 100.

// The rest is calculated linearly automatically.

}

,

outOfRange

:

{

// Check the out of range visual configuration

symbolSize

:

[

30

,

100

]

}

}

// ...

]

}

;

where

visualMap.inRange

indicates the style used for data within the data mapping range; while

visualMap.outOfRange

specifies the style for data outside the mapping range.

visualMap.dimension

specifies which dimension of the data will be visually mapped.

Piecewise Visual Mapping

The piecewise visual mapping component has three modes.

Continuous data average segmentation: based on

visualMap-piecewise.splitNumber

to automatically split the data into pieces equally.

Continuous data custom segmentation: define the range of each piece based on

visualMap-piecewise.pieces

.

Discrete data (categorical data): categories are defined in

visualMap-piecewise.categories

.

To use segmented visual map, you need to set

type

to

'piecewise'

and choose one of the above three configuration items.

Contributors

Edit this page on GitHub

KrzysztofMadejski

pissang
