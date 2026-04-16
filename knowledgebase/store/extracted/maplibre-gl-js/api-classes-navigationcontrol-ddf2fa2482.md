---
title: NavigationControl - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/NavigationControl/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:14.779201+00:00
kind: extracted-doc
---

# NavigationControl - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/NavigationControl/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:14.779201+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/NavigationControl/
- https://maplibre.org/maplibre-gl-js/docs/examples/display-map-navigation-controls/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/IControl/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/NavigationControlOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Captured summary:

- NavigationControl - MapLibre GL JS Skip to content NavigationControl Defined in: ui/control/navigation_control.ts:52 A NavigationControl control contains zoom buttons and a compass.
- Example let nav = new NavigationControl (); map .
- addControl ( nav , 'top-left' ); See Display map navigation controls Implements IControl Constructors Constructor new NavigationControl ( options?
- : NavigationControlOptions ): NavigationControl Defined in: ui/control/navigation_control.ts:65 Parameters Parameter Type Description options?
- NavigationControlOptions the control's options Returns NavigationControl Methods onAdd() onAdd ( map : Map ): HTMLElement Defined in: ui/control/navigation_control.ts:117 Register a control on the map and give it a chance to register event listeners and resources.

Extracted text:

NavigationControl - MapLibre GL JS

Skip to content

NavigationControl

Defined in:

ui/control/navigation_control.ts:52

A

NavigationControl

control contains zoom buttons and a compass.

Example

let

nav

=

new

NavigationControl

();

map

.

addControl

(

nav

,

'top-left'

);

See

Display map navigation controls

Implements

IControl

Constructors

Constructor

new NavigationControl

(

options?

:

NavigationControlOptions

):

NavigationControl

Defined in:

ui/control/navigation_control.ts:65

Parameters

Parameter

Type

Description

options?

NavigationControlOptions

the control's options

Returns

NavigationControl

Methods

onAdd()

onAdd

(

map

:

Map

):

HTMLElement

Defined in:

ui/control/navigation_control.ts:117

Register a control on the map and give it a chance to register event listeners and resources. This method is called by

Map.addControl

internally.

Parameters

Parameter

Type

Description

map

Map

the Map this control will be added to

Returns

HTMLElement

The control's container element. This should be created by the control and returned by onAdd without being attached to the DOM: the map will insert the control's element into the DOM as necessary.

Implementation of

IControl

.

onAdd

onRemove()

onRemove

():

void

Defined in:

ui/control/navigation_control.ts:141

Unregister a control on the map and give it a chance to detach event listeners and resources. This method is called by

Map.removeControl

internally.

Returns

void

Implementation of

IControl

.

onRemove

Back to top
