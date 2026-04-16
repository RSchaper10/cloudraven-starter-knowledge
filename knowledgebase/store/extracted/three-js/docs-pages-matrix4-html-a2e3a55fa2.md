---
title: Matrix4 - Three.js Docs
source_url: https://threejs.org/docs/pages/Matrix4.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:30.016871+00:00
kind: extracted-doc
---

# Matrix4 - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Matrix4.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:30.016871+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Matrix4.html
- https://threejs.org/docs/pages/Vector3.html
- https://threejs.org/docs/pages/Quaternion.html
- https://threejs.org/docs/pages/global.html
- https://threejs.org/docs/pages/OrthographicCamera.html
- https://threejs.org/docs/pages/PerspectiveCamera.html
- https://threejs.org/docs/pages/Euler.html
- https://threejs.org/docs/pages/Matrix3.html

Captured summary:

- Matrix4 - Three.js Docs Matrix4 Constructor new Matrix4 ( n11 : number , n12 : number , n13 : number , n14 : number , n21 : number , n22 : number , n23 : number , n24 : number , n31 : number , n32 : number , n33 : number , n34 : number , n41 : number , n42 : number , n43 : number , n44 : number ) Constructs a new 4x4 matrix.
- The arguments are supposed to be in row-major order.
- If no arguments are provided, the constructor initializes the matrix as an identity matrix.
- elements : Array.<number> A column-major list of matrix values.
- isMatrix4 : boolean (readonly) This flag can be used for type testing.

Extracted text:

Matrix4 - Three.js Docs

Matrix4

Constructor

new

Matrix4

( n11 :

number

, n12 :

number

, n13 :

number

, n14 :

number

, n21 :

number

, n22 :

number

, n23 :

number

, n24 :

number

, n31 :

number

, n32 :

number

, n33 :

number

, n34 :

number

, n41 :

number

, n42 :

number

, n43 :

number

, n44 :

number

)

Constructs a new 4x4 matrix. The arguments are supposed to be in row-major order. If no arguments are provided, the constructor initializes the matrix as an identity matrix.

n11

1-1 matrix element.

n12

1-2 matrix element.

n13

1-3 matrix element.

n14

1-4 matrix element.

n21

2-1 matrix element.

n22

2-2 matrix element.

n23

2-3 matrix element.

n24

2-4 matrix element.

n31

3-1 matrix element.

n32

3-2 matrix element.

n33

3-3 matrix element.

n34

3-4 matrix element.

n41

4-1 matrix element.

n42

4-2 matrix element.

n43

4-3 matrix element.

n44

4-4 matrix element.

Properties

.

elements

: Array.<number>

A column-major list of matrix values.

.

isMatrix4

: boolean

(readonly)

This flag can be used for type testing.

Default is

true

.

Methods

.

clone

()

:

Matrix4

Returns a matrix with copied values from this instance.

Returns:

A clone of this instance.

.

compose

( position :

Vector3

, quaternion :

Quaternion

, scale :

Vector3

)

:

Matrix4

Sets this matrix to the transformation composed of the given position, rotation (Quaternion) and scale.

position

The position vector.

quaternion

The rotation as a Quaternion.

scale

The scale vector.

Returns:

A reference to this matrix.

.

copy

( m :

Matrix4

)

:

Matrix4

Copies the values of the given matrix to this instance.

m

The matrix to copy.

Returns:

A reference to this matrix.

.

copyPosition

( m :

Matrix4

)

:

Matrix4

Copies the translation component of the given matrix into this matrix's translation component.

m

The matrix to copy the translation component.

Returns:

A reference to this matrix.

.

decompose

( position :

Vector3

, quaternion :

Quaternion

, scale :

Vector3

)

:

Matrix4

Decomposes this matrix into its position, rotation and scale components and provides the result in the given objects.

Note: Not all matrices are decomposable in this way. For example, if an object has a non-uniformly scaled parent, then the object's world matrix may not be decomposable, and this method may not be appropriate.

position

The position vector.

quaternion

The rotation as a Quaternion.

scale

The scale vector.

Returns:

A reference to this matrix.

.

determinant

()

: number

Computes and returns the determinant of this matrix.

Based on the method outlined

here

.

Returns:

The determinant.

.

equals

( matrix :

Matrix4

)

: boolean

Returns

true

if this matrix is equal with the given one.

matrix

The matrix to test for equality.

Returns:

Whether this matrix is equal with the given one.

.

extractBasis

( xAxis :

Vector3

, yAxis :

Vector3

, zAxis :

Vector3

)

:

Matrix4

Extracts the basis of this matrix into the three axis vectors provided.

xAxis

