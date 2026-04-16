---
title: MD2Loader - Three.js Docs
source_url: https://threejs.org/docs/pages/MD2Loader.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:27.055497+00:00
kind: extracted-doc
---

# MD2Loader - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/MD2Loader.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:27.055497+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Loader.html
- https://threejs.org/docs/pages/MD2Loader.html
- https://threejs.org/docs/pages/LoadingManager.html
- https://threejs.org/docs/pages/global.html
- https://threejs.org/docs/pages/BufferGeometry.html

Captured summary:

- MD2Loader - Three.js Docs Loader → MD2Loader Import MD2Loader is an addon, and must be imported explicitly, see Installation#Addons .
- import { MD2Loader } from 'three/addons/loaders/MD2Loader.js'; Constructor new MD2Loader ( manager : LoadingManager ) Constructs a new MD2 loader.
- load ( url : string , onLoad : function , onProgress : onProgressCallback , onError : onErrorCallback ) Starts loading from the given URL and passes the loaded MD2 asset to the onLoad() callback.
- url The path/URL of the file to be loaded.
- onLoad Executed when the loading process has been finished.

Extracted text:

MD2Loader - Three.js Docs

Loader

→

MD2Loader

Import

MD2Loader

is an addon, and must be imported explicitly, see

Installation#Addons

.

import { MD2Loader } from 'three/addons/loaders/MD2Loader.js';

Constructor

new

MD2Loader

( manager :

LoadingManager

)

Constructs a new MD2 loader.

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

Starts loading from the given URL and passes the loaded MD2 asset to the

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

parse

( buffer :

ArrayBuffer

)

:

BufferGeometry

Parses the given MD2 data and returns a geometry.

buffer

The raw MD2 data as an array buffer.

Overrides:

Loader#parse

Returns:

The parsed geometry data.

Source

examples/jsm/loaders/MD2Loader.js
