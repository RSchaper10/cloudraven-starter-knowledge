---
title: Add custom queries and mutations - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/build-a-backend/data/custom-business-logic/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:04.621664+00:00
kind: extracted-doc
---

# Add custom queries and mutations - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/build-a-backend/data/custom-business-logic/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:04.621664+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/frontend/data/
- https://docs.amplify.aws/nextjs/build-a-backend/data/custom-business-logic/
- https://docs.amplify.aws/nextjs/build-a-backend/functions/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/
- https://docs.amplify.aws/nextjs/build-a-backend/data/connect-to-existing-data-sources/

Captured summary:

- Add custom queries and mutations - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Looking for how to use this in your app?
- See Frontend Libraries → Add custom queries and mutations ✨ Use with AI The a.model() data model provides a solid foundation for querying, mutating, and fetching data.

Extracted text:

Add custom queries and mutations - AWS Amplify Gen 2 Documentation

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

Add custom queries and mutations

✨

Use with AI

The

a.model()

data model provides a solid foundation for querying, mutating, and fetching data. However, you may need additional customizations to meet specific requirements around custom API requests, response formatting, and/or fetching from external data sources.

In the following sections, we walk through the three steps to create a custom query or mutation:

Define a custom query or mutation

Configure custom business logic handler code

Invoke the custom query or mutation

Step 1 - Define a custom query or mutation

Type

When to choose

Query

When the request only needs to read data and will not modify any backend data

Mutation

When the request will modify backend data

For every custom query or mutation, you need to set a return type and, optionally, arguments. Use

a.query()

or

a.mutation()

to define your custom query or mutation in your

amplify/data/resource.ts

file:

Custom query

Custom mutation

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

// 1. Define your return type as a custom type

EchoResponse

:

a

.

customType

(

{

content

:

a

.

string

(

)

,

executionDuration

:

a

.

float

(

)

}

)

,

// 2. Define your query with the return type and, optionally, arguments

echo

:

a

.

query

(

)

// arguments that this query accepts

.

arguments

(

{

content

:

a

.

string

(

)

}

)

// return type of the query

.

returns

(

a

.

ref

(

'EchoResponse'

)

)

// only allow signed-in users to call this API

.

authorization

(

allow

=>

[

allow

.

authenticated

(

)

]

)

}

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

}

)

;

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

// 1. Define your return type as a custom type or model

Post

:

a

.

model

(

{

id

:

a

.

id

(

)

,

content

:

a

.

string

(

)

,

likes

:

a

.

integer

(

)

}

)

,

// 2. Define your mutation with the return type and, optionally, arguments

likePost

:

a

.

mutation

(

)

// arguments that this query accepts

.

arguments

(

{

postId

:

a

.

string

(

)

}

)

// return type of the query

.

returns

(

a

.

ref

(

'Post'

)

)

// only allow signed-in users to call this API

.

authorization

(

allow

=>

[

allow

.

authenticated

(

)

]

)

}

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

}

)

;

Step 2 - Configure custom business logic handler code

After your query or mutation is defined, you need to author your custom business logic. You can either define it in a

function

or using a

custom resolver powered by AppSync JavaScript resolver

.

Function

Custom resolver powered by AppSync JavaScript resolvers

In your

amplify/data/echo-handler/

folder, create a

handler.ts

file. You can import a utility type for your function handler via the

Schema

type from your backend resource. This gives you type-safe handler parameters and return values.

amplify/data/echo-handler/handler.ts

Copy

amplify/data/echo-handler/handler.ts

code example

import

type

{

Schema

}

from

'../resource'

export

const

handler

:

Schema

[

"echo"

]

[

"functionHandler"

]

=

async

(

event

,

context

)

=>

{

const

start

=

performance

.

now

(

)

;

return

{

content

:

`

Echoing content:

${

event

.

arguments

.

content

}

`

,

executionDuration

:

performance

.

now

(

)

-

start

}

;

}

;

In your

amplify/data/resource.ts

file, define the function using

defineFunction

and then reference the function with your query or mutation using

a.handler.function()

as a handler.

amplify/data/resource.ts

Copy

amplify/data/resource.ts

code example

import

{

type

ClientSchema

,

a

,

defineData

,

defineFunction

// 1.Import "defineFunction" to create new functions

}

from

'@aws-amplify/backend'

;

// 2. define a function

const

