---
title: BoxZoomHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/BoxZoomHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:21.043487+00:00
kind: extracted-doc
---

# BoxZoomHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/BoxZoomHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:21.043487+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/BoxZoomHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Handler/

Captured summary:

- BoxZoomHandler - MapLibre GL JS Skip to content BoxZoomHandler Defined in: ui/handler/box_zoom.ts:32 The BoxZoomHandler allows the user to zoom the map to fit within a bounding box.
- The bounding box is defined by clicking and holding shift while dragging the cursor.
- Implements Handler Methods disable() disable (): void Defined in: ui/handler/box_zoom.ts:99 Disables the "box zoom" interaction.
- disable (); Implementation of Handler.disable enable() enable (): void Defined in: ui/handler/box_zoom.ts:86 Enables the "box zoom" interaction.
- enable (); Implementation of Handler.enable isActive() isActive (): boolean Defined in: ui/handler/box_zoom.ts:74 Returns a Boolean indicating whether the "box zoom" interaction is active, i.e.

Extracted text:

BoxZoomHandler - MapLibre GL JS

Skip to content

BoxZoomHandler

Defined in:

ui/handler/box_zoom.ts:32

The

BoxZoomHandler

allows the user to zoom the map to fit within a bounding box. The bounding box is defined by clicking and holding

shift

while dragging the cursor.

Implements

Handler

Methods

disable()

disable

():

void

Defined in:

ui/handler/box_zoom.ts:99

Disables the "box zoom" interaction.

Returns

void

Example

map

.

boxZoom

.

disable

();

Implementation of

Handler.disable

enable()

enable

():

void

Defined in:

ui/handler/box_zoom.ts:86

Enables the "box zoom" interaction.

Returns

void

Example

map

.

boxZoom

.

enable

();

Implementation of

Handler.enable

isActive()

isActive

():

boolean

Defined in:

ui/handler/box_zoom.ts:74

Returns a Boolean indicating whether the "box zoom" interaction is active, i.e. currently being used.

Returns

boolean

true

if the "box zoom" interaction is active.

Implementation of

Handler

.

isActive

isEnabled()

isEnabled

():

boolean

Defined in:

ui/handler/box_zoom.ts:65

Returns a Boolean indicating whether the "box zoom" interaction is enabled.

Returns

boolean

true

if the "box zoom" interaction is enabled.

Implementation of

Handler.isEnabled

reset()

reset

():

void

Defined in:

ui/handler/box_zoom.ts:177

reset

can be called by the manager at any time and must reset everything to it's original state

Returns

void

Implementation of

Handler

.

reset

Back to top
