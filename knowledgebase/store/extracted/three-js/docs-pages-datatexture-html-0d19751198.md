---
title: DataTexture - Three.js Docs
source_url: https://threejs.org/docs/pages/DataTexture.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:39.606543+00:00
kind: extracted-doc
---

# DataTexture - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/DataTexture.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:39.606543+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html
- https://threejs.org/docs/pages/Texture.html
- https://threejs.org/docs/pages/DataTexture.html

Captured summary:

- DataTexture - Three.js Docs EventDispatcher → Texture → DataTexture Constructor new DataTexture ( data : TypedArray , width : number , height : number , format : number , type : number , mapping : number , wrapS : number , wrapT : number , magFilter : number , minFilter : number , anisotropy : number , colorSpace : string ) Constructs a new data texture.
- flipY : boolean If set to true , the texture is flipped along the vertical axis when uploaded to the GPU.
- Overwritten and set to false by default.
- generateMipmaps : boolean Whether to generate mipmaps (if possible) for a texture.
- Overwritten and set to false by default.

Extracted text:

DataTexture - Three.js Docs

EventDispatcher

→

Texture

→

DataTexture

Constructor

new

DataTexture

( data :

TypedArray

, width :

number

, height :

number

, format :

number

, type :

number

, mapping :

number

, wrapS :

number

, wrapT :

number

, magFilter :

number

, minFilter :

number

, anisotropy :

number

, colorSpace :

string

)

Constructs a new data texture.

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

format

The texture format.

Default is

RGBAFormat

.

type

The texture type.

Default is

UnsignedByteType

.

mapping

The texture mapping.

Default is

Texture.DEFAULT_MAPPING

.

wrapS

The wrapS value.

Default is

ClampToEdgeWrapping

.

wrapT

The wrapT value.

Default is

ClampToEdgeWrapping

.

magFilter

The mag filter value.

Default is

NearestFilter

.

minFilter

The min filter value.

Default is

NearestFilter

.

anisotropy

The anisotropy value.

Default is

Texture.DEFAULT_ANISOTROPY

.

colorSpace

The color space.

Default is

NoColorSpace

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

isDataTexture

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

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

Source

src/textures/DataTexture.js
