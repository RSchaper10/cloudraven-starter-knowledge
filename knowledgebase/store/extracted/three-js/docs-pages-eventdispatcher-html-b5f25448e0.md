---
title: EventDispatcher - Three.js Docs
source_url: https://threejs.org/docs/pages/EventDispatcher.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:22.385502+00:00
kind: extracted-doc
---

# EventDispatcher - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/EventDispatcher.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:22.385502+00:00

Direct links in scope:

- https://threejs.org/docs/pages/EventDispatcher.html

Captured summary:

- EventDispatcher - Three.js Docs EventDispatcher Constructor new EventDispatcher () Methods .
- addEventListener ( type : string , listener : function ) Adds the given event listener to the given event type.
- listener The function that gets called when the event is fired.
- dispatchEvent ( event : Object ) Dispatches an event object.
- hasEventListener ( type : string , listener : function ) : boolean Returns true if the given event listener has been added to the given event type.

Extracted text:

EventDispatcher - Three.js Docs

EventDispatcher

Constructor

new

EventDispatcher

()

Methods

.

addEventListener

( type :

string

, listener :

function

)

Adds the given event listener to the given event type.

type

The type of event to listen to.

listener

The function that gets called when the event is fired.

.

dispatchEvent

( event :

Object

)

Dispatches an event object.

event

The event that gets fired.

.

hasEventListener

( type :

string

, listener :

function

)

: boolean

Returns

true

if the given event listener has been added to the given event type.

type

The type of event.

listener

The listener to check.

Returns:

Whether the given event listener has been added to the given event type.

.

removeEventListener

( type :

string

, listener :

function

)

Removes the given event listener from the given event type.

type

The type of event.

listener

The listener to remove.

Source

src/core/EventDispatcher.js
