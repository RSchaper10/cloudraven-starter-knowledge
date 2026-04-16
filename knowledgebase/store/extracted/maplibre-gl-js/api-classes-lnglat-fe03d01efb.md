---
title: LngLat - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLat/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:17.247394+00:00
kind: extracted-doc
---

# LngLat - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLat/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:17.247394+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLat/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatLike/
- https://maplibre.org/maplibre-gl-js/docs/examples/get-coordinates-of-the-mouse-pointer/

Captured summary:

- LngLat - MapLibre GL JS Skip to content LngLat Defined in: geo/lng_lat.ts:51 A LngLat object represents a given longitude and latitude coordinate, measured in degrees.
- These coordinates are based on the WGS84 (EPSG:4326) standard .
- MapLibre GL JS uses longitude, latitude coordinate order (as opposed to latitude, longitude) to match the GeoJSON specification .
- Note that any MapLibre GL JS method that accepts a LngLat object as an argument or option can also accept an Array of two numbers and will perform an implicit conversion.
- This flexible type is documented as LngLatLike .

Extracted text:

LngLat - MapLibre GL JS

Skip to content

LngLat

Defined in:

geo/lng_lat.ts:51

A

LngLat

object represents a given longitude and latitude coordinate, measured in degrees. These coordinates are based on the

WGS84 (EPSG:4326) standard

.

MapLibre GL JS uses longitude, latitude coordinate order (as opposed to latitude, longitude) to match the

GeoJSON specification

.

Note that any MapLibre GL JS method that accepts a

LngLat

object as an argument or option can also accept an

Array

of two numbers and will perform an implicit conversion. This flexible type is documented as

LngLatLike

.

Example

let

ll

=

new

LngLat

(

-

123.9749

,

40.7736

);

ll

.

lng

;

// = -123.9749

See

Get coordinates of the mouse pointer

Constructors

Constructor

new LngLat

(

lng

:

number

,

lat

:

number

):

LngLat

Defined in:

geo/lng_lat.ts:66

Parameters

Parameter

Type

Description

lng

number

Longitude, measured in degrees.

lat

number

Latitude, measured in degrees.

Returns

LngLat

Methods

distanceTo()

distanceTo

(

lngLat

:

LngLat

):

number

Defined in:

geo/lng_lat.ts:133

Returns the approximate distance between a pair of coordinates in meters Uses the Haversine Formula (from R.W. Sinnott, "Virtues of the Haversine", Sky and Telescope, vol. 68, no. 2, 1984, p. 159)

Parameters

Parameter

Type

Description

lngLat

LngLat

coordinates to compute the distance to

Returns

number

Distance in meters between the two coordinates.

Example

let

new_york

=

new

LngLat

(

-

74.0060

,

40.7128

);

let

los_angeles

=

new

LngLat

(

-

118.2437

,

34.0522

);

new_york

.

distanceTo

(

los_angeles

);

// = 3935751.690893987, "true distance" using a non-spherical approximation is ~3966km

toArray()

toArray

(): [

number

,

number

]

Defined in:

geo/lng_lat.ts:102

Returns the coordinates represented as an array of two numbers.

Returns

[

number

,

number

]

The coordinates represented as an array of longitude and latitude.

Example

let

ll

=

new

LngLat

(

-

73.9749

,

40.7736

);

ll

.

toArray

();

// = [-73.9749, 40.7736]

toString()

toString

():

string

Defined in:

geo/lng_lat.ts:116

Returns the coordinates represent as a string.

Returns

string

The coordinates represented as a string of the format

'LngLat(lng, lat)'

.

Example

let

ll

=

new

LngLat

(

-

73.9749

,

40.7736

);

ll

.

toString

();

// = "LngLat(-73.9749, 40.7736)"

wrap()

wrap

():

LngLat

Defined in:

geo/lng_lat.ts:88

Returns a new

LngLat

object whose longitude is wrapped to the range (-180, 180).

Returns

LngLat

The wrapped

LngLat

object.

Example

let

ll

=

new

LngLat

(

286.0251

,

40.7736

);

let

wrapped

=

ll

.

wrap

();

wrapped

.

lng

;

// = -73.9749

convert()

static

convert

(

input

:

LngLatLike

):

LngLat

Defined in:

geo/lng_lat.ts:157

Converts an array of two numbers or an object with

lng

and

lat

or

lon

and

lat

properties to a

LngLat

object.

If a

LngLat

object is passed in, the function returns it unchanged.

Parameters

Parameter

Type

Description

input

LngLatLike

An array of two numbers or object to convert, or a

LngLat

object to return.

Returns

LngLat

A new

LngLat

object, if a conversion occurred, or the original

LngLat

object.

Example

let

arr

=

[

-

73.9749

,

40.7736

];

let

ll

=

LngLat

.

convert

(

arr

);

ll

;

// = LngLat {lng: -73.9749, lat: 40.7736}

Properties

lat

lat

:

number

Defined in:

geo/lng_lat.ts:60

Latitude, measured in degrees.

lng

lng

:

number

Defined in:

geo/lng_lat.ts:55

Longitude, measured in degrees.

Back to top
