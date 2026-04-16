---
title: Customize your auth rules - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:03.420609+00:00
kind: extracted-doc
---

# Customize your auth rules - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:03.420609+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/frontend/data/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/public-data-access/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/per-user-per-owner-data-access/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/signed-in-user-data-access/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/user-group-based-data-access/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/custom-data-access-patterns/
- https://docs.amplify.aws/nextjs/build-a-backend/data/manage-with-amplify-console/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/multi-user-data-access/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/using-oidc-authorization-provider/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/configure-custom-identity-and-group-claim/
- https://docs.amplify.aws/nextjs/build-a-backend/data/customize-authz/grant-lambda-function-access-to-api/

Captured summary:

- Customize your auth rules - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Looking for how to use this in your app?
- See Frontend Libraries → Customize your auth rules Use the .authorization() modifier to configure authorization rules for public, signed-in user, per user, and per user group data access.

Extracted text:

Customize your auth rules - AWS Amplify Gen 2 Documentation

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

Customize your auth rules

Use the

.authorization()

modifier to configure authorization rules for public, signed-in user, per user, and per user group data access.

Authorization rules operate on the deny-by-default principle

. Meaning that if an authorization rule is not specifically configured, it is denied.

Copy

code example

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

}

)

.

authorization

(

allow

=>

[

// Allow anyone auth'd with an API key to read everyone's posts.

allow

.

publicApiKey

(

)

.

to

(

[

'read'

]

)

,

// Allow signed-in user to create, read, update,

// and delete their __OWN__ posts.

allow

.

owner

(

)

,

]

)

}

)

In the example above, everyone (

public

) can read every Post but authenticated users (

owner

) can create, read, update, and delete their own posts. Amplify also allows you to restrict the allowed operations, combine multiple authorization rules, and apply fine-grained field-level authorization.

Available authorization strategies

Use the guide below to select the correct authorization strategy for your use case:

Recommended use case

Strategy

authMode

Public data access where users or devices are anonymous. Anyone with the AppSync API key is granted access.

publicApiKey

apiKey

Recommended for production environment's public data access. Public data access where unauthenticated users or devices are granted permissions using Amazon Cognito identity pool's role for unauthenticated identities.

guest

identityPool

Per user data access. Access is restricted to the "owner" of a record. Leverages

amplify/auth/resource.ts

Cognito user pool by default.

owner

/

ownerDefinedIn

/

ownersDefinedIn

userPool

/

oidc

Any signed-in data access. Unlike owner-based access,

any

signed-in user has access.

authenticated

userPool

/

oidc

/

identityPool

Per user group data access. A specific or dynamically configured group of users has access.

group

/

groupDefinedIn

/

groups

/

groupsDefinedIn

userPool

/

oidc

Define your own custom authorization rule within a serverless function.

custom

lambda

Understand how authorization rules are applied

Authorization rules can be applied globally across all data models in a schema, onto specific data models, and onto specific fields.

Amplify will always use the most specific authorization rule that is available. For example, if there is an authorization rule for a field and an authorization rule for the model that the field belongs to, Amplify will evaluate against the field-level authorization rule. Review

Field-level authorization rules

to learn more.

If there are multiple authorization rules present, they will be logically OR'ed. Review

Configure multiple authorization rules

to learn more. For

userPools

and

oidc

authorization modes, the rules are evaluated in the sequence

authenticated

>

group(s)

>

owner(s)DefinedIn

>

group(s)DefinedIn

.

Global authorization rule (only for getting started)

To help you get started, you can define an authorization rule on the data schema that will be applied to all data models that

do not

have a model-level authorization rule. Instead of having a global authorization rule for all production environments, we recommend creating specific authorization rules for each model or field.

The global authorization rule below uses

allow.publicApiKey()

. This example allows anyone to create, read, update, and delete and is applied to every data model.

Copy

code example

const

schema

=

a

.

schema

(

{

// Because no model-level authorization rule is present

// this model will use the global authorization rule.

Todo

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

}

)

