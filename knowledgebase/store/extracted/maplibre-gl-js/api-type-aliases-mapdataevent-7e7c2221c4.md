---
title: MapDataEvent - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapDataEvent/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:33.318207+00:00
kind: extracted-doc
---

# MapDataEvent - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapDataEvent/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:33.318207+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapDataEvent/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/MapSourceDataType/

Captured summary:

- MapDataEvent - MapLibre GL JS Skip to content MapDataEvent MapDataEvent = object Defined in: ui/events.ts:731 A MapDataEvent object is emitted with the data and dataloading events.
- Possible values for dataType s are: 'source' : The non-tile data associated with any source 'style' : The style used by the map Possible values for sourceDataType s are: 'metadata' : indicates that any necessary source metadata has been loaded (such as TileJSON) and it is ok to start loading tiles 'content' : indicates the source data has changed (such as when source.setData() has been called on GeoJSONSource) 'visibility' : send when the source becomes used when at least one of its layers becomes visible in style sense (inside the layer's zoom range and with layout.visibility set to 'visible') 'idle' : indicates that no new source data has been fetched (but the source has done loading) Example // The sourcedata event is an example of MapDataEvent.
- isSourceLoaded ) { // Do something when the source has finished loading } }); Properties dataType dataType : string Defined in: ui/events.ts:739 The type of data that has changed.
- sourceDataType sourceDataType : MapSourceDataType Defined in: ui/events.ts:743 Included if the event has a dataType of source and the event signals that internal data has been received or changed.
- Possible values are metadata , content , visibility and idle .

Extracted text:

MapDataEvent - MapLibre GL JS

Skip to content

MapDataEvent

MapDataEvent

=

object

Defined in:

ui/events.ts:731

A

MapDataEvent

object is emitted with the

data

and

dataloading

events. Possible values for

dataType

s are:

'source'

: The non-tile data associated with any source

'style'

: The

style

used by the map

Possible values for

sourceDataType

s are:

'metadata'

: indicates that any necessary source metadata has been loaded (such as TileJSON) and it is ok to start loading tiles

'content'

: indicates the source data has changed (such as when source.setData() has been called on GeoJSONSource)

'visibility'

: send when the source becomes used when at least one of its layers becomes visible in style sense (inside the layer's zoom range and with layout.visibility set to 'visible')

'idle'

: indicates that no new source data has been fetched (but the source has done loading)

Example

// The sourcedata event is an example of MapDataEvent.

// Set up an event listener on the map.

map

.

on

(

'sourcedata'

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

isSourceLoaded

)

{

// Do something when the source has finished loading

}

});

Properties

dataType

dataType

:

string

Defined in:

ui/events.ts:739

The type of data that has changed. One of

'source'

,

'style'

.

sourceDataType

sourceDataType

:

MapSourceDataType

Defined in:

ui/events.ts:743

Included if the event has a

dataType

of

source

and the event signals that internal data has been received or changed. Possible values are

metadata

,

content

,

visibility

and

idle

.

type

type

:

string

Defined in:

ui/events.ts:735

The event type.

Back to top
