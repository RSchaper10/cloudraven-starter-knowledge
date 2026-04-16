---
title: TwoFingersTouchRotateHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchRotateHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:25.370759+00:00
kind: extracted-doc
---

# TwoFingersTouchRotateHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchRotateHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:25.370759+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchRotateHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/AroundCenterOptions/

Captured summary:

- TwoFingersTouchRotateHandler - MapLibre GL JS Skip to content TwoFingersTouchRotateHandler Defined in: ui/handler/two_fingers_touch.ts:227 The TwoFingersTouchHandler s allows the user to rotate the map two fingers Extends TwoFingersTouchHandler Methods disable() disable (): void Defined in: ui/handler/two_fingers_touch.ts:108 Disables the "drag to pitch" interaction.
- disable (); Inherited from TwoFingersTouchHandler.disable enable() enable ( options?
- : boolean | AroundCenterOptions ): void Defined in: ui/handler/two_fingers_touch.ts:95 Enables the "drag to pitch" interaction.
- boolean | AroundCenterOptions Returns void Example map .
- enable (); Inherited from TwoFingersTouchHandler.enable isActive() isActive (): boolean Defined in: ui/handler/two_fingers_touch.ts:127 Returns a Boolean indicating whether the "drag to pitch" interaction is active, i.e.

Extracted text:

TwoFingersTouchRotateHandler - MapLibre GL JS

Skip to content

TwoFingersTouchRotateHandler

Defined in:

ui/handler/two_fingers_touch.ts:227

The

TwoFingersTouchHandler

s allows the user to rotate the map two fingers

Extends

TwoFingersTouchHandler

Methods

disable()

disable

():

void

Defined in:

ui/handler/two_fingers_touch.ts:108

Disables the "drag to pitch" interaction.

Returns

void

Example

map

.

touchPitch

.

disable

();

Inherited from

TwoFingersTouchHandler.disable

enable()

enable

(

options?

:

boolean

|

AroundCenterOptions

):

void

Defined in:

ui/handler/two_fingers_touch.ts:95

Enables the "drag to pitch" interaction.

Parameters

Parameter

Type

options?

boolean

|

AroundCenterOptions

Returns

void

Example

map

.

touchPitch

.

enable

();

Inherited from

TwoFingersTouchHandler.enable

isActive()

isActive

():

boolean

Defined in:

ui/handler/two_fingers_touch.ts:127

Returns a Boolean indicating whether the "drag to pitch" interaction is active, i.e. currently being used.

Returns

boolean

true

if the "drag to pitch" interaction is active.

Inherited from

TwoFingersTouchHandler.isActive

isEnabled()

isEnabled

():

boolean

Defined in:

ui/handler/two_fingers_touch.ts:118

Returns a Boolean indicating whether the "drag to pitch" interaction is enabled.

Returns

boolean

true

if the "drag to pitch" interaction is enabled.

Inherited from

TwoFingersTouchHandler.isEnabled

Back to top