The basis's x axis.

yAxis

The basis's y axis.

zAxis

The basis's z axis.

Returns:

A reference to this matrix.

.

extractRotation

( m :

Matrix4

)

:

Matrix4

Extracts the rotation component of the given matrix into this matrix's rotation component.

Note: This method does not support reflection matrices.

m

The matrix.

Returns:

A reference to this matrix.

.

fromArray

( array :

Array.<number>

, offset :

number

)

:

Matrix4

Sets the elements of the matrix from the given array.

array

The matrix elements in column-major order.

offset

Index of the first element in the array.

Default is

0

.

Returns:

A reference to this matrix.

.

getMaxScaleOnAxis

()

: number

Gets the maximum scale value of the three axes.

Returns:

The maximum scale.

.

identity

()

:

Matrix4

Sets this matrix to the 4x4 identity matrix.

Returns:

A reference to this matrix.

.

invert

()

:

Matrix4

Inverts this matrix, using the

analytic method

. You can not invert with a determinant of zero. If you attempt this, the method produces a zero matrix instead.

Returns:

A reference to this matrix.

.

lookAt

( eye :

Vector3

, target :

Vector3

, up :

Vector3

)

:

Matrix4

Sets the rotation component of the transformation matrix, looking from

eye

towards

target

, and oriented by the up-direction.

eye

The eye vector.

target

The target vector.

up

The up vector.

Returns:

A reference to this matrix.

.

makeBasis

( xAxis :

Vector3

, yAxis :

Vector3

, zAxis :

Vector3

)

:

Matrix4

Sets the given basis vectors to this matrix.

xAxis

The basis's x axis.

yAxis

The basis's y axis.

zAxis

The basis's z axis.

Returns:

A reference to this matrix.

.

makeOrthographic

( left :

number

, right :

number

, top :

number

, bottom :

number

, near :

number

, far :

number

, coordinateSystem :

WebGLCoordinateSystem

|

WebGPUCoordinateSystem

, reversedDepth :

boolean

)

:

Matrix4

Creates a orthographic projection matrix. This is used internally by

OrthographicCamera#updateProjectionMatrix

.

left

Left boundary of the viewing frustum at the near plane.

right

Right boundary of the viewing frustum at the near plane.

top

Top boundary of the viewing frustum at the near plane.

bottom

Bottom boundary of the viewing frustum at the near plane.

near

The distance from the camera to the near plane.

far

The distance from the camera to the far plane.

coordinateSystem

The coordinate system.

Default is

WebGLCoordinateSystem

.

reversedDepth

Whether to use a reversed depth.

Default is

false

.

Returns:

A reference to this matrix.

.

makePerspective

( left :

number

, right :

number

, top :

number

, bottom :

number

, near :

number

, far :

number

, coordinateSystem :

WebGLCoordinateSystem

|

WebGPUCoordinateSystem

, reversedDepth :

boolean

)

:

Matrix4

Creates a perspective projection matrix. This is used internally by

PerspectiveCamera#updateProjectionMatrix

.

left

Left boundary of the viewing frustum at the near plane.

right

Right boundary of the viewing frustum at the near plane.

top

Top boundary of the viewing frustum at the near plane.

bottom

Bottom boundary of the viewing frustum at the near plane.

near

The distance from the camera to the near plane.

far

The distance from the camera to the far plane.

coordinateSystem

The coordinate system.

Default is

WebGLCoordinateSystem

.

reversedDepth

Whether to use a reversed depth.

Default is

false

.

Returns:

A reference to this matrix.

.

makeRotationAxis

( axis :

Vector3

, angle :

number

)

:

Matrix4

Sets this matrix as a rotational transformation around the given axis by the given angle.

This is a somewhat controversial but mathematically sound alternative to rotating via Quaternions. See the discussion

here

.

axis

The normalized rotation axis.

angle

The rotation in radians.

Returns:

A reference to this matrix.

.

makeRotationFromEuler

( euler :

Euler

)

:

Matrix4

Sets the rotation component (the upper left 3x3 matrix) of this matrix to the rotation specified by the given Euler angles. The rest of the matrix is set to the identity. Depending on the

Euler#order

, there are six possible outcomes. See

this page

for a complete list.

euler

The Euler angles.

Returns:

A reference to this matrix.

.

makeRotationFromQuaternion

( q :

Quaternion

)

:

Matrix4

Sets the rotation component of this matrix to the rotation specified by the given Quaternion as outlined

here

The rest of the matrix is set to the identity.

q

The Quaternion.

Returns:

A reference to this matrix.

.

makeRotationX

( theta :

number

)

:

Matrix4

