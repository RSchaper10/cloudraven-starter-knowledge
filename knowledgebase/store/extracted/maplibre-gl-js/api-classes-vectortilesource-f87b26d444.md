---
title: VectorTileSource - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/VectorTileSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:28.770729+00:00
kind: extracted-doc
---

# VectorTileSource - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/VectorTileSource/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:28.770729+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/VectorTileSource/
- https://maplibre.org/maplibre-gl-js/docs/examples/add-a-vector-tile-source/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Tile/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/OverscaledTileID/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Captured summary:

- VectorTileSource - MapLibre GL JS Skip to content VectorTileSource Defined in: source/vector_tile_source.ts:65 A source containing vector tiles in Maplibre Vector Tile format or Mapbox Vector Tile format .
- (See the Style Specification for detailed documentation of options.) Examples map .
- addSource ( 'some id' , { type : 'vector' , url : 'https://demotiles.maplibre.org/tiles/tiles.json' }); map .
- addSource ( 'some id' , { type : 'vector' , tiles : [ 'https://d25uarhxywzl1j.cloudfront.net/v0.1/{z}/{x}/{y}.mvt' ], minzoom : 6 , maxzoom : 14 }); map .
- setUrl ( "https://demotiles.maplibre.org/tiles/tiles.json" ); map .

Extracted text:

VectorTileSource - MapLibre GL JS

Skip to content

VectorTileSource

Defined in:

source/vector_tile_source.ts:65

A source containing vector tiles in

Maplibre Vector Tile format

or

Mapbox Vector Tile format

. (See the

Style Specification

for detailed documentation of options.)

Examples

map

.

addSource

(

'some id'

,

{

type

:

'vector'

,

url

:

'https://demotiles.maplibre.org/tiles/tiles.json'

});

map

.

addSource

(

'some id'

,

{

type

:

'vector'

,

tiles

:

[

'https://d25uarhxywzl1j.cloudfront.net/v0.1/{z}/{x}/{y}.mvt'

],

minzoom

:

6

,

maxzoom

:

14

});

map

.

getSource

(

'some id'

).

setUrl

(

"https://demotiles.maplibre.org/tiles/tiles.json"

);

map

.

getSource

(

'some id'

).

setTiles

([

'https://d25uarhxywzl1j.cloudfront.net/v0.1/{z}/{x}/{y}.mvt'

]);

See

Add a vector tile source

Extends

Evented

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

source/vector_tile_source.ts:297

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

hasTile()

hasTile

(

tileID

:

OverscaledTileID

):

boolean

Defined in:

source/vector_tile_source.ts:147

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

hasTransition()

hasTransition

():

boolean

Defined in:

source/vector_tile_source.ts:323

True if the source has transition, false otherwise.

Returns

boolean

Implementation of

Source

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

Evented

.

listens

loaded()

loaded

():

boolean

Defined in:

source/vector_tile_source.ts:143

True if the source is loaded, false otherwise.

Returns

boolean

Implementation of

Source

.

loaded

loadTile()

loadTile

(

tile

:

Tile

):

Promise

<

void

|

LoadTileResult

>

Defined in:

source/vector_tile_source.ts:204

This method does the heavy lifting of loading a tile. In most cases it will defer the work to the relevant worker source.

Parameters

Parameter

Type

Description

tile

Tile

The tile to load

Returns

Promise

<

void

|

LoadTileResult

>

Implementation of

Source

.

loadTile

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

VectorTileSource

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

VectorTileSource

Inherited from

Evented

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

Evented

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

source/vector_tile_source.ts:151

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

VectorTileSource

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

VectorTileSource

this

or a promise if a listener is not provided

Inherited from

Evented

.

once

onRemove()

onRemove

():

void

Defined in:

source/vector_tile_source.ts:193

This method is called when the source is removed from the map.

Returns

void

Implementation of

Source

.

onRemove

serialize()

serialize

():

VectorSourceSpecification

Defined in:

source/vector_tile_source.ts:200

Returns

VectorSourceSpecification

A plain (stringifiable) JS object representing the current state of the source. Creating a source using the returned object as the

options

should result in a Source that is equivalent to this one.

Implementation of

Source

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

VectorTileSource

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

VectorTileSource

Inherited from

Evented

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

source/vector_tile_source.ts:171

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

An array of one or more tile source URLs, as in the TileJSON spec.

Returns

this

setUrl()

setUrl

(

url

:

string

):

this

Defined in:

source/vector_tile_source.ts:184

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

unloadTile()

unloadTile

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

source/vector_tile_source.ts:310

Allows to unload a tile.

Parameters

Parameter

Type

Description

tile

Tile

The tile to unload

Returns

Promise

<

void

>

Implementation of

Source

.

unloadTile

Properties

id

id

:

string

Defined in:

source/vector_tile_source.ts:67

The id for the source. Must not be used by any existing source.

Implementation of

Source

.

id

isTileClipped

isTileClipped

:

boolean

Defined in:

source/vector_tile_source.ts:84

false

if tiles can be drawn outside their boundaries,

true

if they cannot.

Implementation of

Source

.

isTileClipped

maxzoom

maxzoom

:

number

Defined in:

source/vector_tile_source.ts:69

The maximum zoom level for the source.

Implementation of

Source

.

maxzoom

minzoom

minzoom

:

number

Defined in:

source/vector_tile_source.ts:68

The minimum zoom level for the source.

Implementation of

Source

.

minzoom

reparseOverscaled

reparseOverscaled

:

boolean

Defined in:

source/vector_tile_source.ts:83

true

if tiles should be sent back to the worker for each overzoomed zoom level,

false

if not.

Implementation of

Source

.

reparseOverscaled

tileSize

tileSize

:

number

Defined in:

source/vector_tile_source.ts:73

The tile size for the source.

Implementation of

Source

.

tileSize

Back to top