,

// Will use model-level authorization rule

Notes

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

// [Model-level authorization rule]

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

publicApiKey

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

// [Global authorization rule]

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

publicApiKey

(

)

]

)

Model-level authorization rules

Add an authorization rule to a model to apply the authorization rule to all fields of that model.

Copy

code example

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

createdBy

:

a

.

string

(

)

// [Model-level authorization rule]

// All fields (content, createdBy) will be protected by

// this authorization rule

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

publicApiKey

(

)

.

to

(

[

'read'

]

)

,

allow

.

owner

(

)

,

]

)

}

)

Field-level authorization rules

When an authorization rule is added to a field, it will strictly define the authorization rules applied on the field. Field-level authorization rules

do not

inherit model-level authorization rules. Meaning, only the specified field-level authorization rule is applied.

In the example below:

Owners are allowed to create, read, update, and delete Employee records they own

Any signed in user has read access and can read data with the exception of the

ssn

field

Only the

ssn

field has

owner

auth applied and this field-level auth rule means that model-level auth rules are not applied

Copy

code example

const

schema

=

a

.

schema

(

{

Employee

:

a

.

model

(

{

name

:

a

.

string

(

)

,

email

:

a

.

string

(

)

,

// [Field-level authorization rule]

// This auth rule will be used for the "ssn" field

// All other fields will use the model-level auth rule

ssn

:

a

.

string

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

owner

(

)

]

)

,

}

)

// [Model-level authorization rule]

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

"read"

]

)

,

allow

.

owner

(

)

]

)

,

}

)

;

Non-model authorization rules

Non-model

types are any types added to the schema without using

a.model()

. These consist of modifiers such as

a.customType()

,

a.enum()

,

a.query()

,

a.mutation()

, or

a.subscription()

.

Dynamic authorization rules such as

allow.owner()

,

allow.ownerDefinedIn()

,

allow.groupDefinedIn()

are not supported for

non-model

types.

Copy

code example

const

schema

=

a

.

schema

(

{

// ...

listCustomType

:

a

.

query

(

)

.

returns

(

a

.

ref

(

"CustomType"

)

.

array

(

)

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

entry

:

"./handler.js"

,

}

)

)

.

authorization

(

(

allow

)

=>

[

// Static auth rules - Supported

allow

.

guest

(

)

,

allow

.

publicApiKey

(

)

,

allow

.

authenticated

(

)

,

allow

.

group

(

"Admin"

)

,

allow

.

groups

(

[

"Teacher"

,

"Student"

]

)

,

// Dynamic auth rules - Not supported

allow

.

owner

(

)

,

allow

.

ownerDefinedIn

(

"owner"

)

,

allow

.

ownersDefinedIn

(

"otherOwners"

)

,

allow

.

groupDefinedIn

(

"group"

)

,

allow

.

groupsDefinedIn

(

"otherGroups"

)

,

]

)

,

}

)

;

There are TS warnings and validation checks in place that will cause a sandbox deployment to fail if unsupported auth rules are defined on custom queries and mutations.

Configure multiple authorization rules

When combining multiple authorization rules, they are "logically OR"-ed. In the following example:

Any user (using Amazon Cognito identity pool's unauthenticated roles) is allowed to read all posts

Owners are allowed to create, read, update, and delete their own posts

Copy

code example

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

title

:

a

.

string

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

guest

(

)

.

to

(

[

"read"

]

)

,

allow

.

owner

(

)

]

)

}

)

On the client side, make sure to always authenticate with the corresponding authorization mode.

Copy

code example

import

{

generateClient

}

from

'aws-amplify/data'

import

type

{

Schema

}

from

'@/amplify/data/resource'

// Path to your backend resource definition

const

client

=

generateClient

<

Schema

>

(

)

// Creating a post is restricted to Cognito User Pools

const

{

data

:

newPostResult

,

errors

}

=

await

client

.

models

.

Post

.

create

