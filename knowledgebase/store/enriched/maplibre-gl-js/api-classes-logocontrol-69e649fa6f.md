---
title: LogoControl - MapLibre GL JS | CloudRaven Enrichment
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/LogoControl/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:13.698240+00:00
kind: enriched-doc
tags: maps, geospatial, maplibre
---

# LogoControl - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/LogoControl/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- LogoControl - MapLibre GL JS Skip to content LogoControl Defined in: ui/control/logo_control.ts:27 A LogoControl is a control that adds the watermark.
- addControl ( new LogoControl ({ compact : false })); Implements IControl Constructors Constructor new LogoControl ( options?
- : LogoControlOptions ): LogoControl Defined in: ui/control/logo_control.ts:36 Parameters Parameter Type Description options LogoControlOptions the control's options Returns LogoControl Methods getDefaultPosition() getDefaultPosition (): ControlPosition Defined in: ui/control/logo_control.ts:40 Optionally provide a default position for this control.
- If this method is implemented and Map.addControl is called without the position parameter, the value returned by getDefaultPosition will be used as the control's position.

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-logocontrol-69e649fa6f.md`
- Raw source: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-logocontrol-69e649fa6f.html`
