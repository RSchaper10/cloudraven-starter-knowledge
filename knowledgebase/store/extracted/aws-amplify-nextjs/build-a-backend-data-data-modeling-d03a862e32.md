---
title: Customize your data model - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/build-a-backend/data/data-modeling/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:02.831440+00:00
kind: extracted-doc
---

# Customize your data model - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/build-a-backend/data/data-modeling/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:02.831440+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/frontend/data/
- https://docs.amplify.aws/nextjs/build-a-backend/data/data-modeling/
- https://docs.amplify.aws/nextjs/build-a-backend/data/data-modeling/add-fields/
- https://docs.amplify.aws/nextjs/build-a-backend/data/data-modeling/relationships/
- https://docs.amplify.aws/nextjs/build-a-backend/data/data-modeling/identifiers/
- https://docs.amplify.aws/nextjs/build-a-backend/data/data-modeling/secondary-index/
- https://docs.amplify.aws/nextjs/build-a-backend/data/data-modeling/disable-operations/
- https://docs.amplify.aws/nextjs/start/migrate-to-gen2/

Captured summary:

- Customize your data model - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Looking for how to use this in your app?
- See Frontend Libraries → Customize your data model Data modeling capabilities Every data model is defined as part of a data schema ( a.schema() ).

Extracted text:

Customize your data model - AWS Amplify Gen 2 Documentation

Name:

interface

Value:

Introducing Amplify Gen 2

Dismiss Gen 2 introduction dialog

Amplify has re-imagined the way frontend developers build fullstack applications. Develop and deploy without the hassle.

Fullstack TypeScript

Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.

🚀

Built with the AWS CDK

Use any cloud resource your app needs. Never worry about scale.

Back to Gen 1 Docs

Learn more about Gen 2

Looking for how to use this in your app?

See Frontend Libraries

→

Customize your data model

Data modeling capabilities

Every data model is defined as part of a data schema (

a.schema()

). You can enhance your data model with various fields, customize their identifiers, apply authorization rules, or model relationships. Every data model (

a.model()

) automatically provides create, read, update, and delete API operations as well as real-time subscription events. Below is a quick tour of the many functionalities you can add to your data model:

Copy

code example

import

{

type

ClientSchema

,

a

,

defineData

}

from

'@aws-amplify/backend'

;

const

schema

=

a

.

schema

(

{

Customer

:

a

.

model

(

{

customerId

:

a

.

id

(

)

.

required

(

)

,

// fields can be of various scalar types,

// such as string, boolean, float, integers etc.

name

:

a

.

string

(

)

,

// fields can be of custom types

location

:

a

.

customType

(

{

// fields can be required or optional

lat

:

a

.

float

(

)

.

required

(

)

,

long

:

a

.

float

(

)

.

required

(

)

,

}

)

,

// fields can be enums

engagementStage

:

a

.

enum

(

[

"PROSPECT"

,

"INTERESTED"

,

"PURCHASED"

]

)

,

collectionId

:

a

.

id

(

)

,

collection

:

a

.

belongsTo

(

"Collection"

,

"collectionId"

)

// Use custom identifiers. By default, it uses an `id: a.id()` field

}

)

.

identifier

(

[

"customerId"

]

)

,

Collection

:

a

.

model

(

{

customers

:

a

.

hasMany

(

"Customer"

,

"collectionId"

)

,

// setup relationships between types

tags

:

a

.

string

(

)

.

array

(

)

,

// fields can be arrays

representativeId

:

a

.

id

(

)

.

required

(

)

,

// customize secondary indexes to optimize your query performance

}

)

.

secondaryIndexes

(

(

index

)

=>

[

index

(

"representativeId"

)

]

)

,

}

)

.

authorization

(

(

allow

)

=>

[

allow

.

publicApiKey

(

)

]

)

;

export

type

Schema

=

ClientSchema

<

typeof

schema

>

;

export

const

data

=

defineData

(

{

schema

,

authorizationModes

:

{

defaultAuthorizationMode

:

"apiKey"

,

apiKeyAuthorizationMode

:

{

expiresInDays

:

30

,

}

,

}

,

}

)

;

Add fields to data model

Configure built-in and custom field types.

Modeling relationships

Learn about the types of model relationships and modeling relationships.

Customize data model identifiers

Define the primary key for a model using single-field or composite identifiers.

Customize secondary indexes

Define the secondary indexes for your data model to optimize query performance

Disable Operations

Disable Operations for your data model

Gen 1 schema support

If you are coming from Gen 1, you can continue to use the GraphQL Schema Definition Language (SDL) for defining your schema. However, we strongly recommend you use the TypeScript-first schema builder experience in your project as it provides type safety and is the recommended way of working with Amplify going forward.

Note:

Some features available in Gen 1 GraphQL SDL are not available in Gen 2. See the

feature matrix

for features supported in Gen 2.

amplify/data/resource.ts

Copy

amplify/data/resource.ts

code example

import

{

defineData

}

from

'@aws-amplify/backend'

;

const

schema

=

/* GraphQL */

`

type Todo @model @auth(rules: [{ allow: owner }]) {

content: String

isDone: Boolean

}

`

;

export

const

data

=

defineData

(

{

schema

,

authorizationModes

:

{

defaultAuthorizationMode

:

"apiKey"

,

apiKeyAuthorizationMode

:

{

expiresInDays

:

30

,

}

,

}

,

}

)

;
