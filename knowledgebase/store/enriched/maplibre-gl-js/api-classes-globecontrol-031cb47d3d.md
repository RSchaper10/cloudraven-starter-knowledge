# GlobeControl - MapLibre GL JS | CloudRaven Enrichment

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/GlobeControl/

Dependency:

- MapLibre GL JS

Collection scope:

- Collect API entry points and examples for interactive map work.

What this page is useful for:

- GlobeControl - MapLibre GL JS Skip to content GlobeControl Defined in: ui/control/globe_control.ts:20 A GlobeControl control contains a button for toggling the map projection between "mercator" and "globe".
- addControl ( new GlobeControl ()); See Display a globe with a fill extrusion layer Sky, Fog, Terrain Implements IControl Methods onAdd() onAdd ( map : Map ): HTMLElement Defined in: ui/control/globe_control.ts:26 Register a control on the map and give it a chance to register event listeners and resources.
- This method is called by Map.addControl internally.
- Parameters Parameter Type Description map Map the Map this control will be added to Returns HTMLElement The control's container element.

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

- Extracted page: `knowledgebase/store/extracted/maplibre-gl-js/api-classes-globecontrol-031cb47d3d.md`
- Raw HTML: `knowledgebase/store/raw_html/maplibre-gl-js/api-classes-globecontrol-031cb47d3d.html`
