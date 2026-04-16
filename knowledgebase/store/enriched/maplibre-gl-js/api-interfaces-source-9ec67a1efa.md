---
title: Source - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:30.173967+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# Source - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/Source/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- Source - MapLibre GL JS Skip to content Source Defined in: source/source.ts:31 The Source interface must be implemented by each source type, including "core" types ( vector , raster , video , etc.) and all custom, third-party types.
- Event data - Fired with {dataType: 'source', sourceDataType: 'metadata'} to indicate that any necessary metadata has been loaded so that it's okay to call loadTile ; and with {dataType: 'source', sourceDataType: 'content'} to indicate that the source data has changed, so that any current caches should be flushed.
- optional abortTile ( tile : Tile ): Promise < void > Defined in: source/source.ts:105 Allows to abort a tile loading.
- Parameters Parameter Type Description tile Tile The tile to abort Returns Promise < void > fire() fire ( event : Event ): unknown Defined in: source/source.ts:79 An ability to fire an event to all the listeners, see Evented Parameters Parameter Type Description event Event The event to fire Returns unknown hasTile()?

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-interfaces-source-9ec67a1efa.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-interfaces-source-9ec67a1efa.html`
