---
title: LightsNode - Three.js Docs
source_url: https://threejs.org/docs/pages/LightsNode.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:41.805936+00:00
kind: extracted-doc
---

# LightsNode - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/LightsNode.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:41.805936+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Node.html
- https://threejs.org/docs/pages/LightsNode.html
- https://threejs.org/docs/pages/NodeBuilder.html
- https://threejs.org/docs/pages/Light.html
- https://threejs.org/docs/pages/LightingNode.html

Captured summary:

- LightsNode - Three.js Docs EventDispatcher → Node → LightsNode Constructor new LightsNode () Constructs a new lights node.
- global : boolean LightsNode sets this property to true by default.
- hasLights : boolean Whether the scene has lights or not.
- outgoingLightNode : Node .<vec3> A node representing the outgoing light.
- totalDiffuseNode : Node .<vec3> A node representing the total diffuse light.

Extracted text:

LightsNode - Three.js Docs

EventDispatcher

→

Node

→

LightsNode

Constructor

new

LightsNode

()

Constructs a new lights node.

Properties

.

global

: boolean

LightsNode

sets this property to

true

by default.

Default is

true

.

Overrides:

Node#global

.

hasLights

: boolean

Whether the scene has lights or not.

.

outgoingLightNode

:

Node

.<vec3>

A node representing the outgoing light.

.

totalDiffuseNode

:

Node

.<vec3>

A node representing the total diffuse light.

.

totalSpecularNode

:

Node

.<vec3>

A node representing the total specular light.

Methods

.

customCacheKey

()

: number

Overwrites the default

Node#customCacheKey

implementation by including light data into the cache key.

Overrides:

Node#customCacheKey

Returns:

The custom cache key.

.

getHash

( builder :

NodeBuilder

)

: string

Computes a hash value for identifying the current light nodes setup.

builder

A reference to the current node builder.

Overrides:

Node#getHash

Returns:

The computed hash.

.

getLights

()

: Array.<

Light

>

Returns an array of the scene's lights.

Returns:

The scene's lights.

.

setLights

( lights :

Array.<

Light

>

)

:

LightsNode

Configures this node with an array of lights.

lights

An array of lights.

Returns:

A reference to this node.

.

setup

( builder :

NodeBuilder

)

:

Node

.<vec3>

The implementation makes sure that for each light in the scene there is a corresponding light node. By building the light nodes and evaluating the lighting model the outgoing light is computed.

builder

A reference to the current node builder.

Overrides:

Node#setup

Returns:

A node representing the outgoing light.

.

setupDirectLight

( builder :

Object

, lightNode :

Object

, lightData :

Object

)

Sets up a direct light in the lighting model.

builder

The builder object containing the context and stack.

lightNode

The light node.

lightData

The light object containing color and direction properties.

.

setupLights

( builder :

NodeBuilder

, lightNodes :

Array.<

LightingNode

>

)

Setups the internal lights by building all respective light nodes.

builder

A reference to the current node builder.

lightNodes

An array of lighting nodes.

.

setupLightsNode

( builder :

NodeBuilder

)

Creates lighting nodes for each scene light. This makes it possible to further process lights in the node system.

builder

A reference to the current node builder.

Source

src/nodes/lighting/LightsNode.js
