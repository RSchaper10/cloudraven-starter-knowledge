---
title: Basic Bar - Bar - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/bar/basic-bar
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:53.017748+00:00
kind: extracted-doc
---

# Basic Bar - Bar - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/bar/basic-bar

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:53.017748+00:00

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

- Basic Bar - Bar - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Basic Bar Chart Bar Chart, is a chart that presents the comparisons among discrete data.
- The length of the bars is proportionally related to the categorical data.
- To set the bar chart, you need to set the type of series as 'bar' .
- [Option] Simple Example Let's begin with a basic bar chart: option = { xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] }; option = { xAxis : { data : [ 'Mon' , 'Tue' , 'Wed' , 'Thu' , 'Fri' , 'Sat' , 'Sun' ] } , yAxis : { } , series : [ { type : 'bar' , data : [ 23 , 24 , 18 , 25 , 27 , 28 , 25 ] } ] } ; live In this case, the x-axis is under the category type.

Extracted text:

Basic Bar - Bar - Common Charts - How To Guides - Handbook - Apache ECharts

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

Basic Bar Chart

Bar Chart, is a chart that presents the comparisons among discrete data. The length of the bars is proportionally related to the categorical data.

To set the bar chart, you need to set the

type

of

series

as

'bar'

.

[Option]

Simple Example

Let's begin with a basic bar chart:

option = { xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] } ] };

option

=

{

xAxis

:

{

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

data

:

[

23

,

24

,

18

,

25

,

27

,

28

,

25

]

}

]

}

;

live

In this case, the x-axis is under the category type. Therefore, you should define some corresponding values for

'xAxis'

. Meanwhile, the data type of the y-axis is numerical. The range of the y-axis will be generated automatically by the

data

in

'series'

.

Multi-series Bar Chart

You may use a series to represent a group of related data. To show multiple series in the same chart, you need to add one more array under the

series

.

option = { xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 27, 28, 25] }, { type: 'bar', data: [26, 24, 18, 22, 23, 20, 27] } ] };

option

=

{

xAxis

:

{

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

data

:

[

23

,

24

,

18

,

25

,

27

,

28

,

25

]

}

,

{

type

:

'bar'

,

data

:

[

26

,

24

,

18

,

22

,

23

,

20

,

27

]

}

]

}

;

live

Customized Bar Chart

Styles

It is a good idea to install the style of Bar Chart by using

'series.itemStyle'

. Description of the SCI:

Color of column(

'color'

);

Outline color(

'borderColor'

), width(

'borderWidth'

), type(

'borderType'

) of column;

Border radius of column(

'barBorderRadius'

);

Transparency(

'opacity'

);

Shadow type(

'shadowBlur'

,

'shadowColor'

,

'shadowOffsetX'

,

'shadowOffsetY'

)

Here is a example:

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { type: 'bar', data: [ 10, 22, 28, { value: 43, // Specify the style for single bar itemStyle: { color: '#91cc75', shadowColor: '#91cc75', borderType: 'dashed', opacity: 0.5 } }, 49 ], itemStyle: { barBorderRadius: 5, borderWidth: 1, borderType: 'solid', borderColor: '#73c0de', shadowColor: '#5470c6', shadowBlur: 3 } } ] };

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

type

:

'bar'

,

data

:

[

10

,

22

,

28

,

{

value

:

43

,

// Specify the style for single bar

itemStyle

:

{

color

:

'#91cc75'

,

shadowColor

:

'#91cc75'

,

borderType

:

'dashed'

,

opacity

:

0.5

}

}

,

49

]

,

itemStyle

:

{

barBorderRadius

:

5

,

borderWidth

:

1

,

borderType

:

'solid'

,

borderColor

:

'#73c0de'

,

shadowColor

:

'#5470c6'

,

shadowBlur

:

3

}

}

]

}

;

live

In this case, we defined the style of the bar chart by

'itemStyle'

of corresponding

series

. For complete configuration items and their usage, please check the configuration item manual:

series.itemStyle

。

Width and Height of Column

You can use

barWidth

to change the width of the bar. For instance, the

'barWidth'

in the following case was set to

'20%'

. It indicates that width of each bar is 20% of the category width. As there are 5 data in every series, 20%

'barWidth'

means 4% for the entire x-axis.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { type: 'bar', data: [10, 22, 28, 43, 49], barWidth: '20%' } ] };

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

type

:

'bar'

,

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

barWidth

:

'20%'

}

]

}

;

live

In addition,

barMaxWidth

has limited the maximum width of the bar. For some small value, you can declare a minimum height for the bar:

barMinHeight

. When the corresponding height of data is smaller than the limit, ECharts will take 'barMinHeight' as the replaced height.

Column Spacing

There are two kinds of column spacing. One is the spacing between different series under the same category:

barGap

. The other is the spacing between categories:

barCategoryGap

.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { type: 'bar', data: [23, 24, 18, 25, 18], barGap: '20%', barCategoryGap: '40%' }, { type: 'bar', data: [12, 14, 9, 9, 11] } ] };

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

type

:

'bar'

,

data

:

[

23

,

24

,

18

,

25

,

18

]

,

barGap

:

'20%'

,

barCategoryGap

:

'40%'

}

,

{

type

:

'bar'

,

data

:

[

12

,

14

,

9

,

9

,

11

]

}

]

}

;

live

In this case, the

barGap

is

'20%'

. That means the distance between bars under the same category is 20% of the bar width. For instance, if we set the

barCategoryGap

to

'40%'

, the gap on each side of the bar will take 40% place in categories (compared with the width of the column).

Usually,

barWidth

is not necessary to be clarified if

'barGap'

and

barCategoryGap

was set. If you need to make sure the bar is not too wide while the graph is large, try to use

barMaxWidth

to limit the maximum width of bars.

In the same cartesian coordinate system, the property will be shared by several column series. To make sure it takes effect on the graph, please set the property on the last bar chart series of the system.

Add Background Color for Bars

You might want to change the background color of bars sometimes. After ECharts v4.7.0, this function can be enabled by

'showBackground'

and configured by

'backgroundStyle'

.

option = { xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: { type: 'value' }, series: [ { data: [120, 200, 150, 80, 70, 110, 130], type: 'bar', showBackground: true, backgroundStyle: { color: 'rgba(220, 220, 220, 0.8)' } } ] };

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

data

:

[

120

,

200

,

150

,

80

,

70

,

110

,

130

]

,

type

:

'bar'

,

showBackground

:

true

,

backgroundStyle

:

{

color

:

'rgba(220, 220, 220, 0.8)'

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
