---
title: SVG Base Map - Geo - Common Components - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/component-types/geo/svg-base-map
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:03.860287+00:00
kind: extracted-doc
---

# SVG Base Map - Geo - Common Components - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/component-types/geo/svg-base-map

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:23:03.860287+00:00

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

- SVG Base Map - Geo - Common Components - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide SVG Base Map Since v5.1.0 , ECharts support to use SVG as the base map in geo coordinate system and map series , where previously only GeoJSON is supported.
- This feature enables ECharts to display SVG in either of the render modes ( canvas render mode and svg render mode), and enables features like zoom , pan , select , emphasis , focus-blur , label , labelLayout , tooltip on SVG with only simple some ECharts options.
- Series like scatter , effectScatter , lines , custom that are available on geo coordinate system can also be positioned and displayed based on SVG base map.
- There are several examples where SVG base map is used: Beef Cuts | Organ Visualization | Flight Seatmap | SVG Map | SVG Scatter | SVG Lines | SVG Traffic Basic Usage The usage of SVG base map is the same as the usage of GeoJSON .

Extracted text:

SVG Base Map - Geo - Common Components - How To Guides - Handbook - Apache ECharts

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

SVG Base Map

Since

v5.1.0

, ECharts support to use SVG as the base map in

geo coordinate system

and

map series

, where previously only

GeoJSON

is supported.

This feature enables ECharts to display SVG in either of the render modes (

canvas

render mode and

svg

render mode), and enables features like

zoom

,

pan

,

select

,

emphasis

,

focus-blur

,

label

,

labelLayout

,

tooltip

on SVG with only simple some ECharts options. Series like

scatter

,

effectScatter

,

lines

,

custom

that are available on

geo coordinate system

can also be positioned and displayed based on SVG base map.

There are several examples where SVG base map is used:

Beef Cuts

|

Organ Visualization

|

Flight Seatmap

|

SVG Map

|

SVG Scatter

|

SVG Lines

|

SVG Traffic

Basic Usage

The usage of SVG base map is the same as the usage of

GeoJSON

.

If using it in

geo coordinate system

:

$

.

get

(

'map/organ.svg'

,

function

(

svg

)

{

// Firstly we need to register SVG raw string or parsed SVG DOM

// to echarts with a name:

echarts

.

registerMap

(

'organ_diagram'

,

{

svg

:

svg

}

)

;

var

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

'main'

)

)

;

chart

.

setOption

(

{

geo

:

{

// Reference it in echarts option.

map

:

'organ_diagram'

,

...

}

}

)

;

}

)

;

If using it in

map series

:

$

.

get

(

'map/beef_cuts.svg'

,

function

(

svg

)

{

// Firstly we need to register SVG raw string or parsed SVG DOM

// to echarts with a name:

echarts

.

registerMap

(

'beef_cuts_diagram'

,

{

svg

:

svg

}

)

;

var

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

'main'

)

)

;

chart

.

setOption

(

{

series

:

{

type

:

'map'

,

// Reference it in echarts option.

map

:

'beef_cuts_diagram'

,

...

}

}

)

;

}

)

;

Zoom and Pan

For

Geo coordinate system

option

=

{

geo

:

{

// Enable zoom and pan.

roam

:

true

,

...

}

}

;

For

map series

option

=

{

series

:

{

type

:

'map'

,

// Enable zoom and pan.

roam

:

true

,

...

}

}

;

See

roam

. See also example

SVG Map

.

Named Element

If intending to interact with some elements of SVG, we need to mark those elements in SVG firstly. That can be done simply by adding names to the target elements. The interaction related feature like

select

,

emphasis

,

focus-blur

,

label

,

labelLayout

,

tooltip

depend on those named elements.

For example, we add name attribute

name="named_rect"

only to the left SVG

path

.

<?xml version="1.0" encoding="utf-8"?>

<

svg

xmlns

=

"

http://www.w3.org/2000/svg

"

version

=

"

1.2

"

fill-rule

=

"

evenodd

"

xml:

space

=

"

preserve

"

>

<

path

name

=

"

named_rect

"

d

=

"

M 0,0 L 0,100 100,100 100,0 Z

"

fill

=

"

#765

"

/>

<

path

d

=

"

M 150,0 L 150,100 250,100 250,0 Z

"

fill

=

"

#567

"

/>

</

svg

>

Then hover on the left rect, it can be highlighted, whereas the right one can not.

Option for some certain named elements can be specified in

geo.regions

, like:

option

=

{

geo

:

{

map

:

'some_svg'

,

regions

:

[

{

name

:

'element_name_1'

,

itemStyle

:

{

...

}

}

,

{

name

:

'element_name_2'

,

itemStyle

:

{

...

}

}

]

}

}

;

Note:

These SVG elements can be named and recognized by ECharts:

