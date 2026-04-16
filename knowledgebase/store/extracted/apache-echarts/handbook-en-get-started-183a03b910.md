---
title: Get Started - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/get-started/
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:35.910187+00:00
kind: extracted-doc
---

# Get Started - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/get-started/

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:35.910187+00:00

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

- Get Started - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Get Started Getting Apache ECharts Apache ECharts supports several download methods, which are further explained in the next tutorial Installation .
- Here, we take the example of getting it from the jsDelivr CDN and explain how to install it quickly.
- At https://www.jsdelivr.com/package/npm/echarts select dist/echarts.js , click and save it as echarts.js file.
- More information about these files can be found in the next tutorial Installation .

Extracted text:

Get Started - Handbook - Apache ECharts

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

Get Started

Getting Apache ECharts

Apache ECharts supports several download methods, which are further explained in the next tutorial

Installation

. Here, we take the example of getting it from the

jsDelivr

CDN and explain how to install it quickly.

At

https://www.jsdelivr.com/package/npm/echarts

select

dist/echarts.js

, click and save it as

echarts.js

file.

More information about these files can be found in the next tutorial

Installation

.

Including ECharts

Create a new

index.html

file in the directory where you just saved

echarts.js

, with the following content:

<!

DOCTYPE

html

>

<

html

>

<

head

>

<

meta

charset

=

"

utf-8

"

/>

<!-- Include the ECharts file you just downloaded -->

<

script

src

=

"

echarts.js

"

>

</

script

>

</

head

>

</

html

>

When you open this

index.html

, you will see an empty page. But don't worry. Open the console and make sure that no error message is reported, then you can proceed to the next step.

Plotting a Simple Chart

Before drawing we need to prepare a DOM container for ECharts with a defined height and width. Add the following code after the

</head>

tag introduced earlier.

<

body

>

<!-- Prepare a DOM with a defined width and height for ECharts -->

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

</

body

>

Then you can initialize an echarts instance with the

echarts.init

method and set the echarts instance with

setOption

method to generate a simple bar chart. Here is the complete code.

<!

DOCTYPE

html

>

<

html

>

<

head

>

<

meta

charset

=

"

utf-8

"

/>

<

title

>

ECharts

</

title

>

<!-- Include the ECharts file you just downloaded -->

<

script

src

=

"

echarts.js

"

>

</

script

>

</

head

>

<

body

>

<!-- Prepare a DOM with a defined width and height for ECharts -->

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

// Initialize the echarts instance based on the prepared dom var myChart = echarts.init(document.getElementById('main')); // Specify the configuration items and data for the chart var option = { title: { text: 'ECharts Getting Started Example' }, tooltip: {}, legend: { data: ['sales'] }, xAxis: { data: ['Shirts', 'Cardigans', 'Chiffons', 'Pants', 'Heels', 'Socks'] }, yAxis: {}, series: [ { name: 'sales', type: 'bar', data: [5, 20, 36, 10, 10, 20] } ] }; // Display the chart using the configuration items and data just specified. myChart.setOption(option);

</

script

>

</

body

>

</

html

>

And this is your first chart with Apache ECharts!

Contributors

Edit this page on GitHub

plainheart

Ovilia

randyl

pissang
