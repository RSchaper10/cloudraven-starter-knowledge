---
title: RasterDEMTileSource - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/RasterDEMTileSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:28.302388+00:00
kind: extracted-doc
---

# RasterDEMTileSource - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/RasterDEMTileSource/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:28.302388+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/RasterDEMTileSource/
- https://maplibre.org/maplibre-gl-js/docs/examples/3d-terrain/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/RasterTileSource/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Tile/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/OverscaledTileID/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/

Captured summary:

- RasterDEMTileSource - MapLibre GL JS Skip to content RasterDEMTileSource Defined in: source/raster_dem_tile_source.ts:37 A source containing raster DEM tiles (See the Style Specification for detailed documentation of options.) This source can be used to show hillshading and 3D terrain Example map .
- addSource ( 'raster-dem-source' , { type : 'raster-dem' , url : 'https://demotiles.maplibre.org/terrain-tiles/tiles.json' , tileSize : 256 }); See 3D Terrain Extends RasterTileSource Implements Source Methods abortTile() abortTile ( tile : Tile ): Promise < void > Defined in: source/raster_tile_source.ts:219 Allows to abort a tile loading.
- Parameters Parameter Type Description tile Tile The tile to abort Returns Promise < void > Implementation of Source .
- abortTile Inherited from RasterTileSource .
- abortTile hasTile() hasTile ( tileID : OverscaledTileID ): boolean Defined in: source/raster_tile_source.ts:178 True is the tile is part of the source, false otherwise.

Extracted text:

RasterDEMTileSource - MapLibre GL JS

Skip to content

RasterDEMTileSource

Defined in:

source/raster_dem_tile_source.ts:37

A source containing raster DEM tiles (See the

Style Specification

for detailed documentation of options.) This source can be used to show hillshading and 3D terrain

Example

map

.

addSource

(

'raster-dem-source'

,

{

type

:

'raster-dem'

,

url

:

'https://demotiles.maplibre.org/terrain-tiles/tiles.json'

,

tileSize

:

256

});

See

3D Terrain

Extends

RasterTileSource

Implements

Source

Methods

abortTile()

abortTile

(

tile

:

Tile

):

Promise

<

void

>

Defined in:

source/raster_tile_source.ts:219

Allows to abort a tile loading.

Parameters

Parameter

Type

Description

tile

Tile

The tile to abort

Returns

Promise

<

void

>

Implementation of

Source

.

abortTile

Inherited from

RasterTileSource

.

abortTile

hasTile()

hasTile

(

tileID

:

OverscaledTileID

):

boolean

Defined in:

source/raster_tile_source.ts:178

True is the tile is part of the source, false otherwise.

Parameters

Parameter

Type

Description

tileID

OverscaledTileID

The tile ID

Returns

boolean

Implementation of

Source

.

hasTile

Inherited from

RasterTileSource

.

hasTile

hasTransition()

hasTransition

():

boolean

Defined in:

source/raster_tile_source.ts:232

True if the source has transition, false otherwise.

Returns

boolean

Implementation of

Source

.

hasTransition

Inherited from

RasterTileSource

.

hasTransition

listens()

listens

(

type

:

string

):

boolean

Defined in:

util/evented.ts:165

Returns a true if this instance of Evented or any forwardeed instances of Evented have a listener for the specified type.

Parameters

Parameter

Type

Description

type

string

The event type

Returns

boolean

true

if there is at least one registered listener for specified event type,

false

otherwise

Inherited from

RasterTileSource

.

listens

loaded()

loaded

():

boolean

Defined in:

source/raster_tile_source.ts:120

True if the source is loaded, false otherwise.

Returns

boolean

Implementation of

Source

.

loaded

Inherited from

RasterTileSource

.

loaded

off()

off

(

type

:

string

,

listener

:

Listener

):

RasterDEMTileSource

Defined in:

util/evented.ts:90

Removes a previously registered event listener.

Parameters

Parameter

Type

Description

type

string

The event type to remove listeners for.

listener

Listener

The listener function to remove.

Returns

RasterDEMTileSource

Inherited from

RasterTileSource

.

off

on()

on

(

type

:

string

,

listener

:

Listener

):

Subscription

Defined in:

