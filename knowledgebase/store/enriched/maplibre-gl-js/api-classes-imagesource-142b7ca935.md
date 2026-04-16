---
title: ImageSource - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/ImageSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:27.779839+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# ImageSource - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/ImageSource/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- ImageSource - MapLibre GL JS Skip to content ImageSource Defined in: source/image_source.ts:101 A data source containing an image.
- (See the Style Specification for detailed documentation of options.) Example // add to map map .
- addSource ( 'some id' , { type : 'image' , url : 'https://www.maplibre.org/images/foo.png' , coordinates : [ [ - 76.54 , 39.18 ], [ - 76.52 , 39.18 ], [ - 76.52 , 39.17 ], [ - 76.54 , 39.17 ] ] }); // update coordinates let mySource = map .
- setCoordinates ([ [ - 76.54335737228394 , 39.18579907229748 ], [ - 76.52803659439087 , 39.1838364847587 ], [ - 76.5295386314392 , 39.17683392507606 ], [ - 76.54520273208618 , 39.17876344106642 ] ]); // update url and coordinates simultaneously mySource .

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-imagesource-142b7ca935.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-imagesource-142b7ca935.html`
