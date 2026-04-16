---
title: Custom Series - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/custom-series
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:03.120027+00:00
kind: extracted-doc
---

# Custom Series - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/custom-series

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:23:03.120027+00:00

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

- Custom Series - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Custom Series Custom series allow for the customization of graphic element rendering within a series, enabling the extension of various chart types.
- This article will introduce how to develop or use custom series.
- For more detailed information, please refer to the Option API .
- Registerable Custom Series (New) Starting from Apache ECharts v6.0.0, we support registerable custom series and provide several custom series that can be installed directly via NPM in echarts-custom-series .

Extracted text:

Custom Series - How To Guides - Handbook - Apache ECharts

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

Custom Series

Custom series allow for the customization of graphic element rendering within a series, enabling the extension of various chart types. This article will introduce how to develop or use custom series. For more detailed information, please refer to the

Option API

.

Registerable Custom Series (New)

Starting from Apache ECharts v6.0.0, we support registerable custom series and provide several custom series that can be installed directly via NPM in

echarts-custom-series

.

You can directly use the custom series in this project to develop charts, use custom series published by others, or develop your own custom series (which will be introduced in detail later) and use them in a similar way. First, let's look at the simplest way—using officially published custom series.

Using Published Custom Series

Below, we take the range bar chart as an example to introduce how to use published custom series.

The documentation for the range bar chart is at

echarts-custom-series/custom-series/barRange

, which includes detailed introductions, APIs, and examples.

In short, when using a published custom series, you first need to download it using a command like

npm install @echarts-x/custom-bar-range

, and then choose the usage method based on your development environment.

For example, if you are using it in a web environment without additional bundling tools, the simplest way is:

<

script

src

=

"

./node_modules/echarts/dist/echarts.js

"

>

</

script

>

<

script

src

=

"

./node_modules/@echarts-x/custom-bar-range/dist/bar-range.auto.js

"

>

</

script

>

<

script

>

// No need to call echarts.use(), automatically registered const chart = echarts.init(...); const option = { series: [{ type: 'custom', renderItem: 'barRange', data: [ [0, 26.7, 32.5], [1, 25.3, 32.4], [2, 24.6, 32.7], [3, 26.8, 35.8], [4, 26.2, 33.1], [5, 24.9, 31.4], [6, 25.3, 32.9] ], itemPayload: { barWidth: 10, borderRadius: 5, }, encode: { x: 0, y: [1, 2], tooltip: [1, 2], } }] }; chart.setOption(option);

</

script

>

The

auto

in

bar-range.auto.js

means that when it is loaded, it will automatically register the custom series to the

echarts

global variable. Developers do not need to register it manually; they only need to specify

type: 'custom'

in

setOption

and specify the name of the custom series used via

renderItem: 'barRange'

.

You usually need to pass parameters to the custom series through

itemPayload

. You can find its configurable parameters in the README of each custom series.

Note that you usually need to configure

encode

to specify data mapping. You can find the recommended usage for each custom series in its README and examples.

Developing Your Own Custom Series

You can refer to the source code of

echarts-custom-series

to learn how to develop custom series. It is recommended to fork the project and use

npm run generate xxx

to generate a new custom series framework. It also provides scaffolding for compilation, documentation, examples, etc., which can help you quickly develop new custom series.

The main development task is to implement a

renderItem

. For documentation, see the

Configuration Manual

.

If you develop a general-purpose custom series, it is recommended to submit it via a Pull Request so that more developers can use it.

Non-Registerable Custom Series

If the custom series you develop is not intended for reuse, you can also implement the rendering algorithm for the custom series directly in

renderItem

. You can find many examples in the

Official Custom Series Examples

and develop based on them.

Contributors

Edit this page on GitHub

Ovilia
