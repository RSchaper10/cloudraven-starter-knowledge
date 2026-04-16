---
title: DirectionalLight - Three.js Docs
source_url: https://threejs.org/docs/pages/DirectionalLight.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:28.005860+00:00
kind: extracted-doc
---

# DirectionalLight - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/DirectionalLight.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:28.005860+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Light.html
- https://threejs.org/docs/pages/DirectionalLight.html
- https://threejs.org/docs/pages/Color.html
- https://threejs.org/docs/pages/DirectionalLightShadow.html

Captured summary:

- DirectionalLight - Three.js Docs EventDispatcher → Object3D → Light → DirectionalLight Constructor new DirectionalLight ( color : number | Color | string , intensity : number ) Constructs a new directional light.
- intensity The light's strength/intensity.
- isDirectionalLight : boolean (readonly) This flag can be used for type testing.
- shadow : DirectionalLightShadow This property holds the light's shadow configuration.
- target : Object3D The directional light points from its position to the target's position.

Extracted text:

DirectionalLight - Three.js Docs

EventDispatcher

→

Object3D

→

Light

→

DirectionalLight

Constructor

new

DirectionalLight

( color :

number |

Color

| string

, intensity :

number

)

Constructs a new directional light.

color

The light's color.

Default is

0xffffff

.

intensity

The light's strength/intensity.

Default is

1

.

Properties

.

isDirectionalLight

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

shadow

:

DirectionalLightShadow

This property holds the light's shadow configuration.

.

target

:

Object3D

The directional light points from its position to the target's position.

For the target's position to be changed to anything other than the default, it must be added to the scene.

It is also possible to set the target to be another 3D object in the scene. The light will now track the target object.

Source

src/lights/DirectionalLight.js
