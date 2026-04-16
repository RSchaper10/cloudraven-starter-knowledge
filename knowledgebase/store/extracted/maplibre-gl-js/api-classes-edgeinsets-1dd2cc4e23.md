---
title: EdgeInsets - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/EdgeInsets/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:16.745847+00:00
kind: extracted-doc
---

# EdgeInsets - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/EdgeInsets/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:16.745847+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/EdgeInsets/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/PaddingOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Complete/

Captured summary:

- EdgeInsets - MapLibre GL JS Skip to content EdgeInsets Defined in: geo/edge_insets.ts:12 An EdgeInset object represents screen space padding applied to the edges of the viewport.
- This shifts the apparent center or the vanishing point of the map.
- This is useful for adding floating UI elements on top of the map and having the vanishing point shift as UI elements resize.
- Methods getCenter() getCenter ( width : number , height : number ): Point Defined in: geo/edge_insets.ts:70 Utility method that computes the new apparent center or vanishing point after applying insets.
- This is in pixels and with the top left being (0.0) and +y being downwards.

Extracted text:

EdgeInsets - MapLibre GL JS

Skip to content

EdgeInsets

Defined in:

geo/edge_insets.ts:12

An

EdgeInset

object represents screen space padding applied to the edges of the viewport. This shifts the apparent center or the vanishing point of the map. This is useful for adding floating UI elements on top of the map and having the vanishing point shift as UI elements resize.

Methods

getCenter()

getCenter

(

width

:

number

,

height

:

number

):

Point

Defined in:

geo/edge_insets.ts:70

Utility method that computes the new apparent center or vanishing point after applying insets. This is in pixels and with the top left being (0.0) and +y being downwards.

Parameters

Parameter

Type

Description

width

number

the width

height

number

the height

Returns

Point

the point

interpolate()

interpolate

(

start

:

EdgeInsets

|

PaddingOptions

,

target

:

PaddingOptions

,

t

:

number

):

this

Defined in:

geo/edge_insets.ts:53

Interpolates the inset in-place. This maintains the current inset value for any inset not present in

target

.

Parameters

Parameter

Type

Description

start

EdgeInsets

|

PaddingOptions

interpolation start

target

PaddingOptions

interpolation target

t

number

interpolation step/weight

Returns

this

the insets

toJSON()

toJSON

():

Complete

<

PaddingOptions

>

Defined in:

geo/edge_insets.ts:95

Returns the current state as json, useful when you want to have a read-only representation of the inset.

Returns

Complete

<

PaddingOptions

>

state as json

Properties

bottom

bottom

:

number

Defined in:

geo/edge_insets.ts:20

Default Value

0

left

left

:

number

Defined in:

geo/edge_insets.ts:24

Default Value

0

right

right

:

number

Defined in:

geo/edge_insets.ts:28

Default Value

0

top

top

:

number

Defined in:

geo/edge_insets.ts:16

Default Value

0

Back to top
