---
title: MapTouchEvent - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/MapTouchEvent/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:31.628159+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# MapTouchEvent - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapTouchEvent/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- MapTouchEvent - MapLibre GL JS Skip to content MapTouchEvent Defined in: ui/events.ts:563 MapTouchEvent is the event type for touch-related map events.
- Extends Event Implements MapLibreEvent < TouchEvent > Accessors defaultPrevented Get Signature get defaultPrevented (): boolean Defined in: ui/events.ts:618 true if preventDefault has been called.
- Returns boolean Methods preventDefault() preventDefault (): void Defined in: ui/events.ts:611 Prevents subsequent default processing of the event by the map.
- Calling this method will prevent the following default map behaviors: On touchstart events, the behavior of DragPanHandler On touchstart events, the behavior of TwoFingersTouchZoomRotateHandler Returns void Properties lngLat lngLat : LngLat Defined in: ui/events.ts:582 The geographic location on the map of the center of the touch event points.

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-maptouchevent-e91b7659a7.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-maptouchevent-e91b7659a7.html`