Sets this matrix as a rotational transformation around the X axis by the given angle.

theta

The rotation in radians.

Returns:

A reference to this matrix.

.

makeRotationY

( theta :

number

)

:

Matrix4

Sets this matrix as a rotational transformation around the Y axis by the given angle.

theta

The rotation in radians.

Returns:

A reference to this matrix.

.

makeRotationZ

( theta :

number

)

:

Matrix4

Sets this matrix as a rotational transformation around the Z axis by the given angle.

theta

The rotation in radians.

Returns:

A reference to this matrix.

.

makeScale

( x :

number

, y :

number

, z :

number

)

:

Matrix4

Sets this matrix as a scale transformation.

x

The amount to scale in the X axis.

y

The amount to scale in the Y axis.

z

The amount to scale in the Z axis.

Returns:

A reference to this matrix.

.

makeShear

( xy :

number

, xz :

number

, yx :

number

, yz :

number

, zx :

number

, zy :

number

)

:

Matrix4

Sets this matrix as a shear transformation.

xy

The amount to shear X by Y.

xz

The amount to shear X by Z.

yx

The amount to shear Y by X.

yz

The amount to shear Y by Z.

zx

The amount to shear Z by X.

zy

The amount to shear Z by Y.

Returns:

A reference to this matrix.

.

makeTranslation

( x :

number |

Vector3

, y :

number

, z :

number

)

:

Matrix4

Sets this matrix as a translation transform from the given vector.

x

The amount to translate in the X axis or alternatively a translation vector.

y

The amount to translate in the Y axis.

z

The amount to translate in the z axis.

Returns:

A reference to this matrix.

.

multiply

( m :

Matrix4

)

:

Matrix4

Post-multiplies this matrix by the given 4x4 matrix.

m

The matrix to multiply with.

Returns:

A reference to this matrix.

.

multiplyMatrices

( a :

Matrix4

, b :

Matrix4

)

:

Matrix4

Multiples the given 4x4 matrices and stores the result in this matrix.

a

The first matrix.

b

The second matrix.

Returns:

A reference to this matrix.

.

multiplyScalar

( s :

number

)

:

Matrix4

Multiplies every component of the matrix by the given scalar.

s

The scalar.

Returns:

A reference to this matrix.

.

premultiply

( m :

Matrix4

)

:

Matrix4

Pre-multiplies this matrix by the given 4x4 matrix.

m

The matrix to multiply with.

Returns:

A reference to this matrix.

.

scale

( v :

Vector3

)

:

Matrix4

Multiplies the columns of this matrix by the given vector.

v

The scale vector.

Returns:

A reference to this matrix.

.

set

( n11 :

number

, n12 :

number

, n13 :

number

, n14 :

number

, n21 :

number

, n22 :

number

, n23 :

number

, n24 :

number

, n31 :

number

, n32 :

number

, n33 :

number

, n34 :

number

, n41 :

number

, n42 :

number

, n43 :

number

, n44 :

number

)

:

Matrix4

Sets the elements of the matrix.The arguments are supposed to be in row-major order.

n11

1-1 matrix element.

n12

1-2 matrix element.

n13

1-3 matrix element.

n14

1-4 matrix element.

n21

2-1 matrix element.

n22

2-2 matrix element.

n23

2-3 matrix element.

n24

2-4 matrix element.

n31

3-1 matrix element.

n32

3-2 matrix element.

n33

3-3 matrix element.

n34

3-4 matrix element.

n41

4-1 matrix element.

n42

4-2 matrix element.

n43

4-3 matrix element.

n44

4-4 matrix element.

Returns:

A reference to this matrix.

.

setFromMatrix3

( m :

Matrix3

)

:

Matrix4

Set the upper 3x3 elements of this matrix to the values of given 3x3 matrix.

m

The 3x3 matrix.

Returns:

A reference to this matrix.

.

setPosition

( x :

number |

Vector3

, y :

number

, z :

number

)

:

Matrix4

Sets the position component for this matrix from the given vector, without affecting the rest of the matrix.

x

The x component of the vector or alternatively the vector object.

y

The y component of the vector.

z

The z component of the vector.

Returns:

A reference to this matrix.

.

toArray

( array :

Array.<number>

, offset :

number

)

: Array.<number>

Writes the elements of this matrix to the given array. If no array is provided, the method returns a new instance.

array

The target array holding the matrix elements in column-major order.

Default is

[]

.

offset

Index of the first element in the array.

Default is

0

.

Returns:

The matrix elements in column-major order.

.

transpose

()

:

Matrix4

Transposes this matrix in place.

Returns:

A reference to this matrix.

Source

src/math/Matrix4.js
