---
title: 5.6 - What's New - Basics - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/basics/release-note/5-6-0
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:45.574953+00:00
kind: extracted-doc
---

# 5.6 - What's New - Basics - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/basics/release-note/5-6-0

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:45.574953+00:00

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

- 5.6 - What's New - Basics - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Apache ECharts 5.6.0 Features Define Region Styles in Original GeoJSON Data ECharts maps use GeoJSON format to define data.
- In theory, following the principle of "separation of data and style", GeoJSON should only define data while styles should be defined in ECharts.
- However, in some cases, styles themselves are a form of data expression (for example: using dashed lines to represent disputed borders - here the "dashed line" is a style but actually expresses a data concept, so defining styles in GeoJSON is reasonable).
- In ECharts 5.6.0, we support defining region styles in the original GeoJSON data by specifying features[].properties.echartsStyle .

Extracted text:

5.6 - What's New - Basics - Handbook - Apache ECharts

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

Apache ECharts 5.6.0 Features

Define Region Styles in Original GeoJSON Data

ECharts maps use GeoJSON format to define data. In theory, following the principle of "separation of data and style", GeoJSON should only define data while styles should be defined in ECharts. However, in some cases, styles themselves are a form of data expression (for example: using dashed lines to represent disputed borders - here the "dashed line" is a style but actually expresses a data concept, so defining styles in GeoJSON is reasonable).

In ECharts 5.6.0, we support defining region styles in the original GeoJSON data by specifying

features[].properties.echartsStyle

. This is consistent with the

data

option, which supports configuring

itemStyle

,

label

,

tooltip

etc. Example:

geoJSON

.

features

[

0

]

.

properties

.

echartsStyle

=

{

itemStyle

:

{

areaColor

:

'green'

}

}

geoJSON

.

features

[

1

]

.

properties

.

echartsStyle

=

{

selected

:

true

,

label

:

{

formatter

:

'Default Selected:\n{b}'

}

}

geoJSON

.

features

[

2

]

.

properties

.

echartsStyle

=

{

itemStyle

:

{

borderType

:

'dotted'

,

borderColor

:

'blue'

}

}

geoJSON

.

features

[

11

]

.

properties

.

echartsStyle

=

{

itemStyle

:

{

// This region will be overridden as `cyan` by the data item option

areaColor

:

'black'

}

,

tooltip

:

{

formatter

:

function

(

params

)

{

return

'This is a custom tooltip from GeoJSON: '

+

params

.

name

;

}

}

}

Axis Labels Support Tooltips

In some cases, axis labels are too long or we want to display more information on axis labels. In ECharts 5.6.0, we support adding tooltips to axis labels. The configuration is consistent with the

tooltip

option, please refer to

axis.tooltip documentation

for details.

Sunburst Chart Supports Focusing All Descendants and Ancestors

In previous versions of sunburst charts,

emphasis.focus

supported the following values:

'none'

Do not fade out other data, it's by default.

'self'

Only focus (not fade out) the element of the currently highlighted data.

'series'

Focus on all elements of the series which the currently highlighted data belongs to.

'ancestor'

Focus on all ancestor nodes. 'descendant' Focus on all descendants nodes.

In ECharts 5.6.0, we added

'relative'

, which focuses on all descendants and ancestor nodes.

Added Support for Two New Languages

In this version, support for Swedish and Persian languages has been added. With this, ECharts now supports 22 languages.

Line Chart Performance Optimization

In this version, we optimized the rendering performance of line charts, solving the problem of memory growth with time.

Complete Changelog

View the

changelog

The next major version, Apache ECharts 6.0.0, is currently being actively developed and is expected to be released in the first quarter of 2025. Stay tuned for more updates.

Contributors

Edit this page on GitHub

Ovilia
