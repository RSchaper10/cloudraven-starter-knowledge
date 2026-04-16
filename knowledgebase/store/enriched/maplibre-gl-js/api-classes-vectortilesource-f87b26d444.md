---
title: VectorTileSource - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/VectorTileSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:28.770729+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# VectorTileSource - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/VectorTileSource/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- VectorTileSource - MapLibre GL JS Skip to content VectorTileSource Defined in: source/vector_tile_source.ts:65 A source containing vector tiles in Maplibre Vector Tile format or Mapbox Vector Tile format .
- (See the Style Specification for detailed documentation of options.) Examples map .
- addSource ( 'some id' , { type : 'vector' , url : 'https://demotiles.maplibre.org/tiles/tiles.json' }); map .
- addSource ( 'some id' , { type : 'vector' , tiles : [ 'https://d25uarhxywzl1j.cloudfront.net/v0.1/{z}/{x}/{y}.mvt' ], minzoom : 6 , maxzoom : 14 }); map .

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-vectortilesource-f87b26d444.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-vectortilesource-f87b26d444.html`
