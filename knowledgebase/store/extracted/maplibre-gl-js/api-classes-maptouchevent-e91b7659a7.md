---
title: MapTouchEvent - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/MapTouchEvent/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:31.628159+00:00
kind: extracted-doc
---

# MapTouchEvent - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapTouchEvent/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:31.628159+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapTouchEvent/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Event/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapLibreEvent/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/DragPanHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchZoomRotateHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLat/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Captured summary:

- MapTouchEvent - MapLibre GL JS Skip to content MapTouchEvent Defined in: ui/events.ts:563 MapTouchEvent is the event type for touch-related map events.
- Extends Event Implements MapLibreEvent < TouchEvent > Accessors defaultPrevented Get Signature get defaultPrevented (): boolean Defined in: ui/events.ts:618 true if preventDefault has been called.
- Returns boolean Methods preventDefault() preventDefault (): void Defined in: ui/events.ts:611 Prevents subsequent default processing of the event by the map.
- Calling this method will prevent the following default map behaviors: On touchstart events, the behavior of DragPanHandler On touchstart events, the behavior of TwoFingersTouchZoomRotateHandler Returns void Properties lngLat lngLat : LngLat Defined in: ui/events.ts:582 The geographic location on the map of the center of the touch event points.
- lngLats lngLats : LngLat [] Defined in: ui/events.ts:600 The geographical locations on the map corresponding to a touch event's touches property.

Extracted text:

MapTouchEvent - MapLibre GL JS

Skip to content

MapTouchEvent

Defined in:

ui/events.ts:563

MapTouchEvent

is the event type for touch-related map events.

Extends

Event

Implements

MapLibreEvent

<

TouchEvent

>

Accessors

defaultPrevented

Get Signature

get

defaultPrevented

():

boolean

Defined in:

ui/events.ts:618

true

if

preventDefault

has been called.

Returns

boolean

Methods

preventDefault()

preventDefault

():

void

Defined in:

ui/events.ts:611

Prevents subsequent default processing of the event by the map.

Calling this method will prevent the following default map behaviors:

On

touchstart

events, the behavior of

DragPanHandler

On

touchstart

events, the behavior of

TwoFingersTouchZoomRotateHandler

Returns

void

Properties

lngLat

lngLat

:

LngLat

Defined in:

ui/events.ts:582

The geographic location on the map of the center of the touch event points.

lngLats

lngLats

:

LngLat

[]

Defined in:

ui/events.ts:600

The geographical locations on the map corresponding to a

touch event's

touches

property.

originalEvent

originalEvent

:

TouchEvent

Defined in:

ui/events.ts:577

The DOM event which caused the map event.

Implementation of

MapLibreEvent.originalEvent

point

point

:

Point

Defined in:

ui/events.ts:588

The pixel coordinates of the center of the touch event points, relative to the map and measured from the top left corner.

points

points

:

Point

[]

Defined in:

ui/events.ts:594

The array of pixel coordinates corresponding to a

touch event's

touches

property.

target

target

:

Map

Defined in:

ui/events.ts:572

The

Map

object that fired the event.

Implementation of

MapLibreEvent.target

type

type

:

"touchcancel"

|

"touchend"

|

"touchmove"

|

"touchstart"

Defined in:

ui/events.ts:567

The event type.

Implementation of

MapLibreEvent.type

Overrides

Event.type

Back to top
