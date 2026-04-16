---
title: Map - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:09.500280+00:00
kind: extracted-doc
---

# Map - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:09.500280+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapOptions/
- https://maplibre.org/maplibre-gl-js/docs/examples/display-a-map/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapLayerEventType/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapEventType/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/
- https://maplibre.org/maplibre-gl-js/docs/examples/display-a-popup-on-click/
- https://maplibre.org/maplibre-gl-js/docs/examples/center-the-map-on-a-clicked-symbol/
- https://maplibre.org/maplibre-gl-js/docs/examples/create-a-hover-effect/
- https://maplibre.org/maplibre-gl-js/docs/examples/create-a-draggable-point/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/IControl/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/ControlPosition/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/ErrorEvent/
- https://maplibre.org/maplibre-gl-js/docs/examples/display-map-navigation-controls/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/StyleImageInterface/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/StyleImageMetadata/
- https://maplibre.org/maplibre-gl-js/docs/examples/add-an-icon-to-the-map/
- https://maplibre.org/maplibre-gl-js/docs/examples/add-a-generated-icon-to-the-map/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/AddLayerObject/

Captured summary:

- Map - MapLibre GL JS Skip to content Map Defined in: ui/map.ts:541 The Map object represents the map on your page.
- It exposes methods and properties that enable you to programmatically change the map, and fires events as users interact with it.
- You create a Map by specifying a container and other options, see MapOptions for the full list.
- Then MapLibre GL JS initializes the map on the page and returns your Map object.
- Example let map = new Map ({ container : 'map' , center : [ - 122.420679 , 37.772537 ], zoom : 13 , style : style_object , hash : true , transformRequest : ( url , resourceType )=> { if ( resourceType === 'Source' && url .

Extracted text:

Map - MapLibre GL JS

Skip to content

Map

Defined in:

ui/map.ts:541

The

Map

object represents the map on your page. It exposes methods and properties that enable you to programmatically change the map, and fires events as users interact with it.

You create a

Map

by specifying a

container

and other options, see

MapOptions

for the full list. Then MapLibre GL JS initializes the map on the page and returns your

Map

object.

Example

let

map

=

new

Map

({

container

:

'map'

,

center

:

[

-

122.420679

,

37.772537

],

zoom

:

13

,

style

:

style_object

,

hash

:

true

,

transformRequest

:

(

url

,

resourceType

)=>

{

if

(

resourceType

===

'Source'

&&

url

.

startsWith

(

'http://myHost'

))

{

return

{

url

:

url.replace

(

'http'

,

'https'

),

headers

:

{

'my-custom-header'

:

true

},

credentials

:

'include'

// Include cookies for cross-origin requests

}

}

}

});

See

Display a map

Extends

Camera

Accessors

repaint

Get Signature

get

repaint

():

boolean

Defined in:

ui/map.ts:3901

Gets and sets a Boolean indicating whether the map will continuously repaint. This information is useful for analyzing performance.

Returns

boolean

showCollisionBoxes

Get Signature

get

showCollisionBoxes

():

boolean

Defined in:

ui/map.ts:3869

Gets and sets a Boolean indicating whether the map will render boxes around all symbols in the data source, revealing which symbols were rendered or which were hidden due to collisions. This information is useful for debugging.

Returns

boolean

showOverdrawInspector

Get Signature

get

showOverdrawInspector

():

boolean

Defined in:

ui/map.ts:3890

Gets and sets a Boolean indicating whether the map should color-code each fragment to show how many times it has been shaded. White fragments have been shaded 8 or more times. Black fragments have been shaded 0 times. This information is useful for debugging.

Returns

boolean

showPadding

Get Signature

get

showPadding

():

boolean

Defined in:

ui/map.ts:3856

Gets and sets a Boolean indicating whether the map will visualize the padding offsets.

Returns

boolean

showTileBoundaries

Get Signature

get

showTileBoundaries

():

boolean

Defined in:

ui/map.ts:3845

Gets and sets a Boolean indicating whether the map will render an outline around each tile and the tile ID. These tile boundaries are useful for debugging.

The uncompressed file size of the first vector source is drawn in the top left corner of each tile, next to the tile ID.

Example

map

.

showTileBoundaries

=

true

;

Returns

boolean

version

Get Signature

get

version

():

string

Defined in:

ui/map.ts:3916

Returns the package version of the library

Returns

string

Package version of the library

Events

off()

Call Signature

off

<

T

>(

type

:

T

,

layer

:

string

,

listener

: (

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

):

this

Defined in:

ui/map.ts:1845

Removes an event listener for events previously added with

{@link Map.on}

.

Type Parameters

Type Parameter

T

extends

keyof

MapLayerEventType

Parameters

Parameter

Type

Description

type

T

The event type previously used to install the listener.

layer

string

The layer ID or listener previously used to install the listener.

listener

(

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

The function previously installed as a listener.

Returns

this

Overrides

Camera.off

Call Signature

off

<

T

>(

type

:

T

,

layers

:

string

[],

listener

: (

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

):

this

Defined in:

ui/map.ts:1858

Overload of the

off

method that allows to remove an event created with multiple layers. Provide the same layer IDs as to

on

or

once

, when the listener was registered.

Type Parameters

Type Parameter

T

extends

keyof

MapLayerEventType

Parameters

Parameter

Type

Description

type

T

The type of the event.

layers

string

[]

The layer IDs previously used to install the listener.

listener

(

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

The function previously installed as a listener.

Returns

this

Overrides

Camera.off

Call Signature

off

<

T

>(

type

:

T

,

listener

: (

ev

:

MapEventType

[

T

] &

Object

) =>

void

):

this

Defined in:

ui/map.ts:1869

Overload of the

off

method that allows to remove an event created without specifying a layer.

Type Parameters

Type Parameter

T

extends

keyof

MapEventType

Parameters

Parameter

Type

Description

type

T

The type of the event.

listener

(

ev

:

MapEventType

[

T

] &

Object

) =>

void

The function previously installed as a listener.

Returns

this

Overrides

Camera.off

Call Signature

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

this

Defined in:

ui/map.ts:1876

Overload of the

off

method that allows to remove an event created without specifying a layer.

Parameters

Parameter

Type

Description

type

string

The type of the event.

listener

Listener

The function previously installed as a listener.

Returns

this

Overrides

Camera.off

on()

Call Signature

on

<

T

>(

type

:

T

,

layer

:

string

,

listener

: (

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

):

Subscription

Defined in:

ui/map.ts:1711

Adds a listener for events of a specified type, optionally limited to features in a specified style layer(s). See

MapEventType

and

MapLayerEventType

for a full list of events and their description.

Event

Compatible with

layerId

mousedown

yes

mouseup

yes

mouseover

yes

mouseout

yes

mousemove

yes

mouseenter

yes (required)

mouseleave

yes (required)

click

yes

dblclick

yes

contextmenu

yes

touchstart

yes

touchend

yes

touchcancel

yes

wheel

resize

remove

touchmove

movestart

move

moveend

dragstart

drag

dragend

zoomstart

zoom

zoomend

rotatestart

rotate

rotateend

pitchstart

pitch

pitchend

boxzoomstart

boxzoomend

boxzoomcancel

webglcontextlost

webglcontextrestored

load

render

idle

error

data

styledata

sourcedata

dataloading

styledataloading

sourcedataloading

styleimagemissing

dataabort

sourcedataabort

Type Parameters

Type Parameter

T

extends

keyof

MapLayerEventType

Parameters

Parameter

Type

Description

type

T

The event type to listen for. Events compatible with the optional

layerId

parameter are triggered when the cursor enters a visible portion of the specified layer from outside that layer or outside the map canvas.

layer

string

The ID of a style layer or a listener if no ID is provided. Event will only be triggered if its location is within a visible feature in this layer. The event will have a

features

property containing an array of the matching features. If

layer

is not supplied, the event will not have a

features

property. Please note that many event types are not compatible with the optional

layer

parameter.

listener

(

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

The function to be called when the event is fired.

Returns

Subscription

Examples

// Set an event listener that will fire

// when the map has finished loading

map

.

on

(

'load'

,

()

=>

{

// Once the map has finished loading,

// add a new layer

map

.

addLayer

({

id

:

'points-of-interest'

,

source

:

{

type

:

'vector'

,

url

:

'https://maplibre.org/maplibre-style-spec/'

},

'source-layer'

:

'poi_label'

,

type

:

'circle'

,

paint

:

{

// MapLibre Style Specification paint properties

},

layout

:

{

// MapLibre Style Specification layout properties

}

});

});

// Set an event listener that will fire

// when a feature on the countries layer of the map is clicked

map

.

on

(

'click'

,

'countries'

,

(

e

)

=>

{

new

Popup

()

.

setLngLat

(

e

.

lngLat

)

.

setHTML

(

`Country name:

${

e

.

features

[

0

].

properties

.

name

}

`

)

.

addTo

(

map

);

});

See

Display popup on click

Center the map on a clicked symbol

Create a hover effect

Create a draggable marker

Overrides

Camera.on

Call Signature

on

<

T

>(

type

:

T

,

layerIds

:

string

[],

listener

: (

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

):

Subscription

Defined in:

ui/map.ts:1723

Overload of the

on

method that allows to listen to events specifying multiple layers.

Type Parameters

Type Parameter

T

extends

keyof

MapLayerEventType

Parameters

Parameter

Type

Description

type

T

The type of the event.

layerIds

string

[]

The array of style layer IDs.

listener

(

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

The listener callback.

Returns

Subscription

Overrides

Camera.on

Call Signature

on

<

T

>(

type

:

T

,

listener

: (

ev

:

MapEventType

[

T

] &

Object

) =>

void

):

Subscription

Defined in:

ui/map.ts:1734

Overload of the

on

method that allows to listen to events without specifying a layer.

Type Parameters

Type Parameter

T

extends

keyof

MapEventType

Parameters

Parameter

Type

Description

type

T

The type of the event.

listener

(

ev

:

MapEventType

[

T

] &

Object

) =>

void

The listener callback.

Returns

Subscription

Overrides

Camera.on

Call Signature

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

ui/map.ts:1741

Overload of the

on

method that allows to listen to events without specifying a layer.

Parameters

Parameter

Type

Description

type

string

The type of the event.

listener

Listener

The listener callback.

Returns

Subscription

Overrides

Camera.on

once()

Call Signature

once

<

T

>(

type

:

T

,

layer

:

string

,

listener?

: (

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

):

Map

|

Promise

<

MapLayerEventType

[

T

] &

Object

>

Defined in:

ui/map.ts:1780

Adds a listener that will be called only once to a specified event type, optionally limited to features in a specified style layer.

Type Parameters

Type Parameter

T

extends

keyof

MapLayerEventType

Parameters

Parameter

Type

Description

type

T

The event type to listen for; one of

'mousedown'

,

'mouseup'

,

'click'

,

'dblclick'

,

'mousemove'

,

'mouseenter'

,

'mouseleave'

,

'mouseover'

,

'mouseout'

,

'contextmenu'

,

'touchstart'

,

'touchend'

, or

'touchcancel'

.

mouseenter

and

mouseover

events are triggered when the cursor enters a visible portion of the specified layer from outside that layer or outside the map canvas.

mouseleave

and

mouseout

events are triggered when the cursor leaves a visible portion of the specified layer, or leaves the map canvas.

layer

string

The ID of a style layer or a listener if no ID is provided. Only events whose location is within a visible feature in this layer will trigger the listener. The event will have a

features

property containing an array of the matching features.

listener?

(

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

The function to be called when the event is fired.

Returns

Map

|

Promise

<

MapLayerEventType

[

T

] &

Object

>

this

if listener is provided, promise otherwise to allow easier usage of async/await

Overrides

Camera.once

Call Signature

once

<

T

>(

type

:

T

,

layerIds

:

string

[],

listener?

: (

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

):

Promise

<

any

> |

Map

Defined in:

ui/map.ts:1792

Overload of the

once

method that allows to listen to events specifying multiple layers.

Type Parameters

Type Parameter

T

extends

keyof

MapLayerEventType

Parameters

Parameter

Type

Description

type

T

The type of the event.

layerIds

string

[]

The array of style layer IDs.

listener?

(

ev

:

MapLayerEventType

[

T

] &

Object

) =>

void

The listener callback.

Returns

Promise

<

any

> |

Map

Overrides

Camera.once

Call Signature

once

<

T

>(

type

:

T

,

listener?

: (

ev

:

MapEventType

[

T

] &

Object

) =>

void

):

Promise

<

any

> |

Map

Defined in:

ui/map.ts:1803

Overload of the

once

method that allows to listen to events without specifying a layer.

Type Parameters

Type Parameter

T

extends

keyof

MapEventType

Parameters

Parameter

Type

Description

type

T

The type of the event.

listener?

(

ev

:

MapEventType

[

T

] &

Object

) =>

void

The listener callback.

Returns

Promise

<

any

> |

Map

Overrides

Camera.once

Call Signature

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

Map

Defined in:

ui/map.ts:1810

Overload of the

once

method that allows to listen to events without specifying a layer.

Parameters

Parameter

Type

Description

type

string

The type of the event.

listener?

Listener

The listener callback.

Returns

Promise

<

any

> |

Map

Overrides

Camera.once

Methods

addControl()

addControl

(

control

:

IControl

,

position?

:

ControlPosition

):

this

Defined in:

ui/map.ts:897

Adds an

IControl

to the map, calling

control.onAdd(this)

.

An

ErrorEvent

will be fired if the control is invalid.

Parameters

Parameter

Type

Description

control

IControl

The

IControl

to add.

position?

ControlPosition

position on the map to which the control will be added. Valid values are

'top-left'

,

'top-right'

,

'bottom-left'

, and

'bottom-right'

. Defaults to

'top-right'

.

Returns

this

Example

Add zoom and rotation controls to the map.

map

.

addControl

(

new

NavigationControl

());

See

Display map navigation controls

addImage()

addImage

(

id

:

string

,

image

:

ImageBitmap

|

ImageData

|

HTMLImageElement

|

StyleImageInterface

| {

data

:

Uint8Array

<

ArrayBufferLike

> |

Uint8ClampedArray

<

ArrayBufferLike

>;

height

:

number

;

width

:

number

; },

options?

:

Partial

<

StyleImageMetadata

>):

this

Defined in:

ui/map.ts:2552

Add an image to the style. This image can be displayed on the map like any other icon in the style's sprite using the image's ID with

icon-image

,

background-pattern

,

fill-pattern

, or

line-pattern

.

A

ErrorEvent

event will be fired if the image parameter is invalid or there is not enough space in the sprite to add this image.

Parameters

Parameter

Type

Description

id

string

The ID of the image.

image

ImageBitmap

|

ImageData

|

HTMLImageElement

|

StyleImageInterface

| {

data

:

Uint8Array

<

ArrayBufferLike

> |

Uint8ClampedArray

<

ArrayBufferLike

>;

height

:

number

;

width

:

number

; }

The image as an

HTMLImageElement

,

ImageData

,

ImageBitmap

or object with

width

,

height

, and

data

properties with the same format as

ImageData

.

options

Partial

<

StyleImageMetadata

>

Options object.

Returns

this

Example

// If the style's sprite does not already contain an image with ID 'cat',

// add the image 'cat-icon.png' to the style's sprite with the ID 'cat'.

const

image

=

await

map

.

loadImage

(

'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Cat_silhouette.svg/400px-Cat_silhouette.svg.png'

);

if

(

!

map

.

hasImage

(

'cat'

))

map

.

addImage

(

'cat'

,

image

.

data

);

// Add a stretchable image that can be used with `icon-text-fit`

// In this example, the image is 600px wide by 400px high.

const

image

=

await

map

.

loadImage

(

'https://upload.wikimedia.org/wikipedia/commons/8/89/Black_and_White_Boxed_%28bordered%29.png'

);

if

(

map

.

hasImage

(

'border-image'

))

return

;

map

.

addImage

(

'border-image'

,

image

.

data

,

{

content

:

[

16

,

16

,

300

,

384

],

// place text over left half of image, avoiding the 16px border

stretchX

:

[[

16

,

584

]],

// stretch everything horizontally except the 16px border

stretchY

:

[[

16

,

384

]],

// stretch everything vertically except the 16px border

});

See

Use

HTMLImageElement

:

Add an icon to the map

Use

ImageData

:

Add a generated icon to the map

addLayer()

addLayer

(

layer

:

AddLayerObject

,

beforeId?

:

string

):

Map

Defined in:

ui/map.ts:2832

Adds a

MapLibre style layer

to the map's style.

A layer defines how data from a specified source will be styled. Read more about layer types and available paint and layout properties in the

MapLibre Style Specification

.

Parameters

Parameter

Type

Description

layer

AddLayerObject

The layer to add, conforming to either the MapLibre Style Specification's

layer definition

or, less commonly, the

CustomLayerInterface

specification. Can also be a layer definition with an embedded source definition. The MapLibre Style Specification's layer definition is appropriate for most layers.

beforeId?

string

The ID of an existing layer to insert the new layer before, resulting in the new layer appearing visually beneath the existing layer. If this argument is not specified, the layer will be appended to the end of the layers array and appear visually above all other layers.

Returns

Map

Examples

Add a circle layer with a vector source

map

.

addLayer

({

id

:

'points-of-interest'

,

source

:

{

type

:

'vector'

,

url

:

'https://demotiles.maplibre.org/tiles/tiles.json'

},

'source-layer'

:

'poi_label'

,

type

:

'circle'

,

paint

:

{

// MapLibre Style Specification paint properties

},

layout

:

{

// MapLibre Style Specification layout properties

}

});

Define a source before using it to create a new layer

map

.

addSource

(

'state-data'

,

{

type

:

'geojson'

,

data

:

'path/to/data.geojson'

});

map

.

addLayer

({

id

:

'states'

,

// References the GeoJSON source defined above

// and does not require a `source-layer`

source

:

'state-data'

,

type

:

'symbol'

,

layout

:

{

// Set the label content to the

// feature's `name` property

text

-

field

:

[

'get'

,

'name'

]

}

});

Add a new symbol layer before an existing layer

map

.

addLayer

({

id

:

'states'

,

// References a source that's already been defined

source

:

'state-data'

,

type

:

'symbol'

,

layout

:

{

// Set the label content to the

// feature's `name` property

text

-

field

:

[

'get'

,

'name'

]

}

// Add the layer before the existing `cities` layer

},

'cities'

);

See

Create and style clusters

Add a vector tile source

Add a WMS source

addSource()

addSource

(

id

:

string

,

source

:

SourceSpecification

|

CanvasSourceSpecification

):

this

Defined in:

ui/map.ts:2286

Adds a source to the map's style.

Events triggered:

Triggers the

source.add

event.

Parameters

Parameter

Type

Description

id

string

The ID of the source to add. Must not conflict with existing sources.

source

SourceSpecification

|

CanvasSourceSpecification

The source object, conforming to the MapLibre Style Specification's

source definition

or

CanvasSourceSpecification

.

Returns

this

Examples

map

.

addSource

(

'my-data'

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

'my-data'

,

{

"type"

:

"geojson"

,

"data"

:

{

"type"

:

"Feature"

,

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

77.0323

,

38.9131

]

},

"properties"

:

{

"title"

:

"Mapbox DC"

,

"marker-symbol"

:

"monument"

}

}

});

See

GeoJSON source:

Add live realtime data

addSprite()

addSprite

(

id

:

string

,

url

:

string

,

options?

:

StyleSetterOptions

):

this

Defined in:

ui/map.ts:3076

Adds a sprite to the map's style. Fires the

style

event.

Parameters

Parameter

Type

Description

id

string

The ID of the sprite to add. Must not conflict with existing sprites.

url

string

The URL to load the sprite from

options

StyleSetterOptions

Options object.

Returns

this

Example

map

.

addSprite

(

'sprite-two'

,

'http://example.com/sprite-two'

);

areTilesLoaded()

areTilesLoaded

():

boolean

Defined in:

ui/map.ts:2410

Returns a Boolean indicating whether all tiles in the viewport from all sources on the style are loaded.

Returns

boolean

A Boolean indicating whether all tiles are loaded.

Example

let

tilesLoaded

=

map

.

areTilesLoaded

();

calculateCameraOptionsFromCameraLngLatAltRotation()

calculateCameraOptionsFromCameraLngLatAltRotation

(

cameraLngLat

:

LngLatLike

,

cameraAlt

:

number

,

bearing

:

number

,

pitch

:

number

,

roll?

:

number

):

CameraOptions

Defined in:

ui/camera.ts:1088

Given a camera position and rotation, calculates zoom and center point and returns them as

CameraOptions

.

Parameters

Parameter

Type

Description

cameraLngLat

LngLatLike

The lng, lat of the camera to look from

cameraAlt

number

The altitude of the camera to look from, in meters above sea level

bearing

number

Bearing of the camera, in degrees

pitch

number

Pitch of the camera, in degrees

roll?

number

Roll of the camera, in degrees

Returns

CameraOptions

the calculated camera options

Example

// Calculate options to look from camera position(1°, 0°, 1000m) with bearing = 90°, pitch = 30°, and roll = 45°

const

cameraLngLat

=

new

LngLat

(

1

,

0

);

const

cameraAltitude

=

1000

;

const

bearing

=

90

;

const

pitch

=

30

;

const

roll

=

45

;

const

cameraOptions

=

map

.

calculateCameraOptionsFromCameraLngLatAltRotation

(

cameraLngLat

,

cameraAltitude

,

bearing

,

pitch

,

roll

);

// Apply calculated options

map

.

jumpTo

(

cameraOptions

);

Inherited from

Camera.calculateCameraOptionsFromCameraLngLatAltRotation

calculateCameraOptionsFromTo()

calculateCameraOptionsFromTo

(

from

:

LngLat

,

altitudeFrom

:

number

,

to

:

LngLat

,

altitudeTo?

:

number

):

CameraOptions

Defined in:

ui/map.ts:983

Given a camera 'from' position and a position to look at (

to

), calculates zoom and camera rotation and returns them as

CameraOptions

.

Parameters

Parameter

Type

Description

from

LngLat

The camera to look from

altitudeFrom

number

The altitude of the camera to look from

to

LngLat

The center to look at

altitudeTo?

number

Optional altitude of the center to look at. If none given the ground height will be used.

Returns

CameraOptions

the calculated camera options

Example

// Calculate options to look from (1°, 0°, 1000m) to (1°, 1°, 0m)

const

cameraLngLat

=

new

LngLat

(

1

,

0

);

const

cameraAltitude

=

1000

;

const

targetLngLat

=

new

LngLat

(

1

,

1

);

const

targetAltitude

=

0

;

const

cameraOptions

=

map

.

calculateCameraOptionsFromTo

(

cameraLngLat

,

cameraAltitude

,

targetLngLat

,

targetAltitude

);

// Apply calculated options

map

.

jumpTo

(

cameraOptions

);

Overrides

Camera.calculateCameraOptionsFromTo

cameraForBounds()

cameraForBounds

(

bounds

:

LngLatBoundsLike

,

options?

:

CameraForBoundsOptions

):

CenterZoomBearing

Defined in:

ui/camera.ts:787

Parameters

Parameter

Type

Description

bounds

LngLatBoundsLike

Calculate the center for these bounds in the viewport and use the highest zoom level up to and including

Map.getMaxZoom

that fits in the viewport. LngLatBounds represent a box that is always axis-aligned with bearing 0. Bounds will be taken in [sw, ne] order. Southwest point will always be to the left of the northeast point.

options?

CameraForBoundsOptions

Options object

Returns

CenterZoomBearing

If map is able to fit to provided bounds, returns

center

,

zoom

, and

bearing

. If map is unable to fit, method will warn and return undefined.

Example

let

bbox

=

[[

-

79

,

43

],

[

-

73

,

45

]];

let

newCameraTransform

=

map

.

cameraForBounds

(

bbox

,

{

padding

:

{

top

:

10

,

bottom

:

25

,

left

:

15

,

right

:

5

}

});

Inherited from

Camera.cameraForBounds

coveringTiles()

coveringTiles

(

options

:

CoveringTilesOptions

):

OverscaledTileID

[]

Defined in:

ui/map.ts:979

Returns an array of

OverscaledTileID

objects that cover the current viewport for a given tile size. This method is useful for determining which tiles are visible in the current viewport.

Parameters

Parameter

Type

Description

options

CoveringTilesOptions

Options for calculating the covering tiles.

Returns

OverscaledTileID

[]

An array of

OverscaledTileID

objects.

Example

// Get the tiles to cover the view for a 512x512px tile source

const

tiles

=

map

.

coveringTiles

({

tileSize

:

512

});

easeTo()

easeTo

(

options

:

EaseToOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:1118

Changes any combination of

center

,

zoom

,

bearing

,

pitch

,

roll

, and

padding

with an animated transition between old and new values. The map will retain its current values for any details not specified in

options

.

Reduced Motion

The transition will happen instantly if the user has enabled the

reduced motion

accessibility feature enabled in their operating system, unless

options

includes

essential: true

.

Triggers the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

,

zoomend

,

pitchstart

,

pitch

,

pitchend

,

rollstart

,

roll

,

rollend

, and

rotate

.

Parameters

Parameter

Type

Description

options

EaseToOptions

Options describing the destination and animation of the transition. Accepts

CameraOptions

and

AnimationOptions

.

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

See

Navigate the map with game-like controls

Inherited from

Camera.easeTo

fitBounds()

fitBounds

(

bounds

:

LngLatBoundsLike

,

options?

:

FitBoundsOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:870

Pans and zooms the map to contain its visible area within the specified geographical bounds. This function will also reset the map's bearing to 0 if bearing is nonzero.

Triggers the following events:

movestart

and

moveend

.

Parameters

Parameter

Type

Description

bounds

LngLatBoundsLike

Center these bounds in the viewport and use the highest zoom level up to and including

Map.getMaxZoom

that fits them in the viewport. Bounds will be taken in [sw, ne] order. Southwest point will always be to the left of the northeast point.

options?

FitBoundsOptions

Options supports all properties from

AnimationOptions

and

CameraOptions

in addition to the fields below.

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

let

bbox

=

[[

-

79

,

43

],

[

-

73

,

45

]];

map

.

fitBounds

(

bbox

,

{

padding

:

{

top

:

10

,

bottom

:

25

,

left

:

15

,

right

:

5

}

});

See

Fit a map to a bounding box

Inherited from

Camera.fitBounds

fitScreenCoordinates()

fitScreenCoordinates

(

p0

:

PointLike

,

p1

:

PointLike

,

bearing

:

number

,

options?

:

FitBoundsOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:899

Pans, rotates and zooms the map to to fit the box made by points p0 and p1 once the map is rotated to the specified bearing. To zoom without rotating, pass in the current map bearing.

Triggers the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

,

zoomend

and

rotate

.

Parameters

Parameter

Type

Description

p0

PointLike

First point on screen, in pixel coordinates

p1

PointLike

Second point on screen, in pixel coordinates

bearing

number

Desired map bearing at end of animation, in degrees

options?

FitBoundsOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

let

p0

=

[

220

,

400

];

let

p1

=

[

500

,

900

];

map

.

fitScreenCoordinates

(

p0

,

p1

,

map

.

getBearing

(),

{

padding

:

{

top

:

10

,

bottom

:

25

,

left

:

15

,

right

:

5

}

});

See

Used by

BoxZoomHandler

Inherited from

Camera.fitScreenCoordinates

flyTo()

flyTo

(

options

:

FlyToOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:1423

Changes any combination of center, zoom, bearing, pitch, and roll, animating the transition along a curve that evokes flight. The animation seamlessly incorporates zooming and panning to help the user maintain her bearings even after traversing a great distance.

Reduced Motion

The animation will be skipped, and this will behave equivalently to

jumpTo

if the user has the

reduced motion

accessibility feature enabled in their operating system, unless 'options' includes

essential: true

.

Triggers the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

,

zoomend

,

pitchstart

,

pitch

,

pitchend

,

rollstart

,

roll

,

rollend

, and

rotate

.

Parameters

Parameter

Type

Description

options

FlyToOptions

Options describing the destination and animation of the transition. Accepts

CameraOptions

,

AnimationOptions

, and the following additional options.

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

// fly with default options to null island

map

.

flyTo

({

center

:

[

0

,

0

],

zoom

:

9

});

// using flyTo options

map

.

flyTo

({

center

:

[

0

,

0

],

zoom

:

9

,

speed

:

0.2

,

curve

:

1

,

easing

(

t

)

{

return

t

;

}

});

See

Fly to a location

Slowly fly to a location

Fly to a location based on scroll position

Inherited from

Camera.flyTo

getAnisotropicFilterPitch()

getAnisotropicFilterPitch

():

number

Defined in:

ui/map.ts:1368

Returns the map's anisotropic filter pitch. If the map is pitched beyond this threshold, anisotropic filtering will be applied to all raster layers.

Returns

number

The anisotropicFilterPitch

Example

let

anisotropicFilterPitch

=

map

.

getAnisotropicFilterPitch

();

getBearing()

getBearing

():

number

Defined in:

ui/camera.ts:599

Returns the map's current bearing. The bearing is the compass direction that is "up"; for example, a bearing of 90° orients the map so that east is up.

Returns

number

The map's current bearing.

See

Navigate the map with game-like controls

Inherited from

Camera.getBearing

getBounds()

getBounds

():

LngLatBounds

Defined in:

ui/map.ts:1119

Returns the map's geographical bounds. When the bearing or pitch is non-zero, the visible region is not an axis-aligned rectangle, and the result is the smallest bounds that encompasses the visible region.

Returns

LngLatBounds

The geographical bounds of the map as

LngLatBounds

.

Example

let

bounds

=

map

.

getBounds

();

getCameraTargetElevation()

getCameraTargetElevation

():

number

Defined in:

ui/map.ts:3926

Returns the elevation for the point where the camera is looking. This value corresponds to: "meters above sea level" * "exaggeration"

Returns

number

The elevation.

getCanvas()

getCanvas

():

HTMLCanvasElement

Defined in:

ui/map.ts:3344

Returns the map's

<canvas>

element.

Returns

HTMLCanvasElement

The map's

<canvas>

element.

See

Measure distances

Display a popup on hover

Center the map on a clicked symbol

getCanvasContainer()

getCanvasContainer

():

HTMLElement

Defined in:

ui/map.ts:3332

Returns the HTML element containing the map's

<canvas>

element.

If you want to add non-GL overlays to the map, you should append them to this element.

This is the element to which event bindings for map interactivity (such as panning and zooming) are attached. It will receive bubbled events from child elements such as the

<canvas>

, but not from map controls.

Returns

HTMLElement

The container of the map's

<canvas>

.

See

Create a draggable point

getCenter()

getCenter

():

LngLat

Defined in:

ui/camera.ts:369

Returns the map's geographical centerpoint.

Returns

LngLat

The map's geographical centerpoint.

Example

Return a LngLat object such as

{lng: 0, lat: 0}

let

center

=

map

.

getCenter

();

// access longitude and latitude values directly

let

{

lng

,

lat

}

=

map

.

getCenter

();

Inherited from

Camera.getCenter

getCenterClampedToGround()

getCenterClampedToGround

():

boolean

Defined in:

ui/camera.ts:415

Returns the value of

centerClampedToGround

.

If true, the elevation of the center point will automatically be set to the terrain elevation (or zero if terrain is not enabled). If false, the elevation of the center point will default to sea level and will not automatically update. Defaults to true. Needs to be set to false to keep the camera above ground when pitch > 90 degrees.

Returns

boolean

Inherited from

Camera.getCenterClampedToGround

getCenterElevation()

getCenterElevation

():

number

Defined in:

ui/camera.ts:392

Returns the elevation of the map's center point.

Returns

number

The elevation of the map's center point, in meters above sea level.

Inherited from

Camera.getCenterElevation

getContainer()

getContainer

():

HTMLElement

Defined in:

ui/map.ts:3316

Returns the map's containing HTML element.

Returns

HTMLElement

The map's container.

getFeatureState()

getFeatureState

(

feature

:

FeatureIdentifier

):

any

Defined in:

ui/map.ts:3307

Gets the

state

of a feature. A feature's

state

is a set of user-defined key-value pairs that are assigned to a feature at runtime. Features are identified by their

feature.id

attribute, which can be any number or string.

Note

To access the values in a feature's state object for the purposes of styling the feature, use the

feature-state

expression

.

Parameters

Parameter

Type

Description

feature

FeatureIdentifier

Feature identifier. Feature objects returned from

Map.queryRenderedFeatures

or event handlers can be used as feature identifiers.

Returns

any

The state of the feature: a set of key-value pairs that was assigned to the feature at runtime.

Example

When the mouse moves over the

my-layer

layer, get the feature state for the feature under the mouse

map

.

on

(

'mousemove'

,

'my-layer'

,

(

e

)

=>

{

if

(

e

.

features

.

length

>

0

)

{

map

.

getFeatureState

({

source

:

'my-source'

,

sourceLayer

:

'my-source-layer'

,

id

:

e.features

[

0

].

id

});

}

});

getFilter()

getFilter

(

layerId

:

string

):

void

|

FilterSpecification

Defined in:

ui/map.ts:2975

Returns the filter applied to the specified style layer.

Parameters

Parameter

Type

Description

layerId

string

The ID of the style layer whose filter to get.

Returns

void

|

FilterSpecification

The layer's filter.

getGlobalState()

getGlobalState

():

Record

<

string

,

any

>

Defined in:

ui/map.ts:878

Returns the global map state

Returns

Record

<

string

,

any

>

The map state object.

getGlyphs()

getGlyphs

():

string

Defined in:

ui/map.ts:3061

Returns the value of the style's glyphs URL

Returns

string

glyphs Style's glyphs url, or

null

if glyphs are unset.

getImage()

getImage

(

id

:

string

):

StyleImage

Defined in:

ui/map.ts:2670

Returns an image, specified by ID, currently available in the map. This includes both images from the style's original sprite and any images that have been added at runtime using

Map.addImage

.

Parameters

Parameter

Type

Description

id

string

The ID of the image.

Returns

StyleImage

An image in the map with the specified ID.

Example

let

coffeeShopIcon

=

map

.

getImage

(

"coffee_cup"

);

getLayer()

getLayer

(

id

:

string

):

StyleLayer

Defined in:

ui/map.ts:2887

Returns the layer with the specified ID in the map's style.

Parameters

Parameter

Type

Description

id

string

The ID of the layer to get.

Returns

StyleLayer

The layer with the specified ID, or

undefined

if the ID corresponds to no existing layers.

Example

let

stateDataLayer

=

map

.

getLayer

(

'state-data'

);

See

Filter symbols by toggling a list

Filter symbols by text input

getLayersOrder()

getLayersOrder

():

string

[]

Defined in:

ui/map.ts:2901

Return the ids of all layers currently in the style, including custom layers, in order.

Returns

string

[]

ids of layers, in order

Example

const

orderedLayerIds

=

map

.

getLayersOrder

();

getLayoutProperty()

getLayoutProperty

(

layerId

:

string

,

name

:

string

):

any

Defined in:

ui/map.ts:3035

Returns the value of a layout property in the specified style layer.

Parameters

Parameter

Type

Description

layerId

string

The ID of the layer to get the layout property from.

name

string

The name of the layout property to get.

Returns

any

The value of the specified layout property.

getLight()

getLight

():

LightSpecification

Defined in:

ui/map.ts:3153

Returns the value of the light object.

Returns

LightSpecification

light Light properties of the style.

getMaxBounds()

getMaxBounds

():

LngLatBounds

Defined in:

ui/map.ts:1131

Returns the maximum geographical bounds the map is constrained to, or

null

if none set.

Returns

LngLatBounds

The map object.

Example

let

maxBounds

=

map

.

getMaxBounds

();

getMaxPitch()

getMaxPitch

():

number

Defined in:

ui/map.ts:1356

Returns the map's maximum allowable pitch.

Returns

number

The maxPitch

getMaxZoom()

getMaxZoom

():

number

Defined in:

ui/map.ts:1264

Returns the map's maximum allowable zoom level.

Returns

number

The maxZoom

Example

let

maxZoom

=

map

.

getMaxZoom

();

getMinPitch()

getMinPitch

():

number

Defined in:

ui/map.ts:1310

Returns the map's minimum allowable pitch.

Returns

number

The minPitch

getMinZoom()

getMinZoom

():

number

Defined in:

ui/map.ts:1214

Returns the map's minimum allowable zoom level.

Returns

number

minZoom

Example

let

minZoom

=

map

.

getMinZoom

();

getPadding()

getPadding

():

PaddingOptions

Defined in:

ui/camera.ts:646

Returns the current padding applied around the map viewport.

Returns

PaddingOptions

The current padding around the map viewport.

Inherited from

Camera.getPadding

getPaintProperty()

getPaintProperty

(

layerId

:

string

,

name

:

string

):

unknown

Defined in:

ui/map.ts:3007

Returns the value of a paint property in the specified style layer.

Parameters

Parameter

Type

Description

layerId

string

The ID of the layer to get the paint property from.

name

string

The name of a paint property to get.

Returns

unknown

The value of the specified paint property.

getPitch()

getPitch

():

number

Defined in:

ui/camera.ts:736

Returns the map's current pitch (tilt).

Returns

number

The map's current pitch, measured in degrees away from the plane of the screen.

Inherited from

Camera.getPitch

getPixelRatio()

getPixelRatio

():

number

Defined in:

ui/map.ts:1093

Returns the map's pixel ratio. Note that the pixel ratio actually applied may be lower to respect maxCanvasSize.

Returns

number

The pixel ratio.

getProjection()

getProjection

():

ProjectionSpecification

Defined in:

ui/map.ts:3938

Gets the

ProjectionSpecification

.

Returns

ProjectionSpecification

the projection specification.

Example

let

projection

=

map

.

getProjection

();

getRenderWorldCopies()

getRenderWorldCopies

():

boolean

Defined in:

ui/map.ts:1414

Returns the state of

renderWorldCopies

. If

true

, multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude. If set to

false

:

When the map is zoomed out far enough that a single representation of the world does not fill the map's entire container, there will be blank space beyond 180 and -180 degrees longitude.

Features that cross 180 and -180 degrees longitude will be cut in two (with one portion on the right edge of the map and the other on the left edge of the map) at every zoom level.

Returns

boolean

The renderWorldCopies

Example

let

worldCopiesRendered

=

map

.

getRenderWorldCopies

();

See

Render world copies

getRoll()

getRoll

():

number

Defined in:

ui/camera.ts:756

Returns the map's current roll angle.

Returns

number

The map's current roll, measured in degrees about the camera boresight.

Inherited from

Camera.getRoll

getSky()

getSky

():

SkySpecification

Defined in:

ui/map.ts:3183

Returns the value of the style's sky.

Returns

SkySpecification

the sky properties of the style.

Example

map

.

getSky

();

getSource()

getSource

<

TSource

>(

id

:

string

):

TSource

Defined in:

ui/map.ts:2456

Returns the source with the specified ID in the map's style.

This method is often used to update a source using the instance members for the relevant source type as defined in classes that derive from

Source

. For example, setting the

data

for a GeoJSON source or updating the

url

and

coordinates

of an image source.

Type Parameters

Type Parameter

TSource

extends

Source

Parameters

Parameter

Type

Description

id

string

The ID of the source to get.

Returns

TSource

The style source with the specified ID or

undefined

if the ID corresponds to no existing sources. The shape of the object varies by source type. A list of options for each source type is available on the MapLibre Style Specification's

Sources

page.

Example

let

sourceObject

=

map

.

getSource

(

'points'

);

See

Create a draggable point

Animate a point

Add live realtime data

getSprite()

getSprite

():

object

[]

Defined in:

ui/map.ts:3107

Returns the as-is value of the style's sprite.

Returns

object

[]

style's sprite list of id-url pairs

getStyle()

getStyle

():

StyleSpecification

Defined in:

ui/map.ts:2210

Returns the map's MapLibre style object, a JSON object which can be used to recreate the map's style.

Returns

StyleSpecification

The map's style JSON object.

Example

let

styleJson

=

map

.

getStyle

();

getTerrain()

getTerrain

():

TerrainSpecification

Defined in:

ui/map.ts:2396

Get the terrain-options if terrain is loaded

Returns

TerrainSpecification

the TerrainSpecification passed to setTerrain

Example

map

.

getTerrain

();

// { source: 'terrain' };

getVerticalFieldOfView()

getVerticalFieldOfView

():

number

Defined in:

ui/camera.ts:566

Returns the map's current vertical field of view, in degrees.

Returns

number

The map's current vertical field of view.

Default Value

36.87

Example

const

verticalFieldOfView

=

map

.

getVerticalFieldOfView

();

Inherited from

Camera.getVerticalFieldOfView

getZoom()

getZoom

():

number

Defined in:

ui/camera.ts:475

Returns the map's current zoom level.

Returns

number

The map's current zoom level.

Example

map

.

getZoom

();

Inherited from

Camera.getZoom

getZoomSnap()

getZoomSnap

():

number

Defined in:

ui/camera.ts:616

Returns the map's current zoom snap level.

Returns

number

The map's current zoom snap level.

Inherited from

Camera.getZoomSnap

hasControl()

hasControl

(

control

:

IControl

):

boolean

Defined in:

ui/map.ts:963

Checks if a control exists on the map.

Parameters

Parameter

Type

Description

control

IControl

The

IControl

to check.

Returns

boolean

true if map contains control.

Example

// Define a new navigation control.

let

navigation

=

new

NavigationControl

();

// Add zoom and rotation controls to the map.

map

.

addControl

(

navigation

);

// Check that the navigation control exists on the map.

map

.

hasControl

(

navigation

);

hasImage()

hasImage

(

id

:

string

):

boolean

Defined in:

ui/map.ts:2690

Check whether or not an image with a specific ID exists in the style. This checks both images in the style's original sprite and any images that have been added at runtime using

Map.addImage

.

An

ErrorEvent

will be fired if the image ID is missing.

Parameters

Parameter

Type

Description

id

string

The ID of the image.

Returns

boolean

A Boolean indicating whether the image exists.

Example

Check if an image with the ID 'cat' exists in the style's sprite.

let

catIconExists

=

map

.

hasImage

(

'cat'

);

isMoving()

isMoving

():

boolean

Defined in:

ui/map.ts:1499

Returns true if the map is panning, zooming, rotating, or pitching due to a camera animation or user gesture.

Returns

boolean

true if the map is moving.

Example

let

isMoving

=

map

.

isMoving

();

isRotating()

isRotating

():

boolean

Defined in:

ui/map.ts:1523

Returns true if the map is rotating due to a camera animation or user gesture.

Returns

boolean

true if the map is rotating.

Example

map

.

isRotating

();

isSourceLoaded()

isSourceLoaded

(

id

:

string

):

boolean

Defined in:

ui/map.ts:2305

Returns a Boolean indicating whether the source is loaded. Returns

true

if the source with the given ID in the map's style has no outstanding network requests, otherwise

false

.

A

ErrorEvent

event will be fired if there is no source with the specified ID.

Parameters

Parameter

Type

Description

id

string

The ID of the source to be checked.

Returns

boolean

A Boolean indicating whether the source is loaded.

Example

let

sourceLoaded

=

map

.

isSourceLoaded

(

'bathymetry-data'

);

isStyleLoaded()

isStyleLoaded

():

boolean

|

void

Defined in:

ui/map.ts:2241

Returns a Boolean indicating whether the map's style is fully loaded.

Returns

boolean

|

void

A Boolean indicating whether the style is fully loaded.

Example

let

styleLoadStatus

=

map

.

isStyleLoaded

();

isZooming()

isZooming

():

boolean

Defined in:

ui/map.ts:1511

Returns true if the map is zooming due to a camera animation or user gesture.

Returns

boolean

true if the map is zooming.

Example

let

isZooming

=

map

.

isZooming

();

jumpTo()

jumpTo

(

options

:

JumpToOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:948

Changes any combination of center, zoom, bearing, pitch, and roll, without an animated transition. The map will retain its current values for any details not specified in

options

.

Triggers the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

,

zoomend

,

pitchstart

,

pitch

,

pitchend

,

rollstart

,

roll

,

rollend

and

rotate

.

Parameters

Parameter

Type

Description

options

JumpToOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

// jump to coordinates at current zoom

map

.

jumpTo

({

center

:

[

0

,

0

]});

// jump with zoom, pitch, and bearing options

map

.

jumpTo

({

center

:

[

0

,

0

],

zoom

:

8

,

pitch

:

45

,

bearing

:

90

});

See

Jump to a series of locations

Update a feature in realtime

Inherited from

Camera.jumpTo

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

Camera.listens

listImages()

listImages

():

string

[]

Defined in:

ui/map.ts:2749

Returns an Array of strings containing the IDs of all images currently available in the map. This includes both images from the style's original sprite and any images that have been added at runtime using

Map.addImage

.

Returns

string

[]

An Array of strings containing the names of all sprites/images currently available in the map.

Example

let

allImages

=

map

.

listImages

();

loaded()

loaded

():

boolean

Defined in:

ui/map.ts:3566

Returns a Boolean indicating whether the map is fully loaded.

Returns

false

if the style is not yet fully loaded, or if there has been a change to the sources or style that has not yet fully loaded.

Returns

boolean

A Boolean indicating whether the map is fully loaded.

loadImage()

loadImage

(

url

:

string

):

Promise

<

GetResourceResponse

<

ImageBitmap

|

HTMLImageElement

>>

Defined in:

ui/map.ts:2733

Load an image from an external URL to be used with

Map.addImage

. External domains must support

CORS

.

Parameters

Parameter

Type

Description

url

string

The URL of the image file. Image file must be in png, webp, or jpg format.

Returns

Promise

<

GetResourceResponse

<

ImageBitmap

|

HTMLImageElement

>>

a promise that is resolved when the image is loaded

Example

Load an image from an external URL.

const

response

=

await

map

.

loadImage

(

'https://picsum.photos/50/50'

);

// Add the loaded image to the style's sprite with the ID 'photo'.

map

.

addImage

(

'photo'

,

response

.

data

);

See

Add an icon to the map

moveLayer()

moveLayer

(

id

:

string

,

beforeId?

:

string

):

this

Defined in:

ui/map.ts:2850

Moves a layer to a different z-position.

Parameters

Parameter

Type

Description

id

string

The ID of the layer to move.

beforeId?

string

The ID of an existing layer to insert the new layer before. When viewing the map, the

id

layer will appear beneath the

beforeId

layer. If

beforeId

is omitted, the layer will be appended to the end of the layers array and appear above all other layers on the map.

Returns

this

Example

Move a layer with ID 'polygon' before the layer with ID 'country-label'. The

polygon

layer will appear beneath the

country-label

layer on the map.

map

.

moveLayer

(

'polygon'

,

'country-label'

);

panBy()

panBy

(

offset

:

PointLike

,

options?

:

EaseToOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:439

Pans the map by the specified offset.

Triggers the following events:

movestart

and

moveend

.

Parameters

Parameter

Type

Description

offset

PointLike

x

and

y

coordinates by which to pan the map.

options?

EaseToOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

See

Navigate the map with game-like controls

Inherited from

Camera.panBy

panTo()

panTo

(

lnglat

:

LngLatLike

,

options?

:

EaseToOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:460

Pans the map to the specified location with an animated transition.

Triggers the following events:

movestart

and

moveend

.

Parameters

Parameter

Type

Description

lnglat

LngLatLike

The location to pan the map to.

options?

EaseToOptions

Options describing the destination and animation of the transition.

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

map

.

panTo

([

-

74

,

38

]);

// Specify that the panTo animation should last 5000 milliseconds.

map

.

panTo

([

-

74

,

38

],

{

duration

:

5000

});

See

Update a feature in realtime

Inherited from

Camera.panTo

project()

project

(

lnglat

:

LngLatLike

):

Point

Defined in:

ui/map.ts:1469

Returns a

Point

representing pixel coordinates, relative to the map's

container

, that correspond to the specified geographical location.

Parameters

Parameter

Type

Description

lnglat

LngLatLike

The geographical location to project.

Returns

Point

The

Point

corresponding to

lnglat

, relative to the map's

container

.

Example

let

coordinate

=

[

-

122.420679

,

37.772537

];

let

point

=

map

.

project

(

coordinate

);

queryRenderedFeatures()

queryRenderedFeatures

(

geometryOrOptions?

:

PointLike

|

QueryRenderedFeaturesOptions

| [

PointLike

,

PointLike

],

options?

:

QueryRenderedFeaturesOptions

):

MapGeoJSONFeature

[]

Defined in:

ui/map.ts:1968

Returns an array of MapGeoJSONFeature objects representing visible features that satisfy the query parameters.

Parameters

Parameter

Type

Description

geometryOrOptions?

PointLike

|

QueryRenderedFeaturesOptions

| [

PointLike

,

PointLike

]

(optional) The geometry of the query region in pixel points within the map viewport: either a single pixel point or a pair of top-left and bottom-right pixel points describing a bounding box. The origin of the pixel points is at the top-left of the map viewport. Omitting this parameter (i.e. calling

Map.queryRenderedFeatures

with zero arguments, or with only a

options

argument) is equivalent to passing a bounding box encompassing the entire map viewport. The geometryOrOptions can receive a

QueryRenderedFeaturesOptions

only to support a situation where the function receives only one parameter which is the options parameter.

options?

QueryRenderedFeaturesOptions

(optional) Options object.

Returns

MapGeoJSONFeature

[]

An array of MapGeoJSONFeature objects.

The

properties

value of each returned feature object contains the properties of its source feature. For GeoJSON sources, only string and numeric property values are supported (i.e.

null

,

Array

, and

Object

values are not supported).

Each feature includes top-level

layer

,

source

, and

sourceLayer

properties. The

layer

property is an object representing the style layer to which the feature belongs. Layout and paint properties in this object contain values which are fully evaluated for the given zoom level and feature.

Only features that are currently rendered are included. Some features will

not

be included, like:

Features from layers whose

visibility

property is

"none"

.

Features from layers whose zoom range excludes the current zoom level.

Symbol features that have been hidden due to text or icon collision.

Features from all other layers are included, including features that may have no visible contribution to the rendered result; for example, because the layer's opacity or color alpha component is set to 0.

The topmost rendered feature appears first in the returned array, and subsequent features are sorted by descending z-order. Features that are rendered multiple times (due to wrapping across the antemeridian at low zoom levels) are returned only once (though subject to the following caveat).

Because features come from tiled vector data or GeoJSON data that is converted to tiles internally, feature geometries may be split or duplicated across tile boundaries and, as a result, features may appear multiple times in query results. For example, suppose there is a highway running through the bounding rectangle of a query. The results of the query will be those parts of the highway that lie within the map tiles covering the bounding rectangle, even if the highway extends into other tiles, and the portion of the highway within each map tile will be returned as a separate feature. Similarly, a point feature near a tile boundary may appear in multiple tiles due to tile buffering.

Examples

Find all features at a point

let

features

=

map

.

queryRenderedFeatures

(

[

20

,

35

],

{

layers

:

[

'my-layer-name'

]

}

);

Find all features within a static bounding box

let

features

=

map

.

queryRenderedFeatures

(

[[

10

,

20

],

[

30

,

50

]],

{

layers

:

[

'my-layer-name'

]

}

);

Find all features within a bounding box around a point

let

width

=

10

;

let

height

=

20

;

let

features

=

map

.

queryRenderedFeatures

([

[

point

.

x

-

width

/

2

,

point

.

y

-

height

/

2

],

[

point

.

x

+

width

/

2

,

point

.

y

+

height

/

2

]

],

{

layers

:

[

'my-layer-name'

]

});

Query all rendered features from a single layer

let

features

=

map

.

queryRenderedFeatures

({

layers

:

[

'my-layer-name'

]

});

See

Get features under the mouse pointer

querySourceFeatures()

querySourceFeatures

(

sourceId

:

string

,

parameters?

:

QuerySourceFeatureOptions

):

GeoJSONFeature

[]

Defined in:

ui/map.ts:2018

Returns an array of MapGeoJSONFeature objects representing features within the specified vector tile or GeoJSON source that satisfy the query parameters.

Parameters

Parameter

Type

Description

sourceId

string

The ID of the vector tile or GeoJSON source to query.

parameters?

QuerySourceFeatureOptions

The options object.

Returns

GeoJSONFeature

[]

An array of MapGeoJSONFeature objects.

In contrast to

Map.queryRenderedFeatures

, this function returns all features matching the query parameters, whether or not they are rendered by the current style (i.e. visible). The domain of the query includes all currently-loaded vector tiles and GeoJSON source tiles: this function does not check tiles outside the currently visible viewport.

Because features come from tiled vector data or GeoJSON data that is converted to tiles internally, feature geometries may be split or duplicated across tile boundaries and, as a result, features may appear multiple times in query results. For example, suppose there is a highway running through the bounding rectangle of a query. The results of the query will be those parts of the highway that lie within the map tiles covering the bounding rectangle, even if the highway extends into other tiles, and the portion of the highway within each map tile will be returned as a separate feature. Similarly, a point feature near a tile boundary may appear in multiple tiles due to tile buffering.

Example

Find all features in one source layer in a vector source

let

features

=

map

.

querySourceFeatures

(

'your-source-id'

,

{

sourceLayer

:

'your-source-layer'

});

queryTerrainElevation()

queryTerrainElevation

(

lngLatLike

:

LngLatLike

):

number

Defined in:

ui/camera.ts:1677

Gets the elevation at a given location, in meters above sea level. Returns null if terrain is not enabled. If terrain is enabled with some exaggeration value, the value returned here will be reflective of (multiplied by) that exaggeration value. This method should be used for proper positioning of custom 3d objects, as explained

here

Parameters

Parameter

Type

Description

lngLatLike

LngLatLike

[x,y] or LngLat coordinates of the location

Returns

number

elevation in meters

Inherited from

Camera.queryTerrainElevation

redraw()

redraw

():

this

Defined in:

ui/map.ts:3739

Force a synchronous redraw of the map.

Returns

this

Example

map

.

redraw

();

refreshTiles()

refreshTiles

(

sourceId

:

string

,

tileIds?

:

object

[]):

void

Defined in:

ui/map.ts:2506

Triggers a reload of the selected tiles

Parameters

Parameter

Type

Description

sourceId

string

The ID of the source

tileIds?

object

[]

An array of tile IDs to be reloaded. If not defined, all tiles will be reloaded.

Returns

void

Example

map

.

refreshTiles

(

'satellite'

,

[{

x

:

1024

,

y

:

1023

,

z

:

11

},

{

x

:

1023

,

y

:

1023

,

z

:

11

}]);

remove()

remove

():

void

Defined in:

ui/map.ts:3760

Clean up and release all internal resources associated with this map.

This includes DOM elements, event bindings, web workers, and WebGL resources.

Use this method when you are done using the map and wish to ensure that it no longer consumes browser resources. Afterwards, you must not call any other methods on the map.

Returns

void

removeControl()

removeControl

(

control

:

IControl

):

this

Defined in:

ui/map.ts:937

Removes the control from the map.

An

ErrorEvent

will be fired if the control is invalid.

Parameters

Parameter

Type

Description

control

IControl

The

IControl

to remove.

Returns

this

Example

// Define a new navigation control.

let

navigation

=

new

NavigationControl

();

// Add zoom and rotation controls to the map.

map

.

addControl

(

navigation

);

// Remove zoom and rotation controls from the map.

map

.

removeControl

(

navigation

);

removeFeatureState()

removeFeatureState

(

target

:

FeatureIdentifier

,

key?

:

string

):

this

Defined in:

ui/map.ts:3275

Removes the

state

of a feature, setting it back to the default behavior. If only a

target.source

is specified, it will remove the state for all features from that source. If

target.id

is also specified, it will remove all keys for that feature's state. If

key

is also specified, it removes only that key from that feature's state. Features are identified by their

feature.id

attribute, which can be any number or string.

Parameters

Parameter

Type

Description

target

FeatureIdentifier

Identifier of where to remove state. It can be a source, a feature, or a specific key of feature. Feature objects returned from

Map.queryRenderedFeatures

or event handlers can be used as feature identifiers.

key?

string

(optional) The key in the feature state to reset.

Returns

this

Examples

Reset the entire state object for all features in the

my-source

source

map

.

removeFeatureState

({

source

:

'my-source'

});

When the mouse leaves the

my-layer

layer, reset the entire state object for the feature under the mouse

map

.

on

(

'mouseleave'

,

'my-layer'

,

(

e

)

=>

{

map

.

removeFeatureState

({

source

:

'my-source'

,

sourceLayer

:

'my-source-layer'

,

id

:

e.features

[

0

].

id

});

});

When the mouse leaves the

my-layer

layer, reset only the

hover

key-value pair in the state for the feature under the mouse

map

.

on

(

'mouseleave'

,

'my-layer'

,

(

e

)

=>

{

map

.

removeFeatureState

({

source

:

'my-source'

,

sourceLayer

:

'my-source-layer'

,

id

:

e.features

[

0

].

id

},

'hover'

);

});

removeImage()

removeImage

(

id

:

string

):

void

Defined in:

ui/map.ts:2713

Remove an image from a style. This can be an image from the style's original sprite or any images that have been added at runtime using

Map.addImage

.

Parameters

Parameter

Type

Description

id

string

The ID of the image.

Returns

void

Example

// If an image with the ID 'cat' exists in

// the style's sprite, remove it.

if

(

map

.

hasImage

(

'cat'

))

map

.

removeImage

(

'cat'

);

removeLayer()

removeLayer

(

id

:

string

):

this

Defined in:

ui/map.ts:2868

Removes the layer with the given ID from the map's style.

An

ErrorEvent

will be fired if no such layer exists.

Parameters

Parameter

Type

Description

id

string

The ID of the layer to remove

Returns

this

Example

If a layer with ID 'state-data' exists, remove it.

if

(

map

.

getLayer

(

'state-data'

))

map

.

removeLayer

(

'state-data'

);

removeSource()

removeSource

(

id

:

string

):

this

Defined in:

ui/map.ts:2429

Removes a source from the map's style.

Parameters

Parameter

Type

Description

id

string

The ID of the source to remove.

Returns

this

Example

map

.

removeSource

(

'bathymetry-data'

);

removeSprite()

removeSprite

(

id

:

string

):

Map

Defined in:

ui/map.ts:3096

Removes the sprite from the map's style. Fires the

style

event.

Parameters

Parameter

Type

Description

id

string

The ID of the sprite to remove. If the sprite is declared as a single URL, the ID must be "default".

Returns

Map

Example

map

.

removeSprite

(

'sprite-two'

);

map

.

removeSprite

(

'default'

);

resetNorth()

resetNorth

(

options?

:

AnimationOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:692

Rotates the map so that north is up (0° bearing), with an animated transition.

Triggers the following events:

movestart

,

moveend

, and

rotate

.

Parameters

Parameter

Type

Description

options?

AnimationOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Inherited from

Camera.resetNorth

resetNorthPitch()

resetNorthPitch

(

options?

:

AnimationOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:705

Rotates and pitches the map so that north is up (0° bearing) and pitch and roll are 0°, with an animated transition.

Triggers the following events:

movestart

,

move

,

moveend

,

pitchstart

,

pitch

,

pitchend

,

rollstart

,

roll

,

rollend

, and

rotate

.

Parameters

Parameter

Type

Description

options?

AnimationOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Inherited from

Camera.resetNorthPitch

resize()

resize

(

eventData?

:

any

,

constrainTransform?

:

boolean

):

this

Defined in:

ui/map.ts:1010

Resizes the map according to the dimensions of its

container

element.

Checks if the map container size changed and updates the map if it has changed. This method must be called after the map's

container

is resized programmatically or when the map is shown after being initially hidden with CSS.

Triggers the following events:

movestart

,

move

,

moveend

, and

resize

.

Parameters

Parameter

Type

Default value

Description

eventData?

any

undefined

Additional properties to be passed to

movestart

,

move

,

resize

, and

moveend

events that get triggered as a result of resize. This can be useful for differentiating the source of an event (for example, user-initiated or programmatically-triggered events).

constrainTransform?

boolean

true

-

Returns

this

Example

Resize the map when the map container is shown after being initially hidden with CSS.

let

mapDiv

=

document

.

getElementById

(

'map'

);

if

(

mapDiv

.

style

.

visibility

===

true

)

map

.

resize

();

rotateTo()

rotateTo

(

bearing

:

number

,

options?

:

EaseToOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:678

Rotates the map to the specified bearing, with an animated transition. The bearing is the compass direction that is "up"; for example, a bearing of 90° orients the map so that east is up.

Triggers the following events:

movestart

,

moveend

, and

rotate

.

Parameters

Parameter

Type

Description

bearing

number

The desired bearing.

options?

EaseToOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Inherited from

Camera.rotateTo

setAnisotropicFilterPitch()

setAnisotropicFilterPitch

(

anisotropicFilterPitch?

:

number

):

this

Defined in:

ui/map.ts:1384

Sets the map's anisotropic filter pitch or reverts it to its default.

A

ErrorEvent

event will be fired if anisotropicFilterPitch is out of bounds.

Parameters

Parameter

Type

Description

anisotropicFilterPitch?

number

The pitch above which to apply anisotropic filtering to the map's raster layers (0-180). If

null

or

undefined

is provided, the function reverts to the default pitch threshold (20).

Returns

this

Example

map

.

setAnisotropicFilterPitch

(

85

);

setBearing()

setBearing

(

bearing

:

number

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:636

Sets the map's bearing (rotation). The bearing is the compass direction that is "up"; for example, a bearing of 90° orients the map so that east is up.

Equivalent to

jumpTo({bearing: bearing})

.

Triggers the following events:

movestart

,

moveend

, and

rotate

.

Parameters

Parameter

Type

Description

bearing

number

The desired bearing.

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

Rotate the map to 90 degrees

map

.

setBearing

(

90

);

Inherited from

Camera.setBearing

setCenter()

setCenter

(

center

:

LngLatLike

,

eventData?

:

any

):

Map

Defined in:

ui/camera.ts:383

Sets the map's geographical centerpoint. Equivalent to

jumpTo({center: center})

.

Triggers the following events:

movestart

and

moveend

.

Parameters

Parameter

Type

Description

center

LngLatLike

The centerpoint to set.

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

Map

Example

map

.

setCenter

([

-

74

,

38

]);

Inherited from

Camera.setCenter

setCenterClampedToGround()

setCenterClampedToGround

(

centerClampedToGround

:

boolean

):

void

Defined in:

ui/camera.ts:425

Sets the value of

centerClampedToGround

.

If true, the elevation of the center point will automatically be set to the terrain elevation (or zero if terrain is not enabled). If false, the elevation of the center point will default to sea level and will not automatically update. Defaults to true. Needs to be set to false to keep the camera above ground when pitch > 90 degrees.

Parameters

Parameter

Type

centerClampedToGround

boolean

Returns

void

Inherited from

Camera.setCenterClampedToGround

setCenterElevation()

setCenterElevation

(

elevation

:

number

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:402

Sets the elevation of the map's center point, in meters above sea level. Equivalent to

jumpTo({elevation: elevation})

.

Triggers the following events:

movestart

and

moveend

.

Parameters

Parameter

Type

Description

elevation

number

The elevation to set, in meters above sea level.

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Inherited from

Camera.setCenterElevation

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

Map

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

Map

Inherited from

Camera.setEventedParent

setFeatureState()

setFeatureState

(

feature

:

FeatureIdentifier

,

state

:

any

):

this

Defined in:

ui/map.ts:3224

Sets the

state

of a feature. A feature's

state

is a set of user-defined key-value pairs that are assigned to a feature at runtime. When using this method, the

state

object is merged with any existing key-value pairs in the feature's state. Features are identified by their

feature.id

attribute, which can be any number or string.

This method can only be used with sources that have a

feature.id

attribute. The

feature.id

attribute can be defined in three ways:

For vector or GeoJSON sources, including an

id

attribute in the original data file.

For vector or GeoJSON sources, using the

promoteId

option at the time the source is defined.

For GeoJSON sources, using the

generateId

option to auto-assign an

id

based on the feature's index in the source data. If you change feature data using

map.getSource('some id').setData(..)

, you may need to re-apply state taking into account updated

id

values.

Note

You can use the

feature-state

expression

to access the values in a feature's state object for the purposes of styling.

Parameters

Parameter

Type

Description

feature

FeatureIdentifier

Feature identifier. Feature objects returned from

Map.queryRenderedFeatures

or event handlers can be used as feature identifiers.

state

any

A set of key-value pairs. The values should be valid JSON types.

Returns

this

Example

// When the mouse moves over the `my-layer` layer, update

// the feature state for the feature under the mouse

map

.

on

(

'mousemove'

,

'my-layer'

,

(

e

)

=>

{

if

(

e

.

features

.

length

>

0

)

{

map

.

setFeatureState

({

source

:

'my-source'

,

sourceLayer

:

'my-source-layer'

,

id

:

e.features

[

0

].

id

,

},

{

hover

:

true

});

}

});

See

Create a hover effect

setFilter()

setFilter

(

layerId

:

string

,

filter?

:

FilterSpecification

,

options?

:

StyleSetterOptions

):

Map

Defined in:

ui/map.ts:2964

Sets the filter for the specified style layer.

Filters control which features a style layer renders from its source. Any feature for which the filter expression evaluates to

true

will be rendered on the map. Those that are false will be hidden.

Use

setFilter

to show a subset of your source data.

To clear the filter, pass

null

or

undefined

as the second parameter.

Parameters

Parameter

Type

Description

layerId

string

The ID of the layer to which the filter will be applied.

filter?

FilterSpecification

The filter, conforming to the MapLibre Style Specification's

filter definition

. If

null

or

undefined

is provided, the function removes any existing filter from the layer.

options?

StyleSetterOptions

Options object.

Returns

Map

Examples

Display only features with the 'name' property 'USA'

map

.

setFilter

(

'my-layer'

,

[

'=='

,

[

'get'

,

'name'

],

'USA'

]);

Display only features with five or more 'available-spots'

map

.

setFilter

(

'bike-docks'

,

[

'>='

,

[

'get'

,

'available-spots'

],

5

]);

Remove the filter for the 'bike-docks' style layer

map

.

setFilter

(

'bike-docks'

,

null

);

See

Create a timeline animation

setGlobalStateProperty()

setGlobalStateProperty

(

propertyName

:

string

,

value

:

any

):

Map

Defined in:

ui/map.ts:868

Sets a global state property that can be retrieved with the

global-state

expression

. If the value is null, it resets the property to its default value defined in the

state

style property

.

Parameters

Parameter

Type

Description

propertyName

string

The name of the state property to set.

value

any

The value of the state property to set.

Returns

Map

setGlyphs()

setGlyphs

(

glyphsUrl

:

string

,

options?

:

StyleSetterOptions

):

this

Defined in:

ui/map.ts:3050

Sets the value of the style's glyphs property. Pass a falsy value (null or undefined) to unset glyphs. * *

Parameters

Parameter

Type

Description

glyphsUrl

string

Glyph URL to set. Must conform to the

MapLibre Style Specification

. *

options

StyleSetterOptions

Options object. *

Returns

this

Example

```ts

map.setGlyphs('https://demotiles.maplibre.org/font/{fontstack}/{range}.pbf');

```

setLayerZoomRange()

setLayerZoomRange

(

layerId

:

string

,

minzoom

:

number

,

maxzoom

:

number

):

this

Defined in:

ui/map.ts:2926

Sets the zoom extent for the specified style layer. The zoom extent includes the

minimum zoom level

and

maximum zoom level

) at which the layer will be rendered.

Note

For style layers using vector sources, style layers cannot be rendered at zoom levels lower than the minimum zoom level of the

source layer

because the data does not exist at those zoom levels. If the minimum zoom level of the source layer is higher than the minimum zoom level defined in the style layer, the style layer will not be rendered at all zoom levels in the zoom range.

Parameters

Parameter

Type

Description

layerId

string

The ID of the layer to which the zoom extent will be applied.

minzoom

number

The minimum zoom to set (0-24).

maxzoom

number

The maximum zoom to set (0-24).

Returns

this

Example

map

.

setLayerZoomRange

(

'my-layer'

,

2

,

5

);

setLayoutProperty()

setLayoutProperty

(

layerId

:

string

,

name

:

string

,

value

:

any

,

options?

:

StyleSetterOptions

):

this

Defined in:

ui/map.ts:3023

Sets the value of a layout property in the specified style layer.

Parameters

Parameter

Type

Description

layerId

string

The ID of the layer to set the layout property in.

name

string

The name of the layout property to set.

value

any

The value of the layout property. Must be of a type appropriate for the property, as defined in the

MapLibre Style Specification

.

options

StyleSetterOptions

The options object.

Returns

this

Example

map

.

setLayoutProperty

(

'my-layer'

,

'visibility'

,

'none'

);

setLight()

setLight

(

light

:

LightSpecification

,

options?

:

StyleSetterOptions

):

Map

Defined in:

ui/map.ts:3142

Sets the any combination of light values.

Parameters

Parameter

Type

Description

light

LightSpecification

Light properties to set. Must conform to the

MapLibre Style Specification

.

options

StyleSetterOptions

Options object.

Returns

Map

Example

let

layerVisibility

=

map

.

getLayoutProperty

(

'my-layer'

,

'visibility'

);

setMaxBounds()

setMaxBounds

(

bounds?

:

LngLatBoundsLike

):

this

Defined in:

ui/map.ts:1156

Sets or clears the map's geographical bounds.

Pan and zoom operations are constrained within these bounds. If a pan or zoom is performed that would display regions outside these bounds, the map will instead display a position and zoom level as close as possible to the operation's request while still remaining within the bounds.

Parameters

Parameter

Type

Description

bounds?

LngLatBoundsLike

The maximum bounds to set. If

null

or

undefined

is provided, the function removes the map's maximum bounds.

Returns

this

Example

Define bounds that conform to the

LngLatBoundsLike

object as set the max bounds.

let

bounds

=

[

[

-

74.04728

,

40.68392

],

// [west, south]

[

-

73.91058

,

40.87764

]

// [east, north]

];

map

.

setMaxBounds

(

bounds

);

setMaxPitch()

setMaxPitch

(

maxPitch?

:

number

):

this

Defined in:

ui/map.ts:1323

Sets or clears the map's maximum pitch. If the map's current pitch is higher than the new maximum, the map will pitch to the new maximum and trigger the following events:

movestart

,

move

,

moveend

,

pitchstart

,

pitch

, and

pitchend

.

A

ErrorEvent

event will be fired if maxPitch is out of bounds.

Parameters

Parameter

Type

Description

maxPitch?

number

The maximum pitch to set (0-180). Values greater than 60 degrees are experimental and may result in rendering issues. If you encounter any, please raise an issue with details in the MapLibre project. If

null

or

undefined

is provided, the function removes the current maximum pitch (sets it to 60).

Returns

this

setMaxZoom()

setMaxZoom

(

maxZoom?

:

number

):

this

Defined in:

ui/map.ts:1231

Sets or clears the map's maximum zoom level. If the map's current zoom level is higher than the new maximum, the map will zoom to the new maximum and trigger the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

, and

zoomend

.

A

ErrorEvent

event will be fired if minZoom is out of bounds.

Parameters

Parameter

Type

Description

maxZoom?

number

The maximum zoom level to set. If

null

or

undefined

is provided, the function removes the current maximum zoom (sets it to 22).

Returns

this

Example

map

.

setMaxZoom

(

18.75

);

setMinPitch()

setMinPitch

(

minPitch?

:

number

):

this

Defined in:

ui/map.ts:1277

Sets or clears the map's minimum pitch. If the map's current pitch is lower than the new minimum, the map will pitch to the new minimum and trigger the following events:

movestart

,

move

,

moveend

,

pitchstart

,

pitch

, and

pitchend

.

A

ErrorEvent

event will be fired if minPitch is out of bounds.

Parameters

Parameter

Type

Description

minPitch?

number

The minimum pitch to set (0-180). Values greater than 60 degrees are experimental and may result in rendering issues. If you encounter any, please raise an issue with details in the MapLibre project. If

null

or

undefined

is provided, the function removes the current minimum pitch (i.e. sets it to 0).

Returns

this

setMinZoom()

setMinZoom

(

minZoom?

:

number

):

this

Defined in:

ui/map.ts:1181

Sets or clears the map's minimum zoom level. If the map's current zoom level is lower than the new minimum, the map will zoom to the new minimum and trigger the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

, and

zoomend

.

It is not always possible to zoom out and reach the set

minZoom

. Other factors such as map height may restrict zooming. For example, if the map is 512px tall it will not be possible to zoom below zoom 0 no matter what the

minZoom

is set to.

A

ErrorEvent

event will be fired if minZoom is out of bounds.

Parameters

Parameter

Type

Description

minZoom?

number

The minimum zoom level to set (-2 - 24). If

null

or

undefined

is provided, the function removes the current minimum zoom (i.e. sets it to -2).

Returns

this

Example

map

.

setMinZoom

(

12.25

);

setPadding()

setPadding

(

padding

:

PaddingOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:663

Sets the padding in pixels around the viewport.

Equivalent to

jumpTo({padding: padding})

.

Triggers the following events:

movestart

and

moveend

.

Parameters

Parameter

Type

Description

padding

PaddingOptions

The desired padding.

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

Sets a left padding of 300px, and a top padding of 50px

map

.

setPadding

({

left

:

300

,

top

:

50

});

Inherited from

Camera.setPadding

setPaintProperty()

setPaintProperty

(

layerId

:

string

,

name

:

string

,

value

:

any

,

options?

:

StyleSetterOptions

):

this

Defined in:

ui/map.ts:2995

Sets the value of a paint property in the specified style layer.

Parameters

Parameter

Type

Description

layerId

string

The ID of the layer to set the paint property in.

name

string

The name of the paint property to set.

value

any

The value of the paint property to set. Must be of a type appropriate for the property, as defined in the

MapLibre Style Specification

. Pass

null

to unset the existing value.

options

StyleSetterOptions

Options object.

Returns

this

Example

map

.

setPaintProperty

(

'my-layer'

,

'fill-color'

,

'#faafee'

);

See

Change a layer's color with buttons

Create a draggable point

setPitch()

setPitch

(

pitch

:

number

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:746

Sets the map's pitch (tilt). Equivalent to

jumpTo({pitch: pitch})

.

Triggers the following events:

movestart

,

moveend

,

pitchstart

, and

pitchend

.

Parameters

Parameter

Type

Description

pitch

number

The pitch to set, measured in degrees away from the plane of the screen (0-60).

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Inherited from

Camera.setPitch

setPixelRatio()

setPixelRatio

(

pixelRatio

:

number

):

void

Defined in:

ui/map.ts:1105

Sets the map's pixel ratio. This allows to override

devicePixelRatio

. After this call, the canvas'

width

attribute will be

container.clientWidth * pixelRatio

and its height attribute will be

container.clientHeight * pixelRatio

. Set this to null to disable

devicePixelRatio

override. Note that the pixel ratio actually applied may be lower to respect maxCanvasSize.

Parameters

Parameter

Type

Description

pixelRatio

number

The pixel ratio.

Returns

void

setProjection()

setProjection

(

projection

:

ProjectionSpecification

):

Map

Defined in:

ui/map.ts:3945

Sets the

ProjectionSpecification

.

Parameters

Parameter

Type

Description

projection

ProjectionSpecification

the projection specification to set

Returns

Map

setRenderWorldCopies()

setRenderWorldCopies

(

renderWorldCopies?

:

boolean

):

this

Defined in:

ui/map.ts:1433

Sets the state of

renderWorldCopies

.

Parameters

Parameter

Type

Description

renderWorldCopies?

boolean

If

true

, multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude. If set to

false

: - When the map is zoomed out far enough that a single representation of the world does not fill the map's entire container, there will be blank space beyond 180 and -180 degrees longitude. - Features that cross 180 and -180 degrees longitude will be cut in two (with one portion on the right edge of the map and the other on the left edge of the map) at every zoom level.

undefined

is treated as

true

,

null

is treated as

false

.

Returns

this

Example

map

.

setRenderWorldCopies

(

true

);

See

Render world copies

setRoll()

setRoll

(

roll

:

number

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:766

Sets the map's roll angle. Equivalent to

jumpTo({roll: roll})

.

Triggers the following events:

movestart

,

moveend

,

rollstart

, and

rollend

.

Parameters

Parameter

Type

Description

roll

number

The roll to set, measured in degrees about the camera boresight

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Inherited from

Camera.setRoll

setSky()

setSky

(

sky

:

SkySpecification

,

options?

:

StyleSetterOptions

):

Map

Defined in:

ui/map.ts:3168

Sets the value of style's sky properties.

Parameters

Parameter

Type

Description

sky

SkySpecification

Sky properties to set. Must conform to the

MapLibre Style Specification

.

options

StyleSetterOptions

Options object.

Returns

Map

Example

map

.

setSky

({

'atmosphere-blend'

:

1.0

});

setSourceTileLodParams()

setSourceTileLodParams

(

maxZoomLevelsOnScreen

:

number

,

tileCountMaxMinRatio

:

number

,

sourceId?

:

string

):

this

Defined in:

ui/map.ts:2480

Change the tile Level of Detail behavior of the specified source. These parameters have no effect when pitch == 0, and the largest effect when the horizon is visible on screen.

Parameters

Parameter

Type

Description

maxZoomLevelsOnScreen

number

The maximum number of distinct zoom levels allowed on screen at a time. There will generally be fewer zoom levels on the screen, the maximum can only be reached when the horizon is at the top of the screen. Increasing the maximum number of zoom levels causes the zoom level to decay faster toward the horizon.

tileCountMaxMinRatio

number

The ratio of the maximum number of tiles loaded (at high pitch) to the minimum number of tiles loaded. Increasing this ratio allows more tiles to be loaded at high pitch angles. If the ratio would otherwise be exceeded, the zoom level is reduced uniformly to keep the number of tiles within the limit.

sourceId?

string

The ID of the source to set tile LOD parameters for. All sources will be updated if unspecified. If

sourceId

is specified but a corresponding source does not exist, an error is thrown.

Returns

this

Example

map

.

setSourceTileLodParams

(

4.0

,

3.0

,

'terrain'

);

See

Modify Level of Detail behavior

setSprite()

setSprite

(

spriteUrl

:

string

,

options?

:

StyleSetterOptions

):

Map

Defined in:

ui/map.ts:3121

Sets the value of the style's sprite property.

Parameters

Parameter

Type

Description

spriteUrl

string

Sprite URL to set.

options

StyleSetterOptions

Options object.

Returns

Map

Example

map

.

setSprite

(

'YOUR_SPRITE_URL'

);

setStyle()

setStyle

(

style

:

string

|

StyleSpecification

,

options?

:

StyleSwapOptions

&

StyleOptions

):

this

Defined in:

ui/map.ts:2069

Updates the map's MapLibre style object with a new value.

If a style is already set when this is used and options.diff is set to true, the map renderer will attempt to compare the given style against the map's current state and perform only the changes necessary to make the map style match the desired state. Changes in sprites (images used for icons and patterns) and glyphs (fonts for label text)

cannot

be diffed. If the sprites or fonts used in the current style and the given style are different in any way, the map renderer will force a full update, removing the current style and building the given one from scratch.

Parameters

Parameter

Type

Description

style

string

|

StyleSpecification

A JSON object conforming to the schema described in the

MapLibre Style Specification

, or a URL to such JSON.

options?

StyleSwapOptions

&

StyleOptions

The options object.

Returns

this

Example

map

.

setStyle

(

"https://demotiles.maplibre.org/style.json"

);

map

.

setStyle

(

'https://demotiles.maplibre.org/style.json'

,

{

transformStyle

:

(

previousStyle

,

nextStyle

)

=>

({

...

nextStyle

,

sources

:

{

...

nextStyle

.

sources

,

// copy a source from previous style

'osm'

:

previousStyle

.

sources

.

osm

},

layers

:

[

// background layer

nextStyle

.

layers

[

0

],

// copy a layer from previous style

previousStyle

.

layers

[

0

],

// other layers from the next style

...

nextStyle

.

layers

.

slice

(

1

).

map

(

layer

=>

{

// hide the layers we don't need from demotiles style

if

(

layer

.

id

.

startsWith

(

'geolines'

))

{

layer

.

layout

=

{...

layer

.

layout

||

{},

visibility

:

'none'

};

// filter out US polygons

}

else

if

(

layer

.

id

.

startsWith

(

'coastline'

)

||

layer

.

id

.

startsWith

(

'countries'

))

{

layer

.

filter

=

[

'!='

,

[

'get'

,

'ADM0_A3'

],

'USA'

];

}

return

layer

;

})

]

})

});

setTerrain()

setTerrain

(

options

:

TerrainSpecification

):

this

Defined in:

ui/map.ts:2325

Loads a 3D terrain mesh, based on a "raster-dem" source.

Triggers the

terrain

event.

Parameters

Parameter

Type

Description

options

TerrainSpecification

Options object.

Returns

this

Example

map

.

setTerrain

({

source

:

'terrain'

});

setTransformConstrain()

setTransformConstrain

(

constrain?

:

TransformConstrainFunction

):

this

Defined in:

ui/map.ts:1452

Sets or clears the callback overriding how the map constrains the viewport's lnglat and zoom to respect the longitude and latitude bounds.

Parameters

Parameter

Type

Description

constrain?

TransformConstrainFunction

A

TransformConstrainFunction

callback defining how the viewport should respect the bounds.

null

clears the callback and reverts the constrain to the map transform's default constrain function.

Returns

this

Example

function

customTransformConstrain

(

lngLat

,

zoom

)

{

return

{

center

:

lngLat

,

zoom

:

zoom

??

0

};

};

map

.

setTransformConstrain

(

customTransformConstrain

);

See

Customize the map transform constrain

setTransformRequest()

setTransformRequest

(

transformRequest

:

RequestTransformFunction

):

this

Defined in:

ui/map.ts:2096

Updates the requestManager's transform request with a new function

Parameters

Parameter

Type

Description

transformRequest

RequestTransformFunction

A callback run before the Map makes a request for an external URL. The callback can be used to modify the url, set headers, or set the credentials property for cross-origin requests. Expected to return an object with a

url

property and optionally

headers

and

credentials

properties

Returns

this

Example

map

.

setTransformRequest

((

url

:

string

,

resourceType

:

string

)

=>

{});

setVerticalFieldOfView()

setVerticalFieldOfView

(

fov

:

number

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:582

Sets the map's vertical field of view, in degrees.

Triggers the following events:

movestart

,

move

, and

moveend

.

Parameters

Parameter

Type

Description

fov

number

The vertical field of view to set, in degrees (0-180).

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Default Value

36.87

Example

Change vertical field of view to 30 degrees

map

.

setVerticalFieldOfView

(

30

);

Inherited from

Camera.setVerticalFieldOfView

setZoom()

setZoom

(

zoom

:

number

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:490

Sets the map's zoom level. Equivalent to

jumpTo({zoom: zoom})

.

Triggers the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

, and

zoomend

.

Parameters

Parameter

Type

Description

zoom

number

The zoom level to set (0-20).

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

Zoom to the zoom level 5 without an animated transition

map

.

setZoom

(

5

);

Inherited from

Camera.setZoom

setZoomSnap()

setZoomSnap

(

snap

:

number

):

this

Defined in:

ui/camera.ts:606

Sets the map's zoom snap level.

Parameters

Parameter

Type

Description

snap

number

The zoom snap level to set.

Returns

this

Inherited from

Camera.setZoomSnap

snapToNorth()

snapToNorth

(

options?

:

AnimationOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:724

Snaps the map so that north is up (0° bearing), if the current bearing is close enough to it (i.e. within the

bearingSnap

threshold).

Triggers the following events:

movestart

,

moveend

, and

rotate

.

Parameters

Parameter

Type

Description

options?

AnimationOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Inherited from

Camera.snapToNorth

stop()

stop

():

this

Defined in:

ui/camera.ts:1603

Stops any animated transition underway.

Returns

this

Inherited from

Camera.stop

triggerRepaint()

triggerRepaint

():

void

Defined in:

ui/map.ts:3807

Trigger the rendering of a single frame. Use this method with custom layers to repaint the map when the layer changes. Calling this multiple times before the next frame is rendered will still result in only a single frame being rendered.

Returns

void

Example

map

.

triggerRepaint

();

See

Add a 3D model

Add an animated icon to the map

unproject()

unproject

(

point

:

PointLike

):

LngLat

Defined in:

ui/map.ts:1487

Returns a

LngLat

representing geographical coordinates that correspond to the specified pixel coordinates.

Parameters

Parameter

Type

Description

point

PointLike

The pixel coordinates to unproject.

Returns

LngLat

The

LngLat

corresponding to

point

.

Example

map

.

on

(

'click'

,

(

e

)

=>

{

// When the map is clicked, get the geographic coordinate.

let

coordinate

=

map

.

unproject

(

e

.

point

);

});

updateImage()

updateImage

(

id

:

string

,

image

:

ImageBitmap

|

ImageData

|

HTMLImageElement

|

StyleImageInterface

| {

data

:

Uint8Array

<

ArrayBufferLike

> |

Uint8ClampedArray

<

ArrayBufferLike

>;

height

:

number

;

width

:

number

; }):

this

Defined in:

ui/map.ts:2622

Update an existing image in a style. This image can be displayed on the map like any other icon in the style's sprite using the image's ID with

icon-image

,

background-pattern

,

fill-pattern

, or

line-pattern

.

An

ErrorEvent

will be fired if the image parameter is invalid.

Parameters

Parameter

Type

Description

id

string

The ID of the image.

image

ImageBitmap

|

ImageData

|

HTMLImageElement

|

StyleImageInterface

| {

data

:

Uint8Array

<

ArrayBufferLike

> |

Uint8ClampedArray

<

ArrayBufferLike

>;

height

:

number

;

width

:

number

; }

The image as an

HTMLImageElement

,

ImageData

,

ImageBitmap

or object with

width

,

height

, and

data

properties with the same format as

ImageData

.

Returns

this

Example

// If an image with the ID 'cat' already exists in the style's sprite,

// replace that image with a new image, 'other-cat-icon.png'.

if

(

map

.

hasImage

(

'cat'

))

map

.

updateImage

(

'cat'

,

'./other-cat-icon.png'

);

zoomIn()

zoomIn

(

options?

:

AnimationOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:533

Incrementally increases the map's zoom level by 1, first snapping to the nearest

zoomSnap

increment.

Triggers the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

, and

zoomend

.

Parameters

Parameter

Type

Description

options?

AnimationOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

Zoom the map in one level with a custom animation duration

map

.

zoomIn

({

duration

:

1000

});

Inherited from

Camera.zoomIn

zoomOut()

zoomOut

(

options?

:

AnimationOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:551

Decreases the map's zoom level by 1, first snapping to the nearest

zoomSnap

increment.

Triggers the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

, and

zoomend

.

Parameters

Parameter

Type

Description

options?

AnimationOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

Zoom the map out one level with a custom animation offset

map

.

zoomOut

({

offset

:

[

80

,

60

]});

Inherited from

Camera.zoomOut

zoomTo()

zoomTo

(

zoom

:

number

,

options?

:

EaseToOptions

,

eventData?

:

any

):

this

Defined in:

ui/camera.ts:514

Zooms the map to the specified zoom level, with an animated transition.

Triggers the following events:

movestart

,

move

,

moveend

,

zoomstart

,

zoom

, and

zoomend

.

Parameters

Parameter

Type

Description

zoom

number

The zoom level to transition to.

options?

EaseToOptions

Options object

eventData?

any

Additional properties to be added to event objects of events triggered by this method.

Returns

this

Example

// Zoom to the zoom level 5 without an animated transition

map

.

zoomTo

(

5

);

// Zoom to the zoom level 8 with an animated transition

map

.

zoomTo

(

8

,

{

duration

:

2000

,

offset

:

[

100

,

50

]

});

Inherited from

Camera.zoomTo

Properties

boxZoom

boxZoom

:

BoxZoomHandler

Defined in:

ui/map.ts:630

The map's

BoxZoomHandler

, which implements zooming using a drag gesture with the Shift key pressed. Find more details and examples using

boxZoom

in the

BoxZoomHandler

section.

cancelPendingTileRequestsWhileZooming

cancelPendingTileRequestsWhileZooming

:

boolean

Defined in:

ui/map.ts:681

The map's property which determines whether to cancel, or retain, tiles from the current viewport which are still loading but which belong to a farther (smaller) zoom level than the current one. * If

true

, when zooming in, tiles which didn't manage to load for previous zoom levels will become canceled. This might save some computing resources for slower devices, but the map details might appear more abruptly at the end of the zoom. * If

false

, when zooming in, the previous zoom level(s) tiles will progressively appear, giving a smoother map details experience. However, more tiles will be rendered in a short period of time.

Default Value

true

cooperativeGestures

cooperativeGestures

:

CooperativeGesturesHandler

Defined in:

ui/map.ts:673

The map's

CooperativeGesturesHandler

, which allows the user to see cooperative gesture info when user tries to zoom in/out. Find more details and examples using

cooperativeGestures

in the

CooperativeGesturesHandler

section.

doubleClickZoom

doubleClickZoom

:

DoubleClickZoomHandler

Defined in:

ui/map.ts:655

The map's

DoubleClickZoomHandler

, which allows the user to zoom by double clicking. Find more details and examples using

doubleClickZoom

in the

DoubleClickZoomHandler

section.

dragPan

dragPan

:

DragPanHandler

Defined in:

ui/map.ts:643

The map's

DragPanHandler

, which implements dragging the map with a mouse or touch gesture. Find more details and examples using

dragPan

in the

DragPanHandler

section.

dragRotate

dragRotate

:

DragRotateHandler

Defined in:

ui/map.ts:637

The map's

DragRotateHandler

, which implements rotating the map while dragging with the right mouse button or with the Control key pressed. Find more details and examples using

dragRotate

in the

DragRotateHandler

section.

keyboard

keyboard

:

KeyboardHandler

Defined in:

ui/map.ts:649

The map's

KeyboardHandler

, which allows the user to zoom, rotate, and pan the map using keyboard shortcuts. Find more details and examples using

keyboard

in the

KeyboardHandler

section.

scrollZoom

scrollZoom

:

ScrollZoomHandler

Defined in:

ui/map.ts:624

The map's

ScrollZoomHandler

, which implements zooming in and out with a scroll wheel or trackpad. Find more details and examples using

scrollZoom

in the

ScrollZoomHandler

section.

touchPitch

touchPitch

:

TwoFingersTouchPitchHandler

Defined in:

ui/map.ts:667

The map's

TwoFingersTouchPitchHandler

, which allows the user to pitch the map with touch gestures. Find more details and examples using

touchPitch

in the

TwoFingersTouchPitchHandler

section.

touchZoomRotate

touchZoomRotate

:

TwoFingersTouchZoomRotateHandler

Defined in:

ui/map.ts:661

The map's

TwoFingersTouchZoomRotateHandler

, which allows the user to zoom or rotate the map with touch gestures. Find more details and examples using

touchZoomRotate

in the

TwoFingersTouchZoomRotateHandler

section.

transformCameraUpdate

transformCameraUpdate

:

CameraUpdateTransformFunction

Defined in:

ui/camera.ts:314

A callback used to defer camera updates or apply arbitrary constraints. If specified, this Camera instance can be used as a stateless component in React etc.

Inherited from

Camera.transformCameraUpdate

transformConstrain

transformConstrain

:

TransformConstrainFunction

Defined in:

ui/map.ts:687

The map transform's callback that overrides the default constrain function.

Default Value

null

Back to top
