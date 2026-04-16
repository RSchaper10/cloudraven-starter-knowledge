---
title: Marker - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/Marker/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:14.265947+00:00
kind: extracted-doc
---

# Marker - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Marker/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:14.265947+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Marker/
- https://maplibre.org/maplibre-gl-js/docs/examples/add-a-default-marker/
- https://maplibre.org/maplibre-gl-js/docs/examples/add-custom-icons-with-markers/
- https://maplibre.org/maplibre-gl-js/docs/examples/create-a-draggable-marker/
- https://maplibre.org/maplibre-gl-js/docs/examples/animate-a-marker/
- https://maplibre.org/maplibre-gl-js/docs/examples/attach-a-popup-to-a-marker-instance/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Event/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MarkerOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLat/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Alignment/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Popup/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatLike/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/PointLike/

Captured summary:

- Marker - MapLibre GL JS Skip to content Marker Defined in: ui/marker.ts:148 Creates a marker component Examples let marker = new Marker () .
- addTo ( map ); Set options let marker = new Marker ({ color : "#FFFFFF" , draggable : true }).
- maplibregl-marker-covered { pointer-events : none ; cursor : default ; } See Add a default marker Add custom icons with Markers Create a draggable Marker Animate a marker Attach a popup to a marker instance Events Event dragstart of type Event will be fired when dragging starts.
- Event drag of type Event will be fired while dragging.
- Event dragend of type Event will be fired when the marker is finished being dragged.

Extracted text:

Marker - MapLibre GL JS

Skip to content

Marker

Defined in:

ui/marker.ts:148

Creates a marker component

Examples

let

marker

=

new

Marker

()

.

setLngLat

([

30.5

,

50.5

])

.

addTo

(

map

);

Set options

let

marker

=

new

Marker

({

color

:

"#FFFFFF"

,

draggable

:

true

}).

setLngLat

([

30.5

,

50.5

])

.

addTo

(

map

);

.

maplibregl-marker-covered

{

pointer-events

:

none

;

cursor

:

default

;

}

See

Add a default marker

Add custom icons with Markers

Create a draggable Marker

Animate a marker

Attach a popup to a marker instance

Events

Event

dragstart

of type

Event

will be fired when dragging starts.

Event

drag

of type

Event

will be fired while dragging.

Event

dragend

of type

Event

will be fired when the marker is finished being dragged.

Event

click

of type

Event

will be fired when the marker is clicked.

CSS Classes

CSS class

maplibregl-marker-covered

is toggled on the marker element when the marker is hidden behind 3D terrain or on the back of a globe. Use this class to apply custom styles to covered markers.

Extends

Evented

Constructors

Constructor

new Marker

(

options?

:

MarkerOptions

):

Marker

Defined in:

ui/marker.ts:178

Parameters

Parameter

Type

Description

options?

MarkerOptions

the options

Returns

Marker

Overrides

Evented.constructor

Methods

addClassName()

addClassName

(

className

:

string

):

void

Defined in:

ui/marker.ts:700

Adds a CSS class to the marker element.

Parameters

Parameter

Type

Description

className

string

on-empty string with CSS class name to add to marker element

Returns

void

Example

let marker = new Marker()

marker.addClassName('some-class')

addTo()

addTo

(

map

:

Map

):

this

Defined in:

ui/marker.ts:336

Attaches the

Marker

to a

Map

object.

Parameters

Parameter

Type

Description

map

Map

The MapLibre GL JS map to add the marker to.

Returns

this

Example

let

marker

=

new

Marker

()

.

setLngLat

([

30.5

,

50.5

])

.

addTo

(

map

);

// add the marker to the map

getElement()

getElement

():

HTMLElement

Defined in:

ui/marker.ts:447

Returns the

Marker

's HTML element.

Returns

HTMLElement

element

getLngLat()

getLngLat

():

LngLat

Defined in:

ui/marker.ts:418

Get the marker's geographical location.

The longitude of the result may differ by a multiple of 360 degrees from the longitude previously set by

setLngLat

because

Marker

wraps the anchor longitude across copies of the world to keep the marker on screen.

Returns

LngLat

A

LngLat

describing the marker's location.

Example

// Store the marker's longitude and latitude coordinates in a variable

let

lngLat

=

marker

.

getLngLat

();

// Print the marker's longitude and latitude values in the console

console

.

log

(

'Longitude: '

+

lngLat

.

lng

+

', Latitude: '

+

lngLat

.

lat

)

See

Create a draggable Marker

getOffset()

getOffset

():

Point

Defined in:

ui/marker.ts:675

Get the marker's offset.

Returns

Point

The marker's screen coordinates in pixels.

getPitchAlignment()

getPitchAlignment

():

Alignment

Defined in:

ui/marker.ts:878

Returns the current

pitchAlignment

property of the marker.

Returns

Alignment

The current pitch alignment of the marker in degrees.

getPopup()

getPopup

():

Popup

Defined in:

ui/marker.ts:551

Returns the

Popup

instance that is bound to the Marker.

Returns

Popup

popup

Example

let

marker

=

new

Marker

()

.

setLngLat

([

0

,

0

])

.

setPopup

(

new

Popup

().

setHTML

(

"<h1>Hello World!</h1>"

))

.

addTo

(

map

);

console

.

log

(

marker

.

getPopup

());

// return the popup instance

getRotation()

getRotation

():

number

Defined in:

ui/marker.ts:842

Returns the current rotation angle of the marker (in degrees).

Returns

number

The current rotation angle of the marker.

getRotationAlignment()

getRotationAlignment

():

Alignment

Defined in:

ui/marker.ts:860

Returns the current

rotationAlignment

property of the marker.

Returns

Alignment

