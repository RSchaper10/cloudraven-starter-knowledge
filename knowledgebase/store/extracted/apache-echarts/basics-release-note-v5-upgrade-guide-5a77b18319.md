---
title: Migration from v4 to v5 - What's New - Basics - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/basics/release-note/v5-upgrade-guide
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:41.787841+00:00
kind: extracted-doc
---

# Migration from v4 to v5 - What's New - Basics - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/basics/release-note/v5-upgrade-guide

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:41.787841+00:00

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

- Migration from v4 to v5 - What's New - Basics - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Apache ECharts 5 Upgrade Guide This guide is for those who want to upgrade from echarts 4.x (hereafter v4 ) to echarts 5.x (hereafter v5 ).
- You can find out what new features v5 brings that are worth upgrading in New Features in ECharts 5 .
- In most cases, developers won't need to do anything extra for this upgrade, as echarts has always tried to keep the API as stable and backward-compatible as possible.
- However, v5 still brings some breaking changes that require special attention.

Extracted text:

Migration from v4 to v5 - What's New - Basics - Handbook - Apache ECharts

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

Apache ECharts 5 Upgrade Guide

This guide is for those who want to upgrade from echarts 4.x (hereafter

v4

) to echarts 5.x (hereafter

v5

). You can find out what new features

v5

brings that are worth upgrading in

New Features in ECharts 5

. In most cases, developers won't need to do anything extra for this upgrade, as echarts has always tried to keep the API as stable and backward-compatible as possible. However,

v5

still brings some breaking changes that require special attention. In addition, in some cases,

v5

provides a better API to replace the previous one, and these superseded APIs will no longer be recommended (though we have tried to be as compatible as possible with these changes). We'll try to explain these changes in detail in this document.

Breaking Changes

Default Theme

First of all, the default theme has been changed.

v5

has made a lot of changes and optimizations on the theme design. If you still want to keep the colors of the old version, you can manually declare the colors as follows.

chart

.

setOption

(

{

color

:

[

'#c23531'

,

'#2f4554'

,

'#61a0a8'

,

'#d48265'

,

'#91c7ae'

,

'#749f83'

,

'#ca8622'

,

'#bda29a'

,

'#6e7074'

,

'#546570'

,

'#c4ccd3'

]

// ...

}

)

;

Or, to make a simple

v4

theme.

var

themeEC4

=

{

color

:

[

'#c23531'

,

'#2f4554'

,

'#61a0a8'

,

'#d48265'

,

'#91c7ae'

,

'#749f83'

,

'#ca8622'

,

'#bda29a'

,

'#6e7074'

,

'#546570'

,

'#c4ccd3'

]

}

;

var

chart

=

echarts

.

init

(

dom

,

themeEC4

)

;

chart

.

setOption

(

/* ... */

)

;

Importing ECharts

Removing Support for Default Exports

Since

v5

, echarts only provides

named exports

.

So if you are importing

echarts

like this:

import

echarts

from

'echarts'

;

// Or import core module

import

echarts

from

'echarts/lib/echarts'

;

It will throw error in

v5

. You need to change the code as follows to import the entire module.

import

*

as

echarts

from

'echarts'

;

// Or

import

*

as

echarts

from

'echarts/lib/echarts'

;

Tree-shaking API

In 5.0.1, we introduced the new

tree-shaking API

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

}

from

'echarts/charts'

;

import

{

GridComponent

}

from

'echarts/components'

;

// Note that the Canvas renderer is no longer included by default and needs to be imported explictly, or import the SVGRenderer if you need to use the SVG rendering mode

import

{

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

BarChart

,

GridComponent

,

CanvasRenderer

]

)

;

To make it easier for you to know which modules you need to import based on your option, our new example page adds a new feature to generate the three-shakable code, you can check the

Full Code

tab on the example page to see the modules you need to introduce and the related code.

In most cases, we recommend using the new tree-shaking interface whenever possible, as it maximizes the power of the packaging tool tree-shaking and effectively resolves namespace conflicts and prevents the exposure of internal structures. If you are still using the CommonJS method of writing modules, the previous approach is still supported:

const

echarts

=

require

(

'echarts/lib/echarts'

)

;

require

(

'echarts/lib/chart/bar'

)

;

require

(

'echarts/lib/component/grid'

)

;

Second, because our source code has been rewritten using TypeScript,

v5

will no longer support importing files from

echarts/src

. You need to change it to import from

echarts/lib

.