rect

,

circle

,

line

,

ellipse

,

polygon

,

polyline

,

path

,

text

,

tspan

,

g

.

It is supported that multiple elements are named with the same name, will they will be highlighted/selected together.

Style Customization

Although the style (such as color, font, lineWidth, ...) of SVG Elements can be defined directly in SVG file, style of named elements can also be customized in ECharts option, which will be handy in some scenario.

Styles can be specified in

geo.itemStyle

and

series-map.itemStyle

(also includes

emphasis.itemStyle

,

select.itemStyle

,

blur.itemStyle

,

regions[i].itemStyle

,

regions[i].emphasis.itemStyle

,

regions[i].select.itemStyle

,

regions[i].blur.itemStyle

). Some default style of the named elements can also be removed here (e.g., set

emphasis.itemStyle.color: null

to prevent the fill color from changing when mouse hovering.)

Moreover, named elements can also be styled by

visualMap component

if using

series-map

. See

Beef Cuts

.

Note: Only these named elements can be styled in

itemStyle

:

rect

,

circle

,

line

,

ellipse

,

polygon

,

polyline

,

path

.

Select

Named elements can adopt "select" feature by setting

geo.selectedMode

or

series-map.selectedMode

as

'single'

or

'multiple'

. The style of element when selected can be specified in

geo.select

or

series-map.select

.

The selected names can be obtained by

geoselectchanged

event, like:

myChart

.

on

(

'geoselectchanged'

,

function

(

params

)

{

var

selectedNames

=

params

.

allSelected

[

0

]

.

name

;

console

.

log

(

'selected'

,

selectedNames

)

;

}

)

;

See

Flight Seatmap

for more details.

Emphasis and Focus-Blur

emphasis

state (highlight when hovering) can be auto adopted to named elements.

Especially,

geo.emphasis.focus

and be set as

'self'

to enable "focus-blur" feature, where all all of the other elements will be blurred when hovering on an named element.

See

Organ Visualization

for more details.

Tooltip

Tooltip can be enabled or disabled on named elements.

option

=

{

// Need to declare the root tooltip to

// enable tooltip feature on ECharts.

tooltip

:

{

}

,

geo

:

{

map

:

'some_svg'

,

tooltip

:

{

// Use `show` to enable/disable tooltip

// on geo coordinate system.

show

:

true

}

,

regions

:

[

{

name

:

'some_name1'

,

// Set named element specified tooltip option if needed.

tooltip

:

{

formatter

:

'some special tooltip 1'

}

}

,

{

name

:

'some_name2'

,

tooltip

:

{

formatter

:

'some special tooltip 2'

}

}

]

}

}

;

If intending to disable the geo tooltip when hovering a on named elements, just:

option

=

{

tooltip

:

{

}

,

geo

:

{

map

:

'some_svg'

,

tooltip

:

{

show

:

false

}

}

}

;

See

SVG Map

for more details.

Label

Although text label can be declared in SVG file directly via

<text>

/

<tspan>

, we can also use ECharts built-in label feature on named elements by specifying

geo.label

or

series-map.label

.

By default the label feature is enabled when hovering on a named element. If intending to disable it, just:

option

=

{

geo

:

{

map

:

'some_svg'

,

emphasis

:

{

label

:

{

show

:

false

}

}

}

}

;

When multiple elements need to share one label text, we have two choices:

Wrap those elements in a named

<g>

(e.g.,

<g name="name_a">

), where a single label will be displayed and located based on the bounding rect of the

<g>

.

Name those elements with the same name (e.g.,

<path name="name_b"/><path name="name_b"/>

), where multiple labels will be displayed and located based on each elements self.

For example (hover to show the labels):

Note: Only these named elements can be labeled via

label

option:

rect

,

circle

,

line

,

ellipse

,

polygon

,

polyline

,

path

,

g

.

See also

Organ Visualization

for the usage of label.

Events

Mouse events or touch events of named elements can be listened simply by:

// 'name1' is a name of a SVG element.

myChart

.

on

(

'click'

,

{

geoIndex

:

0

,

name

:

'name1'

}

,

function

(

params

)

{

console

.

log

(

params

)

;

}

)

;

Layout of SVG Base Map

By default ECharts will position the SVG base map in the center of the canvas. If need some adjust, we usually only adjust

layoutCenter

/

layoutSize

, and occasionally

<svg viewBox="...">

/

geo.boundingCoords

(difference: clip or not). In most cases they are enough.

If need some advanced precise control of the position and zoom, several concepts below can be noticed.

The layout rule and options of

geo coordinate system

and

map series

are the same. So we only demonstrate

geo coordinate system

below.

The demo above shows six

geo coordinate system

with three SVG files in a single ECharts canvas. Each two

geo

that are in the same column use the same SVG file.

