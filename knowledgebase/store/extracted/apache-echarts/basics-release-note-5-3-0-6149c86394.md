---
title: 5.3 - What's New - Basics - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/basics/release-note/5-3-0
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:43.330173+00:00
kind: extracted-doc
---

# 5.3 - What's New - Basics - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/basics/release-note/5-3-0

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:43.330173+00:00

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

- 5.3 - What's New - Basics - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Apache ECharts 5.3.0 Features Apache ECharts 5.3.0 includes significant enhancements to animation expressiveness, rendering performance, and server-side rendering.
- It also adds long-awaited features from the community, such as automatic alignment of multi-axis ticks, tooltip value formatting, and map projection.
- Keyframe Animations Previously, ECharts animations were focused on transition animations for creating, updating, and removing elements, which often only had a start state and an end state.
- In order to express more complex animations, we introduced new keyframe animations for custom series and graphics components in 5.3.0.

Extracted text:

5.3 - What's New - Basics - Handbook - Apache ECharts

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

Apache ECharts 5.3.0 Features

Apache ECharts 5.3.0 includes significant enhancements to animation expressiveness, rendering performance, and server-side rendering. It also adds long-awaited features from the community, such as automatic alignment of multi-axis ticks, tooltip value formatting, and map projection.

Keyframe Animations

Previously, ECharts animations were focused on transition animations for creating, updating, and removing elements, which often only had a start state and an end state. In order to express more complex animations, we introduced new keyframe animations for custom series and graphics components in 5.3.0.

Here is a simple effect of a breathing animation implemented via keyframe animation

option = { graphic: { type: 'circle', shape: { r: 100 }, left: 'center', top: 'center', keyframeAnimation: [ { duration: 3000, loop: true, keyframes: [ { percent: 0.5, easing: 'sinusoidalInOut', scaleX: 0.1, scaleY: 0.1 }, { percent: 1, easing: 'sinusoidalInOut', scaleX: 1, scaleY: 1 } ] } ] } };

option

=

{

graphic

:

{

type

:

'circle'

,

shape

:

{

r

:

100

}

,

left

:

'center'

,

top

:

'center'

,

keyframeAnimation

:

[

{

duration

:

3000

,

loop

:

true

,

keyframes

:

[

{

percent

:

0.5

,

easing

:

'sinusoidalInOut'

,

scaleX

:

0.1

,

scaleY

:

0.1

}

,

{

percent

:

1

,

easing

:

'sinusoidalInOut'

,

scaleX

:

1

,

scaleY

:

1

}

]

}

]

}

}

;

live

In keyframe animation you can configure the animation duration, delay, easing, whether to loop or not, the position, easing, and graphic properties of each keyframe. You can also set multiple keyframe animations for each element at the same time with different configurations. The flexible configuration allows us to achieve very complex animation effects, and here are a few scenarios where keyframe animation can be applied.

Custom Loading Animations

ECharts has a built-in loading animation by default, which can be displayed by calling

showLoading

. More loading animation effects have been frequently asked in the community. Now with keyframe animations, we can use the

graphic

component with keyframe animations to achieve any loading animation effect we want.

Here is an example of the text stroke animation.