Dependency Changes

Note: This section is only for developers who use tree-shaking interfaces to ensure a minimal bundle size, not for those who imports the whole package.

In order to keep the size of the bundle small enough, we remove some dependencies that would have been imported by default. For example, as mentioned above, when using the new on-demand interface,

CanvasRenderer

is no longer included by default, which ensures that unneeded Canvas rendering code is not imported when only SVG rendering mode is used, and in addition, the following dependencies are adjusted.

The right-angle coordinate system component is no longer introduced by default when using line charts and bar charts, so the following introduction method was used before

const

echarts

=

require

(

'echarts/lib/echarts'

)

;

require

(

'echarts/lib/chart/bar'

)

;

require

(

'echarts/lib/chart/line'

)

;

Need to introduce the

grid

component separately again

require

(

'echarts/lib/component/grid'

)

;

Reference issues:

#14080

,

#13764

aria

components are no longer imported by default. You need import it manually if necessary.

import

{

AriaComponent

}

from

'echarts/components'

;

echarts

.

use

(

AriaComponent

)

;

Or

require

(

'echarts/lib/component/aria'

)

;

Built-in GeoJSON Removed

v5

removes the built-in geoJSON (previously in the

echarts/map

folder). These geoJSON files were always sourced from third parties. If users still need them, they can go get them from the old version, or find more appropriate data and register it with ECharts via the registerMap interface.

Browser Compatibility

IE8 is no longer supported by

v5

. We no longer maintain and upgrade the previous

VML renderer

for IE8 compatibility. If developers have a strong need for a VML renderer, they are welcome to submit a pull request to upgrade the VML renderer or maintain a separate third-party VML renderer, as we support registration of standalone renderers starting with

v5.0.1

.

Configuration Item Adjustment

Axis-Line and Axis-Tick of Y-Axis (Value Axis) Are Hidden by Default

The axis line and axis ticks of the Y axis (

value

axis) has been hidden by default since

v5

. If you prefer the previous style, you will need to explicitly configure as follows,

yAxis

:

{

type

:

'value'

,

// explicitly set `axisLine.show` & `axisTick.show` as `true`

axisLine

:

{

show

:

true

}

,

axisTick

:

{

show

:

true

}

}

Visual Style Settings Priority Changes

The priority of the visuals between

visualMap component

and

itemStyle

|

lineStyle

|

areaStyle

are reversed since

v5

.

That is, previously in

v4

, the visuals (i.e., color, symbol, symbolSize, ...) that generated by

visualMap component

has the highest priority, which will overwrite the same visuals settings in

itemStyle

|

lineStyle

|

areaStyle

. That brought troubles when needing to specify specific style to some certain data items while using

visualMap component

. Since

v5

, the visuals specified in

itemStyle

|

lineStyle

|

areaStyle

has the highest priority.

In most cases, users will probably not notice this change when migrating from

v4

to

v5

. But users can still check that if

visualMap component

and

itemStyle

|

lineStyle

|

areaStyle

are both specified.

padding

for Rich Text

v5

adjusts the

rich.?.padding

to make it more compliant with CSS specifications. In

v4

, for example

rich. .padding: [11, 22, 33, 44]

means that

padding-top

is

33

and

padding-bottom

is

11

. The position of the top and bottom is adjusted in

v5

,

rich. .padding: [11, 22, 33, 44]

means that

padding-top

is

11

and

padding-bottom

is

33

.

If the user is using

rich.?.padding

, this order needs to be adjusted.

Extensions

These extensions need to be upgraded to new version to support echarts

v5

:

echarts-gl

echarts-wordcloud

echarts-liquidfill

Deprecated APIs

Some of the API and echarts options are deprecated since

v5

, but are still backward compatible. Users can

keep using these deprecated API

, with only some warning will be printed to console in dev mode. But if users have spare time, it is recommended to upgraded to new API for the consideration of long term maintenance.

The deprecated API and their corresponding new API are listed as follows:

Transform related props of a graphic element are changed:

Changes:

position: [number, number]

are changed to

x: number

/

y: number

.

scale: [number, number]

are changed to

scaleX: number

/

scaleY: number

.

origin: [number, number]

are changed to

originX: number

/

originY: number

.

The

position

,

scale

and

origin

are still supported but deprecated.

It effects these places:

In the

graphic

components: the declarations of each element.

In

custom series

: the declarations of each element in the return of

renderItem

.

Directly use zrender graphic elements.

