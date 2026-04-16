---
title: Canvas vs. SVG - Best Practices - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/best-practices/canvas-vs-svg
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:10.157565+00:00
kind: extracted-doc
---

# Canvas vs. SVG - Best Practices - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/best-practices/canvas-vs-svg

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:23:10.157565+00:00

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

- SVG - Best Practices - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Render with SVG or Canvas Most browser-side chart libraries use SVG or Canvas as the underlying renderer.
- Generally, both technologies are interchangeable and have a similar effect.
- However, the difference may be notable in some specific scenarios and cases.
- As a result, it's always a hard choice to decide which technology to render charts.

Extracted text:

Canvas vs. SVG - Best Practices - Handbook - Apache ECharts

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

Render with SVG or Canvas

Most browser-side chart libraries use SVG or Canvas as the underlying renderer. Generally, both technologies are interchangeable and have a similar effect. However, the difference may be notable in some specific scenarios and cases. As a result, it's always a hard choice to decide which technology to render charts.

Canvas has been used as the renderer of ECharts from the beginning. Since

v4.0

, ECharts has provided the SVG renderer as an additional option. You can specify the

renderer parameter

as

'canvas'

or

'svg'

when initializing the chart.

SVG and Canvas have a significant difference in use. The uniform support for both technologies in ECharts is attributed to the abstraction and implementation of the underlying library

ZRender

.

How to Choose a Renderer

Generally, Canvas is more suitable for charts with a large number of elements (heat map, large-scale line or scatter plot in geo or parallel coordinates, etc.), and with visual

effect

. However, SVG has an important advantage: It has less memory usage (which is important for mobile devices) and won't be blurry when zooming in.

The choice of renderer can be based on a combination of hardware and software environment, data volume and functional requirements.

In scenarios where the hardware and software environment is good and the amount of data is not too large, both renderers will work and there is not much need to agonize over them.

In scenarios where the environment is poor and performance issues arise that require optimization, experimentation can be used to determine which renderer to use. For example, there are these experiences.

In situations where many instances of ECharts have to be created and the browser is prone to crashing (probably because the number of Canvas is causing the memory footprint to exceed the phone's capacity), the SVG renderer can be used to make improvements. Roughly speaking, the SVG renderer may work better if the chart is running on a low-end Android, or if we are using specific charts such as the

LiquidFill chart

.

For larger amounts of data (>1k is an experience value), canvas renderer is always recommended.

We strongly welcome

feedback

from developers on their experiences and scenarios to help us make better optimizations.

Note: Currently, some special effects still relies on Canvas: e.g.

trail effect

,

heatmap with blending effect

, etc.

Since

v5.3.0

, the SVG renderer got refactored using the Virtual DOM, the performance got improved by 2-10 times and it can even be dozens of times in some specific scenarios! Refer to

#836

for more details.

How to Use the Renderer

If

echarts

is fully imported in the following way, it already automatically imported and registered the SVG renderer and the Canvas renderer.

import

*

as

echarts

from

'echarts'

;

If you are using

tree-shakable import

, you will need to import the required renderers manually.

import

*

as

echarts

from

'echarts/core'

;

// You can use only the renderers you need

import

{

SVGRenderer

,

CanvasRenderer

}

from

'echarts/renderers'

;

echarts

.

use

(

[

SVGRenderer

,

CanvasRenderer

]

)

;

Then you can set the

renderer parameter

when initializing the chart.

// Use the Canvas renderer (default)

var

chart

=

echarts

.

init

(

containerDom

,

null

,

{

renderer

:

'canvas'

}

)

;

// Equivalent to

var

chart

=

echarts

.

init

(

containerDom

)

;

// use the SVG renderer

var

chart

=

echarts

.

init

(

containerDom

,

null

,

{

renderer

:

'svg'

}

)

;

Contributors

Edit this page on GitHub

plainheart

pissang

mrbrianevans
