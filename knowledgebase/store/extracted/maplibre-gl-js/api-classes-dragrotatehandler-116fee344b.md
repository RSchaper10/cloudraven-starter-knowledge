---
title: DragRotateHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/DragRotateHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:23.294133+00:00
kind: extracted-doc
---

# DragRotateHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/DragRotateHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:23.294133+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/DragRotateHandler/

Captured summary:

- DragRotateHandler - MapLibre GL JS Skip to content DragRotateHandler Defined in: ui/handler/shim/drag_rotate.ts:25 The DragRotateHandler allows the user to rotate the map by clicking and dragging the cursor while holding the right mouse button or ctrl key.
- Methods disable() disable (): void Defined in: ui/handler/shim/drag_rotate.ts:64 Disables the "drag to rotate" interaction.
- disable (); enable() enable (): void Defined in: ui/handler/shim/drag_rotate.ts:50 Enables the "drag to rotate" interaction.
- enable (); isActive() isActive (): boolean Defined in: ui/handler/shim/drag_rotate.ts:84 Returns a Boolean indicating whether the "drag to rotate" interaction is active, i.e.
- Returns boolean true if the "drag to rotate" interaction is active.

Extracted text:

DragRotateHandler - MapLibre GL JS

Skip to content

DragRotateHandler

Defined in:

ui/handler/shim/drag_rotate.ts:25

The

DragRotateHandler

allows the user to rotate the map by clicking and dragging the cursor while holding the right mouse button or

ctrl

key.

Methods

disable()

disable

():

void

Defined in:

ui/handler/shim/drag_rotate.ts:64

Disables the "drag to rotate" interaction.

Returns

void

Example

map

.

dragRotate

.

disable

();

enable()

enable

():

void

Defined in:

ui/handler/shim/drag_rotate.ts:50

Enables the "drag to rotate" interaction.

Returns

void

Example

map

.

dragRotate

.

enable

();

isActive()

isActive

():

boolean

Defined in:

ui/handler/shim/drag_rotate.ts:84

Returns a Boolean indicating whether the "drag to rotate" interaction is active, i.e. currently being used.

Returns

boolean

true

if the "drag to rotate" interaction is active.

isEnabled()

isEnabled

():

boolean

Defined in:

ui/handler/shim/drag_rotate.ts:75

Returns a Boolean indicating whether the "drag to rotate" interaction is enabled.

Returns

boolean

true

if the "drag to rotate" interaction is enabled.

Back to top
