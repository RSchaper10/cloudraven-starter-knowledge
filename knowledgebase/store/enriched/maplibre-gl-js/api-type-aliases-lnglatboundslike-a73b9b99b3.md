---
title: LngLatBoundsLike - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatBoundsLike/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:18.954084+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# LngLatBoundsLike - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatBoundsLike/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- LngLatBoundsLike - MapLibre GL JS Skip to content LngLatBoundsLike LngLatBoundsLike = LngLatBounds | [ LngLatLike , LngLatLike ] | [ number , number , number , number ] Defined in: geo/lng_lat_bounds.ts:21 A LngLatBounds object, an array of LngLatLike objects in [sw, ne] order, or an array of numbers in [west, south, east, north] order.
- Example let v1 = new LngLatBounds ( new LngLat ( - 73.9876 , 40.7661 ), new LngLat ( - 73.9397 , 40.8002 ) ); let v2 = new LngLatBounds ([ - 73.9876 , 40.7661 ], [ - 73.9397 , 40.8002 ]) let v3 = [[ - 73.9876 , 40.7661 ], [ - 73.9397 , 40.8002 ]]; Back to top

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-type-aliases-lnglatboundslike-a73b9b99b3.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-type-aliases-lnglatboundslike-a73b9b99b3.html`
