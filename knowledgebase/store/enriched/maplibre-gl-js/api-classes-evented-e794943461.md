---
title: Evented - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:30.642091+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# Evented - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Evented/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- Evented - MapLibre GL JS Skip to content Evented Defined in: util/evented.ts:59 Methods mixed in to other classes for event capabilities.
- Extended by GeolocateControl FullscreenControl Popup Marker Style GeoJSONSource ImageSource RasterTileSource VectorTileSource StyleLayer Methods listens() listens ( type : string ): boolean Defined in: util/evented.ts:165 Returns a true if this instance of Evented or any forwardeed instances of Evented have a listener for the specified type.
- Parameters Parameter Type Description type string The event type Returns boolean true if there is at least one registered listener for specified event type, false otherwise off() off ( type : string , listener : Listener ): Evented Defined in: util/evented.ts:90 Removes a previously registered event listener.
- Parameters Parameter Type Description type string The event type to remove listeners for.

CloudRaven applicability:

- Use this material for open, portable map-based interfaces and geospatial storytelling.

Prototype-to-production review:

- Strong fit when the map stack should stay open and customizable.
- Choose tile, geocoding, and style providers deliberately.

CloudRaven example paths:

- Visualize service coverage, assets, or route activity on a live map.
- Create location-aware dashboards without locking into a proprietary front-end map SDK.

Suggested retrieval tags:

- `maps`
- `geospatial`
- `maplibre`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-evented-e794943461.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-evented-e794943461.html`
