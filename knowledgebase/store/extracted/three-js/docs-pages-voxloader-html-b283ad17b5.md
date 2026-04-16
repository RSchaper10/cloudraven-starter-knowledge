---
title: VOXLoader - Three.js Docs
source_url: https://threejs.org/docs/pages/VOXLoader.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:37.434597+00:00
kind: extracted-doc
---

# VOXLoader - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/VOXLoader.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:37.434597+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Loader.html
- https://threejs.org/docs/pages/VOXLoader.html
- https://threejs.org/docs/pages/global.html

Captured summary:

- VOXLoader - Three.js Docs Loader → VOXLoader Import VOXLoader is an addon, and must be imported explicitly, see Installation#Addons .
- import { VOXLoader } from 'three/addons/loaders/VOXLoader.js'; Constructor new VOXLoader () Methods .
- load ( url : string , onLoad : function , onProgress : onProgressCallback , onError : onErrorCallback ) Starts loading from the given URL and passes the loaded VOX asset to the onLoad() callback.
- url The path/URL of the file to be loaded.
- onLoad Executed when the loading process has been finished.

Extracted text:

VOXLoader - Three.js Docs

Loader

→

VOXLoader

Import

VOXLoader

is an addon, and must be imported explicitly, see

Installation#Addons

.

import { VOXLoader } from 'three/addons/loaders/VOXLoader.js';

Constructor

new

VOXLoader

()

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

Starts loading from the given URL and passes the loaded VOX asset to the

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

: Object

Parses the given VOX data and returns the result object.

buffer

The raw VOX data as an array buffer.

Overrides:

Loader#parse

Returns:

The parsed VOX data with properties: chunks, scene.

Source

examples/jsm/loaders/VOXLoader.js
