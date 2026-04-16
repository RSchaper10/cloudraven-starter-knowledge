---
title: 5.2 - What's New - Basics - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/basics/release-note/5-2-0
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:42.521552+00:00
kind: extracted-doc
---

# 5.2 - What's New - Basics - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/basics/release-note/5-2-0

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:42.521552+00:00

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

- 5.2 - What's New - Basics - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide What's New in Apache ECharts 5.2.0 Universal Transition Natural and smooth transition animations have been an important feature in Apache ECharts.
- By avoiding abrupt changes from data update, it not only improves the visual effect, but also provides the possibility to express the association and evolution of data.
- Therefore, in 5.2.0, we have further enhanced this animation capability.
- Next, we will see how this Universal Transition adds expressiveness and narrative power to the chart.

Extracted text:

5.2 - What's New - Basics - Handbook - Apache ECharts

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

What's New in Apache ECharts 5.2.0

Universal Transition

Natural and smooth transition animations have been an important feature in Apache ECharts. By avoiding abrupt changes from data update, it not only improves the visual effect, but also provides the possibility to express the association and evolution of data. Therefore, in 5.2.0, we have further enhanced this animation capability. Next, we will see how this

Universal Transition

adds expressiveness and narrative power to the chart.

In previous versions, transition animations had certain limitations: they could only be used for the position, size of the same shape, and they could only work on the same type of series. For example, the following example reflects the change in data percent through the change in sector shape in a pie chart.

function makeRandomData() { return [ { value: Math.random(), name: 'A' }, { value: Math.random(), name: 'B' }, { value: Math.random(), name: 'C' } ]; } option = { series: [ { type: 'pie', radius: [0, '50%'], data: makeRandomData() } ] }; setInterval(() => { myChart.setOption({ series: { data: makeRandomData() } }); }, 2000);

function

makeRandomData

(

)

{

return

[

{

value

:

Math

.

random

(

)

,

name

:

'A'

}

,

{

value

:

Math

.

random

(

)

,

name

:

'B'

}

,

{

value

:

Math

.

random

(

)

,

name

:

'C'

}

]

;

}

option

=

{

series

:

[

{

type

:

'pie'

,

radius

:

[

0

,

'50%'

]

,

data

:

makeRandomData

(

)

}

]

}

;

setInterval

(

(

)

=>

{

myChart

.

setOption

(

{

series

:

{

data

:

makeRandomData

(

)

}

}

)

;

}

,

2000

)

;

live

And starting with 5.2.0, we introduced universal transition, a more powerful animation feature. With that, transitions are no longer limited to between series of the same type. Now, we can use this cross-series morphing to animate between any type of series and any type of shapes.

How cool would this be? Let's have a look!

Morphing transition across series

With

universalTransition: true

set to enable universion transition feature, switching from pie charts to bar charts, or from bar charts to scatter charts, or even between more complex charts like Sunburst and Treemap, can be morphed naturally.

As follows, switching between a pie chart and a bar chart.

