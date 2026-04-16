---
title: Matrix3 - Three.js Docs
source_url: https://threejs.org/docs/pages/Matrix3.html
target_id: three-js
dependency: Three.js
collected_at: 2026-04-16T03:23:30.431482+00:00
kind: extracted-doc
---

# Matrix3 - Three.js Docs

Source URL:

- https://threejs.org/docs/pages/Matrix3.html

Dependency:

- Three.js

Collected at:

- 2026-04-16T03:23:30.431482+00:00

Direct links in scope:

- https://threejs.org/docs/pages/Matrix3.html
- https://threejs.org/docs/pages/Vector3.html
- https://threejs.org/docs/pages/Matrix4.html
- https://threejs.org/docs/pages/Vector2.html

Captured summary:

- Matrix3 - Three.js Docs Matrix3 Constructor new Matrix3 ( n11 : number , n12 : number , n13 : number , n21 : number , n22 : number , n23 : number , n31 : number , n32 : number , n33 : number ) Constructs a new 3x3 matrix.
- The arguments are supposed to be in row-major order.
- If no arguments are provided, the constructor initializes the matrix as an identity matrix.
- elements : Array.<number> A column-major list of matrix values.
- isMatrix3 : boolean (readonly) This flag can be used for type testing.

Extracted text:

Matrix3 - Three.js Docs

Matrix3

Constructor

new

Matrix3

( n11 :

number

, n12 :

number

, n13 :

number

, n21 :

number

, n22 :

number

, n23 :

number

, n31 :

number

, n32 :

number

, n33 :

number

)

Constructs a new 3x3 matrix. The arguments are supposed to be in row-major order. If no arguments are provided, the constructor initializes the matrix as an identity matrix.

n11

1-1 matrix element.

n12

1-2 matrix element.

n13

1-3 matrix element.

n21

2-1 matrix element.

n22

2-2 matrix element.

n23

2-3 matrix element.

n31

3-1 matrix element.

n32

3-2 matrix element.

n33

3-3 matrix element.

Properties

.

elements

: Array.<number>

A column-major list of matrix values.

.

isMatrix3

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

Matrix3

Returns a matrix with copied values from this instance.

Returns:

A clone of this instance.

.

copy

( m :

Matrix3

)

:

Matrix3

Copies the values of the given matrix to this instance.

m

The matrix to copy.

Returns:

A reference to this matrix.

.

determinant

()

: number

Computes and returns the determinant of this matrix.

Returns:

The determinant.

.

equals

( matrix :

Matrix3

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

Matrix3

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

fromArray

( array :

Array.<number>

, offset :

number

)

:

Matrix3

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

getNormalMatrix

( matrix4 :

Matrix4

)

:

Matrix3

Computes the normal matrix which is the inverse transpose of the upper left 3x3 portion of the given 4x4 matrix.

matrix4

The 4x4 matrix.

Returns:

A reference to this matrix.

.

identity

()

:

Matrix3

Sets this matrix to the 3x3 identity matrix.

Returns:

A reference to this matrix.

.

invert

()

:

Matrix3

Inverts this matrix, using the

analytic method

. You can not invert with a determinant of zero. If you attempt this, the method produces a zero matrix instead.

Returns:

A reference to this matrix.

.

makeRotation

( theta :

number

)

:

Matrix3

Sets this matrix as a 2D rotational transformation.

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

)

:

Matrix3

Sets this matrix as a 2D scale transform.

x

The amount to scale in the X axis.

y

The amount to scale in the Y axis.

Returns:

A reference to this matrix.

.

makeTranslation

( x :

number |

Vector2

, y :

number

)

:

Matrix3

Sets this matrix as a 2D translation transform.

x

The amount to translate in the X axis or alternatively a translation vector.

y

The amount to translate in the Y axis.

Returns:

A reference to this matrix.

.

multiply

( m :

Matrix3

)

:

Matrix3

Post-multiplies this matrix by the given 3x3 matrix.

m

The matrix to multiply with.

Returns:

A reference to this matrix.

.

multiplyMatrices

( a :

Matrix3

, b :

Matrix3

)

:

Matrix3

Multiples the given 3x3 matrices and stores the result in this matrix.

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

Matrix3

Multiplies every component of the matrix by the given scalar.

s

The scalar.

Returns:

A reference to this matrix.

.

premultiply

( m :

Matrix3

)

:

Matrix3

Pre-multiplies this matrix by the given 3x3 matrix.

m

The matrix to multiply with.

Returns:

A reference to this matrix.

.

rotate

( theta :

number

)

:

Matrix3

Rotates this matrix by the given angle.

theta

The rotation in radians.

Returns:

A reference to this matrix.

.

scale

( sx :

number

, sy :

number

)

:

Matrix3

Scales this matrix with the given scalar values.

sx

The amount to scale in the X axis.

sy

The amount to scale in the Y axis.

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

, n21 :

number

, n22 :

number

, n23 :

number

, n31 :

number

, n32 :

number

, n33 :

number

)

:

Matrix3

Sets the elements of the matrix.The arguments are supposed to be in row-major order.

n11

1-1 matrix element.

n12

1-2 matrix element.

n13

1-3 matrix element.

n21

2-1 matrix element.

n22

2-2 matrix element.

n23

2-3 matrix element.

n31

3-1 matrix element.

n32

3-2 matrix element.

n33

3-3 matrix element.

Returns:

A reference to this matrix.

.

setFromMatrix4

( m :

Matrix4

)

:

Matrix3

Set this matrix to the upper 3x3 matrix of the given 4x4 matrix.

m

The 4x4 matrix.

Returns:

A reference to this matrix.

.

setUvTransform

( tx :

number

, ty :

number

, sx :

number

, sy :

number

, rotation :

number

, cx :

number

, cy :

number

)

:

Matrix3

Sets the UV transform matrix from offset, repeat, rotation, and center.

tx

Offset x.

ty

Offset y.

sx

Repeat x.

sy

Repeat y.

rotation

Rotation, in radians. Positive values rotate counterclockwise.

cx

Center x of rotation.

cy

Center y of rotation

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

translate

( tx :

number

, ty :

number

)

:

Matrix3

Translates this matrix by the given scalar values.

tx

The amount to translate in the X axis.

ty

The amount to translate in the Y axis.

Returns:

A reference to this matrix.

.

transpose

()

:

Matrix3

Transposes this matrix in place.

Returns:

A reference to this matrix.

.

transposeIntoArray

( r :

Array.<number>

)

:

Matrix3

Transposes this matrix into the supplied array, and returns itself unchanged.

r

An array to store the transposed matrix elements.

Returns:

A reference to this matrix.

Source

src/math/Matrix3.js
