---
title: GeoJSONSource - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/GeoJSONSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:27.274351+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# GeoJSONSource - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/GeoJSONSource/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- GeoJSONSource - MapLibre GL JS Skip to content GeoJSONSource Defined in: source/geojson_source.ts:124 A source containing GeoJSON.
- (See the Style Specification for detailed documentation of options.) Examples map .
- addSource ( 'some id' , { type : 'geojson' , data : 'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_10m_ports.geojson' }); map .
- addSource ( 'some id' , { type : 'geojson' , data : { "type" : "FeatureCollection" , "features" : [{ "type" : "Feature" , "properties" : {}, "geometry" : { "type" : "Point" , "coordinates" : [ - 76.53063297271729 , 39.18174077994108 ] } }] } }); map .

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-geojsonsource-311244f730.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-geojsonsource-311244f730.html`
