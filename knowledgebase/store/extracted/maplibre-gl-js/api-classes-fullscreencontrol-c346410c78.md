---
title: FullscreenControl - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/FullscreenControl/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:11.099652+00:00
kind: extracted-doc
---

# FullscreenControl - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/FullscreenControl/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:11.099652+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/FullscreenControl/
- https://maplibre.org/maplibre-gl-js/docs/examples/view-a-fullscreen-map/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Event/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/IControl/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/FullscreenControlOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Captured summary:

- FullscreenControl - MapLibre GL JS Skip to content FullscreenControl Defined in: ui/control/fullscreen_control.ts:46 A FullscreenControl control contains a button for toggling the map in and out of fullscreen mode.
- When requestFullscreen is not supported, fullscreen is handled via CSS properties.
- The map's cooperativeGestures option is temporarily disabled while the map is in fullscreen mode, and is restored when the map exist fullscreen mode.
- Param the full screen control options Example map .
- addControl ( new FullscreenControl ({ container : document.querySelector ( 'body' )})); See View a fullscreen map Events Event fullscreenstart of type Event will be fired when fullscreen mode has started.

Extracted text:

FullscreenControl - MapLibre GL JS

Skip to content

FullscreenControl

Defined in:

ui/control/fullscreen_control.ts:46

A

FullscreenControl

control contains a button for toggling the map in and out of fullscreen mode. When

requestFullscreen

is not supported, fullscreen is handled via CSS properties. The map's

cooperativeGestures

option is temporarily disabled while the map is in fullscreen mode, and is restored when the map exist fullscreen mode.

Param

the full screen control options

Example

map

.

addControl

(

new

FullscreenControl

({

container

:

document.querySelector

(

'body'

)}));

See

View a fullscreen map

Events

Event

fullscreenstart

of type

Event

will be fired when fullscreen mode has started.

Event

fullscreenend

of type

Event

will be fired when fullscreen mode has ended.

Extends

Evented

Implements

IControl

Constructors

Constructor

new FullscreenControl

(

options?

:

FullscreenControlOptions

):

FullscreenControl

Defined in:

ui/control/fullscreen_control.ts:59

Parameters

Parameter

Type

Description

options

FullscreenControlOptions

the control's options

Returns

FullscreenControl

Overrides

Evented.constructor

Methods

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

FullscreenControl

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

FullscreenControl

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

HTMLElement

Defined in:

ui/control/fullscreen_control.ts:84

Register a control on the map and give it a chance to register event listeners and resources. This method is called by

Map.addControl

internally.

Parameters

Parameter

Type

Description

map

Map

the Map this control will be added to

Returns

HTMLElement

The control's container element. This should be created by the control and returned by onAdd without being attached to the DOM: the map will insert the control's element into the DOM as necessary.

Implementation of

IControl

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

FullscreenControl

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

FullscreenControl

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

ui/control/fullscreen_control.ts:93

Unregister a control on the map and give it a chance to detach event listeners and resources. This method is called by

Map.removeControl

internally.

Returns

void

Implementation of

IControl

.

onRemove

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

FullscreenControl

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

FullscreenControl

Inherited from

Evented

.

setEventedParent

Back to top
