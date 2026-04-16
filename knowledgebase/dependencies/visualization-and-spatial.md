# Visualization and Spatial

This brief covers MapLibre GL JS, Apache ECharts, and Three.js.

## MapLibre GL JS

Role:

- Browser-based interactive mapping built on an open-source map rendering stack.

Priority docs:

- https://maplibre.org/maplibre-gl-js/docs/API/
- https://maplibre.org/maplibre-gl-js/docs/examples/

Why it fits CloudRaven:

- Useful for logistics, coverage maps, asset visualization, location intelligence, and any spatial interface that should stay open and portable.

Production cautions:

- document tile source, geocoding, and style hosting choices early
- map performance and mobile interaction quality should be tested with real datasets

Suggested tags:

- `maps`
- `geospatial`
- `maplibre`

## Apache ECharts

Role:

- Flexible charting layer for dashboards, reporting, and data storytelling.

Priority docs:

- https://echarts.apache.org/handbook/en/get-started/

Why it fits CloudRaven:

- Strong fit for operational dashboards, analytics products, and generated reporting surfaces.

Production cautions:

- chart choices should map to user decisions, not just data availability
- define responsive behavior and export behavior early if dashboards may become decks or PDFs

Suggested tags:

- `charts`
- `analytics`
- `dashboards`

## Three.js

Role:

- 3D scene and rendering library for immersive or spatially expressive web interfaces.

Priority docs:

- https://threejs.org/docs/
- https://threejs.org/manual/en/creating-a-scene.html

Why it fits CloudRaven:

- Useful when a prototype needs physical object visualization, product interaction, or high-impact storytelling beyond standard dashboards.

Production cautions:

- reserve Three.js for workflows that truly benefit from 3D
- performance budgets, accessibility fallbacks, and interaction design need to be explicit

Suggested tags:

- `3d`
- `threejs`
- `interactive-visuals`