The current rotational alignment of the marker.

isDraggable()

isDraggable

():

boolean

Defined in:

ui/marker.ts:824

Returns true if the marker can be dragged

Returns

boolean

True if the marker is draggable.

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

Marker

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

Marker

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

Marker

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

Marker

this

or a promise if a listener is not provided

Inherited from

Evented

.

once

remove()

remove

():

this

Defined in:

ui/marker.ts:376

Removes the marker from a map

Returns

this

Example

let

marker

=

new

Marker

().

addTo

(

map

);

marker

.

remove

();

removeClassName()

removeClassName

(

className

:

string

):

void

Defined in:

ui/marker.ts:715

Removes a CSS class from the marker element.

Parameters

Parameter

Type

Description

className

string

Non-empty string with CSS class name to remove from marker element

Returns

void

Example

let

marker

=

new

Marker

()

marker

.

removeClassName

(

'some-class'

)

setDraggable()

setDraggable

(

shouldBeDraggable?

:

boolean

):

this

Defined in:

ui/marker.ts:802

Sets the

draggable

property and functionality of the marker

Parameters

Parameter

Type

Description

shouldBeDraggable?

boolean

Turns drag functionality on/off

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

Marker

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

Marker

Inherited from

Evented

.

setEventedParent

setLngLat()

setLngLat

(

lnglat

:

LngLatLike

):

this

Defined in:

ui/marker.ts:435

Set the marker's geographical position and move it.

Parameters

Parameter

Type

Description

lnglat

LngLatLike

A

LngLat

describing where the marker should be located.

Returns

this

Example

Create a new marker, set the longitude and latitude, and add it to the map

new

Marker

()

.

setLngLat

([

-

65.017

,

-

16.457

])

.

addTo

(

map

);

See

Add custom icons with Markers

Create a draggable Marker

setOffset()

setOffset

(

offset

:

PointLike

):

this

Defined in:

ui/marker.ts:683

Sets the offset of the marker

Parameters

Parameter

Type

Description

offset

PointLike

The offset in pixels as a

PointLike

object to apply relative to the element's center. Negatives indicate left and up.

Returns

this

setOpacity()

setOpacity

(

opacity?

:

string

|

number

,

opacityWhenCovered?

:

string

|

number

):

this

Defined in:

ui/marker.ts:888

Sets the

opacity

and

opacityWhenCovered

properties of the marker. When called without arguments, resets opacity and opacityWhenCovered to defaults

Parameters

Parameter

Type

Description

opacity?

string

|

number

Sets the

opacity

property of the marker.

opacityWhenCovered?

string

|

number

Sets the

opacityWhenCovered

property of the marker.

Returns

this

setPitchAlignment()

setPitchAlignment

(

alignment?

:

Alignment

):

this

Defined in:

ui/marker.ts:868

Sets the

pitchAlignment

property of the marker.

Parameters

Parameter

Type

Description

alignment?

Alignment

Sets the

pitchAlignment

property of the marker. If alignment is 'auto', it will automatically match

rotationAlignment

.

Returns

this

setPopup()

setPopup

(

popup?

:

Popup

):

this

Defined in:

ui/marker.ts:464

Binds a

Popup

to the Marker.

Parameters

Parameter

Type

Description

popup?

Popup

An instance of the

Popup

class. If undefined or null, any popup set on this Marker instance is unset.

Returns

this

Example

let

marker

=

new

Marker

()

.

setLngLat

([

0

,

0

])

.

setPopup

(

new

Popup

().

setHTML

(

"<h1>Hello World!</h1>"

))

// add popup

.

addTo

(

map

);

See

Attach a popup to a marker instance

setRotation()

setRotation

(

rotation?

:

number

):

this

Defined in:

ui/marker.ts:832

Sets the

rotation

property of the marker.

Parameters

Parameter

Type

Description

rotation?

number

The rotation angle of the marker (clockwise, in degrees), relative to its respective

Marker.setRotationAlignment

setting.

Returns

this

setRotationAlignment()

setRotationAlignment

(

alignment?

:

Alignment

):

this

Defined in:

ui/marker.ts:850

Sets the

rotationAlignment

property of the marker.

Parameters

Parameter

Type

Description

alignment?

Alignment

Sets the

rotationAlignment

property of the marker. defaults to 'auto'

Returns

this

setSubpixelPositioning()

setSubpixelPositioning

(

value

:

boolean

):

Marker

Defined in:

ui/marker.ts:514

Set the option to allow subpixel positioning of the marker by passing a boolean

Parameters

Parameter

Type

Description

value

boolean

when set to

true

, subpixel positioning is enabled for the marker.

Returns

Marker

Example

let

marker

=

new

Marker

()

marker

.

setSubpixelPositioning

(

true

);

toggleClassName()

toggleClassName

(

className

:

string

):

boolean

Defined in:

ui/marker.ts:732

Add or remove the given CSS class on the marker element, depending on whether the element currently has that class.

Parameters

Parameter

Type

Description

className

string

Non-empty string with CSS class name to add/remove

Returns

boolean

if the class was removed return false, if class was added, then return true

Example

let

marker

=

new

Marker

()

marker

.

toggleClassName

(

'toggleClass'

)

togglePopup()

togglePopup

():

this

Defined in:

ui/marker.ts:567

Opens or closes the

Popup

instance that is bound to the Marker, depending on the current state of the

Popup

.

Returns

this

Example

let

marker

=

new

Marker

()

.

setLngLat

([

0

,

0

])

.

setPopup

(

new

Popup

().

setHTML

(

"<h1>Hello World!</h1>"

))

.

addTo

(

map

);

marker

.

togglePopup

();

// toggle popup open or closed

Back to top
