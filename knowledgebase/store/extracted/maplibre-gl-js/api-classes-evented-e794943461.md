---
title: Evented - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:30.642091+00:00
kind: extracted-doc
---

# Evented - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:30.642091+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/GeolocateControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/FullscreenControl/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Popup/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Marker/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Style/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/GeoJSONSource/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/ImageSource/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/RasterTileSource/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/VectorTileSource/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/StyleLayer/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Listener/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Subscription/

Captured summary:

- Evented - MapLibre GL JS Skip to content Evented Defined in: util/evented.ts:59 Methods mixed in to other classes for event capabilities.
- Extended by GeolocateControl FullscreenControl Popup Marker Style GeoJSONSource ImageSource RasterTileSource VectorTileSource StyleLayer Methods listens() listens ( type : string ): boolean Defined in: util/evented.ts:165 Returns a true if this instance of Evented or any forwardeed instances of Evented have a listener for the specified type.
- Parameters Parameter Type Description type string The event type Returns boolean true if there is at least one registered listener for specified event type, false otherwise off() off ( type : string , listener : Listener ): Evented Defined in: util/evented.ts:90 Removes a previously registered event listener.
- Parameters Parameter Type Description type string The event type to remove listeners for.
- listener Listener The listener function to remove.

Extracted text:

Evented - MapLibre GL JS

Skip to content

Evented

Defined in:

util/evented.ts:59

Methods mixed in to other classes for event capabilities.

Extended by

GeolocateControl

FullscreenControl

Popup

Marker

Style

GeoJSONSource

ImageSource

RasterTileSource

VectorTileSource

StyleLayer

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

Evented

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

Evented

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

Evented

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

Evented

this

or a promise if a listener is not provided

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

Evented

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

Evented

Back to top
