---
title: Timer - Three.js Docs
source_url: https://threejs.org/docs/pages/Timer.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:26.228373+00:00
kind: extracted-doc
---

# Timer - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Timer.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:26.228373+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Timer.html

Captured summary:

- Timer - Three.js Docs Timer Constructor new Timer () Constructs a new timer.
- connect ( document : Document ) Connect the timer to the given document.Calling this method is not mandatory to use the timer but enables the usage of the Page Visibility API to avoid large time delta values.
- disconnect () Disconnects the timer from the DOM and also disables the usage of the Page Visibility API.
- dispose () Can be used to free all internal resources.
- Usually called when the timer instance isn't required anymore.

Extracted text:

Timer - Three.js Docs

Timer

Constructor

new

Timer

()

Constructs a new timer.

Methods

.

connect

( document :

Document

)

Connect the timer to the given document.Calling this method is not mandatory to use the timer but enables the usage of the Page Visibility API to avoid large time delta values.

document

The document.

.

disconnect

()

Disconnects the timer from the DOM and also disables the usage of the Page Visibility API.

.

dispose

()

Can be used to free all internal resources. Usually called when the timer instance isn't required anymore.

.

getDelta

()

: number

Returns the time delta in seconds.

Returns:

The time delta in second.

.

getElapsed

()

: number

Returns the elapsed time in seconds.

Returns:

The elapsed time in second.

.

getTimescale

()

: number

Returns the timescale.

Returns:

The timescale.

.

reset

()

:

Timer

Resets the time computation for the current simulation step.

Returns:

A reference to this timer.

.

setTimescale

( timescale :

number

)

:

Timer

Sets the given timescale which scale the time delta computation in

update()

.

timescale

The timescale to set.

Returns:

A reference to this timer.

.

update

( timestamp :

number

)

:

Timer

Updates the internal state of the timer. This method should be called once per simulation step and before you perform queries against the timer (e.g. via

getDelta()

).

timestamp

The current time in milliseconds. Can be obtained from the

requestAnimationFrame

callback argument. If not provided, the current time will be determined with

performance.now

.

Returns:

A reference to this timer.

Source

src/core/Timer.js
