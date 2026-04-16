---
title: MapWheelEvent - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/MapWheelEvent/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:32.091233+00:00
kind: extracted-doc
---

# MapWheelEvent - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapWheelEvent/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:32.091233+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapWheelEvent/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Event/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/ScrollZoomHandler/

Captured summary:

- MapWheelEvent - MapLibre GL JS Skip to content MapWheelEvent Defined in: ui/events.ts:642 MapWheelEvent is the event type for the wheel map event.
- Extends Event Accessors defaultPrevented Get Signature get defaultPrevented (): boolean Defined in: ui/events.ts:670 true if preventDefault has been called.
- Returns boolean Constructors Constructor new MapWheelEvent ( type : string , map : Map , originalEvent : WheelEvent ): MapWheelEvent Defined in: ui/events.ts:677 Parameters Parameter Type type string map Map originalEvent WheelEvent Returns MapWheelEvent Overrides Event.constructor Methods preventDefault() preventDefault (): void Defined in: ui/events.ts:663 Prevents subsequent default processing of the event by the map.
- Calling this method will prevent the behavior of ScrollZoomHandler .
- Returns void Properties originalEvent originalEvent : WheelEvent Defined in: ui/events.ts:656 The DOM event which caused the map event.

Extracted text:

MapWheelEvent - MapLibre GL JS

Skip to content

MapWheelEvent

Defined in:

ui/events.ts:642

MapWheelEvent

is the event type for the

wheel

map event.

Extends

Event

Accessors

defaultPrevented

Get Signature

get

defaultPrevented

():

boolean

Defined in:

ui/events.ts:670

true

if

preventDefault

has been called.

Returns

boolean

Constructors

Constructor

new MapWheelEvent

(

type

:

string

,

map

:

Map

,

originalEvent

:

WheelEvent

):

MapWheelEvent

Defined in:

ui/events.ts:677

Parameters

Parameter

Type

type

string

map

Map

originalEvent

WheelEvent

Returns

MapWheelEvent

Overrides

Event.constructor

Methods

preventDefault()

preventDefault

():

void

Defined in:

ui/events.ts:663

Prevents subsequent default processing of the event by the map.

Calling this method will prevent the behavior of

ScrollZoomHandler

.

Returns

void

Properties

originalEvent

originalEvent

:

WheelEvent

Defined in:

ui/events.ts:656

The DOM event which caused the map event.

target

target

:

Map

Defined in:

ui/events.ts:651

The

Map

object that fired the event.

type

type

:

"wheel"

Defined in:

ui/events.ts:646

The event type.

Overrides

Event.type

Back to top