echoHandler

=

defineFunction

(

{

entry

:

'./echo-handler/handler.ts'

}

)

const

schema

=

a

.

schema

(

{

EchoResponse

:

a

.

customType

(

{

content

:

a

.

string

(

)

,

executionDuration

:

a

.

float

(

)

}

)

,

echo

:

a

.

query

(

)

.

arguments

(

{

content

:

a

.

string

(

)

}

)

.

returns

(

a

.

ref

(

'EchoResponse'

)

)

.

authorization

(

allow

=>

[

allow

.

publicApiKey

(

)

]

)

// 3. set the function has the handler

.

handler

(

a

.

handler

.

function

(

echoHandler

)

)

}

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

'apiKey'

,

apiKeyAuthorizationMode

:

{

expiresInDays

:

30

}

,

}

,

}

)

;

If you want to use an existing Lambda function, you can reference it by its name:

a.handler.function('name-of-existing-lambda-fn')

. Note that Amplify will not update this external Lambda function or its dependencies.

Custom resolvers work on a "request/response" basis. You choose a data source, map your request to the data source's input parameters, and then map the data source's response back to the query/mutation's return type. Custom resolvers provide the benefit of no cold starts, less infrastructure to manage, and no additional charge for Lambda function invocations. Review

Choosing between custom resolver and function

.

In your

amplify/data/resource.ts

file, define a custom handler using

a.handler.custom

.

amplify/data/resource.ts

Copy

amplify/data/resource.ts

code example

import

{

type

ClientSchema

,

a

,

defineData

,

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

Post

:

a

.

model

(

{

content

:

a

.

string

(

)

,

likes

:

a

.

integer

(

)

.

authorization

(

allow

=>

[

allow

.

authenticated

(

)

.

to

(

[

'read'

]

)

]

)

}

)

.

authorization

(

allow

=>

[

allow

.

owner

(

)

,

allow

.

authenticated

(

)

.

to

(

[

'read'

]

)

]

)

,

likePost

:

a

.

mutation

(

)

.

arguments

(

{

postId

:

a

.

id

(

)

}

)

.

returns

(

a

.

ref

(

'Post'

)

)

.

authorization

(

allow

=>

[

allow

.

authenticated

(

)

]

)

.

handler

(

a

.

handler

.

custom

(

{

dataSource

:

a

.

ref

(

'Post'

)

,

entry

:

'./increment-like.js'

}

)

)

}

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

'apiKey'

,

apiKeyAuthorizationMode

:

{

expiresInDays

:

30

}

}

,

}

)

;

amplify/data/increment-like.js

Copy

amplify/data/increment-like.js

code example

import

{

util

}

from

'@aws-appsync/utils'

;

export

function

request

(

ctx

)

{

return

{

operation

:

'UpdateItem'

,

key

:

util

.

dynamodb

.

toMapValues

(

{

id

:

ctx

.

args

.

postId

}

)

,

update

:

{

expression

:

'ADD likes :plusOne'

,

expressionValues

:

{

':plusOne'

:

{

N

:

1

}

}

,

}

}

}

export

function

response

(

ctx

)

{

return

ctx

.

result

}

By default, you'll be able to access any existing database tables (powered by Amazon DynamoDB) using

a.ref('MODEL_NAME')

. But you can also reference any other external data source from within your AWS account, by adding them to your backend definition.

The supported data sources are:

Amazon DynamoDB

AWS Lambda

Amazon RDS databases with Data API

Amazon EventBridge

OpenSearch

HTTP endpoints

You can add these additional data sources via our

amplify/backend.ts

file:

amplify/backend.ts

import

*

as

dynamoDb

from

'aws-cdk-lib/aws-dynamodb'

import

{

defineBackend

}

from

'@aws-amplify/backend'

;

import

{

auth

}

from

'./auth/resource'

;

import

{

data

}

from

'./data/resource'

;

export

const

backend

=

defineBackend

(

{

auth

,

data

,

}

)

;

const

externalDataSourcesStack

=

backend

.

createStack

(

"MyExternalDataSources"

)

const

externalTable

=

dynamoDb

.

Table

.

fromTableName

(

externalDataSourcesStack

,

"MyTable"

,

"MyExternalTable"

)

backend

.

data

.

addDynamoDbDataSource

(

Copy

highlighted code example

"ExternalTableDataSource"

,

externalTable

)

