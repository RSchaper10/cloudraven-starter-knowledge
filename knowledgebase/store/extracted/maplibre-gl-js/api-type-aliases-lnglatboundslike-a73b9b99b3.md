---
title: LngLatBoundsLike - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatBoundsLike/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:18.954084+00:00
kind: extracted-doc
---

# LngLatBoundsLike - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatBoundsLike/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:18.954084+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatBoundsLike/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLatBounds/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatLike/

Captured summary:

- LngLatBoundsLike - MapLibre GL JS Skip to content LngLatBoundsLike LngLatBoundsLike = LngLatBounds | [ LngLatLike , LngLatLike ] | [ number , number , number , number ] Defined in: geo/lng_lat_bounds.ts:21 A LngLatBounds object, an array of LngLatLike objects in [sw, ne] order, or an array of numbers in [west, south, east, north] order.
- Example let v1 = new LngLatBounds ( new LngLat ( - 73.9876 , 40.7661 ), new LngLat ( - 73.9397 , 40.8002 ) ); let v2 = new LngLatBounds ([ - 73.9876 , 40.7661 ], [ - 73.9397 , 40.8002 ]) let v3 = [[ - 73.9876 , 40.7661 ], [ - 73.9397 , 40.8002 ]]; Back to top

Extracted text:

LngLatBoundsLike - MapLibre GL JS

Skip to content

LngLatBoundsLike

LngLatBoundsLike

=

LngLatBounds

| [

LngLatLike

,

LngLatLike

] | [

number

,

number

,

number

,

number

]

Defined in:

geo/lng_lat_bounds.ts:21

A

LngLatBounds

object, an array of

LngLatLike

objects in [sw, ne] order, or an array of numbers in [west, south, east, north] order.

Example

let

v1

=

new

LngLatBounds

(

new

LngLat

(

-

73.9876

,

40.7661

),

new

LngLat

(

-

73.9397

,

40.8002

)

);

let

v2

=

new

LngLatBounds

([

-

73.9876

,

40.7661

],

[

-

73.9397

,

40.8002

])

let

v3

=

[[

-

73.9876

,

40.7661

],

[

-

73.9397

,

40.8002

]];

Back to top
