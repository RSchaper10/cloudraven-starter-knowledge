---
title: Camera - Three.js Docs
source_url: https://threejs.org/docs/pages/Camera.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:24.428803+00:00
kind: extracted-doc
---

# Camera - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Camera.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:24.428803+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Camera.html
- https://threejs.org/docs/pages/global.html
- https://threejs.org/docs/pages/Matrix4.html
- https://threejs.org/docs/pages/Vector3.html

Captured summary:

- Camera - Three.js Docs EventDispatcher → Object3D → Camera Constructor new Camera () (abstract) Constructs a new camera.
- coordinateSystem : WebGLCoordinateSystem | WebGPUCoordinateSystem The coordinate system in which the camera is used.
- isCamera : boolean (readonly) This flag can be used for type testing.
- matrixWorldInverse : Matrix4 The inverse of the camera's world matrix.
- projectionMatrix : Matrix4 The camera's projection matrix.

Extracted text:

Camera - Three.js Docs

EventDispatcher

→

Object3D

→

Camera

Constructor

new

Camera

()

(abstract)

Constructs a new camera.

Properties

.

coordinateSystem

:

WebGLCoordinateSystem

|

WebGPUCoordinateSystem

The coordinate system in which the camera is used.

.

isCamera

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

matrixWorldInverse

:

Matrix4

The inverse of the camera's world matrix.

.

projectionMatrix

:

Matrix4

The camera's projection matrix.

.

projectionMatrixInverse

:

Matrix4

The inverse of the camera's projection matrix.

.

reversedDepth

: boolean

The flag that indicates whether the camera uses a reversed depth buffer.

Default is

false

.

Methods

.

getWorldDirection

( target :

Vector3

)

:

Vector3

Returns a vector representing the ("look") direction of the 3D object in world space.

This method is overwritten since cameras have a different forward vector compared to other 3D objects. A camera looks down its local, negative z-axis by default.

target

The target vector the result is stored to.

Overrides:

Object3D#getWorldDirection

Returns:

The 3D object's direction in world space.

Source

src/cameras/Camera.js
