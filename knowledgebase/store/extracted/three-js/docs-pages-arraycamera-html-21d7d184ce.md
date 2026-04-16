---
title: ArrayCamera - Three.js Docs
source_url: https://threejs.org/docs/pages/ArrayCamera.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:41.015566+00:00
kind: extracted-doc
---

# ArrayCamera - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/ArrayCamera.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:41.015566+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Camera.html
- https://threejs.org/docs/pages/PerspectiveCamera.html
- https://threejs.org/docs/pages/ArrayCamera.html

Captured summary:

- ArrayCamera - Three.js Docs EventDispatcher → Object3D → Camera → PerspectiveCamera → ArrayCamera Constructor new ArrayCamera ( array : Array.< PerspectiveCamera > ) Constructs a new array camera.
- array An array of perspective sub cameras.
- cameras : Array.< PerspectiveCamera > An array of perspective sub cameras.
- isArrayCamera : boolean (readonly) This flag can be used for type testing.
- isMultiViewCamera : boolean (readonly) Whether this camera is used with multiview rendering or not.

Extracted text:

ArrayCamera - Three.js Docs

EventDispatcher

→

Object3D

→

Camera

→

PerspectiveCamera

→

ArrayCamera

Constructor

new

ArrayCamera

( array :

Array.<

PerspectiveCamera

>

)

Constructs a new array camera.

array

An array of perspective sub cameras.

Default is

[]

.

Properties

.

cameras

: Array.<

PerspectiveCamera

>

An array of perspective sub cameras.

.

isArrayCamera

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

isMultiViewCamera

: boolean

(readonly)

Whether this camera is used with multiview rendering or not.

Default is

false

.

Source

src/cameras/ArrayCamera.js
