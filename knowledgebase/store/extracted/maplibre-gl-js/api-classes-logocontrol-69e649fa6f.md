---
title: LogoControl - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/LogoControl/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:13.698240+00:00
kind: extracted-doc
---

# LogoControl - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/LogoControl/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:13.698240+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/LogoControl/
- https://maplibre.org/maplibre-gl-js/docs/API/interfaces/IControl/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LogoControlOptions/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/ControlPosition/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/

Captured summary:

- LogoControl - MapLibre GL JS Skip to content LogoControl Defined in: ui/control/logo_control.ts:27 A LogoControl is a control that adds the watermark.
- addControl ( new LogoControl ({ compact : false })); Implements IControl Constructors Constructor new LogoControl ( options?
- : LogoControlOptions ): LogoControl Defined in: ui/control/logo_control.ts:36 Parameters Parameter Type Description options LogoControlOptions the control's options Returns LogoControl Methods getDefaultPosition() getDefaultPosition (): ControlPosition Defined in: ui/control/logo_control.ts:40 Optionally provide a default position for this control.
- If this method is implemented and Map.addControl is called without the position parameter, the value returned by getDefaultPosition will be used as the control's position.
- Returns ControlPosition a control position, one of the values valid in addControl.

Extracted text:

LogoControl - MapLibre GL JS

Skip to content

LogoControl

Defined in:

ui/control/logo_control.ts:27

A

LogoControl

is a control that adds the watermark.

Example

map

.

addControl

(

new

LogoControl

({

compact

:

false

}));

Implements

IControl

Constructors

Constructor

new LogoControl

(

options?

:

LogoControlOptions

):

LogoControl

Defined in:

ui/control/logo_control.ts:36

Parameters

Parameter

Type

Description

options

LogoControlOptions

the control's options

Returns

LogoControl

Methods

getDefaultPosition()

getDefaultPosition

():

ControlPosition

Defined in:

ui/control/logo_control.ts:40

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

ui/control/logo_control.ts:45

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

ui/control/logo_control.ts:65

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
