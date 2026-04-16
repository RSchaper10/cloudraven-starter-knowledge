# Migration from v5 to v6 - What's New - Basics - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/basics/release-note/v6-upgrade-guide

Dependency:

- Apache ECharts

Collected at:

- 2026-04-15T19:45:04.229410+00:00

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

- Migration from v5 to v6 - What's New - Basics - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Apache ECharts 6 Upgrade Guide This guide is for users who wish to upgrade from echarts 5.x (hereinafter referred to as v5 ) to echarts 6.x (hereinafter referred to as v6 ).
- You can learn about the new features brought by v6 in ECharts 6 New Features .
- In most cases, developers do not need to do anything extra for this upgrade, as echarts has always tried to keep the API stable and backward compatible.
- However, v6 does introduce some breaking changes that require special attention.

Extracted text:

Migration from v5 to v6 - What's New - Basics - Handbook - Apache ECharts

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

Apache ECharts 6 Upgrade Guide

This guide is for users who wish to upgrade from echarts 5.x (hereinafter referred to as

v5

) to echarts 6.x (hereinafter referred to as

v6

). You can learn about the new features brought by

v6

in

ECharts 6 New Features

. In most cases, developers do not need to do anything extra for this upgrade, as echarts has always tried to keep the API stable and backward compatible. However,

v6

does introduce some breaking changes that require special attention. In addition, in some cases,

v6

provides better APIs to replace previous ones, and these replaced APIs are no longer recommended (of course, we have tried to maintain compatibility for these changes). We will explain these changes in detail in this document.

How to Upgrade

You can download the latest source code and builds from the

official download page

. If you use npm, upgrade with:

npm install echarts@6

Breaking Changes

Default Theme

First, the default theme has changed.

v6

has made many optimizations in color schemes and theme design for better visual effects. If you want to keep the old version's colors, you can use the

echarts/theme/v5.js

theme file and initialize the chart as follows:

import

'echarts/theme/v5'

;

const

chart

=

echarts

.

init

(

document

.

getElementById

(

'container'

)

,

'v5'

)

;

Note that the new styles in

v6

not only change the theme colors, but also optimize and adjust the default positions and sizes of some components (for example, the default position of the legend is now at the bottom of the canvas). Using

echarts/theme/v5.js

can restore the previous default positions and sizes of components.

If you don't mind other changes but only want to restore the default color palette to that of v5, you can create a theme that only defines the v5 default colors:

const

colorPaletteV5

=

[

'#5470c6'

,

'#91cc75'

,

'#fac858'

,

'#ee6666'

,

'#73c0de'

,

'#3ba272'

,

'#fc8452'

,

'#9a60b4'

,

'#ea7ccc'

]

;

echarts

.

registerTheme

(

'myTheme'

,

{

color

:

colorPaletteV5

}

)

;

const

chart

=

echarts

.

init

(

document

.

getElementById

(

'container'

)

,

'myTheme'

)

;

In addition, the

echarts/src/theme/light.ts

file from v5 has been moved to

echarts/theme/rainbow.js

.

Label Position

In Cartesian coordinate systems (

grid

component), if axis names (

axisName

) or labels (

axisLabel

) previously overflowed the canvas or overlapped, the position of the axes may shift slightly after upgrading, because overflow prevention and axis name/label overlap prevention are now enabled by default. In most cases, these changes are barely noticeable. But if there are unreasonable changes, you can disable the overflow prevention by setting

grid.outerBoundsMode: 'none'

, or disable the overlap prevention by setting

xAxis/yAxis.nameMoveOverlap: false

.

Rich Text

In v6, the following styles of

rich text labels (label.rich / textStyle.rich)

:

fontStyle

,

fontWeight

,

fontSize

,

fontFamily

,

textShadowColor

,

textShadowBlur

,

textShadowOffsetX

, and

textShadowOffsetY

will inherit from the same-named styles in

plain labels (label / textStyle)

. To restore the old behavior, you can set

richInheritPlainLabel: false

at the root level of the ECharts option or in the label/textStyle option.

For example:

option

=

{

richInheritPlainLabel

:

false

,

// Usually set here.

xxx1

:

{

// Or set here to only control this label.

label

:

{

richInheritPlainLabel

:

false

,

rich

:

{

/* ... */

}

,

}

}

,

xxx2

:

{

textStyle

:

{

richInheritPlainLabel

:

false

,

rich

:

{

/* ... */

}

,

}

}

}

Contributors

Edit this page on GitHub

Ovilia
