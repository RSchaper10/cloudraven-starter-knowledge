---
title: MapWheelEvent - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/MapWheelEvent/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:32.091233+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# MapWheelEvent - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/MapWheelEvent/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- MapWheelEvent - MapLibre GL JS Skip to content MapWheelEvent Defined in: ui/events.ts:642 MapWheelEvent is the event type for the wheel map event.
- Extends Event Accessors defaultPrevented Get Signature get defaultPrevented (): boolean Defined in: ui/events.ts:670 true if preventDefault has been called.
- Returns boolean Constructors Constructor new MapWheelEvent ( type : string , map : Map , originalEvent : WheelEvent ): MapWheelEvent Defined in: ui/events.ts:677 Parameters Parameter Type type string map Map originalEvent WheelEvent Returns MapWheelEvent Overrides Event.constructor Methods preventDefault() preventDefault (): void Defined in: ui/events.ts:663 Prevents subsequent default processing of the event by the map.
- Calling this method will prevent the behavior of ScrollZoomHandler .

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-mapwheelevent-d4e2f9bd2c.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-mapwheelevent-d4e2f9bd2c.html`
