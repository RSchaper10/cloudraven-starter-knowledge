---
title: Clock - Three.js Docs
source_url: https://threejs.org/docs/pages/Clock.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:25.862283+00:00
kind: extracted-doc
---

# Clock - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Clock.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:25.862283+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Clock.html

Captured summary:

- Clock - Three.js Docs Clock Constructor new Clock ( autoStart : boolean ) Constructs a new clock.
- autoStart Whether to automatically start the clock when getDelta() is called for the first time.
- autoStart : boolean If set to true , the clock starts automatically when getDelta() is called for the first time.
- elapsedTime : number Keeps track of the total time that the clock has been running.
- oldTime : number Holds the time at which the clock's start() , getElapsedTime() or getDelta() methods were last called.

Extracted text:

Clock - Three.js Docs

Clock

Constructor

new

Clock

( autoStart :

boolean

)

Constructs a new clock.

autoStart

Whether to automatically start the clock when

getDelta()

is called for the first time.

Default is

true

.

Deprecated:

since r183.

Properties

.

autoStart

: boolean

If set to

true

, the clock starts automatically when

getDelta()

is called for the first time.

Default is

true

.

.

elapsedTime

: number

Keeps track of the total time that the clock has been running.

Default is

0

.

.

oldTime

: number

Holds the time at which the clock's

start()

,

getElapsedTime()

or

getDelta()

methods were last called.

Default is

0

.

.

running

: boolean

Whether the clock is running or not.

Default is

true

.

.

startTime

: number

Holds the time at which the clock's

start()

method was last called.

Default is

0

.

Methods

.

getDelta

()

: number

Returns the delta time in seconds.

Returns:

The delta time.

.

getElapsedTime

()

: number

Returns the elapsed time in seconds.

Returns:

The elapsed time.

.

start

()

Starts the clock. When

autoStart

is set to

true

, the method is automatically called by the class.

.

stop

()

Stops the clock.

Source

src/core/Clock.js