(

{

query

:

queries

.

createPost

,

variables

:

{

input

:

{

title

:

'Hello World'

}

}

,

authMode

:

'userPool'

,

}

)

;

// Listing posts is available to unauthenticated users (verified by Amazon Cognito identity pool's unauthenticated role)

const

{

data

:

listPostsResult

,

errors

}

=

await

client

.

models

.

Post

.

list

(

{

query

:

queries

.

listPosts

,

authMode

:

'identityPool'

,

}

)

;

IAM authorization

All Amplify Gen 2 projects enable IAM authorization for data access. This ensures that the Amplify console's

data manager

will be able to access your API. It also allows you to authorize other administrative or machine-to-machine access using your own IAM policies. See the

AWS AppSync Developer Guide

for details on how AWS AppSync works with IAM.

Authorization on custom types

Authorization rules are only supported on data models (model-level and field-level) and custom operations (queries, mutations and subscriptions). They are not fully supported on custom types, including custom types returned by custom operations. For example, consider a custom query that returns a custom type:

Copy

code example

const

schema

=

a

.

schema

(

{

Counter

:

a

.

customType

(

{

value

:

a

.

integer

(

)

,

}

)

.

authorization

(

...

)

,

// <-- not supported

getCounter

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

id

:

a

.

string

(

)

.

required

(

)

,

}

)

.

returns

(

a

.

ref

(

"Counter"

)

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

entry

:

"./getCounter.js"

,

}

)

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

authenticated

(

)

]

)

,

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

:

schema

,

authorizationModes

:

{

defaultAuthorizationMode

:

"userPool"

,

}

,

}

)

;

As you can see, the custom

Counter

type does not support the

.authorization()

modifier. Instead, behind the scenes, Amplify will add appropriate authorization rules to

Counter

to allow authenticated users to access it. That means that any signed-in user will be able to access the custom operation and all fields of the custom type.

Note

: IAM authorization is not currently supported for custom operations that return custom types if

defaultAuthorizationMode

is not

iam

. See

GitHub issue #2929

for details and suggested workarounds.

Learn more about specific authorization strategies

Public data access

The public authorization strategy grants everyone access to the API, which is protected behind the scenes with an API key. You can also override the authorization provider to use an unauthenticated IAM role from Cognito instead of an API key for public access.

Per-user/per-owner data access

The owner authorization strategy restricts operations on a record to only the record's owner. When configured, the owner field (default 'owner') will automatically be added and populated with the identity of the created user. The API will authorize against the 'owner' field to allow or deny operations.

Multi-user data access

The 'ownersDefinedIn' rule grants a set of users access to a record by automatically creating an 'owners' field to store the allowed record owners. You can override the default owners field name by specifying 'inField' with the desired field name to store the owner information. You can dynamically manage which users can access a record by updating the owner field.

Signed-in user data access

The 'private' authorization strategy restricts record access to only signed-in users authenticated through IAM, Cognito, or OpenID Connect, applying the authorization rule to all users. It provides a simple way to make data private to all authenticated users.

User group-based data access

The user group authorization strategy allows restricting data access to specific user groups or groups defined dynamically on each data record. Both static and dynamic group authorization options are available, with some limitations around real-time subscriptions when using dynamic group authorization.

Custom data access using Lambda functions

Define a custom authorization rule with a Lambda function.

Use OpenID Connect as an authorization provider

Use OpenID Connect with 'private', 'owner', and 'group' authorization strategies.

Configure custom identity and group claims

Amplify Data allows you to configure custom identity and group claims instead of using the default Cognito claims, which can be useful if you want to populate claims from an external source like a database or 3rd party auth provider. The example shows how to check the 'user_id' identity claim and the 'user_groups' group claim that could come from a custom pre token generation Lambda trigger. Defining these custom claims provides more flexibility in authorization rules.

Grant Lambda function access to API and Data

Amplify Data uses a 'deny-by-default' authorization model. Function access must be explicitly defined in the schema.
