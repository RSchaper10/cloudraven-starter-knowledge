---
title: RasterDEMTileSource - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/RasterDEMTileSource/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:28.302388+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# RasterDEMTileSource - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/RasterDEMTileSource/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- RasterDEMTileSource - MapLibre GL JS Skip to content RasterDEMTileSource Defined in: source/raster_dem_tile_source.ts:37 A source containing raster DEM tiles (See the Style Specification for detailed documentation of options.) This source can be used to show hillshading and 3D terrain Example map .
- addSource ( 'raster-dem-source' , { type : 'raster-dem' , url : 'https://demotiles.maplibre.org/terrain-tiles/tiles.json' , tileSize : 256 }); See 3D Terrain Extends RasterTileSource Implements Source Methods abortTile() abortTile ( tile : Tile ): Promise < void > Defined in: source/raster_tile_source.ts:219 Allows to abort a tile loading.
- Parameters Parameter Type Description tile Tile The tile to abort Returns Promise < void > Implementation of Source .
- abortTile Inherited from RasterTileSource .

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-rasterdemtilesource-24924b3809.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-rasterdemtilesource-24924b3809.html`
