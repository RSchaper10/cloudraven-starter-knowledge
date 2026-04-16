---
title: GeoJSONSource - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/GeoJSONSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:27.274351+00:00
kind: extracted-doc
---

# GeoJSONSource - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/GeoJSONSource/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:27.274351+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/GeoJSONSource/
- https://maplibre.org/maplibre-gl-js/docs/examples/draw-geojson-points/
- https://maplibre.org/maplibre-gl-js/docs/examples/add-a-geojson-line/
- https://maplibre.org/maplibre-gl-js/docs/examples/create-a-heatmap-layer/
- https://maplibre.org/maplibre-gl-js/docs/examples/create-and-style-clusters/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Tile/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLatBounds/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/SetClusterOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/GeoJSONSourceDiff/

Captured summary:

- GeoJSONSource - MapLibre GL JS Skip to content GeoJSONSource Defined in: source/geojson_source.ts:124 A source containing GeoJSON.
- (See the Style Specification for detailed documentation of options.) Examples map .
- addSource ( 'some id' , { type : 'geojson' , data : 'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_10m_ports.geojson' }); map .
- addSource ( 'some id' , { type : 'geojson' , data : { "type" : "FeatureCollection" , "features" : [{ "type" : "Feature" , "properties" : {}, "geometry" : { "type" : "Point" , "coordinates" : [ - 76.53063297271729 , 39.18174077994108 ] } }] } }); map .
- setData ({ "type" : "FeatureCollection" , "features" : [{ "type" : "Feature" , "properties" : { "name" : "Null Island" }, "geometry" : { "type" : "Point" , "coordinates" : [ 0 , 0 ] } }] }); See Draw GeoJSON points Add a GeoJSON line Create a heatmap from points Create and style clusters Extends Evented Implements Source Methods _updateWorkerData() _updateWorkerData (): Promise < void > Defined in: source/geojson_source.ts:392 Responsible for invoking WorkerSource's geojson.loadData target, which handles loading the geojson data and preparing to serve it up as tiles, using geojson-vt or supercluster as appropriate.

Extracted text:

GeoJSONSource - MapLibre GL JS

Skip to content

GeoJSONSource

Defined in:

source/geojson_source.ts:124

A source containing GeoJSON. (See the

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

'geojson'

,

data

:

'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_10m_ports.geojson'

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

'geojson'

,

data

:

{

"type"

:

"FeatureCollection"

,

"features"

:

[{

"type"

:

"Feature"

,

"properties"

:

{},

"geometry"

:

{

"type"

:

"Point"

,

"coordinates"

:

[

-

76.53063297271729

,

39.18174077994108

]

}

}]

}

});

map

.

getSource

(

'some id'

).

setData

({

"type"

:

"FeatureCollection"

,

"features"

:

[{

"type"

:

"Feature"

,

"properties"

:

{

"name"

:

"Null Island"

},

"geometry"

:

{

"type"

:

"Point"

,

"coordinates"

:

[

0

,

0

]

}

}]

});

See

Draw GeoJSON points

Add a GeoJSON line

Create a heatmap from points

Create and style clusters

Extends

Evented

Implements

Source

Methods

_updateWorkerData()

_updateWorkerData

():

Promise

<

void

>

Defined in:

source/geojson_source.ts:392

Responsible for invoking WorkerSource's geojson.loadData target, which handles loading the geojson data and preparing to serve it up as tiles, using geojson-vt or supercluster as appropriate.

Returns

Promise

<

void

>

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

source/geojson_source.ts:614

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

getBounds()

getBounds

():

Promise

<

LngLatBounds

>

Defined in:

source/geojson_source.ts:306

Allows getting the source's boundaries. If there's a problem with the source's data, it will return an empty

LngLatBounds

.

Returns

Promise

<

LngLatBounds

>

a promise which resolves to the source's boundaries

getClusterChildren()

getClusterChildren

(

clusterId

:

number

):

Promise

<

Feature

<

Geometry

, {[

name

:

string

]:

any

; }>[]>

Defined in:

source/geojson_source.ts:348

For clustered sources, fetches the children of the given cluster on the next zoom level (as an array of GeoJSON features).

Parameters

Parameter

Type

Description

clusterId

number

The value of the cluster's

cluster_id

property.

Returns

Promise

<

Feature

<

Geometry

, {[

name

:

string

]:

any

; }>[]>

a promise that is resolved when the features are retrieved

getClusterExpansionZoom()

getClusterExpansionZoom

(

clusterId

:

number

):

Promise

<

number

>

Defined in:

source/geojson_source.ts:338

For clustered sources, fetches the zoom at which the given cluster expands.

Parameters

Parameter

Type

Description

clusterId

number

The value of the cluster's

cluster_id

property.

Returns

Promise

<

number

>

a promise that is resolved with the zoom number

getClusterLeaves()

getClusterLeaves

(

clusterId

:

number

,

limit

:

number

,

offset

:

number

):

Promise

<

Feature

<

Geometry

, {[

name

:

string

]:

any

; }>[]>

Defined in:

source/geojson_source.ts:377

For clustered sources, fetches the original points that belong to the cluster (as an array of GeoJSON features).

Parameters

Parameter

Type

Description

clusterId

number

The value of the cluster's

cluster_id

property.

limit

number

The maximum number of features to return.

offset

number

The number of features to skip (e.g. for pagination).

Returns

Promise

<

Feature

<

Geometry

, {[

name

:

string

]:

any

; }>[]>

a promise that is resolved when the features are retrieved

Example

Retrieve cluster leaves on click

map

.

on

