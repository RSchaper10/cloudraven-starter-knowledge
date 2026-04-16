---
title: Scene - Three.js Docs
source_url: https://threejs.org/docs/pages/Scene.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:22.746312+00:00
kind: extracted-doc
---

# Scene - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Scene.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:22.746312+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Scene.html
- https://threejs.org/docs/pages/Color.html
- https://threejs.org/docs/pages/Texture.html
- https://threejs.org/docs/pages/Euler.html
- https://threejs.org/docs/pages/Fog.html
- https://threejs.org/docs/pages/FogExp2.html
- https://threejs.org/docs/pages/Material.html

Captured summary:

- Scene - Three.js Docs EventDispatcher → Object3D → Scene Constructor new Scene () Constructs a new scene.
- background : Color | Texture Defines the background of the scene.
- Valid inputs are: A color for defining a uniform colored background.
- A texture for defining a (flat) textured background.
- Cube textures or equirectangular textures for defining a skybox.

Extracted text:

Scene - Three.js Docs

EventDispatcher

→

Object3D

→

Scene

Constructor

new

Scene

()

Constructs a new scene.

Properties

.

background

:

Color

|

Texture

Defines the background of the scene. Valid inputs are:

A color for defining a uniform colored background.

A texture for defining a (flat) textured background.

Cube textures or equirectangular textures for defining a skybox.

Default is

null

.

.

backgroundBlurriness

: number

Sets the blurriness of the background. Only influences environment maps assigned to

Scene#background

. Valid input is a float between

0

and

1

.

Default is

0

.

.

backgroundIntensity

: number

Attenuates the color of the background. Only applies to background textures.

Default is

1

.

.

backgroundRotation

:

Euler

The rotation of the background in radians. Only influences environment maps assigned to

Scene#background

.

Default is

(0,0,0)

.

.

environment

:

Texture

Sets the environment map for all physical materials in the scene. However, it's not possible to overwrite an existing texture assigned to the

envMap

material property.

Default is

null

.

.

environmentIntensity

: number

Attenuates the color of the environment. Only influences environment maps assigned to

Scene#environment

.

Default is

1

.

.

environmentRotation

:

Euler

The rotation of the environment map in radians. Only influences physical materials in the scene when

Scene#environment

is used.

Default is

(0,0,0)

.

.

fog

:

Fog

|

FogExp2

A fog instance defining the type of fog that affects everything rendered in the scene.

Default is

null

.

.

isScene

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

overrideMaterial

:

Material

Forces everything in the scene to be rendered with the defined material. It is possible to exclude materials from override by setting

Material#allowOverride

to

false

.

Default is

null

.

Source

src/scenes/Scene.js
