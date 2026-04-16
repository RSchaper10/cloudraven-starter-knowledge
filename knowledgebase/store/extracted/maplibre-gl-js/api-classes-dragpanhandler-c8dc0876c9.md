---
title: DragPanHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/DragPanHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:22.517421+00:00
kind: extracted-doc
---

# DragPanHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/DragPanHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:22.517421+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/DragPanHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/DragPanOptions/

Captured summary:

- DragPanHandler - MapLibre GL JS Skip to content DragPanHandler Defined in: ui/handler/shim/drag_pan.ts:37 The DragPanHandler allows the user to pan the map by clicking and dragging the cursor.
- Methods disable() disable (): void Defined in: ui/handler/shim/drag_pan.ts:81 Disables the "drag to pan" interaction.
- : boolean | DragPanOptions ): void Defined in: ui/handler/shim/drag_pan.ts:66 Enables the "drag to pan" interaction.
- Parameters Parameter Type Description options?
- boolean | DragPanOptions Options object Returns void Example map .

Extracted text:

DragPanHandler - MapLibre GL JS

Skip to content

DragPanHandler

Defined in:

ui/handler/shim/drag_pan.ts:37

The

DragPanHandler

allows the user to pan the map by clicking and dragging the cursor.

Methods

disable()

disable

():

void

Defined in:

ui/handler/shim/drag_pan.ts:81

Disables the "drag to pan" interaction.

Returns

void

Example

map

.

dragPan

.

disable

();

enable()

enable

(

options?

:

boolean

|

DragPanOptions

):

void

Defined in:

ui/handler/shim/drag_pan.ts:66

Enables the "drag to pan" interaction.

Parameters

Parameter

Type

Description

options?

boolean

|

DragPanOptions

Options object

Returns

void

Example

map

.

dragPan

.

enable

();

map

.

dragPan

.

enable

({

linearity

:

0.3

,

easing

:

bezier

(

0

,

0

,

0.3

,

1

),

maxSpeed

:

1400

,

deceleration

:

2500

,

});

isActive()

isActive

():

boolean

Defined in:

ui/handler/shim/drag_pan.ts:101

Returns a Boolean indicating whether the "drag to pan" interaction is active, i.e. currently being used.

Returns

boolean

true

if the "drag to pan" interaction is active.

isEnabled()

isEnabled

():

boolean

Defined in:

ui/handler/shim/drag_pan.ts:92

Returns a Boolean indicating whether the "drag to pan" interaction is enabled.

Returns

boolean

true

if the "drag to pan" interaction is enabled.

Back to top