const dataset = { dimensions: ['name', 'score'], source: [ ['Hannah Krause', 314], ['Zhao Qian', 351], ['Jasmin Krause ', 287], ['Li Lei', 219], ['Karle Neumann', 253], ['Mia Neumann', 165], ['Böhm Fuchs', 318], ['Han Meimei', 366] ] }; const pieOption = { dataset: [dataset], series: [ { type: 'pie', // associate the series to be animated by id id: 'Score', radius: [0, '50%'], universalTransition: true, animationDurationUpdate: 1000 } ] }; const barOption = { dataset: [dataset], xAxis: { type: 'category' }, yAxis: {}, series: [ { type: 'bar', // associate the series to be animated by id id: 'Score', // Each data will have a different color colorBy: 'data', encode: { x: 'name', y: 'score' }, universalTransition: true, animationDurationUpdate: 1000 } ] }; option = barOption; setInterval(() => { option = option === pieOption ? barOption : pieOption; // Use the notMerge form to remove the axes myChart.setOption(option, true); }, 2000);

const

dataset

=

{

dimensions

:

[

'name'

,

'score'

]

,

source

:

[

[

'Hannah Krause'

,

314

]

,

[

'Zhao Qian'

,

351

]

,

[

'Jasmin Krause '

,

287

]

,

[

'Li Lei'

,

219

]

,

[

'Karle Neumann'

,

253

]

,

[

'Mia Neumann'

,

165

]

,

[

'Böhm Fuchs'

,

318

]

,

[

'Han Meimei'

,

366

]

]

}

;

const

pieOption

=

{

dataset

:

[

dataset

]

,

series

:

[

{

type

:

'pie'

,

// associate the series to be animated by id

id

:

'Score'

,

radius

:

[

0

,

'50%'

]

,

universalTransition

:

true

,

animationDurationUpdate

:

1000

}

]

}

;

const

barOption

=

{

dataset

:

[

dataset

]

,

xAxis

:

{

type

:

'category'

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

type

:

'bar'

,

// associate the series to be animated by id

id

:

'Score'

,

// Each data will have a different color

colorBy

:

'data'

,

encode

:

{

x

:

'name'

,

y

:

'score'

}

,

universalTransition

:

true

,

animationDurationUpdate

:

1000

}

]

}

;

option

=

barOption

;

setInterval

(

(

)

=>

{

option

=

option

===

pieOption

?

barOption

:

pieOption

;

// Use the notMerge form to remove the axes

myChart

.

setOption

(

option

,

true

)

;

}

,

2000

)

;

live

More transitions between common charts.

Such transitions are no longer limited to just the basic line, bar, and pie charts, but also between bars and maps:

or between Sunburst and Treemap, or even between very flexible custom series can be transitions.

Note that you need to configure the series ids to ensure that there is a one-to-one correspondence between the series that need to be animated for the transition.

Minimal bundle needs to import this feature manually.

import { UniversalTransition } from 'echarts/features'; echarts.use([UniversalTransition]);

Data split and merge animations

In addition to the common update of data values, sometimes we also encounter data aggregation, drill-down and other updates after interactions, when we can not directly apply one-to-one transitions, but need to use more animation effects like splitting and merging to express the transformation of data.

In order to be able to express the possible many-to-many connections between data, in 5.2.0 we introduced a new concept

groupId

. We can set the group to the whole series via

series.dataGroupId

, or more fine-grained by

series.data.groupId

to set the group to which each data belongs. It's even easier if you use a

dataset

to manage the data, you can use

encode.itemGroupId

to specify a dimension encoded as

groupId

.

For example, if we want to implement a drill-down animation for a bar chart, we can set the entire series of data after the drill-down to the same

groupId

, which then corresponds to the data before the drill-down

option = { xAxis: { data: ['Animals', 'Fruits', 'Cars'] }, yAxis: {}, dataGroupId: '', animationDurationUpdate: 500, series: { type: 'bar', id: 'sales', data: [ { value: 5, groupId: 'animals' }, { value: 2, groupId: 'fruits' }, { value: 4, groupId: 'cars' } ], universalTransition: { enabled: true, divideShape: 'clone' } } }; const drilldownData = [ { dataGroupId: 'animals', data: [ ['Cats', 4], ['Dogs', 2], ['Cows', 1], ['Sheep', 2], ['Pigs', 1], ['Cows', 1], ['Sheep', 2], ['Pigs', 1] ] }, { dataGroupId: 'fruits', data: [ ['Apples', 4], ['Oranges', 2], ['Oranges', 2] ] }, { dataGroupId: 'cars', data: [ ['Toyota', 4], ['Opel', 2], ['Volkswagen', 2], ['Volkswagen', 2] ] } ]; myChart.on('click', event => { if (event.data) { const subData = drilldownData.find(data => { return data.dataGroupId === event.data.groupId; }); if (!subData) { return; } myChart.setOption({ xAxis: { data: subData.data.map(item => { return item[0]; }) }, series: { type: 'bar', id: 'sales', dataGroupId: subData.dataGroupId, data: subData.data.map(item => { return item[1]; }), universalTransition: { enabled: true, divideShape: 'clone' } }, graphic: [ { type: 'text', left: 50, top: 20, style: { text: 'Back', fontSize: 18 }, onclick: function() { myChart.setOption(option, true); } } ] }); } });

option

=

{

xAxis

:

{

data

:

[

'Animals'

,

'Fruits'

,

'Cars'

]

}

,

yAxis

:

{

}

,

dataGroupId

:

''

,

animationDurationUpdate

:

500

,

series

:

{

type

:

'bar'

,

id

:

'sales'

,

data

:

[

{

value

:

5

,

groupId

:

'animals'

}

,

{

value

:

2

,

groupId

:

'fruits'

}

,

{

value

:

4

,

groupId

:

'cars'

}

]

,

universalTransition

:

{

enabled

:

true

,

divideShape

:

'clone'

}

}

}

;

const

drilldownData

=

[

{

dataGroupId

:

'animals'

,

data

:

[

[

'Cats'

,

4

]

,

[

'Dogs'

,

2

]

,

[

'Cows'

,

1

]

,

[

'Sheep'

,

2

]

,

[

'Pigs'

,

1

]

,

[

'Cows'

,

1

]

,

[

'Sheep'

,

2

]

,

[

'Pigs'

,

1

]

]

}

,

{

dataGroupId

:

'fruits'

,

data

:

[

[

'Apples'

,

4

]

,

[

'Oranges'

,

2

]

,

[

'Oranges'

,

2

]

]

}

,

{

dataGroupId

:

'cars'

,

data

:

[

[

'Toyota'

,

4

]

,

[

'Opel'

,

2

]

,

[

'Volkswagen'

,

2

]

,

[

'Volkswagen'

,

2

]

]

}

]

;

myChart

.

on

(

'click'

,

event

=>

{

if

(

event

.

data

)

{

const

subData

=

drilldownData

.

find

(

data

=>

{

return

data

.

dataGroupId

===

event

.

data

.

groupId

;

}

)

;

if

(

!

subData

)

{

return

;

}

myChart

.

setOption

(

{

xAxis

:

{

data

:

subData

.

data

.

map

(

item

=>

{

return

item

[

0

]

;

}

)

}

,

series

:

{

type

:

'bar'

,

id

:

'sales'

,

dataGroupId

:

subData

.

dataGroupId

,

data

:

subData

.

data

.

map

(

item

=>

{

return

item

[

1

]

;

}

)

,

universalTransition

:

{

enabled

:

true

,

divideShape

:

'clone'

}

}

,

graphic

:

[

{

type

:

'text'

,

left

:

50

,

top

:

20

,

style

:

{

text

:

'Back'

,

fontSize

:

18

}

,

onclick

:

function

(

)

{

myChart

.

setOption

(

option

,

true

)

;

}

}

]

}

)

;

}

}

)

;

live

With

groupId

, we can also implement richer aggregation and drill-down animations.

Aggregation of data.

Drilling down of a single series into two series:

Universal transition take the ability to express the relationships and evolution of data to a new level, giving wings to your visualization creation inspiration.

At this point, we know you're already eager to try it out. But don't worry, there are even more new features in 5.2.0 that are worth checking out.

Color palette picking strategy

In the above universal transition example, you may have noticed that we use a

colorBy

configuration that was not available in the previous version. This configuration is also a new feature we added in this version to configure different granularity of color palette color picking for the series. This configuration currently supports two strategies.

'series'

assigns the colors in the palette by series, so that all data in the same series are in the same color.

'data'

assigns colors in the palette according to data items, with each data item using a different color.

Previously, we fixed this strategy for each type of series, for example, the bar chart was fixed with

'series'

and the pie chart was fixed with

'data'

.

And now with this new feature, we can assign a different color to each data item in the bar chart.

option = { xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] }, yAxis: { type: 'value' }, series: [ { data: [120, 200, 150, 80, 70, 110, 130], type: 'bar', colorBy: 'data' } ] };

