---
title: ImageSource - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/ImageSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:27.779839+00:00
kind: extracted-doc
---

# ImageSource - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/ImageSource/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:27.779839+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/ImageSource/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/CanvasSource/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/VideoSource/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Tile/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/CanvasSourceSpecification/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Coordinates/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/UpdateImageOptions/

Captured summary:

- ImageSource - MapLibre GL JS Skip to content ImageSource Defined in: source/image_source.ts:101 A data source containing an image.
- (See the Style Specification for detailed documentation of options.) Example // add to map map .
- addSource ( 'some id' , { type : 'image' , url : 'https://www.maplibre.org/images/foo.png' , coordinates : [ [ - 76.54 , 39.18 ], [ - 76.52 , 39.18 ], [ - 76.52 , 39.17 ], [ - 76.54 , 39.17 ] ] }); // update coordinates let mySource = map .
- setCoordinates ([ [ - 76.54335737228394 , 39.18579907229748 ], [ - 76.52803659439087 , 39.1838364847587 ], [ - 76.5295386314392 , 39.17683392507606 ], [ - 76.54520273208618 , 39.17876344106642 ] ]); // update url and coordinates simultaneously mySource .
- updateImage ({ url : 'https://www.maplibre.org/images/bar.png' , coordinates : [ [ - 76.54335737228394 , 39.18579907229748 ], [ - 76.52803659439087 , 39.1838364847587 ], [ - 76.5295386314392 , 39.17683392507606 ], [ - 76.54520273208618 , 39.17876344106642 ] ] }) map .

Extracted text:

ImageSource - MapLibre GL JS

Skip to content

ImageSource

Defined in:

source/image_source.ts:101

A data source containing an image. (See the

Style Specification

for detailed documentation of options.)

Example

// add to map

map

.

addSource

(

'some id'

,

{

type

:

'image'

,

url

:

'https://www.maplibre.org/images/foo.png'

,

coordinates

:

[

[

-

76.54

,

39.18

],

[

-

76.52

,

39.18

],

[

-

76.52

,

39.17

],

[

-

76.54

,

39.17

]

]

});

// update coordinates

let

mySource

=

map

.

getSource

(

'some id'

);

mySource

.

setCoordinates

([

[

-

76.54335737228394

,

39.18579907229748

],

[

-

76.52803659439087

,

39.1838364847587

],

[

-

76.5295386314392

,

39.17683392507606

],

[

-

76.54520273208618

,

39.17876344106642

]

]);

// update url and coordinates simultaneously

mySource

.

updateImage

({

url

:

'https://www.maplibre.org/images/bar.png'

,

coordinates

:

[

[

-

76.54335737228394

,

39.18579907229748

],

[

-

76.52803659439087

,

39.1838364847587

],

[

-

76.5295386314392

,

39.17683392507606

],

[

-

76.54520273208618

,

39.17876344106642

]

]

})

map

.

removeSource

(

'some id'

);

// remove

Extends

Evented

Extended by

CanvasSource

VideoSource

Implements

Source

Methods

hasTransition()

hasTransition

():

boolean

Defined in:

source/image_source.ts:309

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

source/image_source.ts:174

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

source/image_source.ts:286

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

ImageSource

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

ImageSource

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

source/image_source.ts:206

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

ImageSource

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

ImageSource

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

source/image_source.ts:211

This method is called when the source is removed from the map.

Returns

void

Implementation of

Source

.

onRemove

prepare()

prepare

():

void

Defined in:

source/image_source.ts:258

Allows to execute a prepare step before the source is used.

Returns

void

Implementation of

Source

.

prepare

serialize()

serialize

():

VideoSourceSpecification

|

ImageSourceSpecification

|

CanvasSourceSpecification

Defined in:

source/image_source.ts:301

Returns

VideoSourceSpecification

|

ImageSourceSpecification

|

CanvasSourceSpecification

A plain (stringifiable) JS object representing the current state of the source. Creating a source using the returned object as the

options

should result in a Source that is equivalent to this one.

Implementation of

Source

.

serialize

setCoordinates()

setCoordinates

(

coordinates

:

Coordinates

):

this

Defined in:

source/image_source.ts:226

Sets the image's coordinates and re-renders the map.

Parameters

Parameter

Type

Description

coordinates

Coordinates

Four geographical coordinates, represented as arrays of longitude and latitude numbers, which define the corners of the image. The coordinates start at the top left corner of the image and proceed in clockwise order. They do not have to represent a rectangle.

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

ImageSource

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

ImageSource

Inherited from

Evented

.

setEventedParent

updateImage()

updateImage

(

options

:

UpdateImageOptions

):

this

Defined in:

source/image_source.ts:184

Updates the image URL and, optionally, the coordinates. To avoid having the image flash after changing, set the

raster-fade-duration

paint property on the raster layer to 0.

Parameters

Parameter

Type

Description

options

UpdateImageOptions

The options object.

Returns

this

Properties

id

id

:

string

Defined in:

source/image_source.ts:103

The id for the source. Must not be used by any existing source.

Implementation of

Source

.

id

maxzoom

maxzoom

:

number

Defined in:

source/image_source.ts:105

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

source/image_source.ts:104

The minimum zoom level for the source.

Implementation of

Source

.

minzoom

terrainTileRanges

terrainTileRanges

:

object

Defined in:

source/image_source.ts:112

This object is used to store the range of terrain tiles that overlap with this tile. It is relevant for image tiles, as the image exceeds single tile boundaries.

Index Signature

[

zoom

:

string

]:

CanonicalTileRange

tileSize

tileSize

:

number

Defined in:

source/image_source.ts:106

The tile size for the source.

Implementation of

Source

.

tileSize

Back to top
