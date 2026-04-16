---
title: VideoSource - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/VideoSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:29.255113+00:00
kind: extracted-doc
---

# VideoSource - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/VideoSource/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:29.255113+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/VideoSource/
- https://maplibre.org/maplibre-gl-js/docs/examples/video-on-a-map/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/ImageSource/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Tile/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Coordinates/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/UpdateImageOptions/

Captured summary:

- VideoSource - MapLibre GL JS Skip to content VideoSource Defined in: source/video_source.ts:55 A data source containing video.
- (See the Style Specification for detailed documentation of options.) Example // add to map map .
- addSource ( 'some id' , { type : 'video' , url : [ 'https://www.mapbox.com/blog/assets/baltimore-smoke.mp4' , 'https://www.mapbox.com/blog/assets/baltimore-smoke.webm' ], coordinates : [ [ - 76.54 , 39.18 ], [ - 76.52 , 39.18 ], [ - 76.52 , 39.17 ], [ - 76.54 , 39.17 ] ] }); // update let mySource = map .
- setCoordinates ([ [ - 76.54335737228394 , 39.18579907229748 ], [ - 76.52803659439087 , 39.1838364847587 ], [ - 76.5295386314392 , 39.17683392507606 ], [ - 76.54520273208618 , 39.17876344106642 ] ]); map .
- removeSource ( 'some id' ); // remove See Add a video Note that when rendered as a raster layer, the layer's raster-fade-duration property will cause the video to fade in.

Extracted text:

VideoSource - MapLibre GL JS

Skip to content

VideoSource

Defined in:

source/video_source.ts:55

A data source containing video. (See the

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

'video'

,

url

:

[

'https://www.mapbox.com/blog/assets/baltimore-smoke.mp4'

,

'https://www.mapbox.com/blog/assets/baltimore-smoke.webm'

],

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

// update

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

map

.

removeSource

(

'some id'

);

// remove

See

Add a video

Note that when rendered as a raster layer, the layer's

raster-fade-duration

property will cause the video to fade in. This happens when playback is started, paused and resumed, or when the video's coordinates are updated. To avoid this behavior, set the layer's

raster-fade-duration

property to

0

.

Extends

ImageSource

Methods

getVideo()

getVideo

():

HTMLVideoElement

Defined in:

source/video_source.ts:138

Returns the HTML

video

element.

Returns

HTMLVideoElement

The HTML

video

element.

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

ImageSource

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

Inherited from

ImageSource

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

Inherited from

ImageSource

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

VideoSource

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

VideoSource

Inherited from

ImageSource

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

ImageSource

.

on

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

VideoSource

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

VideoSource

this

or a promise if a listener is not provided

Inherited from

ImageSource

.

once

pause()

pause

():

void

Defined in:

source/video_source.ts:106

Pauses the video.

Returns

void

play()

play

():

void

Defined in:

source/video_source.ts:115

Plays the video.

Returns

void

prepare()

prepare

():

this

Defined in:

source/video_source.ts:163

Sets the video's coordinates and re-renders the map.

Returns

this

Overrides

ImageSource

.

prepare

seek()

seek

(

seconds

:

number

):

void

Defined in:

source/video_source.ts:124

Sets playback to a timestamp, in seconds.

Parameters

Parameter

Type

seconds

number

Returns

void

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

Inherited from

ImageSource

.

setCoordinates

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

VideoSource

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

VideoSource

Inherited from

ImageSource

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

Inherited from

ImageSource

.

updateImage

Properties

id

id

:

string

Defined in:

source/image_source.ts:103

The id for the source. Must not be used by any existing source.

Inherited from

ImageSource

.

id

maxzoom

maxzoom

:

number

Defined in:

source/image_source.ts:105

The maximum zoom level for the source.

Inherited from

ImageSource

.

maxzoom

minzoom

minzoom

:

number

Defined in:

source/image_source.ts:104

The minimum zoom level for the source.

Inherited from

ImageSource

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

Inherited from

ImageSource

.

terrainTileRanges

tileSize

tileSize

:

number

Defined in:

source/image_source.ts:106

The tile size for the source.

Inherited from

ImageSource

.

tileSize

Back to top
