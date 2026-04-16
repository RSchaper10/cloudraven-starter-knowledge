---
title: TerrainControl - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/TerrainControl/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:16.278730+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# TerrainControl - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/TerrainControl/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- TerrainControl - MapLibre GL JS Skip to content TerrainControl Defined in: ui/control/terrain_control.ts:24 A TerrainControl control contains a button for turning the terrain on and off.
- Example let map = new Map ({ TerrainControl : false }) .
- addControl ( new TerrainControl ({ source : "terrain" })); See 3D Terrain Create a Heatmap layer on a globe with terrain elevation Display a hybrid satellite map with terrain elevation Sky, Fog, Terrain Implements IControl Constructors Constructor new TerrainControl ( options : TerrainSpecification ): TerrainControl Defined in: ui/control/terrain_control.ts:33 Parameters Parameter Type Description options TerrainSpecification the control's options Returns TerrainControl Methods onAdd() onAdd ( map : Map ): HTMLElement Defined in: ui/control/terrain_control.ts:38 Register a control on the map and give it a chance to register event listeners and resources.
- This method is called by Map.addControl internally.

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-terraincontrol-7cc6471446.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-terraincontrol-7cc6471446.html`