(

'click'

,

'clusters'

,

(

e

)

=>

{

let

features

=

map

.

queryRenderedFeatures

(

e

.

point

,

{

layers

:

[

'clusters'

]

});

let

clusterId

=

features

[

0

].

properties

.

cluster_id

;

let

pointCount

=

features

[

0

].

properties

.

point_count

;

let

clusterSource

=

map

.

getSource

(

'clusters'

);

const

features

=

await

clusterSource

.

getClusterLeaves

(

clusterId

,

pointCount

);

// Print cluster leaves in the console

console

.

log

(

'Cluster leaves:'

,

features

);

});

getData()

getData

():

Promise

<

GeoJSON

<

Geometry

, {[

name

:

string

]:

any

; }>>

Defined in:

source/geojson_source.ts:288

Allows to get the source's actual GeoJSON data.

Returns

Promise

<

GeoJSON

<

Geometry

, {[

name

:

string

]:

any

; }>>

a promise which resolves to the source's actual GeoJSON data

hasTransition()

hasTransition

():

boolean

Defined in:

source/geojson_source.ts:644

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

source/geojson_source.ts:583

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

>

Defined in:

source/geojson_source.ts:587

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

GeoJSONSource

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

GeoJSONSource

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

source/geojson_source.ts:238

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

GeoJSONSource

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

GeoJSONSource

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

source/geojson_source.ts:627

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

GeoJSONSourceSpecification

Defined in:

source/geojson_source.ts:632

Returns

GeoJSONSourceSpecification

A plain (stringifiable) JS object representing the current state of the source. Creating a source using the returned object as the

options

should result in a Source that is equivalent to this one.

Implementation of

Source

.

serialize

setClusterOptions()

setClusterOptions

(

options

:

SetClusterOptions

):

this

Defined in:

source/geojson_source.ts:319

To disable/enable clustering on the source options

Parameters

Parameter

Type

Description

options

SetClusterOptions

The options to set

Returns

this

Example

map

.

getSource

(

'some id'

).

setClusterOptions

({

cluster

:

false

});

map

.

getSource

(

'some id'

).

setClusterOptions

({

cluster

:

false

,

clusterRadius

:

50

,

clusterMaxZoom

:

14

});

setData()

Call Signature

setData

(

data

:

string

|

GeoJSON

<

Geometry

, {[

name

:

string

]:

any

; }>,

waitForCompletion

:

true

):

Promise

<

void

>

Defined in:

source/geojson_source.ts:249

Sets the GeoJSON data and re-renders the map.

Parameters

Parameter

Type

Description

data

string

|

GeoJSON

<

Geometry

, {[

name

:

string

]:

any

; }>

A GeoJSON data object or a URL to one. The latter is preferable in the case of large GeoJSON files.

waitForCompletion

true

If true, the method will return a promise that resolves when set data is complete.

Returns

Promise

<

void

>

Call Signature

setData

(

data

:

string

|

GeoJSON

<

Geometry

, {[

name

:

string

]:

any

; }>,

waitForCompletion?

:

false

):

this

Defined in:

source/geojson_source.ts:250

Sets the GeoJSON data and re-renders the map.

Parameters

Parameter

Type

Description

data

string

|

GeoJSON

<

Geometry

, {[

name

:

string

]:

any

; }>

A GeoJSON data object or a URL to one. The latter is preferable in the case of large GeoJSON files.

waitForCompletion?

false

If true, the method will return a promise that resolves when set data is complete.

Returns

this

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

GeoJSONSource

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

GeoJSONSource

Inherited from

Evented

.

setEventedParent

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

source/geojson_source.ts:622

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

updateData()

Call Signature

updateData

(

diff

:

GeoJSONSourceDiff

,

waitForCompletion

:

true

):

Promise

<

void

>

Defined in:

source/geojson_source.ts:274

Updates the source's GeoJSON, and re-renders the map.

For sources with lots of features, this method can be used to make updates more quickly.

This approach requires unique IDs for every feature in the source. The IDs can either be specified on the feature, or by using the promoteId option to specify which property should be used as the ID.

It is an error to call updateData on a source that did not have unique IDs for each of its features already.

Updates are applied on a best-effort basis, updating an ID that does not exist will not result in an error.

Parameters

Parameter

Type

Description

diff

GeoJSONSourceDiff

The changes that need to be applied.

waitForCompletion

true

If true, the method will return a promise that resolves when the update is complete.

Returns

Promise

<

void

>

Call Signature

updateData

(

diff

:

GeoJSONSourceDiff

,

waitForCompletion?

:

false

):

this

Defined in:

source/geojson_source.ts:275

Updates the source's GeoJSON, and re-renders the map.

For sources with lots of features, this method can be used to make updates more quickly.

This approach requires unique IDs for every feature in the source. The IDs can either be specified on the feature, or by using the promoteId option to specify which property should be used as the ID.

It is an error to call updateData on a source that did not have unique IDs for each of its features already.

Updates are applied on a best-effort basis, updating an ID that does not exist will not result in an error.

Parameters

Parameter

Type

Description

diff

GeoJSONSourceDiff

The changes that need to be applied.

waitForCompletion?

false

If true, the method will return a promise that resolves when the update is complete.

Returns

this

Properties

attribution

attribution

:

string

Defined in:

source/geojson_source.ts:130

The attribution for the source.

Implementation of

Source

.

attribution

id

id

:

string

Defined in:

source/geojson_source.ts:126

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

source/geojson_source.ts:133

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

source/geojson_source.ts:128

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

source/geojson_source.ts:127

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

source/geojson_source.ts:134

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

source/geojson_source.ts:129

The tile size for the source.

Implementation of

Source

.

tileSize

Back to top
