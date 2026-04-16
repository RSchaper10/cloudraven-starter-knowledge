---
title: MapMouseEvent - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/MapMouseEvent/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:31.138311+00:00
kind: extracted-doc
---

# MapMouseEvent - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapMouseEvent/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:31.138311+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapMouseEvent/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Event/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapLibreEvent/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/DragPanHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/DragRotateHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/BoxZoomHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/DoubleClickZoomHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLat/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Captured summary:

- MapMouseEvent - MapLibre GL JS Skip to content MapMouseEvent Defined in: ui/events.ts:498 MapMouseEvent is the event type for mouse-related map events.
- Example // The `click` event is an example of a `MapMouseEvent`.
- on ( 'click' , ( e ) => { // The event object (e) contains information like the // coordinates of the point on the map that was clicked.
- log ( 'A click event has occurred at ' + e .
- lngLat ); }); Extends Event Implements MapLibreEvent < MouseEvent > Accessors defaultPrevented Get Signature get defaultPrevented (): boolean Defined in: ui/events.ts:542 true if preventDefault has been called.

Extracted text:

MapMouseEvent - MapLibre GL JS

Skip to content

MapMouseEvent

Defined in:

ui/events.ts:498

MapMouseEvent

is the event type for mouse-related map events.

Example

// The `click` event is an example of a `MapMouseEvent`.

// Set up an event listener on the map.

map

.

on

(

'click'

,

(

e

)

=>

{

// The event object (e) contains information like the

// coordinates of the point on the map that was clicked.

console

.

log

(

'A click event has occurred at '

+

e

.

lngLat

);

});

Extends

Event

Implements

MapLibreEvent

<

MouseEvent

>

Accessors

defaultPrevented

Get Signature

get

defaultPrevented

():

boolean

Defined in:

ui/events.ts:542

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

ui/events.ts:535

Prevents subsequent default processing of the event by the map.

Calling this method will prevent the following default map behaviors:

On

mousedown

events, the behavior of

DragPanHandler

On

mousedown

events, the behavior of

DragRotateHandler

On

mousedown

events, the behavior of

BoxZoomHandler

On

dblclick

events, the behavior of

DoubleClickZoomHandler

Returns

void

Properties

lngLat

lngLat

:

LngLat

Defined in:

ui/events.ts:522

The geographic location on the map of the mouse cursor.

originalEvent

originalEvent

:

MouseEvent

Defined in:

ui/events.ts:512

The DOM event which caused the map event.

Implementation of

MapLibreEvent.originalEvent

point

point

:

Point

Defined in:

ui/events.ts:517

The pixel coordinates of the mouse cursor, relative to the map and measured from the top left corner.

target

target

:

Map

Defined in:

ui/events.ts:507

The

Map

object that fired the event.

Implementation of

MapLibreEvent.target

type

type

:

"click"

|

"contextmenu"

|

"dblclick"

|

"mousedown"

|

"mouseenter"

|

"mouseleave"

|

"mousemove"

|

"mouseout"

|

"mouseover"

|

"mouseup"

Defined in:

ui/events.ts:502

The event type

Implementation of

MapLibreEvent.type

Overrides

Event.type

Back to top
