---
title: Intro - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:08.202888+00:00
kind: extracted-doc
---

# Intro - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:08.202888+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/
- https://maplibre.org/maplibre-gl-js/docs/examples/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/AttributionControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/FullscreenControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/GeolocateControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/GlobeControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Hash/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LogoControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Marker/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/NavigationControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Popup/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/ScaleControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/TerrainControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/EdgeInsets/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLat/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLatBounds/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/MercatorCoordinate/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatBoundsLike/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatLike/

Captured summary:

- Intro - MapLibre GL JS Skip to content Intro This file is intended as a reference for the important and public classes of this API.
- We recommend looking at the examples as they will help you the most to start with MapLibre.
- Most of the classes written here have an "Options" object for initialization, it is recommended to check which options exist.
- It is recommended to import what you need and then use it.
- Some examples for classes assume you did that.

Extracted text:

Intro - MapLibre GL JS

Skip to content

Intro

This file is intended as a reference for the important and public classes of this API. We recommend looking at the

examples

as they will help you the most to start with MapLibre.

Most of the classes written here have an "Options" object for initialization, it is recommended to check which options exist.

It is recommended to import what you need and then use it. Some examples for classes assume you did that. For example, import the

Map

class like this:

import

{

Map

}

from

'maplibre-gl'

;

const

map

=

new

Map

(...)

Import declarations are omitted from the examples for brevity.

Main

Map

Markers and Controls

AttributionControl

FullscreenControl

GeolocateControl

GlobeControl

Hash

LogoControl

Marker

NavigationControl

Popup

ScaleControl

TerrainControl

Geography and Geometry

EdgeInsets

LngLat

LngLatBounds

MercatorCoordinate

LngLatBoundsLike

LngLatLike

PaddingOptions

PointLike

Handlers

BoxZoomHandler

CooperativeGesturesHandler

DoubleClickZoomHandler

DragPanHandler

DragRotateHandler

KeyboardHandler

ScrollZoomHandler

TwoFingersTouchPitchHandler

TwoFingersTouchRotateHandler

TwoFingersTouchZoomHandler

TwoFingersTouchZoomRotateHandler

Sources

CanvasSource

GeoJSONSource

ImageSource

RasterDEMTileSource

VectorTileSource

VideoSource

Source

Event Related

Evented

MapMouseEvent

MapTouchEvent

MapWheelEvent

MapContextEvent

MapDataEvent

MapEventType

MapLayerEventType

MapLayerMouseEvent

MapLayerTouchEvent

MapLibreEvent

MapLibreZoomEvent

MapProjectionEvent

MapSourceDataEvent

MapStyleDataEvent

MapStyleImageMissingEvent

MapTerrainEvent

Back to top
