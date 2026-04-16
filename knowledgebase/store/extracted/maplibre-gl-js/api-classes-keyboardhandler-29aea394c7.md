---
title: KeyboardHandler - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/KeyboardHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:23.818073+00:00
kind: extracted-doc
---

# KeyboardHandler - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/KeyboardHandler/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:23.818073+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/KeyboardHandler/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Handler/

Captured summary:

- KeyboardHandler - MapLibre GL JS Skip to content KeyboardHandler Defined in: ui/handler/keyboard.ts:28 The KeyboardHandler allows the user to zoom, rotate, and pan the map using the following keyboard shortcuts: = / + : Increase the zoom level by 1.
- Shift-= / Shift-+ : Increase the zoom level by 2.
- Shift+⇢ : Increase the rotation by 15 degrees.
- Shift+⇠ : Decrease the rotation by 15 degrees.
- Shift+⇡ : Increase the pitch by 10 degrees.

Extracted text:

KeyboardHandler - MapLibre GL JS

Skip to content

KeyboardHandler

Defined in:

ui/handler/keyboard.ts:28

The

KeyboardHandler

allows the user to zoom, rotate, and pan the map using the following keyboard shortcuts:

=

/

+

: Increase the zoom level by 1.

Shift-=

/

Shift-+

: Increase the zoom level by 2.

-

: Decrease the zoom level by 1.

Shift--

: Decrease the zoom level by 2.

Arrow keys: Pan by 100 pixels.

Shift+⇢

: Increase the rotation by 15 degrees.

Shift+⇠

: Decrease the rotation by 15 degrees.

Shift+⇡

: Increase the pitch by 10 degrees.

Shift+⇣

: Decrease the pitch by 10 degrees.

Implements

Handler

Methods

disable()

disable

():

void

Defined in:

ui/handler/keyboard.ts:157

Disables the "keyboard rotate and zoom" interaction.

Returns

void

Example

map

.

keyboard

.

disable

();

Implementation of

Handler.disable

disableRotation()

disableRotation

():

void

Defined in:

ui/handler/keyboard.ts:193

Disables the "keyboard pan/rotate" interaction, leaving the "keyboard zoom" interaction enabled.

Returns

void

Example

map

.

keyboard

.

disableRotation

();

enable()

enable

():

void

Defined in:

ui/handler/keyboard.ts:145

Enables the "keyboard rotate and zoom" interaction.

Returns

void

Example

map

.

keyboard

.

enable

();

Implementation of

Handler.enable

enableRotation()

enableRotation

():

void

Defined in:

ui/handler/keyboard.ts:206

Enables the "keyboard pan/rotate" interaction.

Returns

void

Example

map

.

keyboard

.

enable

();

map

.

keyboard

.

enableRotation

();

isActive()

isActive

():

boolean

Defined in:

ui/handler/keyboard.ts:180

Returns true if the handler is enabled and has detected the start of a zoom/rotate gesture.

Returns

boolean

true

if the handler is enabled and has detected the start of a zoom/rotate gesture.

Implementation of

Handler

.

isActive

isEnabled()

isEnabled

():

boolean

Defined in:

ui/handler/keyboard.ts:169

Returns a Boolean indicating whether the "keyboard rotate and zoom" interaction is enabled.

Returns

boolean

true

if the "keyboard rotate and zoom" interaction is enabled.

Implementation of

Handler.isEnabled

reset()

reset

():

void

Defined in:

ui/handler/keyboard.ts:47

reset

can be called by the manager at any time and must reset everything to it's original state

Returns

void

Implementation of

Handler

.

reset

Back to top
