---
title: Data3DTexture - Three.js Docs
source_url: https://threejs.org/docs/pages/Data3DTexture.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:37.056050+00:00
kind: extracted-doc
---

# Data3DTexture - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Data3DTexture.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:37.056050+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Texture.html
- https://threejs.org/docs/pages/Data3DTexture.html
- https://threejs.org/docs/pages/global.html

Captured summary:

- Data3DTexture - Three.js Docs EventDispatcher → Texture → Data3DTexture Constructor new Data3DTexture ( data : TypedArray , width : number , height : number , depth : number ) Constructs a new data array texture.
- flipY : boolean If set to true , the texture is flipped along the vertical axis when uploaded to the GPU.
- Overwritten and set to false by default.
- generateMipmaps : boolean Whether to generate mipmaps (if possible) for a texture.
- Overwritten and set to false by default.

Extracted text:

Data3DTexture - Three.js Docs

EventDispatcher

→

Texture

→

Data3DTexture

Constructor

new

Data3DTexture

( data :

TypedArray

, width :

number

, height :

number

, depth :

number

)

Constructs a new data array texture.

data

The buffer data.

Default is

null

.

width

The width of the texture.

Default is

1

.

height

The height of the texture.

Default is

1

.

depth

The depth of the texture.

Default is

1

.

Properties

.

flipY

: boolean

If set to

true

, the texture is flipped along the vertical axis when uploaded to the GPU.

Overwritten and set to

false

by default.

Default is

false

.

Overrides:

Texture#flipY

.

generateMipmaps

: boolean

Whether to generate mipmaps (if possible) for a texture.

Overwritten and set to

false

by default.

Default is

false

.

Overrides:

Texture#generateMipmaps

.

image

: Object

The image definition of a data texture.

Overrides:

Texture#image

.

isData3DTexture

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

.

magFilter

:

NearestFilter

|

NearestMipmapNearestFilter

|

NearestMipmapLinearFilter

|

LinearFilter

|

LinearMipmapNearestFilter

|

LinearMipmapLinearFilter

How the texture is sampled when a texel covers more than one pixel.

Overwritten and set to

NearestFilter

by default.

Default is

NearestFilter

.

Overrides:

Texture#magFilter

.

minFilter

:

NearestFilter

|

NearestMipmapNearestFilter

|

NearestMipmapLinearFilter

|

LinearFilter

|

LinearMipmapNearestFilter

|

LinearMipmapLinearFilter

How the texture is sampled when a texel covers less than one pixel.

Overwritten and set to

NearestFilter

by default.

Default is

NearestFilter

.

Overrides:

Texture#minFilter

.

unpackAlignment

: boolean

Specifies the alignment requirements for the start of each pixel row in memory.

Overwritten and set to

1

by default.

Default is

1

.

Overrides:

Texture#unpackAlignment

.

wrapR

:

RepeatWrapping

|

ClampToEdgeWrapping

|

MirroredRepeatWrapping

This defines how the texture is wrapped in the depth and corresponds to

W

in UVW mapping.

Default is

ClampToEdgeWrapping

.

Source

src/textures/Data3DTexture.js
