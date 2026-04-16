---
title: Popup - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/Popup/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:15.302838+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# Popup - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/Popup/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- Popup - MapLibre GL JS Skip to content Popup Defined in: ui/popup.ts:178 A popup component.
- Examples Create a popup let popup = new Popup (); // Set an event listener that will fire // any time the popup is opened popup .
- log ( 'popup was opened' ); }); Create a popup let popup = new Popup (); // Set an event listener that will fire // any time the popup is closed popup .
- log ( 'popup was closed' ); }); let markerHeight = 50 , markerRadius = 10 , linearOffset = 25 ; let popupOffsets = { 'top' : [ 0 , 0 ], 'top-left' : [ 0 , 0 ], 'top-right' : [ 0 , 0 ], 'bottom' : [ 0 , - markerHeight ], 'bottom-left' : [ linearOffset , ( markerHeight - markerRadius + linearOffset ) * - 1 ], 'bottom-right' : [ - linearOffset , ( markerHeight - markerRadius + linearOffset ) * - 1 ], 'left' : [ markerRadius , ( markerHeight - markerRadius ) * - 1 ], 'right' : [ - markerRadius , ( markerHeight - markerRadius ) * - 1 ] }; let popup = new Popup ({ offset : popupOffsets , className : 'my-class' }) .

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-popup-d1c7f77023.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-popup-d1c7f77023.html`
