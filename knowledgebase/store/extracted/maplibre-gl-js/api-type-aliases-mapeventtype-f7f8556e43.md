---
title: MapEventType - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapEventType/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:33.849713+00:00
kind: extracted-doc
---

# MapEventType - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapEventType/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:33.849713+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapEventType/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapLayerEventType/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapLibreZoomEvent/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/BoxZoomHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapMouseEvent/
- https://maplibre.org/maplibre-gl-js/docs/examples/measure-distances/
- https://maplibre.org/maplibre-gl-js/docs/examples/center-the-map-on-a-clicked-symbol/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapLibreEvent/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapDataEvent/
- https://maplibre.org/maplibre-gl-js/docs/examples/display-html-clusters-with-custom-properties/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/DragPanHandler/
- https://maplibre.org/maplibre-gl-js/docs/examples/create-a-draggable-marker/
- https://maplibre.org/maplibre-gl-js/docs/examples/draw-geojson-points/
- https://maplibre.org/maplibre-gl-js/docs/examples/add-live-realtime-data/
- https://maplibre.org/maplibre-gl-js/docs/examples/animate-a-point/
- https://maplibre.org/maplibre-gl-js/docs/examples/create-a-draggable-point/
- https://maplibre.org/maplibre-gl-js/docs/examples/get-coordinates-of-the-mouse-pointer/
- https://maplibre.org/maplibre-gl-js/docs/examples/create-a-hover-effect/
- https://maplibre.org/maplibre-gl-js/docs/examples/display-a-popup-on-hover/

Captured summary:

- MapEventType - MapLibre GL JS Skip to content MapEventType MapEventType = object Defined in: ui/events.ts:152 MapEventType - a mapping between the event name and the event value.
- These events are used with the Map.on method.
- When using a layerId with Map.on method, please refer to MapLayerEventType .
- The following example can be used for all the events.
- Example // Initialize the map let map = new Map ({ // map options }); // Set an event listener map .

Extracted text:

MapEventType - MapLibre GL JS

Skip to content

MapEventType

MapEventType

=

object

Defined in:

ui/events.ts:152

MapEventType

- a mapping between the event name and the event value. These events are used with the

Map.on

method. When using a

layerId

with

Map.on

method, please refer to

MapLayerEventType

. The following example can be used for all the events.

Example

// Initialize the map

let

map

=

new

Map

