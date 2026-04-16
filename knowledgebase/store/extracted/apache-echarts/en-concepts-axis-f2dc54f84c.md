---
title: Axis - Concepts - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/concepts/axis
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:49.969275+00:00
kind: extracted-doc
---

# Axis - Concepts - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/concepts/axis

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:49.969275+00:00

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

- Axis - Concepts - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Axis The x/y-axis in the Cartesian coordinate system.
- x-axis, y-axis Both x-axis and y-axis included axis line, tick, label and title.
- Some chart will use the grid to assist the data viewing and calculating.
- A normal 2D coordinate system has x-axis and y-axis.

Extracted text:

Axis - Concepts - Handbook - Apache ECharts

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

Axis

The x/y-axis in the Cartesian coordinate system.

x-axis, y-axis

Both x-axis and y-axis included axis line, tick, label and title. Some chart will use the grid to assist the data viewing and calculating.

A normal 2D coordinate system has x-axis and y-axis. X-axis located at the bottom while y-axis at the left side in common. The Config is shown below:

option

=

{

xAxis

:

{

// ...

}

,

yAxis

:

{

// ...

}

// ...

}

;

The x-axis is usually used to declare the number of categories which was also called the aspects of observing the data: "Sales Time", "Sales Location" and "product name", etc.. The y-axis usually used to indicate the numerical value of categories. These data are used to examine the quantitative value of a certain type of data or some indicator you need to analyze, such as "Sales Quantity" and "Sales Price".

option

=

{

xAxis

:

{

type

:

'time'

,

name

:

'Sales Time'

// ...

}

,

yAxis

:

{

type

:

'value'

,

name

:

'Sales Quantity'

// ...

}

// ...

}

;

When x-axis has a large span, we can use the zoom method to display part of the data in the chart.

option

=

{

xAxis

:

{

type

:

'time'

,

name

:

'Sales Time'

// ...

}

,

yAxis

:

{

type

:

'value'

,

name

:

'Sales Quantity'

// ...

}

,

dataZoom

:

[

]

// ...

}

;

In two-dimensional data, there can be more than two axes. There are usually two x or y axes at the same time in ECharts. You can change the config

offset

to avoid overlaps of axes at the same place. X-axes can be displayed at the top and bottom, y-axes at left and right.

option

=

{

xAxis

:

{

type

:

'time'

,

name

:

'Sales Time'

// ...

}

,

yAxis

:

[

{

type

:

'value'

,

name

:

'Sales Quantity'

// ...

}

,

{

type

:

'value'

,

name

:

'Sales Price'

// ...

}

]

// ...

}

;

Axis Line

ECharts provide the config of

axisLine

. You can change the setting according to the demand, such as the arrow on two sides and the style of axes.

option

=

{

xAxis

:

{

axisLine

:

{

symbol

:

'arrow'

,

lineStyle

:

{

type

:

'dashed'

// ...

}

}

// ...

}

,

yAxis

:

{

axisLine

:

{

symbol

:

'arrow'

,

lineStyle

:

{

type

:

'dashed'

// ...

}

}

}

// ...

}

;

Tick

ECharts provide the config

axisTick

. You can change the setting according to the demand, such as the length of ticks, and the style of ticks.

option

=

{

xAxis

:

{

axisTick

:

{

length

:

6

,

lineStyle

:

{

type

:

'dashed'

// ...

}

}

// ...

}

,

yAxis

:

{

axisTick

:

{

length

:

6

,

lineStyle

:

{

type

:

'dashed'

// ...

}

}

}

// ...

}

;

Label

ECharts provide the config

axisLabel

. You can change the setting according to the demand, such as the text alignment and the customized label content.

option

=

{

xAxis

:

{

axisLabel

:

{

formatter

:

'{value} kg'

,

align

:

'center'

// ...

}

// ...

}

,

yAxis

:

{

axisLabel

:

{

formatter

:

'{value} ¥'

,

align

:

'center'

// ...

}

}

// ...

}

;

Example

The y-axis on the left side represents the monthly average temperature in Tokyo, the y-axis on the right side represents the precipitation of Tokyo. The x-axis represents the time. It reflects the trend and relation between the average temperature and precipitation.

option = { tooltip: { trigger: 'axis', axisPointer: { type: 'cross' } }, legend: {}, xAxis: [ { type: 'category', axisTick: { alignWithLabel: true }, axisLabel: { rotate: 30 }, data: [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ] } ], yAxis: [ { type: 'value', name: 'Precipitation', min: 0, max: 250, position: 'right', axisLabel: { formatter: '{value} ml' } }, { type: 'value', name: 'Temperature', min: 0, max: 25, position: 'left', axisLabel: { formatter: '{value} °C' } } ], series: [ { name: 'Precipitation', type: 'bar', yAxisIndex: 0, data: [6, 32, 70, 86, 68.7, 100.7, 125.6, 112.2, 78.7, 48.8, 36.0, 19.3] }, { name: 'Temperature', type: 'line', smooth: true, yAxisIndex: 1, data: [ 6.0, 10.2, 10.3, 11.5, 10.3, 13.2, 14.3, 16.4, 18.0, 16.5, 12.0, 5.2 ] } ] };

option

=

{

tooltip

:

{

trigger

:

'axis'

,

axisPointer

:

{

type

:

'cross'

}

}

,

legend

:

{

}

,

xAxis

:

[

{

type

:

'category'

,

axisTick

:

{

alignWithLabel

:

true

}

,

axisLabel

:

{

rotate

:

30

}

,

data

:

[

'January'

,

'February'

,

'March'

,

'April'

,

'May'

,

'June'

,

'July'

,

'August'

,

'September'

,

'October'

,

'November'

,

'December'

]

}

]

,

yAxis

:

[

{

type

:

'value'

,

name

:

'Precipitation'

,

min

:

0

,

max

:

250

,

position

:

'right'

,

axisLabel

:

{

formatter

:

'{value} ml'

}

}

,

{

type

:

'value'

,

name

:

'Temperature'

,

min

:

0

,

max

:

25

,

position

:

'left'

,

axisLabel

:

{

formatter

:

'{value} °C'

}

}

]

,

series

:

[

{

name

:

'Precipitation'

,

type

:

'bar'

,

yAxisIndex

:

0

,

data

:

[

6

,

32

,

70

,

86

,

68.7

,

100.7

,

125.6

,

112.2

,

78.7

,

48.8

,

36.0

,

19.3

]

}

,

{

name

:

'Temperature'

,

type

:

'line'

,

smooth

:

true

,

yAxisIndex

:

1

,

data

:

[

6.0

,

10.2

,

10.3

,

11.5

,

10.3

,

13.2

,

14.3

,

16.4

,

18.0

,

16.5

,

12.0

,

5.2

]

}

]

}

;

live

These are the concise intro of the usage of axis config. Check more details at:

Official Website

.

Contributors

Edit this page on GitHub

pissang
