---
title: PointLight - Three.js Docs
source_url: https://threejs.org/docs/pages/PointLight.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:28.828218+00:00
kind: extracted-doc
---

# PointLight - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/PointLight.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:28.828218+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Light.html
- https://threejs.org/docs/pages/PointLight.html
- https://threejs.org/docs/pages/Color.html
- https://threejs.org/docs/pages/PointLightShadow.html

Captured summary:

- PointLight - Three.js Docs EventDispatcher → Object3D → Light → PointLight Constructor new PointLight ( color : number | Color | string , intensity : number , distance : number , decay : number ) Constructs a new point light.
- intensity The light's strength/intensity measured in candela (cd).
- decay The amount the light dims along the distance of the light.
- decay : number The amount the light dims along the distance of the light.
- In context of physically-correct rendering the default value should not be changed.

Extracted text:

PointLight - Three.js Docs

EventDispatcher

→

Object3D

→

Light

→

PointLight

Constructor

new

PointLight

( color :

number |

Color

| string

, intensity :

number

, distance :

number

, decay :

number

)

Constructs a new point light.

color

The light's color.

Default is

0xffffff

.

intensity

The light's strength/intensity measured in candela (cd).

Default is

1

.

distance

Maximum range of the light.

0

means no limit.

Default is

0

.

decay

The amount the light dims along the distance of the light.

Default is

2

.

Properties

.

decay

: number

The amount the light dims along the distance of the light. In context of physically-correct rendering the default value should not be changed.

Default is

2

.

.

distance

: number

When distance is zero, light will attenuate according to inverse-square law to infinite distance. When distance is non-zero, light will attenuate according to inverse-square law until near the distance cutoff, where it will then attenuate quickly and smoothly to 0. Inherently, cutoffs are not physically correct.

Default is

0

.

.

isPointLight

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

power

: number

The light's power. Power is the luminous power of the light measured in lumens (lm). Changing the power will also change the light's intensity.

.

shadow

:

PointLightShadow

This property holds the light's shadow configuration.

Source

src/lights/PointLight.js