Firstly, what shapes looks like is determined by SVG file itself. That is, in the demo above, determined by the

<circle>

and

viewBox

attribute (

viewBox

cut (clips) the circle). We can noticed that the final shape outlines in each column are the same (despite the difference in position, size and scratch), since they use the same SVG file.

Secondly, users can use either of the two option groups below to determine the location and the size of the

geo view port

of

geo coordinate system

according to the entire chart canvas (all of these options are measured in echarts canvas pixel, or percentage value):

layoutCenter

,

layoutSize

(recommended).

top

,

right

,

bottom

,

left

(which is used in the demo above).

In the demo above, the six geo

geo view ports

are displayed as six black squares.

Thirdly, a

bounding rect

of the SVG is determined, which is determined by methods below (all of them are measured in SVG local unit):

If

geo.boundingCoords

is specified, use it as

bounding rect

.

Else if

<svg width="..." height="...">

is specified, use

[0, 0, width, height]

as

bounding rect

. (If only

width

or only

height

is specified, only use

[0, width]

or

[0, height]

).

Else if

svg viewBox="...">

is specified, use

viewBox

as

bounding rect

.

Else use the union bounding rect of all of the SVG elements as the

bounding rect

.

If

geo.center

or

geo.zoom

is specified, transform the

bounding rect

determined by

1~4

above.

Having

bounding rect

determined, it will be placed into its corresponding

geo view port

:

If

layoutCenter

,

layoutSize

is used, the

bounding rect

will be placed at the center and as big as possible into the

geo view port

(keep aspect ratio).

If

top

,

right

,

bottom

,

left

is used, the view rect will be stretched to fill the

geo view port

entirely.

Place Series on SVG Base Map

Series like

scatter

,

effectScatter

,

lines

,

custom

that are available on

geo coordinate system

can also be positioned and displayed on SVG base map.

Note that in this kind of usage the unit of series data value is the SVG file local coords. For example:

option

=

{

geo

:

{

map

:

'some_svg'

}

,

series

:

{

type

:

'effectScatter'

,

coordinateSystem

:

'geo'

,

geoIndex

:

0

,

data

:

[

// SVG local coords.

[

488.2358421078053

,

459.70913833075736

]

,

[

770.3415644319939

,

757.9672194986475

]

,

[

1180.0329284196291

,

743.6141808346214

]

,

]

}

}

;

By the way, there is a simple approach to get SVG local coord:

myChart

.

setOption

(

{

geo

:

{

map

:

'some_svg'

}

}

)

;

myChart

.

getZr

(

)

.

on

(

'click'

,

function

(

params

)

{

var

pixelPoint

=

[

params

.

offsetX

,

params

.

offsetY

]

;

var

dataPoint

=

myChart

.

convertFromPixel

(

{

geoIndex

:

0

}

,

pixelPoint

)

;

// When click, the data in SVG local coords will be printed,

// which can be used in `series.data`.

console

.

log

(

dataPoint

)

;

}

)

;

See also

SVG Scatter

,

SVG Lines

,

SVG Traffic

.

Unsupported SVG features

Unfortunately it is difficult to implement a complete SVG parser. While the common SVG features are supported, at least these features listed below are not supported yet:

Flip and skew (will be supported

v5.1.2

):

Not support

transform: skew(...)

(including

transform: matrix(...)

that includes skew).

Not support

transform: scale(x, y)

that

x

,

y

has different sign while has

rotate

(e.g.,

scale: (1, -1), rotate(90)

).

Standalone

<style>

tag is not supported.

But inline style is supported (e.g.,

<path style="color:red" />

).

Unit:

Only

px

is supported. Other unit like

width="231.65mm"

is not supported.

Percentage value like

<svg width="30%" height="40%">

is not supported.

<defs>

tag:

Only

<linearGradient>

,

<radialGradient>

are supported.

other elements (e.g.,

<pattern>

,

<path>

, ...) defined in

<defs>

are not supported yet.

<linearGradient>

,

<radialGradient>

:

fx

,

fy

is not supported.

gradientTransform

attribute is not supported.

fill:url(...)

,

stroke:utl(...)

:

Only

url(#someId)

is supported.

Other URL patterns are not supported. e.g.,

url(https://example.com/images/myImg.jpg)

;

url(data:image/png;base64,iRxVB0…)

;

url(myFont.woff)

;

<switch>

tag:

All the content inside

<switch>

tag will be displayed. The "switch" feature is not supported.

<text>

:

textPath

is not supported.

Addressable character

is not supported. That is,

<!-- Not supported: --> <tspan x="0 4.94 9.89">abc</tspan> <!-- Supported: --> <tspan x="0">a</tspan> <tspan x="4.94">b</tspan> <tspan x="9.89">c</tspan>

Contributors

Edit this page on GitHub

100pah
