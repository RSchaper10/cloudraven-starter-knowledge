---
title: CooperativeGesturesHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/CooperativeGesturesHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:21.535964+00:00
kind: extracted-doc
---

# CooperativeGesturesHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/CooperativeGesturesHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:21.535964+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/CooperativeGesturesHandler/
- https://maplibre.org/maplibre-gl-js/docs/examples/cooperative-gestures/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Handler/

Captured summary:

- CooperativeGesturesHandler - MapLibre GL JS Skip to content CooperativeGesturesHandler Defined in: ui/handler/cooperative_gestures.ts:27 A CooperativeGestureHandler is a control that adds cooperative gesture info when user tries to zoom in/out.
- When the CooperativeGestureHandler blocks a gesture, it will emit a cooperativegestureprevented event.
- Example const map = new Map ({ cooperativeGestures : true }); See Example: cooperative gestures Implements Handler Methods isActive() isActive (): boolean Defined in: ui/handler/cooperative_gestures.ts:42 This is used to indicate if the handler is currently active or not.
- In case a handler is active, it will block other handlers from getting the relevant events.
- There is an allow list of handlers that can be active at the same time, which is configured when adding a handler.

Extracted text:

CooperativeGesturesHandler - MapLibre GL JS

Skip to content

CooperativeGesturesHandler

Defined in:

ui/handler/cooperative_gestures.ts:27

A

CooperativeGestureHandler

is a control that adds cooperative gesture info when user tries to zoom in/out.

When the CooperativeGestureHandler blocks a gesture, it will emit a

cooperativegestureprevented

event.

Example

const

map

=

new

Map

({

cooperativeGestures

:

true

});

See

Example: cooperative gestures

Implements

Handler

Methods

isActive()

isActive

():

boolean

Defined in:

ui/handler/cooperative_gestures.ts:42

This is used to indicate if the handler is currently active or not. In case a handler is active, it will block other handlers from getting the relevant events. There is an allow list of handlers that can be active at the same time, which is configured when adding a handler.

Returns

boolean

Implementation of

Handler

.

isActive

reset()

reset

():

void

Defined in:

ui/handler/cooperative_gestures.ts:45

reset

can be called by the manager at any time and must reset everything to it's original state

Returns

void

Implementation of

Handler

.

reset

Properties

_bypassKey

_bypassKey

:

"ctrlKey"

|

"metaKey"

Defined in:

ui/handler/cooperative_gestures.ts:34

This is the key that will allow to bypass the cooperative gesture protection

Back to top
