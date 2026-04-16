---
title: AnimationMixer - Three.js Docs
source_url: https://threejs.org/docs/pages/AnimationMixer.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:20.340601+00:00
kind: extracted-doc
---

# AnimationMixer - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/AnimationMixer.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:20.340601+00:00

Direct links in scope:

- https://threejs.org/docs/pages/AnimationMixer.html
- https://threejs.org/docs/pages/Object3D.html
- https://threejs.org/docs/pages/AnimationClip.html
- https://threejs.org/docs/pages/global.html
- https://threejs.org/docs/pages/AnimationAction.html
- https://threejs.org/docs/pages/Clock.html
- https://threejs.org/docs/pages/Timer.html

Captured summary:

- AnimationMixer - Three.js Docs AnimationMixer Constructor new AnimationMixer ( root : Object3D ) Constructs a new animation mixer.
- root The object whose animations shall be played by this mixer.
- time : number The global mixer time (in seconds; starting with 0 on the mixer's creation).
- timeScale : number A scaling factor for the global time.
- Note: Setting this member to 0 and later back to 1 is a possibility to pause/unpause all actions that are controlled by this mixer.

Extracted text:

AnimationMixer - Three.js Docs

AnimationMixer

Constructor

new

AnimationMixer

( root :

Object3D

)

Constructs a new animation mixer.

root

The object whose animations shall be played by this mixer.

Properties

.

time

: number

The global mixer time (in seconds; starting with

0

on the mixer's creation).

Default is

0

.

.

timeScale

: number

A scaling factor for the global time.

Note: Setting this member to

0

and later back to

1

is a possibility to pause/unpause all actions that are controlled by this mixer.

Default is

1

.

Methods

.

clipAction

( clip :

AnimationClip

| string

, optionalRoot :

Object3D

, blendMode :

NormalAnimationBlendMode

|

AdditiveAnimationBlendMode

)

:

AnimationAction

Returns an instance of

AnimationAction

for the passed clip.

If an action fitting the clip and root parameters doesn't yet exist, it will be created by this method. Calling this method several times with the same clip and root parameters always returns the same action.

clip

An animation clip or alternatively the name of the animation clip.

optionalRoot

An alternative root object.

blendMode

The blend mode.

Returns:

The animation action.

.

existingAction

( clip :

AnimationClip

| string

, optionalRoot :

Object3D

)

:

AnimationAction

Returns an existing animation action for the passed clip.

clip

An animation clip or alternatively the name of the animation clip.

optionalRoot

An alternative root object.

Returns:

The animation action. Returns

null

if no action was found.

.

getRoot

()

:

Object3D

Returns this mixer's root object.

Returns:

The mixer's root object.

.

setTime

( time :

number

)

:

AnimationMixer

Sets the global mixer to a specific time and updates the animation accordingly.

This is useful when you need to jump to an exact time in an animation. The input parameter will be scaled by

AnimationMixer#timeScale

time

The time to set in seconds.

Returns:

A reference to this animation mixer.

.

stopAllAction

()

:

AnimationMixer

Deactivates all previously scheduled actions on this mixer.

Returns:

A reference to this animation mixer.

.

uncacheAction

( clip :

AnimationClip

| string

, optionalRoot :

Object3D

)

Deallocates all memory resources for an action. The action is identified by the given clip and an optional root object. Before using this method make sure to call

AnimationAction#stop

to deactivate the action.

clip

An animation clip or alternatively the name of the animation clip.

optionalRoot

An alternative root object.

.

uncacheClip

( clip :

AnimationClip

)

Deallocates all memory resources for a clip. Before using this method make sure to call

AnimationAction#stop

for all related actions.

clip

The clip to uncache.

.

uncacheRoot

( root :

Object3D

)

Deallocates all memory resources for a root object. Before using this method make sure to call

AnimationAction#stop

for all related actions or alternatively

AnimationMixer#stopAllAction

when the mixer operates on a single root.

root

The root object to uncache.

.

update

( deltaTime :

number

)

:

AnimationMixer

Advances the global mixer time and updates the animation.

This is usually done in the render loop by passing the delta time from

Clock

or

Timer

.

deltaTime

The delta time in seconds.

Returns:

A reference to this animation mixer.

Source

src/animation/AnimationMixer.js
