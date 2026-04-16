---
title: MercatorCoordinate - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/MercatorCoordinate/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:18.461407+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# MercatorCoordinate - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MercatorCoordinate/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- MercatorCoordinate - MapLibre GL JS Skip to content MercatorCoordinate Defined in: geo/mercator_coordinate.ts:80 A MercatorCoordinate object represents a projected three dimensional position.
- MercatorCoordinate uses the web mercator projection ( EPSG:3857 ) with slightly different units: the size of 1 unit is the width of the projected world instead of the "mercator meter" the origin of the coordinate space is at the north-west corner instead of the middle For example, MercatorCoordinate(0, 0, 0) is the north-west corner of the mercator world and MercatorCoordinate(1, 1, 0) is the south-east corner.
- If you are familiar with vector tiles it may be helpful to think of the coordinate space as the 0/0/0 tile with an extent of 1 .
- The z dimension of MercatorCoordinate is conformal.

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-mercatorcoordinate-fd8fe218f9.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-mercatorcoordinate-fd8fe218f9.html`
