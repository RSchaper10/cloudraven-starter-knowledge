---
title: LngLatBounds - MapLibre GL JS
source_url: https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLatBounds/
target_id: maplibre-gl-js
dependency: MapLibre GL JS
collected_at: 2026-04-16T03:22:17.907469+00:00
kind: extracted-doc
---

# LngLatBounds - MapLibre GL JS

Source URL:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLatBounds/

Dependency:

- MapLibre GL JS

Collected at:

- 2026-04-16T03:22:17.907469+00:00

Direct links in scope:

- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLatBounds/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatLike/
- https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/LngLatBoundsLike/
- https://maplibre.org/maplibre-gl-js/docs/examples/fit-to-the-bounds-of-a-linestring/
- https://maplibre.org/maplibre-gl-js/docs/API/classes/LngLat/

Captured summary:

- LngLatBounds - MapLibre GL JS Skip to content LngLatBounds Defined in: geo/lng_lat_bounds.ts:43 A LngLatBounds object represents a geographical bounding box, defined by its southwest and northeast points in longitude and latitude.
- If no arguments are provided to the constructor, a null bounding box is created.
- Note that any MapLibre GL method that accepts a LngLatBounds object as an argument or option can also accept an Array of two LngLatLike constructs and will perform an implicit conversion.
- This flexible type is documented as LngLatBoundsLike .
- Example let sw = new LngLat ( - 73.9876 , 40.7661 ); let ne = new LngLat ( - 73.9397 , 40.8002 ); let llb = new LngLatBounds ( sw , ne ); See Fit to the bounds of a LineString Constructors Constructor new LngLatBounds ( sw?

Extracted text:

LngLatBounds - MapLibre GL JS

Skip to content

LngLatBounds

Defined in:

geo/lng_lat_bounds.ts:43

A

LngLatBounds

object represents a geographical bounding box, defined by its southwest and northeast points in longitude and latitude.

If no arguments are provided to the constructor, a

null

bounding box is created.

Note that any MapLibre GL method that accepts a

LngLatBounds

object as an argument or option can also accept an

Array

of two

LngLatLike

constructs and will perform an implicit conversion. This flexible type is documented as

LngLatBoundsLike

.

Example

let

sw

=

new

LngLat

(

-

73.9876

,

40.7661

);

let

ne

=

new

LngLat

(

-

73.9397

,

40.8002

);

let

llb

=

new

LngLatBounds

(

sw

,

ne

);

See

Fit to the bounds of a LineString

Constructors

Constructor

new LngLatBounds

(

sw?

: [

number

,

number

,

number

,

number

] |

LngLatLike

| [

LngLatLike

,

LngLatLike

],

ne?

:

LngLatLike

):

LngLatBounds

Defined in:

geo/lng_lat_bounds.ts:67

Parameters

Parameter

Type

Description

sw?

[

number

,

number

,

number

,

number

] |

LngLatLike

| [

LngLatLike

,

LngLatLike

]

The southwest corner of the bounding box. OR array of 4 numbers in the order of west, south, east, north OR array of 2 LngLatLike: [sw,ne]

ne?

LngLatLike

The northeast corner of the bounding box.

Returns

LngLatBounds

Example

let

sw

=

new

LngLat

(

-

73.9876

,

40.7661

);

let

ne

=

new

LngLat

(

-

73.9397

,

40.8002

);

let

llb

=

new

LngLatBounds

(

sw

,

ne

);

OR

let

llb

=

new

LngLatBounds

([

-

73.9876

,

40.7661

,

-

73.9397

,

40.8002

]);

OR

let

llb

=

new

LngLatBounds

([

sw

,

ne

]);

Methods

adjustAntiMeridian()

adjustAntiMeridian

():

LngLatBounds

Defined in:

geo/lng_lat_bounds.ts:401

Adjusts the given bounds to handle the case where the bounds cross the 180th meridian (antimeridian).

Returns

LngLatBounds

The adjusted LngLatBounds

Example

let

bounds

=

new

LngLatBounds

([

175.813127

,

-

20.157768

],

[

-

178.

340903

,

-

15.449124

]);

let

adjustedBounds

=

bounds

.

adjustAntiMeridian

();

// adjustedBounds will be: [[175.813127, -20.157768], [181.659097, -15.449124]]

contains()

contains

(

lnglat

:

LngLatLike

):

boolean

Defined in:

geo/lng_lat_bounds.ts:279

Check if the point is within the bounding box.

Parameters

Parameter

Type

Description

lnglat

LngLatLike

geographic point to check against.

Returns

boolean

true

if the point is within the bounding box.

Example

let

llb

=

new

LngLatBounds

(

new

LngLat

(

-

73.9876

,

40.7661

),

new

LngLat

(

-

73.9397

,

40.8002

)

);

let

ll

=

new

LngLat

(

-

73.9567

,

40.7789

);

console

.

log

(

llb

.

contains

(

ll

));

// = true

extend()

extend

(

obj

:

LngLatLike

|

LngLatBoundsLike

):

this

Defined in:

geo/lng_lat_bounds.ts:107

Extend the bounds to include a given LngLatLike or LngLatBoundsLike.

Parameters

Parameter

Type

Description

obj

LngLatLike

|

LngLatBoundsLike

object to extend to

Returns

this

getCenter()

getCenter

():

LngLat

Defined in:

geo/lng_lat_bounds.ts:163

Returns the geographical coordinate equidistant from the bounding box's corners.

Returns

LngLat

The bounding box's center.

Example

let

llb

=

new

LngLatBounds

([

-

73.9876

,

40.7661

],

[

-

73.9397

,

40.8002

]);

llb

.

getCenter

();

// = LngLat {lng: -73.96365, lat: 40.78315}

getEast()

getEast

():

number

Defined in:

geo/lng_lat_bounds.ts:214

Returns the east edge of the bounding box.

Returns

number

The east edge of the bounding box.

getNorth()

getNorth

():

number

Defined in:

geo/lng_lat_bounds.ts:221

Returns the north edge of the bounding box.

Returns

number

The north edge of the bounding box.

getNorthEast()

getNorthEast

():

LngLat

Defined in:

geo/lng_lat_bounds.ts:179

Returns the northeast corner of the bounding box.

Returns

LngLat

The northeast corner of the bounding box.

getNorthWest()

getNorthWest

():

LngLat

Defined in:

geo/lng_lat_bounds.ts:186

Returns the northwest corner of the bounding box.

Returns

LngLat

The northwest corner of the bounding box.

getSouth()

getSouth

():

number

Defined in:

geo/lng_lat_bounds.ts:207

Returns the south edge of the bounding box.

Returns

number

The south edge of the bounding box.

getSouthEast()

getSouthEast

():

LngLat

Defined in:

geo/lng_lat_bounds.ts:193

Returns the southeast corner of the bounding box.

Returns

LngLat

The southeast corner of the bounding box.

getSouthWest()

getSouthWest

():

LngLat

Defined in:

geo/lng_lat_bounds.ts:172

Returns the southwest corner of the bounding box.

Returns

LngLat

The southwest corner of the bounding box.

getWest()

getWest

():

number

Defined in:

geo/lng_lat_bounds.ts:200

Returns the west edge of the bounding box.

Returns

number

The west edge of the bounding box.

intersects()

intersects

(

other

:

LngLatBoundsLike

):

boolean

Defined in:

geo/lng_lat_bounds.ts:300

Checks if this bounding box intersects with another bounding box.

Returns true if the bounding boxes share any area, including cases where they only touch along an edge or at a corner.

This method properly handles cases where either or both bounding boxes cross the antimeridian (date line).

Parameters

Parameter

Type

other

LngLatBoundsLike

Returns

boolean

isEmpty()

isEmpty

():

boolean

Defined in:

geo/lng_lat_bounds.ts:258

Check if the bounding box is an empty/

null

-type box.

Returns

boolean

True if bounds have been defined, otherwise false.

setNorthEast()

setNorthEast

(

ne

:

LngLatLike

):

this

Defined in:

geo/lng_lat_bounds.ts:87

Set the northeast corner of the bounding box

Parameters

Parameter

Type

Description

ne

LngLatLike

a

LngLatLike

object describing the northeast corner of the bounding box.

Returns

this

setSouthWest()

setSouthWest

(

sw

:

LngLatLike

):

this

Defined in:

geo/lng_lat_bounds.ts:97

Set the southwest corner of the bounding box

Parameters

Parameter

Type

Description

sw

LngLatLike

a

LngLatLike

object describing the southwest corner of the bounding box.

Returns

this

toArray()

toArray

(): [[

number

,

number

], [

number

,

number

]]

Defined in:

geo/lng_lat_bounds.ts:234

Returns the bounding box represented as an array.

Returns

[[

number

,

number

], [

number

,

number

]]

The bounding box represented as an array, consisting of the southwest and northeast coordinates of the bounding represented as arrays of numbers.

Example

let

llb

=

new

LngLatBounds

([

-

73.9876

,

40.7661

],

[

-

73.9397

,

40.8002

]);

llb

.

toArray

();

// = [[-73.9876, 40.7661], [-73.9397, 40.8002]]

toString()

toString

():

string

Defined in:

geo/lng_lat_bounds.ts:249

Return the bounding box represented as a string.

Returns

string

The bounding box represents as a string of the format

'LngLatBounds(LngLat(lng, lat), LngLat(lng, lat))'

.

Example

let

llb

=

new

LngLatBounds

([

-

73.9876

,

40.7661

],

[

-

73.9397

,

40.8002

]);

llb

.

toString

();

// = "LngLatBounds(LngLat(-73.9876, 40.7661), LngLat(-73.9397, 40.8002))"

convert()

static

convert

(

input

:

LngLatBoundsLike

):

LngLatBounds

Defined in:

geo/lng_lat_bounds.ts:363

Converts an array to a

LngLatBounds

object.

If a

LngLatBounds

object is passed in, the function returns it unchanged.

Internally, the function calls

LngLat.convert

to convert arrays to

LngLat

values.

Parameters

Parameter

Type

Description

input

LngLatBoundsLike

An array of two coordinates to convert, or a

LngLatBounds

object to return.

Returns

LngLatBounds

A new

LngLatBounds

object, if a conversion occurred, or the original

LngLatBounds

object.

Example

let

arr

=

[[

-

73.9876

,

40.7661

],

[

-

73.9397

,

40.8002

]];

let

llb

=

LngLatBounds

.

convert

(

arr

);

// = LngLatBounds {_sw: LngLat {lng: -73.9876, lat: 40.7661}, _ne: LngLat {lng: -73.9397, lat: 40.8002}}

fromLngLat()

static

fromLngLat

(

center

:

LngLat

,

radius?

:

number

):

LngLatBounds

Defined in:

geo/lng_lat_bounds.ts:381

Returns a

LngLatBounds

from the coordinates extended by a given

radius

. The returned

LngLatBounds

completely contains the

radius

.

Parameters

Parameter

Type

Default value

Description

center

LngLat

undefined

center coordinates of the new bounds.

radius

number

0

Distance in meters from the coordinates to extend the bounds.

Returns

LngLatBounds

A new

LngLatBounds

object representing the coordinates extended by the

radius

.

Example

let

center

=

new

LngLat

(

-

73.9749

,

40.7736

);

LngLatBounds

.

fromLngLat

(

100

).

toArray

();

// = [[-73.97501862141328, 40.77351016847229], [-73.97478137858673, 40.77368983152771]]

Back to top
