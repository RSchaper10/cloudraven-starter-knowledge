---
title: HemisphereLight - Three.js Docs
source_url: https://threejs.org/docs/pages/HemisphereLight.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:33.125385+00:00
kind: extracted-doc
---

# HemisphereLight - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/HemisphereLight.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:33.125385+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Light.html
- https://threejs.org/docs/pages/HemisphereLight.html
- https://threejs.org/docs/pages/Color.html

Captured summary:

- HemisphereLight - Three.js Docs EventDispatcher → Object3D → Light → HemisphereLight Constructor new HemisphereLight ( skyColor : number | Color | string , groundColor : number | Color | string , intensity : number ) Constructs a new hemisphere light.
- intensity The light's strength/intensity.
- groundColor : Color The light's ground color.
- isHemisphereLight : boolean (readonly) This flag can be used for type testing.

Extracted text:

HemisphereLight - Three.js Docs

EventDispatcher

→

Object3D

→

Light

→

HemisphereLight

Constructor

new

HemisphereLight

( skyColor :

number |

Color

| string

, groundColor :

number |

Color

| string

, intensity :

number

)

Constructs a new hemisphere light.

skyColor

The light's sky color.

Default is

0xffffff

.

groundColor

The light's ground color.

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

groundColor

:

Color

The light's ground color.

.

isHemisphereLight

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

Source

src/lights/HemisphereLight.js
