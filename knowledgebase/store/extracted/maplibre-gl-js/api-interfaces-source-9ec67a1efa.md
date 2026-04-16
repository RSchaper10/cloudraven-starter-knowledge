---
title: Source - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:30.173967+00:00
kind: extracted-doc
---

# Source - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:30.173967+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Tile/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Event/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/OverscaledTileID/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/CalculateTileZoomFunction/

Captured summary:

- Source - MapLibre GL JS Skip to content Source Defined in: source/source.ts:31 The Source interface must be implemented by each source type, including "core" types ( vector , raster , video , etc.) and all custom, third-party types.
- Event data - Fired with {dataType: 'source', sourceDataType: 'metadata'} to indicate that any necessary metadata has been loaded so that it's okay to call loadTile ; and with {dataType: 'source', sourceDataType: 'content'} to indicate that the source data has changed, so that any current caches should be flushed.
- optional abortTile ( tile : Tile ): Promise < void > Defined in: source/source.ts:105 Allows to abort a tile loading.
- Parameters Parameter Type Description tile Tile The tile to abort Returns Promise < void > fire() fire ( event : Event ): unknown Defined in: source/source.ts:79 An ability to fire an event to all the listeners, see Evented Parameters Parameter Type Description event Event The event to fire Returns unknown hasTile()?
- optional hasTile ( tileID : OverscaledTileID ): boolean Defined in: source/source.ts:100 True is the tile is part of the source, false otherwise.

Extracted text:

Source - MapLibre GL JS

Skip to content

Source

Defined in:

source/source.ts:31

The

Source

interface must be implemented by each source type, including "core" types (

vector

,

raster

,

video

, etc.) and all custom, third-party types.

Event

data

- Fired with

{dataType: 'source', sourceDataType: 'metadata'}

to indicate that any necessary metadata has been loaded so that it's okay to call

loadTile

; and with

{dataType: 'source', sourceDataType: 'content'}

to indicate that the source data has changed, so that any current caches should be flushed.

Methods

abortTile()?

optional

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

source/source.ts:105

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

fire()

fire

(

event

:

Event

):

unknown

Defined in:

source/source.ts:79

An ability to fire an event to all the listeners, see

Evented

Parameters

Parameter

Type

Description

event

Event

The event to fire

Returns

unknown

hasTile()?

optional

hasTile

(

tileID

:

OverscaledTileID

):

boolean

Defined in:

source/source.ts:100

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

hasTransition()

hasTransition

():

boolean

Defined in:

source/source.ts:70

True if the source has transition, false otherwise.

Returns

boolean

loaded()

loaded

():

boolean

Defined in:

source/source.ts:74

True if the source is loaded, false otherwise.

Returns

boolean

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

source/source.ts:95

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

onAdd()?

optional

onAdd

(

map

:

Map

):

void

Defined in:

source/source.ts:84

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

onRemove()?

optional

onRemove

(

map

:

Map

):

void

Defined in:

source/source.ts:89

This method is called when the source is removed from the map.

Parameters

Parameter

Type

Description

map

Map

The map instance

Returns

void

prepare()?

optional

prepare

():

void

Defined in:

source/source.ts:120

Allows to execute a prepare step before the source is used.

Returns

void

serialize()

serialize

():

any

Defined in:

source/source.ts:116

Returns

any

A plain (stringifiable) JS object representing the current state of the source. Creating a source using the returned object as the

options

should result in a Source that is equivalent to this one.

unloadTile()?

optional

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

source/source.ts:110

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

Properties

attribution?

optional

attribution?

:

string

Defined in:

source/source.ts:52

The attribution for the source.

calculateTileZoom?

optional

calculateTileZoom?

:

CalculateTileZoomFunction

Defined in:

source/source.ts:124

Optional function to redefine how tiles are loaded at high pitch angles.

id

id

:

string

Defined in:

source/source.ts:36

The id for the source. Must not be used by any existing source.

isTileClipped?

optional

isTileClipped?

:

boolean

Defined in:

source/source.ts:60

false

if tiles can be drawn outside their boundaries,

true

if they cannot.

maxzoom

maxzoom

:

number

Defined in:

source/source.ts:44

The maximum zoom level for the source.

minzoom

minzoom

:

number

Defined in:

source/source.ts:40

The minimum zoom level for the source.

reparseOverscaled?

optional

reparseOverscaled?

:

boolean

Defined in:

source/source.ts:65

true

if tiles should be sent back to the worker for each overzoomed zoom level,

false

if not.

roundZoom?

optional

roundZoom?

:

boolean

Defined in:

source/source.ts:56

true

if zoom levels are rounded to the nearest integer in the source data,

false

if they are floor-ed to the nearest integer.

tileSize

tileSize

:

number

Defined in:

source/source.ts:48

The tile size for the source.

Back to top
