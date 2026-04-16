---
title: Hash - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/Hash/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:13.204392+00:00
kind: extracted-doc
---

# Hash - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Hash/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:13.204392+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Hash/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Captured summary:

- Hash - MapLibre GL JS Skip to content Hash Defined in: ui/hash.ts:12 Adds the map's position to its page's location hash.
- Methods addTo() addTo ( map : Map ): Hash Defined in: ui/hash.ts:25 Map element to listen for coordinate changes Parameters Parameter Type Description map Map The map object Returns Hash remove() remove (): Hash Defined in: ui/hash.ts:35 Removes hash Returns Hash Properties _updateHash _updateHash : () => Timeout Defined in: ui/hash.ts:155 Mobile Safari doesn't allow updating the hash more than 100 times per 30 seconds.

Extracted text:

Hash - MapLibre GL JS

Skip to content

Hash

Defined in:

ui/hash.ts:12

Adds the map's position to its page's location hash. Passed as an option to the map object.

Methods

addTo()

addTo

(

map

:

Map

):

Hash

Defined in:

ui/hash.ts:25

Map element to listen for coordinate changes

Parameters

Parameter

Type

Description

map

Map

The map object

Returns

Hash

remove()

remove

():

Hash

Defined in:

ui/hash.ts:35

Removes hash

Returns

Hash

Properties

_updateHash

_updateHash

: () =>

Timeout

Defined in:

ui/hash.ts:155

Mobile Safari doesn't allow updating the hash more than 100 times per 30 seconds.

Returns

Timeout

Back to top