In your schema you can then reference these additional data sources based on their name:

amplify/data/resource.ts

import

{

type

ClientSchema

,

a

,

defineData

,

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

Post

:

a

.

model

(

{

content

:

a

.

string

(

)

,

likes

:

a

.

integer

(

)

.

authorization

(

allow

=>

[

allow

.

authenticated

(

)

.

to

(

[

'read'

]

)

]

)

}

)

.

authorization

(

allow

=>

[

allow

.

owner

(

)

,

allow

.

authenticated

(

)

.

to

(

[

'read'

]

)

]

)

,

likePost

:

a

.

mutation

(

)

.

arguments

(

{

postId

:

a

.

id

(

)

}

)

.

returns

(

a

.

ref

(

'Post'

)

)

.

authorization

(

allow

=>

[

allow

.

authenticated

(

)

]

)

.

handler

(

a

.

handler

.

custom

(

{

Copy

highlighted code example

dataSource

:

"ExternalTableDataSource"

,

entry

:

'./increment-like.js'

}

)

)

}

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

'apiKey'

,

apiKeyAuthorizationMode

:

{

expiresInDays

:

30

}

}

,

}

)

;

All handlers must be of the same type. For example, you can't mix and match

a.handler.function

with

a.handler.custom

within a single

.handler()

modifier.

Step 3 - Invoke the custom query or mutation

From your generated Data client, you can find all your custom queries and mutations under the

client.queries.

and

client.mutations.

APIs respectively.

Custom query

Custom mutation

Copy

code example

const

{

data

,

errors

}

=

await

client

.

queries

.

echo

(

{

content

:

'hello world!!!'

}

)

;

Copy

code example

const

{

data

,

errors

}

=

await

client

.

mutations

.

likePost

(

{

postId

:

'hello'

}

)

;

Supported Argument Types in Custom Operations

Custom operations can accept different types of arguments. Understanding these options helps define flexible and well-structured APIs.

Defining Arguments in Custom Operations

When defining a custom operation, you can specify arguments using different types:

Scalar Fields

: Basic types such as

string

,

integer

,

float

, etc

Custom Types

: Define inline

customType

Reference Types

: Use

a.ref()

to reference enums and custom types

amplify/data/resource.ts

Copy

amplify/data/resource.ts

code example

const

schema

=

a

.

schema

(

{

Status

:

a

.

enum

(

[

'ACCEPTED'

,

'REJECTED'

]

)

,

getPost

:

a

.

query

(

)

.

arguments

(

{

// scalar field

content

:

a

.

string

(

)

,

// inline custom type

config

:

a

.

customType

(

{

filter

:

a

.

string

(

)

,

// reference to enum

status

:

a

.

ref

(

'Status'

)

}

)

,

}

)

.

returns

(

a

.

string

(

)

)

.

authorization

(

allow

=>

[

allow

.

authenticated

(

)

]

)

}

)

;

Async function handlers

Async function handlers allow you to execute long-running operations asynchronously, improving the responsiveness of your API. This is particularly useful for tasks that don't require an immediate response, such as batch processing, putting messages in a queue, and initiating a generative AI model inference.

Usage

To define an async function handler, use the

.async()

method when defining your handler:

amplify/data/resource.ts

Copy

amplify/data/resource.ts

code example

const

signUpForNewsletter

=

defineFunction

(

{

entry

:

'./sign-up-for-newsletter/handler.ts'

}

)

;

const

schema

=

a

.

schema

(

{

someAsyncOperation

:

a

.

mutation

(

)

.

arguments

(

{

email

:

a

.

email

(

)

.

required

(

)

}

)

.

handler

(

a

.

handler

.

function

(

signUpForNewsletter

)

.

async

(

)

)

.

authorization

(

(

allow

)

=>

allow

.

guest

(

)

)

,

}

)

Key Characteristics

Single Return Type

: Async handlers return a static type

EventInvocationResponse

and don't support specifying a return type. The

.returns()

method is not available for operations using async handlers.

Fire and Forget

: The client is informed whether the invocation was successfully queued, but doesn't receive data from the Lambda function execution.

Pipeline Support

: Async handlers can be used in function pipelines. If the final handler is an async function, the return type of the query or mutation is

EventInvocationResponse

.

PREVIOUS

Customize your auth rules

NEXT

Connect to existing data sources