option = { graphic: { elements: [ { type: 'text', left: 'center', top: 'center', style: { text: 'Apache ECharts', fontSize: 40, fontWeight: 'bold', lineDash: [0, 200], lineDashOffset: 0, fill: 'transparent', stroke: '#000', lineWidth: 1 }, keyframeAnimation: { duration: 3000, loop: true, keyframes: [ { percent: 0.7, style: { fill: 'transparent', lineDashOffset: 200, lineDash: [200, 0] } }, { // Stop for a while. percent: 0.8, style: { fill: 'transparent' } }, { percent: 1, style: { fill: 'black' } } ] } } ] } };

option

=

{

graphic

:

{

elements

:

[

{

type

:

'text'

,

left

:

'center'

,

top

:

'center'

,

style

:

{

text

:

'Apache ECharts'

,

fontSize

:

40

,

fontWeight

:

'bold'

,

lineDash

:

[

0

,

200

]

,

lineDashOffset

:

0

,

fill

:

'transparent'

,

stroke

:

'#000'

,

lineWidth

:

1

}

,

keyframeAnimation

:

{

duration

:

3000

,

loop

:

true

,

keyframes

:

[

{

percent

:

0.7

,

style

:

{

fill

:

'transparent'

,

lineDashOffset

:

200

,

lineDash

:

[

200

,

0

]

}

}

,

{

// Stop for a while.

percent

:

0.8

,

style

:

{

fill

:

'transparent'

}

}

,

{

percent

:

1

,

style

:

{

fill

:

'black'

}

}

]

}

}

]

}

}

;

live

Or animate columns.

const columns = []; for (let i = 0; i < 7; i++) { columns.push({ type: 'rect', x: i * 20, shape: { x: 0, y: -40, width: 10, height: 80 }, style: { fill: '#5470c6' }, keyframeAnimation: { duration: 1000, delay: i * 200, loop: true, keyframes: [ { percent: 0.5, scaleY: 0.1, easing: 'cubicIn' }, { percent: 1, scaleY: 1, easing: 'cubicOut' } ] } }); } option = { graphic: { elements: [ { type: 'group', left: 'center', top: 'center', children: columns } ] } };

const

columns

=

[

]

;

for

(

let

i

=

0

;

i

<

7

;

i

++

)

{

columns

.

push

(

{

type

:

'rect'

,

x

:

i

*

20

,

shape

:

{

x

:

0

,

y

:

-

40

,

width

:

10

,

height

:

80

}

,

style

:

{

fill

:

'#5470c6'

}

,

keyframeAnimation

:

{

duration

:

1000

,

delay

:

i

*

200

,

loop

:

true

,

keyframes

:

[

{

percent

:

0.5

,

scaleY

:

0.1

,

easing

:

'cubicIn'

}

,

{

percent

:

1

,

scaleY

:

1

,

easing

:

'cubicOut'

}

]

}

}

)

;

}

option

=

{

graphic

:

{

elements

:

[

{

type

:

'group'

,

left

:

'center'

,

top

:

'center'

,

children

:

columns

}

]

}

}

;

live

Extending Richer Animation Effects in the Chart

Scatter charts with animation effects have long been a feature of ECharts. Developers can use the

effectScatter

series to implement dynamic scatter charts with ripple effects, which make charts more interesting and also serve to highlight the user. As with loading animations, developers often ask for more animation effects. Now we can achieve more complex effects by using keyframe animations in our

custom

series.

For example, the following example animates the pins drawn by the custom series on the SVG map with a jumping effect, along with a ripple animation.

fetch( 'https://echarts.apache.org/examples/data/asset/geo/Map_of_Iceland.svg' ) .then(response => response.text()) .then(svg => { echarts.registerMap('iceland_svg', { svg: svg }); option = { geo: { map: 'iceland_svg', left: 0, right: 0 }, series: { type: 'custom', coordinateSystem: 'geo', geoIndex: 0, zlevel: 1, data: [ [488, 459, 100], [770, 757, 30], [1180, 743, 80], [894, 1188, 61], [1372, 477, 70], [1378, 935, 81] ], renderItem(params, api) { const coord = api.coord([ api.value(0, params.dataIndex), api.value(1, params.dataIndex) ]); const circles = []; for (let i = 0; i < 5; i++) { circles.push({ type: 'circle', shape: { cx: 0, cy: 0, r: 30 }, style: { stroke: 'red', fill: 'none', lineWidth: 2 }, // Ripple animation keyframeAnimation: { duration: 4000, loop: true, delay: (-i / 4) * 4000, keyframes: [ { percent: 0, scaleX: 0, scaleY: 0, style: { opacity: 1 } }, { percent: 1, scaleX: 1, scaleY: 0.4, style: { opacity: 0 } } ] } }); } return { type: 'group', x: coord[0], y: coord[1], children: [ ...circles, { type: 'path', shape: { d: 'M16 0c-5.523 0-10 4.477-10 10 0 10 10 22 10 22s10-12 10-22c0-5.523-4.477-10-10-10zM16 16c-3.314 0-6-2.686-6-6s2.686-6 6-6 6 2.686 6 6-2.686 6-6 6z', x: -10, y: -35, width: 20, height: 40 }, style: { fill: 'red' }, // Jump animation. keyframeAnimation: { duration: 1000, loop: true, delay: Math.random() * 1000, keyframes: [ { y: -10, percent: 0.5, easing: 'cubicOut' }, { y: 0, percent: 1, easing: 'bounceOut' } ] } } ] }; } } }; myChart.setOption(option); });

fetch

(

'https://echarts.apache.org/examples/data/asset/geo/Map_of_Iceland.svg'

)

.

then

(

response

=>

response

.

text

(

)

)

.

then

(

svg

=>

{

echarts

.

registerMap

(

'iceland_svg'

,

{

svg

:

svg

}

)

;

option

=

{

geo

:

{

map

:

'iceland_svg'

,

left

:

0

,

right

:

0

}

,

series

:

{

type

:

'custom'

,

coordinateSystem

:

'geo'

,

geoIndex

:

0

,

zlevel

:

1

,

data

:

[

[

488

,

459

,

100

]

,

[

770

,

757

,

30

]

,

[

1180

,

743

,

80

]

,

[

894

,

1188

,

61

]

,

[

1372

,

477

,

70

]

,

[

1378

,

935

,

81

]

]

,

renderItem

(

params

,

api

)

{

const

coord

=

api

.

coord

(

[

api

.

value

(

0

,

params

.

dataIndex

)

,

api

.

value

(

1

,

params

.

dataIndex

)

]

)

;

const

circles

=

[

]

;

for

(

let

i

=

0

;

i

<

5

;

i

++

)

{

circles

.

push

(

{

type

:

'circle'

,

shape

:

{

cx

:

0

,

cy

:

0

,

r

:

30

}

,

style

:

{

stroke

:

'red'

,

fill

:

'none'

,

lineWidth

:

2

}

,

// Ripple animation

keyframeAnimation

:

{

duration

:

4000

,

loop

:

true

,

delay

:

(

-

i

/

4

)

*

4000

,

keyframes

:

[

{

percent

:

0

,

scaleX

:

0

,

scaleY

:

0

,

style

:

{

opacity

:

1

}

}

,

{

percent

:

1

,

scaleX

:

1

,

scaleY

:

0.4

,

style

:

{

opacity

:

0

}

}

]

}

}

)

;

}

return

{

type

:

'group'

,

x

:

coord

[

0

]

,

y

:

coord

[

1

]

,

children

:

[

...

circles

,

{

type

:

'path'

,

shape

:

{

d

:

'M16 0c-5.523 0-10 4.477-10 10 0 10 10 22 10 22s10-12 10-22c0-5.523-4.477-10-10-10zM16 16c-3.314 0-6-2.686-6-6s2.686-6 6-6 6 2.686 6 6-2.686 6-6 6z'

,

x

:

-

10

,

y

:

-

35

,

width

:

20

,

height

:

40

}

,

style

:

{

fill

:

'red'

}

,

// Jump animation.

keyframeAnimation

:

{

duration

:

1000

,

loop

:

true

,

delay

:

Math

.

random

(

)

*

1000

,

keyframes

:

[

{

y

:

-

10

,

percent

:

0.5

,

easing

:

'cubicOut'

}

,

{

y

:

0

,

percent

:

1

,

easing

:

'bounceOut'

}

]

}

}

]

}

;

}

}

}

;

myChart

.

setOption

(

option

)

;

}

)

;

live

Loading Lottie animations

In order to fully exploit the power of new keyframe animations, Yi Shen from the ECharts team wrote a

Lottie animation parsing library

that can parse Lottie animation files into the ECharts graphics format for rendering. Combined with Lottie's expressive power we can introduce more amazing animations to our projects.

Graphical component transition animations

We have provided more flexible transition animation configurations for elements returned in the custom series in 5.0. The

transition

,

enterFrom

, and

leaveTo

configuration items allow you to configure which properties of each element will have transition animations and how they will be animated when the graphic is created and removed. Here is an example.

function

renderItem

(

)

{

//...

return

{

//...

x

:

100

,

// 'style', 'x', 'y' will be animated

transition

:

[

'style'

,

'x'

,

'y'

]

,

enterFrom

:

{

style

:

{

// Fade in

opacity

:

0

}

,

// Fly in from the left

x

:

0

}

,

leaveTo

:

{

// Fade out

opacity

:

0

}

,

// Fly out to the right

x

:

200

}

;

}

In 5.3.0 we extended the configuration of these transition animations to the graphic component, with made additional enhancements.

If you don't want to write out each property to be animated, you can now directly configure

transition: 'all'

to animate all properties.

We also added

enterAnimation

,

updateAnimation

, and

leaveAnimation

to configure the

duration

,

delay

, and

easing

of the entry, update, and exit animations for each graphic, respectively. Gradient colors now also support animations.

New SVG renderer

In 5.3.0 we refactored our SVG renderer, which delivers 2x ~ 10x performance improvements, and even tens of times in some special scenes.

Previously, we updated the SVG renderer directly from the render queue to the DOM, but since zrender's graphics properties were not one-to-one with the DOM, we had to implement very complex diff logic in the middle, which was error-prone and did not provide the best performance in some scenarios. In this version, we reconstruct the full rendering to VDOM first, and then patch the VDOM to DOM to finish the rendering. Full rendering avoids potential bugs caused by complex diff logic, and the one-to-one correspondence between VDOM and DOM ensures that updates are minimal when patching, resulting in a huge performance boost.

This example

gives you an intuitive impression of the performance improvement. The new version is much smoother than the previous version when dragging the chart in SVG mode.

5.2.2 (Before)

5.3.0 (After)

In addition to the performance improvement, we can do more things with the rendered VDOM, such as server-side rendering, which will be described below.

Server-side Rendering with Zero Dependencies

In previous versions, ECharts could also implement server-side rendering, but it had to rely on

node-canvas

, or

JSDOM

if you were using SVG mode to simulate the DOM environment. These dependencies not only bring additional size and usage requirements, but also affect performance.

This new SVG renderer allows us to get the string from the intermediate rendered VDOM, bringing completely zero-dependency server-side rendering and outputting a more refined SVG string integrated CSS animation.

const

echarts

=

require

(

'echarts'

)

;

// In SSR mode the first parameter does not need to be passed in as a DOM object

const

chart

=

echarts

.

init

(

null

,

null

,

{

renderer

:

'svg'

,

// must use SVG mode

ssr

:

true

,

// enable SSR

width

:

400

,

// need to specify height and width

height

:

300

}

)

;

// setOption as normal

chart

.

setOption

(

{

xAxis

:

{

type

:

'category'

,

data

:

[

'Mon'

,

'Tue'

,

'Wed'

,

'Thu'

,

'Fri'

,

'Sat'

,

'Sun'

]

}

,

yAxis

:

{

type

:

'value'

}

,

series

:

[

{

data

:

[

120

,

200

,

150

,

80

,

70

,

110

,

130

]

,

type

:

'bar'

}

]

}

)

;

// Output string

const

svgStr

=

chart

.

renderToSVGString

(

)

;

Customizing Map Projections

Maps have always been a very widely used component in ECharts. Typically a map component uses GeoJSON formatted data with latitude and longitude stored. ECharts then calculates the appropriate display area and maps the latitude and longitude linearly to that area. This is the simplest way to project a map. However, the simple linear projection does not work for complex map scenarios, such as using

Albers

projection to solve the distortion problem in linear projection, or having the Pacific in the middle of the world map, etc.

So in 5.3.0 we introduced extending map projection. It tells ECharts how to project coordinates and how to calculate latitude and longitude from the projected coordinates via the

project

and

unproject

methods. The following is a simple example of using the Mercator projection.

series

=

{

type

:

'map'

,

projection

:

{

project

:

point

=>

[

(

point

[

0

]

/

180

)

*

Math

.

PI

,

-

Math

.

log

(

Math

.

tan

(

(

Math

.

PI

/

2

+

(

point

[

1

]

/

180

)

*

Math

.

PI

)

/

2

)

)

]

,

unproject

:

point

=>

[

(

point

[

0

]

*

180

)

/

Math

.

PI

,

(

(

2

*

180

)

/

Math

.

PI

)

*

Math

.

atan

(

Math

.

exp

(

point

[

1

]

)

)

-

90

]

}

}

;

In addition to implementing our own projection formula, we can also use projections implementations provided by third-party libraries such as

d3-geo

.

const

projection

=

d3

.

geoConicEqualArea

(

)

;

// ...

series

=

{

type

:

'map'

,

projection

:

{

project

:

point

=>

projection

(

point

)

,

unproject

:

point

=>

projection

.

invert

(

point

)

}

}

;

In conjunction with the new global transition animation feature added in 5.2, we can animate the transition between different projection effects: !

In addition to the map projection, we have made the following two enhancements to the map in this release.

Provided

'LineString'

and

'MultiLineString'

support for GeoJSON data.

Changed the calculation of the default label position from the center of the bounding box to the centroid of the largest area for more accurate results.

Ticks Alignment of Multiple Axes

Ticks alignment of multiple axes is a long-standing requirement in the community, and we can see many articles in the community on how to implement axis alignment in ECharts, which is usually troublesome and limited.

In 5.3.0, we finally introduced the feature of aligning ticks on the

'value'

and

'log'

axes. You can configure

alignTicks: true

in the axis that needs to be aligned. The axis will then adjust its own ticks according to the first axis's ticks, enabling automatic alignment.

option = { tooltip: { trigger: 'axis' }, legend: {}, xAxis: [ { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], axisPointer: { type: 'shadow' } } ], yAxis: [ { type: 'value', name: 'Precipitation', alignTicks: true, axisLabel: { formatter: '{value} ml' } }, { type: 'value', name: 'Temperature', axisLabel: { formatter: '{value} °C' } } ], series: [ { name: 'Evaporation', type: 'bar', // prettier-ignore data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3] }, { name: 'Precipitation', type: 'bar', // prettier-ignore data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3] }, { name: 'Temperature', type: 'line', yAxisIndex: 1, data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2] } ] };

option

=

{

tooltip

:

{

trigger

:

'axis'

}

,

legend

:

{

}

,

xAxis

:

[

{

type

:

'category'

,

data

:

[

'Mon'

,

'Tue'

,

'Wed'

,

'Thu'

,

'Fri'

,

'Sat'

,

'Sun'

]

,

axisPointer

:

{

type

:

'shadow'

}

}

]

,

yAxis

:

[

{

type

:

'value'

,

name

:

'Precipitation'

,

alignTicks

:

true

,

axisLabel

:

{

formatter

:

'{value} ml'

}

}

,

{

type

:

'value'

,

name

:

'Temperature'

,

axisLabel

:

{

formatter

:

'{value} °C'

}

}

]

,

series

:

[

{

name

:

'Evaporation'

,

type

:

'bar'

,

// prettier-ignore

data

:

[

2.0

,

4.9

,

7.0

,

23.2

,

25.6

,

76.7

,

135.6

,

162.2

,

32.6

,

20.0

,

6.4

,

3.3

]

}

,

{

name

:

'Precipitation'

,

type

:

'bar'

,

// prettier-ignore

data

:

[

2.6

,

5.9

,

9.0

,

26.4

,

28.7

,

70.7

,

175.6

,

182.2

,

48.7

,

18.8

,

6.0

,

2.3

]

}

,

{

name

:

'Temperature'

,

type

:

'line'

,

yAxisIndex

:

1

,

data

:

[

2.0

,

2.2

,

3.3

,

4.5

,

6.3

,

10.2

,

20.3

,

23.4

,

23.0

,

16.5

,

12.0

,

6.2

]

}

]

}

;

live

Disable Emphasis and Select State

The

emphasis

state in ECharts provides feedback to the user when the mouse is over an element, but in a chart with a large number of elements, the highlighting animation can cause performance issues. In particular, highlighting triggered by

tooltip

or

legend

component linkage can highlight multiple elements at the same time.

Therefore, in this release we have added

emphasis.disabled

configuration. If you don't need the highlighting feedback and you are concerned about the interactivity, you can disable the

emphasis

state with this option.

For the

select

state, we have also added

select.disabled

. This option can be used to configure some of the data to be unselectable.

Support for Selecting Entire Series

As of 5.3.0 we support configuring

selectedMode

to

'series'

to enable selection of all data in a series.

Formatting of Values in Tooltip

Tooltips can be used to display more detailed information about the data item when the user hovers it. ECharts also provides a

formatter

callback function to give developers more flexibility to customize the content of the tooltip.

However, we found that most of the time, developers only needed to format the value part of the tooltip, such as fixed precision, prefixed with

$

, etc. Previously, in order to format the number, developers had to rewrite the entire content of the tooltip with

formatter

. Especially after 5.0, ECharts hint boxes have become more complex and beautiful, so rewriting them becomes costly and difficult to achieve the default results.

So in this version, we have added a

valueFormatter

configuration to the tooltip for formatting the value part.

As in the axis alignment example, we can add the °C and ml suffixes to the value part of the tooltip.

option = { tooltip: { trigger: 'axis' }, legend: {}, xAxis: [ { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], axisPointer: { type: 'shadow' } } ], yAxis: [ { type: 'value', name: 'Precipitation', alignTicks: true, axisLabel: { formatter: '{value} ml' } }, { type: 'value', name: 'Temperature', axisLabel: { formatter: '{value} °C' } } ], series: [ { name: 'Evaporation', type: 'bar', tooltip: { valueFormatter: value => value + ' ml' }, // prettier-ignore data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3] }, { name: 'Precipitation', type: 'bar', tooltip: { valueFormatter: value => value + ' ml' }, // prettier-ignore data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3] }, { name: 'Temperature', type: 'line', yAxisIndex: 1, tooltip: { valueFormatter: value => value + ' °C' }, data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2] } ] };

option

=

{

tooltip

:

{

trigger

:

'axis'

}

,

legend

:

{

}

,

xAxis

:

[

{

type

:

'category'

,

data

:

[

'Mon'

,

'Tue'

,

'Wed'

,

'Thu'

,

'Fri'

,

'Sat'

,

'Sun'

]

,

axisPointer

:

{

type

:

'shadow'

}

}

]

,

yAxis

:

[

{

type

:

'value'

,

name

:

'Precipitation'

,

alignTicks

:

true

,

axisLabel

:

{

formatter

:

'{value} ml'

}

}

,

{

type

:

'value'

,

name

:

'Temperature'

,

axisLabel

:

{

formatter

:

'{value} °C'

}

}

]

,

series

:

[

{

name

:

'Evaporation'

,

type

:

'bar'

,

tooltip

:

{

valueFormatter

:

value

=>

value

+

' ml'

}

,

// prettier-ignore

data

:

[

2.0

,

4.9

,

7.0

,

23.2

,

25.6

,

76.7

,

135.6

,

162.2

,

32.6

,

20.0

,

6.4

,

3.3

]

}

,

{

name

:

'Precipitation'

,

type

:

'bar'

,

tooltip

:

{

valueFormatter

:

value

=>

value

+

' ml'

}

,

// prettier-ignore

data

:

[

2.6

,

5.9

,

9.0

,

26.4

,

28.7

,

70.7

,

175.6

,

182.2

,

48.7

,

18.8

,

6.0

,

2.3

]

}

,

{

name

:

'Temperature'

,

type

:

'line'

,

yAxisIndex

:

1

,

tooltip

:

{

valueFormatter

:

value

=>

value

+

' °C'

}

,

data

:

[

2.0

,

2.2

,

3.3

,

4.5

,

6.3

,

10.2

,

20.3

,

23.4

,

23.0

,

16.5

,

12.0

,

6.2

]

}

]

}

;

live

Each series can configure its own

valueFormatter

according to its own value format.

More Flexible Sector Corner Radius

In 5.0 we have added rounded corners configuration for sectors, which can make pie charts, sunburst charts more interesting. Previously, we only supported the inner and outer radius separately, this time we go a step further and support the four corners of the sector to be configured with different corner radius to bring more flexible display.

option = { tooltip: { trigger: 'item' }, legend: { top: '5%', left: 'center' }, series: [ { name: 'Access From', type: 'pie', radius: ['30%', '70%'], roseType: 'angle', itemStyle: { borderRadius: [20, 5, 5, 10], borderColor: '#fff', borderWidth: 2 }, label: { show: false }, data: [ { value: 800, name: 'Search Engine' }, { value: 735, name: 'Direct' }, { value: 580, name: 'Email' }, { value: 484, name: 'Union Ads' }, { value: 400, name: 'Video Ads' } ] } ] };

option

=

{

tooltip

:

{

trigger

:

'item'

}

,

legend

:

{

top

:

'5%'

,

left

:

'center'

}

,

series

:

[

{

name

:

'Access From'

,

type

:

'pie'

,

radius

:

[

'30%'

,

'70%'

]

,

roseType

:

'angle'

,

itemStyle

:

{

borderRadius

:

[

20

,

5

,

5

,

10

]

,

borderColor

:

'#fff'

,

borderWidth

:

2

}

,

label

:

{

show

:

false

}

,

data

:

[

{

value

:

800

,

name

:

'Search Engine'

}

,

{

value

:

735

,

name

:

'Direct'

}

,

{

value

:

580

,

name

:

'Email'

}

,

{

value

:

484

,

name

:

'Union Ads'

}

,

{

value

:

400

,

name

:

'Video Ads'

}

]

}

]

}

;

live

Complex Label Optimization for Pie charts

Pie charts have always been one of the most complex charts on the label display in ECharts. We have been optimizing the layout and display of the pie chart labels for a long time.

This time, we have done a deep optimization for pie chart labels that use text wrapping, background colors, rich text, and other complex layouts. In the adaptive width, container overflow, guide line calculation than before there are better results:

5.2.2 (Before)

5.3.0 (After)

bar chart large mode optimization

In the cases of a large amount of data (> 2k), we support bar charts to speed up rendering and improve interactive performance by turning on

large

mode. But previously the layout of bar charts in

large

mode was simple and did not support the layout after stacking multiple series. In 5.3.0, we have optimized the layout of

large

mode to be consistent with the normal mode. We can optimize the performance of the bar chart in more scenarios by turning on

large

.

In addition, the optimized bar chart layout also fixes the bug of incorrect stacking on non-linear axes like logarithmic axes.

Breaking Changes

registerMap and getMap methods need to be used only after the map chart is imported

To reduce the size of the minimum bundle, we removed the map data management methods

getMap

and

registerMap

from the core module.

If you are

only importing necessary charts and components

, you need to ensure that you have imported

GeoComponent

or

MapChart

before you can register map data with

registerMap

.

import

*

as

echarts

from

'echarts/core'

;

import

{

MapChart

}

from

'echarts/charts'

;

echarts

.

use

(

[

MapChart

]

)

;

// You must import the MapChart with the `use` method before you can register the map with registerMap

echarts

.

registerMap

(

'world'

,

worldJSON

)

;

If you are using

import * as echarts from 'echarts'

to import the whole package, this change will not affect you in any way.

Removing the default bolding emphasis effect in the line chart

We introduced the default bolding emphasis effect for line charts in 5.0, but the community feedback was that this didn't looks well in many scenarios. So in this version we changed this effect from on by default to off by default. You can enable it by:

series

=

{

type

:

'line'

,

//...

emphasis

:

{

lineStyle

:

{

width

:

'bolder'

}

}

}

;

Full Changelog

View the

Changelog

Contributors

Edit this page on GitHub

Ovilia

pissang

plainheart