option

=

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

,

colorBy

:

'data'

}

]

}

;

live

Or use one color uniformly in the pie chart.

option = { series: { type: 'pie', colorBy: 'series', radius: [0, '50%'], itemStyle: { borderColor: '#fff', borderWidth: 1 }, data: [ { value: 335, name: 'Direct Visit' }, { value: 234, name: 'Union Ad' }, { value: 1548, name: 'Search Engine' } ] } };

option

=

{

series

:

{

type

:

'pie'

,

colorBy

:

'series'

,

radius

:

[

0

,

'50%'

]

,

itemStyle

:

{

borderColor

:

'#fff'

,

borderWidth

:

1

}

,

data

:

[

{

value

:

335

,

name

:

'Direct Visit'

}

,

{

value

:

234

,

name

:

'Union Ad'

}

,

{

value

:

1548

,

name

:

'Search Engine'

}

]

}

}

;

live

This configuration allows us to avoid the trouble of finding palette colors and setting them one by one, and may provide convenience in specific scenarios. We will further enhance this configuration later to provide more strategies.

Labels for polar bar charts

In this version we have implemented labels for bar charts on polar coordinates and support rich label positioning configurations. The following is a progress chart with labels displayed at the start points.

option = { angleAxis: { show: false, max: 10 }, radiusAxis: { show: false, type: 'category', data: ['AAA', 'BBB', 'CCC', 'DDD'] }, polar: {}, series: [ { type: 'bar', data: [3, 4, 5, 6], colorBy: 'data', roundCap: true, label: { show: true, // Try changing it to 'insideStart' position: 'start', formatter: '{b}' }, coordinateSystem: 'polar' } ] };

option

=

{

angleAxis

:

{

show

:

false

,

max

:

10

}

,

radiusAxis

:

{

show

:

false

,

type

:

'category'

,

data

:

[

'AAA'

,

'BBB'

,

'CCC'

,

'DDD'

]

}

,

polar

:

{

}

,

series

:

[

{

type

:

'bar'

,

data

:

[

3

,

4

,

5

,

6

]

,

colorBy

:

'data'

,

roundCap

:

true

,

label

:

{

show

:

true

,

// Try changing it to 'insideStart'

position

:

'start'

,

formatter

:

'{b}'

}

,

coordinateSystem

:

'polar'

}

]

}

;

live

More configurations for label positions.

This flexible label position configuration item greatly enriches the expressiveness of the polar bar chart, allowing the text to clearly match the corresponding data.

Pie chart style for empty data

In the previous version, if there was no data in the pie chart, the screen might be completely blank. Because there was no visual element, users may wonder if there was a bug.

To solve this problem, in this version we will default to display a gray placeholder circle when there is no data to prevent the screen from being completely blank. We can configure the style of this placeholder circle with

emptyCircleStyle

.

option = { series: [ { type: 'pie', data: [], // showEmptyCircle: false, emptyCircleStyle: { // change the style to empty circle color: 'transparent', borderColor: '#ddd', borderWidth: 1 } } ] };

option

=

{

series

:

[

{

type

:

'pie'

,

data

:

[

]

,

// showEmptyCircle: false,

emptyCircleStyle

:

{

// change the style to empty circle

color

:

'transparent'

,

borderColor

:

'#ddd'

,

borderWidth

:

1

}

}

]

}

;

live

If you don't want to show this gray circle, you can also set

showEmptyCircle: false

to turn it off.

Performance enhancements for high-dimensional data

We have introduced

dataset

since 4.0 to manage chart data. However, in some extreme scenarios with particularly high-dimensional (>100) data, we may encounter some dramatic performance degradation, such as the following scenario of visualizing a thousand-dimensional data through a thousand series (

#11907

), which may even may lead to getting stuck.

const

indices

=

Array

.

from

(

Array

(

1000

)

,

(

_

,

i

)

=>

{

return

`

index

${

i

}

`

;

}

)

;

const

option

=

{

xAxis

:

{

type

:

'category'

}

,

yAxis

:

{

}

,

dataset

:

{

// dimension: ['date', . . indices],

source

:

Array

.

from

(

Array

(

10

)

,

(

_

,

i

)

=>

{

return

{

date

:

i

,

...

.

indices

.

reduce

(

(

item

,

next

)

=>

{

item

[

next

]

=

Math

.

random

(

)

*

100

;

return

item

;

}

,

{

}

)

}

;

}

)

}

,

series

:

indices

.

map

(

index

=>

{

return

{

type

:

'line'

,

name

:

index

}

;

}

)

}

;

The reason for this performance problem is that we process the high-dimensional dataset at the bottom of each series as needed and save a copy of the processed data and the meta information about the dimensions of the data. This meant that the

1000 x 1000

dimensions had to be processed and saved in the example, which put a huge pressure on memory and garbage collection, resulting in a dramatic performance drop for high dimensions.

In the new version we have optimized this problem so that all series share the dataset storage as much as possible (whether or not they do depends on how the series uses the data). This optimization ensure that memory does not explode as the dataset dimensions and series grow, significantly improving initialization performance in this extreme scenario. The rendering time for the example just described has also been reduced to an acceptable 300 ms or less.

It is not just this high-dimensional scenario that benefits from this optimization. When using a dataset with large amount of data, multiple series only process the data once because of data sharing, so it can also bring significant performance gains.

Type optimization for custom series

Custom series provide a very flexible way to create series graphs. Compared to other series, the learning curve for custom series can be a bit steep. Therefore, in this release, we have further optimized the type of the core method

renderItem

in the custom series by making more precise inferences about the types of the parameters and return values of

renderItem

, so that it is possible to infer which properties of the elements can be set based on the type returned:

series

=

{

type

:

'custom'

,

renderItem

(

params

)

{

return

{

type

:

'group'

,

// The group type uses children to store children of other types

children

:

[

{

type

:

'circle'

,

// circle has the following configurable shape attributes

shape

:

{

r

:

10

,

cx

:

0

,

cy

:

0

}

,

// Configurable styles

style

:

{

fill

:

'red'

}

}

,

{

type

:

'rect'

,

// rect has the following configurable shape properties

shape

:

{

x

:

0

,

y

:

0

,

width

:

100

,

height

:

100

}

}

,

{

type

:

'path'

,

// Custom path shapes

shape

:

{

d

:

'...'

}

}

]

}

;

}

}

;

Summary

If you're interested in some of the features and optimizations in 5.2.0, you may want to update to the latest version of Apache ECharts and try it out for yourself.

If you're interested in what's next for Apache ECharts, you can also follow our development plans at

GitHub Milestone

. Feel free to join us as a contributor (learn more at

Wiki

).

Full Changelog

View the

Changelog

Contributors

Edit this page on GitHub

pissang

Ovilia
