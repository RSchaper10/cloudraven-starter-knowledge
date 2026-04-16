---
title: Layers - Three.js Docs
source_url: https://threejs.org/docs/pages/Layers.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:29.198331+00:00
kind: extracted-doc
---

# Layers - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Layers.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:29.198331+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Layers.html

Captured summary:

- Layers - Three.js Docs Layers Constructor new Layers () Constructs a new layers instance, with membership initially set to layer 0 .
- mask : number A bit mask storing which of the 32 layers this layers object is currently a member of.
- disable ( layer : number ) Removes membership of the given layer.
- disableAll () Removes the membership from all layers.
- enable ( layer : number ) Adds membership of the given layer.

Extracted text:

Layers - Three.js Docs

Layers

Constructor

new

Layers

()

Constructs a new layers instance, with membership initially set to layer

0

.

Properties

.

mask

: number

A bit mask storing which of the 32 layers this layers object is currently a member of.

Methods

.

disable

( layer :

number

)

Removes membership of the given layer.

layer

The layer to enable.

.

disableAll

()

Removes the membership from all layers.

.

enable

( layer :

number

)

Adds membership of the given layer.

layer

The layer to enable.

.

enableAll

()

Adds membership to all layers.

.

isEnabled

( layer :

number

)

: boolean

Returns

true

if the given layer is enabled.

layer

The layer to test.

Returns:

Whether the given layer is enabled or not.

.

set

( layer :

number

)

Sets membership to the given layer, and remove membership all other layers.

layer

The layer to set.

.

test

( layers :

Layers

)

: boolean

Returns

true

if this and the given layers object have at least one layer in common.

layers

The layers to test.

Returns:

Whether this and the given layers object have at least one layer in common or not.

.

toggle

( layer :

number

)

Toggles the membership of the given layer.

layer

The layer to toggle.

Source

src/core/Layers.js
