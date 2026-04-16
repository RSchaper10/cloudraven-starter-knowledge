# AttributionControl - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/AttributionControl/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-15T19:44:56.200422+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/AttributionControl/
- https://maplibre.org/maplibre-gl-js/docs/examples/change-the-default-position-for-attribution/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/IControl/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/AttributionControlOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/ControlPosition/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Captured summary:

- AttributionControl - MapLibre GL JS Skip to content AttributionControl Defined in: ui/control/attribution_control.ts:40 An AttributionControl control presents the map's attribution information.
- By default, the attribution control is expanded (regardless of map width).
- Example let map = new Map ({ attributionControl : false }) .
- addControl ( new AttributionControl ({ compact : true })); See Change the default position for attribution Implements IControl Constructors Constructor new AttributionControl ( options?
- : AttributionControlOptions ): AttributionControl Defined in: ui/control/attribution_control.ts:55 Parameters Parameter Type Default value Description options AttributionControlOptions defaultAttributionControlOptions the attribution options Returns AttributionControl Methods getDefaultPosition() getDefaultPosition (): ControlPosition Defined in: ui/control/attribution_control.ts:59 Optionally provide a default position for this control.

Extracted text:

AttributionControl - MapLibre GL JS

Skip to content

AttributionControl

Defined in:

ui/control/attribution_control.ts:40

An

AttributionControl

control presents the map's attribution information. By default, the attribution control is expanded (regardless of map width).

Example

let

map

=

new

Map

({

attributionControl

:

false

})

.

addControl

(

new

AttributionControl

({

compact

:

true

}));

See

Change the default position for attribution

Implements

IControl

Constructors

Constructor

new AttributionControl

(

options?

:

AttributionControlOptions

):

AttributionControl

Defined in:

ui/control/attribution_control.ts:55

Parameters

Parameter

Type

Default value

Description

options

AttributionControlOptions

defaultAttributionControlOptions

the attribution options

Returns

AttributionControl

Methods

getDefaultPosition()

getDefaultPosition

():

ControlPosition

Defined in:

ui/control/attribution_control.ts:59

Optionally provide a default position for this control. If this method is implemented and

Map.addControl

is called without the

position

parameter, the value returned by getDefaultPosition will be used as the control's position.

Returns

ControlPosition

a control position, one of the values valid in addControl.

Implementation of

IControl

.

getDefaultPosition

onAdd()

onAdd

(

map

:

Map

):

HTMLElement

Defined in:

ui/control/attribution_control.ts:64

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

ui/control/attribution_control.ts:86

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
