---
title: Secrets and environment vars - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/secrets-and-vars/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:09.410281+00:00
kind: extracted-doc
---

# Secrets and environment vars - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/secrets-and-vars/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:09.410281+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/secrets-and-vars/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/branch-deployments/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/share-resources/

Captured summary:

- Secrets and environment vars - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Secrets and environment vars ✨ Use with AI Amplify Gen 2 offers centralized management of secrets and environment variables for all fullstack branches.
- Secrets allow you to securely configure environment-specific values like social sign-in keys, function environment variables, function secrets, and other sensitive data needed by your application across environments.

Extracted text:

Secrets and environment vars - AWS Amplify Gen 2 Documentation

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

Secrets and environment vars

✨

Use with AI

Amplify Gen 2 offers centralized management of secrets and environment variables for all fullstack branches. Secrets allow you to securely configure environment-specific values like social sign-in keys, function environment variables, function secrets, and other sensitive data needed by your application across environments.

FAQ

How is this different from Amplify Gen 1?

In Amplify Gen 1, you need to define environment variables and secrets using the CLI and store keys in both AWS Parameter Store and a local

team-provider.json

file. We have streamlined this workflow in Amplify Gen 2 by centralizing the management of secrets and environment variables in the Amplify console.

Close accordion

Set secrets

You can set secrets for your fullstack branch deployments or your local dev server.

Branch environment

You can add secrets for branch deployments in the Amplify console. From the App home page, navigate to

Hosting > Secrets

, and then choose the

Manage secrets

button. You can add a secret key or value that applies to all deployed branches or just specific branches.

Secrets are stored in AWS Systems Manager Parameter Store under the following naming conventions:

Secrets that apply to all branches:

/amplify/shared/<app-id>/<secret-key>

Secrets that apply to a specific branch:

/amplify/<app-id>/<branchname>-branch-<unique-hash>/<secret-key>

Local environment

Secrets set in a sandbox do not show up in the Amplify console. You can view them in the AWS Parameter Store console.

When testing features locally, you might want to test with real secrets. You can add secrets while running the cloud sandbox with the following command:

Terminal

Copy

Terminal

code example

npx ampx sandbox secret set foo

? Enter secret value: ###

Done!

> npx ampx sandbox secret set bar

? Enter secret value: ###

Done!

Access secrets

Once you have set a secret, you can access the values in code by calling the

secret()

function. The following example shows how to set up social sign-in with authentication in your app. Depending on your environment, Amplify will automatically load the correct secret value with no extra configuration.

Copy

code example

import

{

defineAuth

,

secret

}

from

'@aws-amplify/backend'

;

export

const

auth

=

defineAuth

(

{

loginWith

:

{

email

:

true

,

externalProviders

:

{

facebook

:

{

clientId

:

secret

(

'foo'

)

,

clientSecret

:

secret

(

'bar'

)

}

}

}

}

)

;

Remove secrets

When deleting branch environments or sandbox environments, you need to manually delete the secrets as well.

Branch environment

Secrets that are used in branch deployments can be managed directly in the Amplify console. You can remove them under

Secret management

by choosing

Remove

.

Local environment

To remove a secret in your local environment, run the following command in your terminal:

Terminal

Copy

Terminal

code example

npx ampx sandbox secret remove foo

Set environment variables

Note: do not store secret values in environment variables. Environment variables values are rendered in plaintext to the build artifacts and can be accessed by anyone with access to the build artifacts or

get-app

command.

Environment variables work like key-value pairs to help manage configurable settings across different deployment environments, including development, staging, and production. Unlike secrets, which store sensitive data, environment variables are typically nonconfidential and are used for controlling application behavior in different environments. Another key difference is that environment variables are stored and managed by the Amplify managed service. You can set environment variables in the Amplify console (view the

AWS Amplify Hosting User Guide

for detailed instructions).

Access environment variables

You can enable access to environment variables for your fullstack branch deployments or your local dev server.

Branch environment

You can manage your branch environment access through the Amplify console.

First, create an environment variable in the Amplify console (in this example, you will name it

REACT_APP_TEST_VARIABLE

)

Next, navigate to the Build Settings in console (or to the

amplify.yml

file) and update the build settings to pipe the environment variable into a file. Here is an example of writing it into an

.env

file:

amplify.yml

build

:

commands

:

Copy

highlighted code example

-

echo "REACT_APP_TEST_VARIABLE=$REACT_APP_TEST_VARIABLE"

>

>

.env

-

npm run build

With the implementation above, the environment variable is written in a

.env

file. However, you can write it to any file depending on your platform.

For Flutter, you can still use

.env

with an external package or generate your configuration file in Dart or JSON format.

For Android, you can use Build Configurations or Gradle variables.

For iOS, you can update your plist file with the necessary code or create a configuration file in JSON format.

Now the

.env

can access the environment variable through

process.env

in your client code:

Copy

code example

console

.

log

(

'REACT_APP_TEST_VARIABLE'

,

process

.

env

.

REACT_APP_TEST_VARIABLE

)

;

Local environment

When working on your local machine, you must manually load the sandbox's environment variables. First, add the environment variable in your

.env.local

file. Then, a library such as

@dotenvx/dotenvx

can load the environment variables, which you can then reference with

process.env

.

Terminal

Copy

Terminal

code example

npx dotenvx run --env-file=.env.local -- ampx sandbox

PREVIOUS

Fullstack branch deployments

NEXT

Share resources across branches
