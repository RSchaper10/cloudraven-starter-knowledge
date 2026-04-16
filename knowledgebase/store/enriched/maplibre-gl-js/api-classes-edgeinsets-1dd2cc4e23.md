---
title: EdgeInsets - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/EdgeInsets/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:16.745847+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# EdgeInsets - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/EdgeInsets/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- EdgeInsets - MapLibre GL JS Skip to content EdgeInsets Defined in: geo/edge_insets.ts:12 An EdgeInset object represents screen space padding applied to the edges of the viewport.
- This shifts the apparent center or the vanishing point of the map.
- This is useful for adding floating UI elements on top of the map and having the vanishing point shift as UI elements resize.
- Methods getCenter() getCenter ( width : number , height : number ): Point Defined in: geo/edge_insets.ts:70 Utility method that computes the new apparent center or vanishing point after applying insets.

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-edgeinsets-1dd2cc4e23.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-edgeinsets-1dd2cc4e23.html`
