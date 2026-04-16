# Import ECharts - Basics - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/basics/import

Dependency:

- Apache ECharts

Collected at:

- 2026-04-15T19:45:00.999664+00:00

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

- Import ECharts - Basics - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Using ECharts as an NPM Package There are two approaches to using ECharts as a package.
- The simplest approach is to make all functionality immediately available by importing from echarts .
- However, it is encouraged to substantially decrease bundle size by only importing as necessary such as echarts/core and echarts/charts .
- Install ECharts via NPM You can install ECharts via npm using the following command npm install echarts Import All ECharts Functionality To include all of ECharts, we simply need to import echarts .

Extracted text:

Import ECharts - Basics - Handbook - Apache ECharts

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

Using ECharts as an NPM Package

There are two approaches to using ECharts as a package. The simplest approach is to make all functionality immediately available by importing from

echarts

. However, it is encouraged to substantially decrease bundle size by only importing as necessary such as

echarts/core

and

echarts/charts

.

Install ECharts via NPM

You can install ECharts via npm using the following command

npm install echarts

Import All ECharts Functionality

To include all of ECharts, we simply need to import

echarts

.

import

*

as

echarts

from

'echarts'

;

// Create the echarts instance

var

myChart

=

echarts

.

init

(

document

.

getElementById

(

'main'

)

)

;

// Draw the chart

myChart

.

setOption

(

{

title

:

{

text

:

'ECharts Getting Started Example'

}

,

tooltip

:

{

}

,

xAxis

:

{

data

:

[

'shirt'

,

'cardigan'

,

'chiffon'

,

'pants'

,

'heels'

,

'socks'

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

name

:

'sales'

,

type

:

'bar'

,

data

:

[

5

,

20

,

36

,

10

,

10

,

20

]

}

]

}

)

;

Shrinking Bundle Size

The above code will import all the charts and components in ECharts, but if you don't want to bring in all the components, you can use the tree-shakeable interface provided by ECharts to bundle the required components and get a minimal bundle.

// Import the echarts core module, which provides the necessary interfaces for using echarts.

import

*

as

echarts

from

'echarts/core'

;

// Import bar charts, all suffixed with Chart

import

{

BarChart

}

from

'echarts/charts'

;

// Import the title, tooltip, rectangular coordinate system, dataset and transform components

import

{

TitleComponent

,

TooltipComponent

,

GridComponent

,

DatasetComponent

,

TransformComponent

}

from

'echarts/components'

;

// Features like Universal Transition and Label Layout

import

{

LabelLayout

,

UniversalTransition

}

from

'echarts/features'

;

// Import the Canvas renderer

// Note that including the CanvasRenderer or SVGRenderer is a required step

import

{

CanvasRenderer

}

from

'echarts/renderers'

;

// Register the required components

echarts

.

use

(

[

BarChart

,

TitleComponent

,

TooltipComponent

,

GridComponent

,

DatasetComponent

,

TransformComponent

,

LabelLayout

,

UniversalTransition

,

CanvasRenderer

]

)

;

// The chart is initialized and configured in the same manner as before

var

myChart

=

echarts

.

init

(

document

.

getElementById

(

'main'

)

)

;

myChart

.

setOption

(

{

// ...

}

)

;

Note that in order to keep the size of the package to a minimum, ECharts does not provide any renderer in the tree-shakeable interface, so you need to choose to import

CanvasRenderer

or

SVGRenderer

as the renderer. The advantage of this is that if you only need to use the SVG rendering mode, the bundle will not include the

CanvasRenderer

module, which is not needed.

The "Full Code" tab on our sample editor page provides a very convenient way to generate a tree-shakable code. It will generate tree-shakable code based on the current option dynamically to use it directly in your project.

Creating an Option Type in TypeScript

For developers who are using TypeScript to develop ECharts, type interface is provided to create a minimal

EChartsOption

type. This type will be stricter than the default one provided because it will know exactly what components are being used. This can help you check for missing components or charts more effectively.

import

*

as

echarts

from

'echarts/core'

;

import

{

BarChart

,

LineChart

,

}

from

'echarts/charts'

;

import

{

TitleComponent

,

TooltipComponent

,

GridComponent

,

// Dataset

DatasetComponent

,

// Built-in transform (filter, sort)

TransformComponent

}

from

'echarts/components'

;

import

{

LabelLayout

,

UniversalTransition

}

from

'echarts/features'

;

import

{

CanvasRenderer

}

from

'echarts/renderers'

;

import

type

{

// The series option types are defined with the SeriesOption suffix

BarSeriesOption

,

LineSeriesOption

,

}

from

'echarts/charts'

;

import

type

{

// The component option types are defined with the ComponentOption suffix

TitleComponentOption

,

TooltipComponentOption

,

GridComponentOption

,

DatasetComponentOption

}

from

'echarts/components'

;

import

type

{

ComposeOption

,

}

from

'echarts/core'

;

// Create an Option type with only the required components and charts via ComposeOption

type

ECOption

=

ComposeOption

<

|

BarSeriesOption

|

LineSeriesOption

|

TitleComponentOption

|

TooltipComponentOption

|

GridComponentOption

|

DatasetComponentOption

>

;

// Register the required components

echarts

.

use

(

[

TitleComponent

,

TooltipComponent

,

GridComponent

,

DatasetComponent

,

TransformComponent

,

BarChart

,

LineChart

,

LabelLayout

,

UniversalTransition

,

CanvasRenderer

]

)

;

const

option

:

ECOption

=

{

// ...

}

;

Contributors

Edit this page on GitHub

plainheart

pissang

aimuz

ikeq

zachary-svoboda-accesso

btea
