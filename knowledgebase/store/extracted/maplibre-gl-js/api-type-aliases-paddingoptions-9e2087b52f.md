---
title: PaddingOptions - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/PaddingOptions/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:19.911655+00:00
kind: extracted-doc
---

# PaddingOptions - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/PaddingOptions/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:19.911655+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/PaddingOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/RequireAtLeastOne/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/examples/zoomto-linestring/
- https://maplibre.org/maplibre-gl-js/docs/examples/fitbounds/

Captured summary:

- PaddingOptions - MapLibre GL JS Skip to content PaddingOptions PaddingOptions = RequireAtLeastOne <{ bottom : number ; left : number ; right : number ; top : number ; }> Defined in: geo/edge_insets.ts:129 Options for setting padding on calls to methods such as Map.fitBounds , Map.fitScreenCoordinates , and Map.setPadding .
- Adjust these options to set the amount of padding in pixels added to the edges of the canvas.
- Set a uniform padding on all edges or individual values for each edge.
- All properties of this object must be non-negative integers.
- Examples let bbox = [[ - 79 , 43 ], [ - 73 , 45 ]]; map .

Extracted text:

PaddingOptions - MapLibre GL JS

Skip to content

PaddingOptions

PaddingOptions

=

RequireAtLeastOne

<{

bottom

:

number

;

left

:

number

;

right

:

number

;

top

:

number

; }>

Defined in:

geo/edge_insets.ts:129

Options for setting padding on calls to methods such as

Map.fitBounds

,

Map.fitScreenCoordinates

, and

Map.setPadding

. Adjust these options to set the amount of padding in pixels added to the edges of the canvas. Set a uniform padding on all edges or individual values for each edge. All properties of this object must be non-negative integers.

Examples

let

bbox

=

[[

-

79

,

43

],

[

-

73

,

45

]];

map

.

fitBounds

(

bbox

,

{

padding

:

{

top

:

10

,

bottom

:

25

,

left

:

15

,

right

:

5

}

});

let

bbox

=

[[

-

79

,

43

],

[

-

73

,

45

]];

map

.

fitBounds

(

bbox

,

{

padding

:

20

});

See

Fit to the bounds of a LineString

Fit a map to a bounding box

Back to top
