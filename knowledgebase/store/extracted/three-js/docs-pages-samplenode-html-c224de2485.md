---
title: SampleNode - Three.js Docs
source_url: https://threejs.org/docs/pages/SampleNode.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:40.649423+00:00
kind: extracted-doc
---

# SampleNode - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/SampleNode.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:40.649423+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Node.html
- https://threejs.org/docs/pages/SampleNode.html

Captured summary:

- SampleNode - Three.js Docs EventDispatcher → Node → SampleNode Constructor new SampleNode ( callback : function , uvNode : Node .<vec2> ) Creates an instance of SampleNode.
- callback The function to be called when sampling.
- Should accept a UV node and return a value.
- uvNode The UV node to be used in the texture sampling.
- isSampleNode : boolean (readonly) This flag can be used for type testing.

Extracted text:

SampleNode - Three.js Docs

EventDispatcher

→

Node

→

SampleNode

Constructor

new

SampleNode

( callback :

function

, uvNode :

Node

.<vec2>

)

Creates an instance of SampleNode.

callback

The function to be called when sampling. Should accept a UV node and return a value.

uvNode

The UV node to be used in the texture sampling.

Default is

null

.

Properties

.

isSampleNode

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

uvNode

:

Node

.<(vec2|vec3)>

Represents the texture coordinates.

Default is

null

.

.

type

: string

(readonly)

Returns the type of the node.

Methods

.

sample

( uv :

Node

.<vec2>

)

:

Node

Calls the callback function with the provided UV node.

uv

The UV node or value to be passed to the callback.

Returns:

The result of the callback function.

.

setup

()

:

Node

Sets up the node by sampling with the default UV accessor.

Overrides:

Node#setup

Returns:

The result of the callback function when called with the UV node.

Source

src/nodes/utils/SampleNode.js