util/evented.ts:73

Adds a listener to a specified event type.

Parameters

Parameter

Type

Description

type

string

The event type to add a listen for.

listener

Listener

The function to be called when the event is fired. The listener function is called with the data object passed to

fire

, extended with

target

and

type

properties.

Returns

Subscription

Inherited from

RasterTileSource

.

on

onAdd()

onAdd

(

map

:

Map

):

void

Defined in:

source/raster_tile_source.ts:124

This method is called when the source is added to the map.

Parameters

Parameter

Type

Description

map

Map

The map instance

Returns

void

Implementation of

Source

.

onAdd

Inherited from

RasterTileSource

.

onAdd

once()

once

(

type

:

string

,

listener?

:

Listener

):

Promise

<

any

> |

RasterDEMTileSource

Defined in:

util/evented.ts:106

Adds a listener that will be called only once to a specified event type.

The listener will be called first time the event fires after the listener is registered.

Parameters

Parameter

Type

Description

type

string

The event type to listen for.

listener?

Listener

The function to be called when the event is fired the first time.

Returns

Promise

<

any

> |

RasterDEMTileSource

this

or a promise if a listener is not provided

Inherited from

RasterTileSource

.

once

onRemove()

onRemove

():

void

Defined in:

source/raster_tile_source.ts:129

This method is called when the source is removed from the map.

Returns

void

Implementation of

Source

.

onRemove

Inherited from

RasterTileSource

.

onRemove

serialize()

serialize

():

RasterSourceSpecification

|

RasterDEMSourceSpecification

Defined in:

source/raster_tile_source.ts:174

Returns

RasterSourceSpecification

|

RasterDEMSourceSpecification

A plain (stringifiable) JS object representing the current state of the source. Creating a source using the returned object as the

options

should result in a Source that is equivalent to this one.

Implementation of

Source

.

serialize

Inherited from

RasterTileSource

.

serialize

setEventedParent()

setEventedParent

(

parent?

:

Evented

,

data?

:

any

):

RasterDEMTileSource

Defined in:

util/evented.ts:176

Bubble all events fired by this instance of Evented to this parent instance of Evented.

Parameters

Parameter

Type

parent?

Evented

data?

any

Returns

RasterDEMTileSource

Inherited from

RasterTileSource

.

setEventedParent

setTiles()

setTiles

(

tiles

:

string

[]):

this

Defined in:

source/raster_tile_source.ts:152

Sets the source

tiles

property and re-renders the map.

Parameters

Parameter

Type

Description

tiles

string

[]

An array of one or more tile source URLs, as in the raster tiles spec (See the

Style Specification

Returns

this

Inherited from

RasterTileSource

.

setTiles

setUrl()

setUrl

(

url

:

string

):

this

Defined in:

source/raster_tile_source.ts:165

Sets the source

url

property and re-renders the map.

Parameters

Parameter

Type

Description

url

string

A URL to a TileJSON resource. Supported protocols are

http:

and

https:

.

Returns

this

Inherited from

RasterTileSource

.

setUrl

Properties

id

id

:

string

Defined in:

source/raster_tile_source.ts:55

The id for the source. Must not be used by any existing source.

Implementation of

Source

.

id

Inherited from

RasterTileSource

.

id

maxzoom

maxzoom

:

number

Defined in:

source/raster_tile_source.ts:57

The maximum zoom level for the source.

Implementation of

Source

.

maxzoom

Inherited from

RasterTileSource

.

maxzoom

minzoom

minzoom

:

number

Defined in:

source/raster_tile_source.ts:56

The minimum zoom level for the source.

Implementation of

Source

.

minzoom

Inherited from

RasterTileSource

.

minzoom

roundZoom

roundZoom

:

boolean

Defined in:

source/raster_tile_source.ts:64

true

if zoom levels are rounded to the nearest integer in the source data,

false

if they are floor-ed to the nearest integer.

Implementation of

Source

.

roundZoom

Inherited from

RasterTileSource

.

roundZoom

tileSize

tileSize

:

number

Defined in:

source/raster_tile_source.ts:60

The tile size for the source.

Implementation of

Source

.

tileSize

Inherited from

RasterTileSource

.

tileSize

Back to top
