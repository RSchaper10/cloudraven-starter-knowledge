---
title: Line - Three.js Docs
source_url: https://threejs.org/docs/pages/Line.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:34.323796+00:00
kind: extracted-doc
---

# Line - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Line.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:34.323796+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Line.html
- https://threejs.org/docs/pages/BufferGeometry.html
- https://threejs.org/docs/pages/Material.html
- https://threejs.org/docs/pages/Raycaster.html

Captured summary:

- Line - Three.js Docs EventDispatcher → Object3D → Line Constructor new Line ( geometry : BufferGeometry , material : Material | Array.< Material > ) Constructs a new line.
- geometry : BufferGeometry The line geometry.
- isLine : boolean (readonly) This flag can be used for type testing.
- material : Material | Array.< Material > The line material.
- morphTargetDictionary : Object.<string, number> | undefined A dictionary representing the morph targets in the geometry.

Extracted text:

Line - Three.js Docs

EventDispatcher

→

Object3D

→

Line

Constructor

new

Line

( geometry :

BufferGeometry

, material :

Material

| Array.<

Material

>

)

Constructs a new line.

geometry

The line geometry.

material

The line material.

Properties

.

geometry

:

BufferGeometry

The line geometry.

.

isLine

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

material

:

Material

| Array.<

Material

>

The line material.

Default is

LineBasicMaterial

.

.

morphTargetDictionary

: Object.<string, number> | undefined

A dictionary representing the morph targets in the geometry. The key is the morph targets name, the value its attribute index. This member is

undefined

by default and only set when morph targets are detected in the geometry.

Default is

undefined

.

.

morphTargetInfluences

: Array.<number> | undefined

An array of weights typically in the range

[0,1]

that specify how much of the morph is applied. This member is

undefined

by default and only set when morph targets are detected in the geometry.

Default is

undefined

.

Methods

.

computeLineDistances

()

:

Line

Computes an array of distance values which are necessary for rendering dashed lines. For each vertex in the geometry, the method calculates the cumulative length from the current point to the very beginning of the line.

Returns:

A reference to this line.

.

raycast

( raycaster :

Raycaster

, intersects :

Array.<Object>

)

Computes intersection points between a casted ray and this line.

raycaster

The raycaster.

intersects

The target array that holds the intersection points.

Overrides:

Object3D#raycast

.

updateMorphTargets

()

Sets the values of

Line#morphTargetDictionary

and

Line#morphTargetInfluences

to make sure existing morph targets can influence this 3D object.

Source

src/objects/Line.js
