---
title: Chart Container - Concepts - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/concepts/chart-size
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:46.293158+00:00
kind: extracted-doc
---

# Chart Container - Concepts - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/concepts/chart-size

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:46.293158+00:00

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

- Chart Container - Concepts - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Chart Container and Size In Get Started , we introduced the API to initialize the ECharts echarts.init .
- API Document has introduced the specific meaning of each parameters.
- Please read and understand the document before reading the following content.
- Refer to several common usage scenarios, here is the example to initialize a chart and change the size.

Extracted text:

Chart Container - Concepts - Handbook - Apache ECharts

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

Chart Container and Size

In

Get Started

, we introduced the API to initialize the ECharts

echarts.init

.

API Document

has introduced the specific meaning of each parameters. Please read and understand the document before reading the following content.

Refer to several common usage scenarios, here is the example to initialize a chart and change the size.

Initialization

Define a Parent Container in HTML

In general, you need to define a

<div>

node and use the CSS to change the width and height. While initializing, import the chart into the node. Without declaring

opts.width

or

opts.height

, the size of the chart will default to the size of the node.

<

div

id

=

"

main

"

style

=

"

width

:

600px

;

height

:

400px

;

"

>

</

div

>

<

script

type

=

"

text/javascript

"

>

var myChart = echarts.init(document.getElementById('main'));

</

script

>

To be noticed, before calling

echarts.init

, you need to make sure the container already has width and height.

Specify the chart size

If the height and width of the container do not exist, or you wish the chart size not equal to the container, you can initialize the size at the beginning.

<

div

id

=

"

main

"

>

</

div

>

<

script

type

=

"

text/javascript

"

>

var myChart = echarts.init(document.getElementById('main'), null, { width: 600, height: 400 });

</

script

>

Reactive of the Container Size

Listen to the Container Size to Change the Chart Size

In some cases, we want to accordingly change the chart size while the size of containers changed.

For instance, the container has a height of 400px and a width of 100% site width. If you are willing to change the site width while stable the chart width as 100% of it, try the following method.

You can listen to

resize

of the site to catch the event that the browser is resized. Then use

echartsInstance.resize

to resize the chart.

<

style

>

#main, html, body

{

width

:

100%

;

}

#main

{

height

:

400px

;

}

</

style

>

<

div

id

=

"

main

"

>

</

div

>

<

script

type

=

"

text/javascript

"

>

var myChart = echarts.init(document.getElementById('main')); window.addEventListener('resize', function() { myChart.resize(); });

</

script

>

Tips：Sometimes we may adjust the container size by JS/CSS, but this doesn't change the page size so that the

resize

event won't be triggered. You can try the

ResizeObserver

API to cover this scenario.

State a Specific Chart Size

Except for calling

resize()

without parameters, you can state the height and width to implement the chart size different from the size of the container.

myChart

.

resize

(

{

width

:

800

,

height

:

400

}

)

;

Tips: Pay attention to how the API defined while reading the documentation.

resize()

API was sometimes mistaken for the form like

myCharts.resize(800, 400)

which do not exist.

Dispose and Rebuild of the Container Node

We assume that there exist several bookmark pages and each page contained some charts. In this case, the content in other pages will be removed in DOM when select one page. The user will not find the chart after reselecting these pages.

Essentially, this is because the container node of the charts was removed. Even if the node is added again later, the node where the graph is located no longer exists.

The correct way is, call

echartsInstance.dispose

to dispose the instance after the container was disposed, and call

echarts.init

to initialize after the container was added again.

Tips: Call

echartsInstance.dispose

to release resources while disposing the node to avoid memory leaks.

Contributors

Edit this page on GitHub

pissang

plainheart

ppd0705