({

// map options });

// Set an event listener

map

.

on

(

'the-event-name'

,

()

=>

{

console

.

log

(

'An event has occurred!'

);

});

Properties

boxzoomcancel

boxzoomcancel

:

MapLibreZoomEvent

Defined in:

ui/events.ts:254

Fired when the user cancels a "box zoom" interaction, or when the bounding box does not meet the minimum size threshold. See

BoxZoomHandler

.

boxzoomend

boxzoomend

:

MapLibreZoomEvent

Defined in:

ui/events.ts:262

Fired when a "box zoom" interaction ends. See

BoxZoomHandler

.

boxzoomstart

boxzoomstart

:

MapLibreZoomEvent

Defined in:

ui/events.ts:258

Fired when a "box zoom" interaction starts. See

BoxZoomHandler

.

click

click

:

MapMouseEvent

Defined in:

ui/events.ts:288

Fired when a pointing device (usually a mouse) is pressed and released at the same point on the map.

See

Measure distances

Center the map on a clicked symbol

contextmenu

contextmenu

:

MapMouseEvent

Defined in:

ui/events.ts:292

Fired when the right button of the mouse is clicked or the context menu key is pressed within the map.

cooperativegestureprevented

cooperativegestureprevented

:

MapLibreEvent

<

WheelEvent

|

TouchEvent

> &

object

Defined in:

ui/events.ts:423

Fired whenever the cooperativeGestures option prevents a gesture from being handled by the map. This is useful for showing your own UI when this happens.

Type Declaration

gestureType

gestureType

:

"wheel_zoom"

|

"touch_pan"

data

data

:

MapDataEvent

Defined in:

ui/events.ts:213

Fired when any map data loads or changes. See

MapDataEvent

for more information.

See

Display HTML clusters with custom properties

dataabort

dataabort

:

MapDataEvent

Defined in:

ui/events.ts:245

Fired when a request for one of the map's sources' tiles or data is aborted.

dataloading

dataloading

:

MapDataEvent

Defined in:

ui/events.ts:208

Fired when any map data (style, source, tile, etc) begins loading or changing asynchronously. All

dataloading

events are followed by a

data

,

dataabort

or

error

event.

dblclick

dblclick

:

MapMouseEvent

Defined in:

ui/events.ts:299

Fired when a pointing device (usually a mouse) is pressed and released twice at the same point on the map in rapid succession.

Note

Under normal conditions, this event will be preceded by two

click

events.

drag

drag

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:389

Fired repeatedly during a "drag to pan" interaction. See

DragPanHandler

.

dragend

dragend

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:394

Fired when a "drag to pan" interaction ends. See

DragPanHandler

.

See

Create a draggable marker

dragstart

dragstart

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:385

Fired when a "drag to pan" interaction starts. See

DragPanHandler

.

error

error

:

ErrorEvent

Defined in:

ui/events.ts:159

Fired when an error occurs. This is GL JS's primary error reporting mechanism. We use an event instead of

throw

to better accommodate asynchronous operations. If no listeners are bound to the

error

event, the error will be printed to the console.

idle

idle

:

MapLibreEvent

Defined in:

ui/events.ts:177

Fired after the last frame rendered before the map enters an "idle" state:

No camera transitions are in progress

All currently requested tiles have loaded

All fade/transition animations have completed

load

load

:

MapLibreEvent

Defined in:

ui/events.ts:168

Fired immediately after all necessary resources have been downloaded and the first visually complete rendering of the map has occurred.

See

Draw GeoJSON points

Add live realtime data

Animate a point

mousedown

mousedown

:

MapMouseEvent

Defined in:

ui/events.ts:320

Fired when a pointing device (usually a mouse) is pressed within the map.

See

Create a draggable point

mousemove

mousemove

:

MapMouseEvent

Defined in:

ui/events.ts:308

Fired when a pointing device (usually a mouse) is moved while the cursor is inside the map. As you move the cursor across the map, the event will fire every time the cursor changes position within the map.

See

Get coordinates of the mouse pointer

Highlight features under the mouse pointer

Display a popup on over

mouseout

mouseout

:

MapMouseEvent

Defined in:

ui/events.ts:324

Fired when a point device (usually a mouse) leaves the map's canvas.

mouseover

mouseover

:

MapMouseEvent

Defined in:

ui/events.ts:334

Fired when a pointing device (usually a mouse) is moved within the map. As you move the cursor across a web page containing a map, the event will fire each time it enters the map or any child elements.

See

Get coordinates of the mouse pointer

Highlight features under the mouse pointer

Display a popup on hover

mouseup

mouseup

:

MapMouseEvent

Defined in:

ui/events.ts:314

Fired when a pointing device (usually a mouse) is released within the map.

See

Create a draggable point

move

move

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

WheelEvent

|

undefined

>

Defined in:

ui/events.ts:347

Fired repeatedly during an animated transition from one view to another, as the result of either user interaction or methods such as

Map.flyTo

.

See

Display HTML clusters with custom properties

moveend

moveend

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

WheelEvent

|

undefined

>

Defined in:

ui/events.ts:354

Fired just after the map completes a transition from one view to another, as the result of either user interaction or methods such as

Map.jumpTo

.

See

Display HTML clusters with custom properties

movestart

movestart

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

WheelEvent

|

undefined

>

Defined in:

ui/events.ts:340

Fired just before the map begins a transition from one view to another, as the result of either user interaction or methods such as

Map.jumpTo

.

pitch

pitch

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:405

Fired repeatedly during the map's pitch (tilt) animation between one state and another as the result of either user interaction or methods such as

Map.flyTo

.

pitchend

pitchend

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:410

Fired immediately after the map's pitch (tilt) finishes changing as the result of either user interaction or methods such as

Map.flyTo

.

pitchstart

pitchstart

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:399

Fired whenever the map's pitch (tilt) begins a change as the result of either user interaction or methods such as

Map.flyTo

.

projectiontransition

projectiontransition

:

MapProjectionEvent

Defined in:

ui/events.ts:429

Fired when map's projection is modified in other ways than by map being moved.

remove

remove

:

MapLibreEvent

Defined in:

ui/events.ts:181

Fired immediately after the map has been removed with

Map.remove

.

render

render

:

MapLibreEvent

Defined in:

ui/events.ts:190

Fired whenever the map is drawn to the screen, as the result of

a change to the map's position, zoom, pitch, or bearing

a change to the map's style

a change to a GeoJSON source

the loading of a vector tile, GeoJSON file, glyph, or sprite

resize

resize

:

MapLibreEvent

Defined in:

ui/events.ts:194

Fired immediately after the map has been resized.

rotate

rotate

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:377

Fired repeatedly during a "drag to rotate" interaction. See

DragRotateHandler

.

rotateend

rotateend

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:381

Fired when a "drag to rotate" interaction ends. See

DragRotateHandler

.

rotatestart

rotatestart

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

undefined

>

Defined in:

ui/events.ts:373

Fired when a "drag to rotate" interaction starts. See

DragRotateHandler

.

sourcedata

sourcedata

:

MapSourceDataEvent

Defined in:

ui/events.ts:230

Fired when one of the map's sources loads or changes, including if a tile belonging to a source loads or changes.

sourcedataabort

sourcedataabort

:

MapSourceDataEvent

Defined in:

ui/events.ts:249

Fired when a request for one of the map's sources' data is aborted.

sourcedataloading

sourcedataloading

:

MapSourceDataEvent

Defined in:

ui/events.ts:219

Fired when one of the map's sources begins loading or changing asynchronously. All

sourcedataloading

events are followed by a

sourcedata

,

sourcedataabort

or

error

event.

styledata

styledata

:

MapStyleDataEvent

Defined in:

ui/events.ts:234

Fired when the map's style loads or changes.

styledataloading

styledataloading

:

MapStyleDataEvent

Defined in:

ui/events.ts:225

Fired when the map's style begins loading or changing asynchronously. All

styledataloading

events are followed by a

styledata

or

error

event.

styleimagemissing

styleimagemissing

:

MapStyleImageMissingEvent

Defined in:

ui/events.ts:241

Fired when an icon or pattern needed by the style is missing. The missing image can be added with

Map.addImage

within this event listener callback to prevent the image from being skipped. This event can be used to dynamically generate icons and patterns.

See

Generate and add a missing icon to the map

terrain

terrain

:

MapTerrainEvent

Defined in:

ui/events.ts:418

Fired when terrain is changed

touchcancel

touchcancel

:

MapTouchEvent

Defined in:

ui/events.ts:266

Fired when a

touchcancel

event occurs within the map.

touchend

touchend

:

MapTouchEvent

Defined in:

ui/events.ts:276

Fired when a

touchend

event occurs within the map.

See

Create a draggable point

touchmove

touchmove

:

MapTouchEvent

Defined in:

ui/events.ts:271

Fired when a

touchmove

event occurs within the map.

See

Create a draggable point

touchstart

touchstart

:

MapTouchEvent

Defined in:

ui/events.ts:281

Fired when a

touchstart

event occurs within the map.

See

Create a draggable point

webglcontextlost

webglcontextlost

:

MapContextEvent

Defined in:

ui/events.ts:198

Fired when the WebGL context is lost.

webglcontextrestored

webglcontextrestored

:

MapContextEvent

Defined in:

ui/events.ts:202

Fired when the WebGL context is restored.

wheel

wheel

:

MapWheelEvent

Defined in:

ui/events.ts:414

Fired when a

wheel

event occurs within the map.

zoom

zoom

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

WheelEvent

|

undefined

>

Defined in:

ui/events.ts:364

Fired repeatedly during an animated transition from one zoom level to another, as the result of either user interaction or methods such as

Map.flyTo

.

zoomend

zoomend

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

WheelEvent

|

undefined

>

Defined in:

ui/events.ts:369

Fired just after the map completes a transition from one zoom level to another, as the result of either user interaction or methods such as

Map.flyTo

.

zoomstart

zoomstart

:

MapLibreEvent

<

MouseEvent

|

TouchEvent

|

WheelEvent

|

undefined

>

Defined in:

ui/events.ts:359

Fired just before the map begins a transition from one zoom level to another, as the result of either user interaction or methods such as

Map.flyTo

.

Back to top
