---
title: CooperativeGesturesHandler - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/CooperativeGesturesHandler/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:21.535964+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# CooperativeGesturesHandler - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/CooperativeGesturesHandler/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- CooperativeGesturesHandler - MapLibre GL JS Skip to content CooperativeGesturesHandler Defined in: ui/handler/cooperative_gestures.ts:27 A CooperativeGestureHandler is a control that adds cooperative gesture info when user tries to zoom in/out.
- When the CooperativeGestureHandler blocks a gesture, it will emit a cooperativegestureprevented event.
- Example const map = new Map ({ cooperativeGestures : true }); See Example: cooperative gestures Implements Handler Methods isActive() isActive (): boolean Defined in: ui/handler/cooperative_gestures.ts:42 This is used to indicate if the handler is currently active or not.
- In case a handler is active, it will block other handlers from getting the relevant events.

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-cooperativegestureshandler-3f852edcb9.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-cooperativegestureshandler-3f852edcb9.html`
