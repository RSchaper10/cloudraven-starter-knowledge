---
title: Stacked Bar - Bar - Common Charts - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/bar/stacked-bar
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:53.753049+00:00
kind: extracted-doc
---

# Stacked Bar - Bar - Common Charts - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/bar/stacked-bar

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:53.753049+00:00

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

- Stacked Bar - Bar - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Stacked Bar Chart Sometimes, we hope to not only figure series separately but also the trend of the sum.
- It's a good choice to implement it by using the stacked bar chart.
- As the name suggests, in the stacked bar chart, data in the same category will be stacked up in one column.
- The overall height of the bar explained the change of total.

Extracted text:

Stacked Bar - Bar - Common Charts - How To Guides - Handbook - Apache ECharts

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

Stacked Bar Chart

Sometimes, we hope to not only figure series separately but also the trend of the sum. It's a good choice to implement it by using the stacked bar chart. As the name suggests, in the stacked bar chart, data in the same category will be stacked up in one column. The overall height of the bar explained the change of total.

There is a simple way to implement a stacked bar chart by ECharts. You need to set the same string type value for a group of series in

stack

. The series with the same

stack

value will be in the same category.

option = { xAxis: { data: ['A', 'B', 'C', 'D', 'E'] }, yAxis: {}, series: [ { data: [10, 22, 28, 43, 49], type: 'bar', stack: 'x' }, { data: [5, 4, 3, 5, 10], type: 'bar', stack: 'x' } ] };

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

'bar'

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

'bar'

,

stack

:

'x'

}

]

}

;

live

In this case, the position of the second series is based on the position of the first series, the height increased is corresponding to the first series' height. Therefore, from the position of the second series, you can find the changing trend of the sum of the two.

The value of

stack

explained what series will be stacked up together. Theoretically, the specific value of 'stack' is meaningless. However, we prefer some suggestive strings for the convenience of reading.

For instance, here is a chart with 4 series that counted the amount of male and female. "adult male" and "boy" need to be stacked while "adult female" and "girl" need to be stacked. In this case, the suggestive value of

stack

is

'male'

and

'female'

. Although meaningless strings like

'a'

and

'b'

can achieve the same effect but the code will have worse readability.

Contributors

Edit this page on GitHub

pissang
