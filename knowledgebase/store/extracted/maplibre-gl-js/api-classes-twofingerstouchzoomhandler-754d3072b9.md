---
title: TwoFingersTouchZoomHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchZoomHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:25.829585+00:00
kind: extracted-doc
---

# TwoFingersTouchZoomHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchZoomHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:25.829585+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchZoomHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/AroundCenterOptions/

Captured summary:

- TwoFingersTouchZoomHandler - MapLibre GL JS Skip to content TwoFingersTouchZoomHandler Defined in: ui/handler/two_fingers_touch.ts:153 The TwoFingersTouchHandler s allows the user to zoom the map two fingers Extends TwoFingersTouchHandler Methods disable() disable (): void Defined in: ui/handler/two_fingers_touch.ts:108 Disables the "drag to pitch" interaction.
- disable (); Inherited from TwoFingersTouchHandler.disable enable() enable ( options?
- : boolean | AroundCenterOptions ): void Defined in: ui/handler/two_fingers_touch.ts:95 Enables the "drag to pitch" interaction.
- boolean | AroundCenterOptions Returns void Example map .
- enable (); Inherited from TwoFingersTouchHandler.enable isActive() isActive (): boolean Defined in: ui/handler/two_fingers_touch.ts:127 Returns a Boolean indicating whether the "drag to pitch" interaction is active, i.e.

Extracted text:

TwoFingersTouchZoomHandler - MapLibre GL JS

Skip to content

TwoFingersTouchZoomHandler

Defined in:

ui/handler/two_fingers_touch.ts:153

The

TwoFingersTouchHandler

s allows the user to zoom the map two fingers

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

setZoomRate()

setZoomRate

(

zoomRate?

:

number

):

void

Defined in:

ui/handler/two_fingers_touch.ts:175

Sets the zoom rate of touch gestures.

Parameters

Parameter

Type

Description

zoomRate?

number

1 The rate used to scale touch movement to a zoom value. Set to

undefined

to restore the default.

Returns

void

Example

Slow down touch zoom

map

.

touchZoomRotate

.

setZoomRate

(

0.5

);

setZoomThreshold()

setZoomThreshold

(

zoomThreshold?

:

number

):

void

Defined in:

ui/handler/two_fingers_touch.ts:188

Sets the threshold before a pinch gesture starts zooming.

Parameters

Parameter

Type

Description

zoomThreshold?

number

0.1 The minimum zoom delta before the pinch gesture becomes active. Set to

undefined

to restore the default.

Returns

void

Example

Make pinch zoom less sensitive

map

.

touchZoomRotate

.

setZoomThreshold

(

0.3

);

Back to top
