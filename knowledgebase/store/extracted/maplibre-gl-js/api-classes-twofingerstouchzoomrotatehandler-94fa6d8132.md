---
title: TwoFingersTouchZoomRotateHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchZoomRotateHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:26.285690+00:00
kind: extracted-doc
---

# TwoFingersTouchZoomRotateHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchZoomRotateHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:26.285690+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TwoFingersTouchZoomRotateHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/AroundCenterOptions/

Captured summary:

- TwoFingersTouchZoomRotateHandler - MapLibre GL JS Skip to content TwoFingersTouchZoomRotateHandler Defined in: ui/handler/shim/two_fingers_touch.ts:13 The TwoFingersTouchZoomRotateHandler allows the user to zoom and rotate the map by pinching on a touchscreen.
- They can zoom with one finger by double tapping and dragging.
- On the second tap, hold the finger down and drag up or down to zoom in or out.
- Methods disable() disable (): void Defined in: ui/handler/shim/two_fingers_touch.ts:58 Disables the "pinch to rotate and zoom" interaction.
- disable (); disableRotation() disableRotation (): void Defined in: ui/handler/shim/two_fingers_touch.ts:121 Disables the "pinch to rotate" interaction, leaving the "pinch to zoom" interaction enabled.

Extracted text:

TwoFingersTouchZoomRotateHandler - MapLibre GL JS

Skip to content

TwoFingersTouchZoomRotateHandler

Defined in:

ui/handler/shim/two_fingers_touch.ts:13

The

TwoFingersTouchZoomRotateHandler

allows the user to zoom and rotate the map by pinching on a touchscreen.

They can zoom with one finger by double tapping and dragging. On the second tap, hold the finger down and drag up or down to zoom in or out.

Methods

disable()

disable

():

void

Defined in:

ui/handler/shim/two_fingers_touch.ts:58

Disables the "pinch to rotate and zoom" interaction.

Returns

void

Example

map

.

touchZoomRotate

.

disable

();

disableRotation()

disableRotation

():

void

Defined in:

ui/handler/shim/two_fingers_touch.ts:121

Disables the "pinch to rotate" interaction, leaving the "pinch to zoom" interaction enabled.

Returns

void

Example

map

.

touchZoomRotate

.

disableRotation

();

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

ui/handler/shim/two_fingers_touch.ts:43

Enables the "pinch to rotate and zoom" interaction.

Parameters

Parameter

Type

Description

options?

boolean

|

AroundCenterOptions

Options object.

Returns

void

Example

map

.

touchZoomRotate

.

enable

();

map

.

touchZoomRotate

.

enable

({

around

:

'center'

});

enableRotation()

enableRotation

():

void

Defined in:

ui/handler/shim/two_fingers_touch.ts:135

Enables the "pinch to rotate" interaction.

Returns

void

Example

map

.

touchZoomRotate

.

enable

();

map

.

touchZoomRotate

.

enableRotation

();

isActive()

isActive

():

boolean

Defined in:

ui/handler/shim/two_fingers_touch.ts:81

Returns true if the handler is enabled and has detected the start of a zoom/rotate gesture.

Returns

boolean

true

if the handler is active,

false

otherwise

isEnabled()

isEnabled

():

boolean

Defined in:

ui/handler/shim/two_fingers_touch.ts:70

Returns a Boolean indicating whether the "pinch to rotate and zoom" interaction is enabled.

Returns

boolean

true

if the "pinch to rotate and zoom" interaction is enabled.

setZoomRate()

setZoomRate

(

zoomRate?

:

number

):

void

Defined in:

ui/handler/shim/two_fingers_touch.ts:94

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

ui/handler/shim/two_fingers_touch.ts:108

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
