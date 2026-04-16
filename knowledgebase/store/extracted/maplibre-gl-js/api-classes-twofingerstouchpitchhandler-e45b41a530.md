---
title: TwoFingersTouchPitchHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchPitchHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:24.898950+00:00
kind: extracted-doc
---

# TwoFingersTouchPitchHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchPitchHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:24.898950+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchPitchHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/AroundCenterOptions/

Captured summary:

- TwoFingersTouchPitchHandler - MapLibre GL JS Skip to content TwoFingersTouchPitchHandler Defined in: ui/handler/two_fingers_touch.ts:288 The TwoFingersTouchPitchHandler allows the user to pitch the map by dragging up and down with two fingers.
- Extends TwoFingersTouchHandler Methods disable() disable (): void Defined in: ui/handler/two_fingers_touch.ts:108 Disables the "drag to pitch" interaction.
- disable (); Inherited from TwoFingersTouchHandler.disable enable() enable ( options?
- : boolean | AroundCenterOptions ): void Defined in: ui/handler/two_fingers_touch.ts:95 Enables the "drag to pitch" interaction.
- boolean | AroundCenterOptions Returns void Example map .

Extracted text:

TwoFingersTouchPitchHandler - MapLibre GL JS

Skip to content

TwoFingersTouchPitchHandler

Defined in:

ui/handler/two_fingers_touch.ts:288

The

TwoFingersTouchPitchHandler

allows the user to pitch the map by dragging up and down with two fingers.

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
