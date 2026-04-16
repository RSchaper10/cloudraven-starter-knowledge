---
title: Mesh - Three.js Docs
source_url: https://threejs.org/docs/pages/Mesh.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:33.953134+00:00
kind: extracted-doc
---

# Mesh - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Mesh.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:33.953134+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/Mesh.html
- https://threejs.org/docs/pages/BufferGeometry.html
- https://threejs.org/docs/pages/Material.html
- https://threejs.org/docs/pages/WebGPURenderer.html
- https://threejs.org/docs/pages/Vector3.html
- https://threejs.org/docs/pages/Raycaster.html

Captured summary:

- Mesh - Three.js Docs EventDispatcher → Object3D → Mesh Constructor new Mesh ( geometry : BufferGeometry , material : Material | Array.< Material > ) Constructs a new mesh.
- count : number The number of instances of this mesh.
- geometry : BufferGeometry The mesh geometry.
- isMesh : boolean (readonly) This flag can be used for type testing.
- material : Material | Array.< Material > The mesh material.

Extracted text:

Mesh - Three.js Docs

EventDispatcher

→

Object3D

→

Mesh

Constructor

new

Mesh

( geometry :

BufferGeometry

, material :

Material

| Array.<

Material

>

)

Constructs a new mesh.

geometry

The mesh geometry.

material

The mesh material.

Properties

.

count

: number

The number of instances of this mesh. Can only be used with

WebGPURenderer

.

Default is

1

.

.

geometry

:

BufferGeometry

The mesh geometry.

.

isMesh

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

The mesh material.

Default is

MeshBasicMaterial

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

getVertexPosition

( index :

number

, target :

Vector3

)

:

Vector3

Returns the local-space position of the vertex at the given index, taking into account the current animation state of both morph targets and skinning.

index

The vertex index.

target

The target object that is used to store the method's result.

Returns:

The vertex position in local space.

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

Mesh#morphTargetDictionary

and

Mesh#morphTargetInfluences

to make sure existing morph targets can influence this 3D object.

Source

src/objects/Mesh.js
