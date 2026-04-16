---
title: SpotLight - Three.js Docs
source_url: https://threejs.org/docs/pages/SpotLight.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:28.455812+00:00
kind: extracted-doc
---

# SpotLight - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/SpotLight.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:28.455812+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Light.html
- https://threejs.org/docs/pages/SpotLight.html
- https://threejs.org/docs/pages/Color.html
- https://threejs.org/docs/pages/Texture.html
- https://threejs.org/docs/pages/SpotLightShadow.html

Captured summary:

- SpotLight - Three.js Docs EventDispatcher → Object3D → Light → SpotLight Constructor new SpotLight ( color : number | Color | string , intensity : number , distance : number , angle : number , penumbra : number , decay : number ) Constructs a new spot light.
- intensity The light's strength/intensity measured in candela (cd).
- angle Maximum angle of light dispersion from its direction whose upper bound is Math.PI/2 .
- penumbra Percent of the spotlight cone that is attenuated due to penumbra.
- decay The amount the light dims along the distance of the light.

Extracted text:

SpotLight - Three.js Docs

EventDispatcher

→

Object3D

→

Light

→

SpotLight

Constructor

new

SpotLight

( color :

number |

Color

| string

, intensity :

number

, distance :

number

, angle :

number

, penumbra :

number

, decay :

number

)

Constructs a new spot light.

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

angle

Maximum angle of light dispersion from its direction whose upper bound is

Math.PI/2

.

Default is

Math.PI/3

.

penumbra

Percent of the spotlight cone that is attenuated due to penumbra. Value range is

[0,1]

.

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

angle

: number

Maximum angle of light dispersion from its direction whose upper bound is

Math.PI/2

.

Default is

Math.PI/3

.

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

Maximum range of the light.

0

means no limit.

Default is

0

.

.

isSpotLight

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

map

:

Texture

A texture used to modulate the color of the light. The spot light color is mixed with the RGB value of this texture, with a ratio corresponding to its alpha value. The cookie-like masking effect is reproduced using pixel values (0, 0, 0, 1-cookie_value).

Warning

: This property is disabled if

Object3D#castShadow

is set to

false

.

Default is

null

.

.

penumbra

: number

Percent of the spotlight cone that is attenuated due to penumbra. Value range is

[0,1]

.

Default is

0

.

.

power

: number

The light's power. Power is the luminous power of the light measured in lumens (lm). Changing the power will also change the light's intensity.

.

shadow

:

SpotLightShadow

This property holds the light's shadow configuration.

.

target

:

Object3D

The spot light points from its position to the target's position.

For the target's position to be changed to anything other than the default, it must be added to the scene.

It is also possible to set the target to be another 3D object in the scene. The light will now track the target object.

Source

src/lights/SpotLight.js
