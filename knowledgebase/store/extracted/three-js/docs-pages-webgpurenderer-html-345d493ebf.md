---
title: WebGPURenderer - Three.js Docs
source_url: https://threejs.org/docs/pages/WebGPURenderer.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:32.757763+00:00
kind: extracted-doc
---

# WebGPURenderer - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/WebGPURenderer.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:32.757763+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Renderer.html
- https://threejs.org/docs/pages/WebGPURenderer.html
- https://threejs.org/docs/pages/StandardNodeLibrary.html

Captured summary:

- WebGPURenderer - Three.js Docs Renderer → WebGPURenderer Constructor new WebGPURenderer ( parameters : WebGPURenderer~Options ) Constructs a new WebGPU renderer.
- isWebGPURenderer : boolean (readonly) This flag can be used for type testing.
- library : StandardNodeLibrary The generic default value is overwritten with the standard node library for type mapping.
- Overrides: Renderer#library Type Definitions .
- logarithmicDepthBuffer boolean Whether logarithmic depth buffer is enabled or not.

Extracted text:

WebGPURenderer - Three.js Docs

Renderer

→

WebGPURenderer

Constructor

new

WebGPURenderer

( parameters :

WebGPURenderer~Options

)

Constructs a new WebGPU renderer.

parameters

The configuration parameter.

Properties

.

isWebGPURenderer

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

library

:

StandardNodeLibrary

The generic default value is overwritten with the standard node library for type mapping.

Overrides:

Renderer#library

Type Definitions

.

Options

WebGPURenderer options.

logarithmicDepthBuffer

boolean

Whether logarithmic depth buffer is enabled or not.

Default is

false

.

reversedDepthBuffer

boolean

Whether reversed depth buffer is enabled or not.

Default is

false

.

alpha

boolean

Whether the default framebuffer (which represents the final contents of the canvas) should be transparent or opaque.

Default is

true

.

depth

boolean

Whether the default framebuffer should have a depth buffer or not.

Default is

true

.

stencil

boolean

Whether the default framebuffer should have a stencil buffer or not.

Default is

false

.

antialias

boolean

Whether MSAA as the default anti-aliasing should be enabled or not.

Default is

false

.

samples

number

When

antialias

is

true

,

4

samples are used by default. Set this parameter to any other integer value than 0 to overwrite the default.

Default is

0

.

forceWebGL

boolean

If set to

true

, the renderer uses a WebGL 2 backend no matter if WebGPU is supported or not.

Default is

false

.

multiview

boolean

If set to

true

, the renderer will use multiview during WebXR rendering if supported.

Default is

false

.

outputType

number

Texture type for output to canvas. By default, device's preferred format is used; other formats may incur overhead.

outputBufferType

number

Defines the type of output buffers. The default

HalfFloatType

is recommend for best quality. To save memory and bandwidth,

UnsignedByteType

might be used. This will reduce rendering quality though.

Default is

HalfFloatType

.

Source

src/renderers/webgpu/WebGPURenderer.js