Text related props on graphic elements are changed:

Changes:

The declaration of attached text (or say, rect text) are changed.

Prop

style.text

are deprecated in elements except

Text

. Instead, Prop set

textContent

and

textConfig

are provided to support more powerful capabilities.

These related props at the left part below are deprecated. Use the right part below instead.

textPosition => textConfig.position

textOffset => textConfig.offset

textRotation => textConfig.rotation

textDistance => textConfig.distance

The props at the left part below are deprecated in

style

and

style.rich.?

. Use the props at the right part below instead.

textFill => fill

textStroke => stroke

textFont => font

textStrokeWidth => lineWidth

textAlign => align

textVerticalAlign => verticalAlign

textLineHeight => lineHeight

textWidth => width

textHeight => hight

textBackgroundColor => backgroundColor

textPadding => padding

textBorderColor => borderColor

textBorderWidth => borderWidth

textBorderRadius => borderRadius

textBoxShadowColor => shadowColor

textBoxShadowBlur => shadowBlur

textBoxShadowOffsetX => shadowOffsetX

textBoxShadowOffsetY => shadowOffsetY

Note: these props are not changed:

textShadowColor

textShadowBlur

textShadowOffsetX

textShadowOffsetY

It effects these places:

In the

graphic

components: the declarations of each element. [compat, but not accurately the same in some complicated cases.]

In

custom series

: the declarations of each element in the return of

renderItem

. [compat, but not accurately the same in some complicated cases].

Directly use zrender API to create graphic elements. [No compat, breaking change].

API on chart instance:

chart.one(...)

is deprecated.

label

:

In props

color

,

textBorderColor

,

backgroundColor

and

borderColor

, the value

'auto'

is deprecated. Use the value

'inherit'

instead.

hoverAnimation

:

option

series.hoverAnimation

is deprecated. Use

series.emphasis.scale

instead.

line series

:

option

series.clipOverflow

is deprecated. Use

series.clip

instead.

custom series

:

In

renderItem

, the

api.style(...)

and

api.styleEmphasis(...)

are deprecated. Because it is not really necessary and hard to ensure backward compatibility. Users can fetch system designated visual by

api.visual(...)

.

sunburst series

:

Action type

sunburstHighlight

is deprecated. Use

highlight

instead.

Action type

sunburstUnhighlight

is deprecated. Use

downplay

instead.

option

series.downplay

is deprecated. Use

series.blur

instead.

option

series.highlightPolicy

is deprecated. Use

series.emphasis.focus

instead.

pie series

:

The action type at the left part below are deprecated. Use the right part instead:

pieToggleSelect

=>

toggleSelect

pieSelect

=>

select

pieUnSelect

=>

unselect

The event type at the left part below are deprecated. Use the right part instead:

pieselectchanged

=>

selectchanged

pieselected

=>

selected

pieunselected

=>

unselected

option

series.label.margin

is deprecated. Use

series.label.edgeDistance

instead.

option

series.clockWise

is deprecated. Use

series.clockwise

instead.

option

series.hoverOffset

is deprecated. Use

series.emphasis.scaleSize

instead.

map series

:

The action type at the left part below are deprecated. Use the right part instead:

mapToggleSelect

=>

toggleSelect

mapSelect

=>

select

mapUnSelect

=>

unselect

The event type at the left part below are deprecated. Use the right part instead:

mapselectchanged

=>

selectchanged

mapselected

=>

selected

mapunselected

=>

unselected

option

series.mapType

is deprecated. Use

series.map

instead.

option

series.mapLocation

is deprecated.

graph series

:

option

series.focusNodeAdjacency

is deprecated. Use

series.emphasis: { focus: 'adjacency'}

instead.

gauge series

:

option

series.clockWise

is deprecated. Use

series.clockwise

instead.

option

series.hoverOffset

is deprecated. Use

series.emphasis.scaleSize

instead.

dataZoom component

:

option

dataZoom.handleIcon

need prefix

path://

if using SVGPath.

radar

:

option

radar.name

is deprecated. Use

radar.axisName

instead.

option

radar.nameGap

is deprecated. Use

radar.axisNameGap

instead.

Parse and format:

echarts.format.formatTime

is deprecated. Use

echarts.time.format

instead.

echarts.number.parseDate

is deprecated. Use

echarts.time.parse

instead.

echarts.format.getTextRect

is deprecated.

Contributors

Edit this page on GitHub

plainheart

Ovilia

fuchunhui

pissang
