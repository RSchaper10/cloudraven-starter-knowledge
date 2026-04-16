---
title: ScaleControl - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/ScaleControl/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:15.787353+00:00
kind: extracted-doc
---

# ScaleControl - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/ScaleControl/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:15.787353+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/ScaleControl/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/IControl/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/ScaleControlOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/ControlPosition/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/Unit/

Captured summary:

- ScaleControl - MapLibre GL JS Skip to content ScaleControl Defined in: ui/control/scale_control.ts:48 A ScaleControl control displays the ratio of a distance on the map to the corresponding distance on the ground.
- Example let scale = new ScaleControl ({ maxWidth : 80 , unit : 'imperial' }); map .
- setUnit ( 'metric' ); Implements IControl Constructors Constructor new ScaleControl ( options?
- : ScaleControlOptions ): ScaleControl Defined in: ui/control/scale_control.ts:56 Parameters Parameter Type Description options?
- ScaleControlOptions the control's options Returns ScaleControl Methods getDefaultPosition() getDefaultPosition (): ControlPosition Defined in: ui/control/scale_control.ts:60 Optionally provide a default position for this control.

Extracted text:

ScaleControl - MapLibre GL JS

Skip to content

ScaleControl

Defined in:

ui/control/scale_control.ts:48

A

ScaleControl

control displays the ratio of a distance on the map to the corresponding distance on the ground.

Example

let

scale

=

new

ScaleControl

({

maxWidth

:

80

,

unit

:

'imperial'

});

map

.

addControl

(

scale

);

scale

.

setUnit

(

'metric'

);

Implements

IControl

Constructors

Constructor

new ScaleControl

(

options?

:

ScaleControlOptions

):

ScaleControl

Defined in:

ui/control/scale_control.ts:56

Parameters

Parameter

Type

Description

options?

ScaleControlOptions

the control's options

Returns

ScaleControl

Methods

getDefaultPosition()

getDefaultPosition

():

ControlPosition

Defined in:

ui/control/scale_control.ts:60

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

ui/control/scale_control.ts:69

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

ui/control/scale_control.ts:80

Unregister a control on the map and give it a chance to detach event listeners and resources. This method is called by

Map.removeControl

internally.

Returns

void

Implementation of

IControl

.

onRemove

setUnit()

setUnit

(

unit

:

Unit

):

void

Defined in:

ui/control/scale_control.ts:91

Set the scale's unit of the distance

Parameters

Parameter

Type

Description

unit

Unit

Unit of the distance (

'imperial'

,

'metric'

or

'nautical'

).

Returns

void

Back to top
