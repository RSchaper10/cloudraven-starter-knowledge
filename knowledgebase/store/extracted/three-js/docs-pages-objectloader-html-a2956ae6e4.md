---
title: ObjectLoader - Three.js Docs
source_url: https://threejs.org/docs/pages/ObjectLoader.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:25.487678+00:00
kind: extracted-doc
---

# ObjectLoader - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/ObjectLoader.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:25.487678+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Loader.html
- https://threejs.org/docs/pages/ObjectLoader.html
- https://threejs.org/docs/pages/LoadingManager.html
- https://threejs.org/docs/pages/global.html
- https://threejs.org/docs/pages/Object3D.html

Captured summary:

- ObjectLoader - Three.js Docs Loader → ObjectLoader Constructor new ObjectLoader ( manager : LoadingManager ) Constructs a new object loader.
- load ( url : string , onLoad : function , onProgress : onProgressCallback , onError : onErrorCallback ) Starts loading from the given URL and pass the loaded 3D object to the onLoad() callback.
- url The path/URL of the file to be loaded.
- onLoad Executed when the loading process has been finished.
- onProgress Executed while the loading is in progress.

Extracted text:

ObjectLoader - Three.js Docs

Loader

→

ObjectLoader

Constructor

new

ObjectLoader

( manager :

LoadingManager

)

Constructs a new object loader.

manager

The loading manager.

Methods

.

load

( url :

string

, onLoad :

function

, onProgress :

onProgressCallback

, onError :

onErrorCallback

)

Starts loading from the given URL and pass the loaded 3D object to the

onLoad()

callback.

url

The path/URL of the file to be loaded. This can also be a data URI.

onLoad

Executed when the loading process has been finished.

onProgress

Executed while the loading is in progress.

onError

Executed when errors occur.

Overrides:

Loader#load

.

loadAsync

( url :

string

, onProgress :

onProgressCallback

)

: Promise.<

Object3D

>

(async)

Async version of

ObjectLoader#load

.

url

The path/URL of the file to be loaded. This can also be a data URI.

onProgress

Executed while the loading is in progress.

Overrides:

Loader#loadAsync

Returns:

A Promise that resolves with the loaded 3D object.

.

parse

( json :

Object

, onLoad :

onLoad

)

:

Object3D

Parses the given JSON. This is used internally by

ObjectLoader#load

but can also be used directly to parse a previously loaded JSON structure.

json

The serialized 3D object.

onLoad

Executed when all resources (e.g. textures) have been fully loaded.

Overrides:

Loader#parse

Returns:

The parsed 3D object.

.

parseAsync

( json :

Object

)

: Promise.<

Object3D

>

(async)

Async version of

ObjectLoader#parse

.

json

The serialized 3D object.

Returns:

A Promise that resolves with the parsed 3D object.

Source

src/loaders/ObjectLoader.js
