---
title: Sandbox features - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/features/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:08.824901+00:00
kind: extracted-doc
---

# Sandbox features - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/features/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:08.824901+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/features/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/concepts/external-identity-providers/
- https://docs.amplify.aws/nextjs/build-a-backend/functions/environment-variables-and-secrets/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/secrets-and-vars/
- https://docs.amplify.aws/nextjs/build-a-backend/functions/streaming-logs/
- https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/setup/
- https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/seed/

Captured summary:

- Sandbox features - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Sandbox features ✨ Use with AI Sandbox environments include additional features for managing secrets, deploying multiple sandboxes, config generation, and client codegen for your Amplify app.
- Secure secrets in your sandbox Secrets set in a sandbox do not show up in the Amplify Console.

Extracted text:

Sandbox features - AWS Amplify Gen 2 Documentation

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

Sandbox features

✨

Use with AI

Sandbox environments include additional features for managing secrets, deploying multiple sandboxes, config generation, and client codegen for your Amplify app.

Secure secrets in your sandbox

Secrets set in a sandbox do not show up in the Amplify Console. You can view them in the AWS Systems Manager (SSM) Parameter Store console.

Amplify Gen 2 offers secure secret storage to manage sensitive data like API keys and database credentials. Secrets are similar to environment variables, but they are encrypted AWS Systems Manager Parameter Store key value pairs. Secrets are stored in AWS Parameter Store under the

/amplify

prefix.

Set secrets

You can add secrets to your sandbox environment using the following command:

Copy

code example

npx ampx sandbox secret set foo

? Enter secret value: ###

Done!

npx ampx sandbox secret set bar

? Enter secret value: ###

Done!

After these commands, your sandbox will have two secrets named

foo

and

bar

.

List secrets

You can list all of the secret names available in your sandbox environment with the following command:

Copy

code example

npx ampx sandbox secret list

- foo

- bar

Retrieve a secret

Note:

This will print a secret value in plain text to the terminal. Do not use this command anywhere that terminal logs may be stored (such as CI/CD jobs).

To show the value of a secret, run the following command.

Copy

code example

npx ampx sandbox secret get foo

name: foo

version: 1

value: abc123

lastUpdated: Mon Nov 13 2023 22:19:12 GMT-0800 (Pacific Standard Time)

Remove secret

To remove a secret from from the sandbox, run the following command in your terminal:

Copy

code example

npx ampx sandbox secret remove foo

Remove all secrets

To remove all secrets from the sandbox, run the following command in your terminal:

Copy

code example

npx ampx sandbox secret remove --all

Reference secrets

Once you have set a secret, you can reference the secret in your backend definition using the

secret()

function. The following example shows how to set up social sign-in with authentication in your app. Depending on your environment, Amplify will automatically load the correct secret value.

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

Copy

highlighted code example

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

The

secret()

function does NOT retrieve the value of the secret. It places a reference to the secret value in the backend definition. The secret value is only resolved during deployment of your backend.

The

secret()

function can only be used in specific places in your backend definition such as

configuring auth providers

and

function secrets

.

To deploy a backend that uses

secret()

references via Amplify hosting, the secret values must be

configured for the Amplify app or branch

Work with multiple AWS profiles

Sometimes you might have multiple AWS profiles set up locally. To run

ampx sandbox secret

commands, use the

--profile

flag to deploy to a specific profile. For example, let's say you have two AWS profiles set up locally—

default

and

work

. To add secrets to the sandbox in the

work

profile, run the following command in your terminal:

Copy

code example

npx ampx sandbox secret set foo --profile work

Work with multiple named sandboxes

Provisioning multiple sandboxes per app is possible but not recommended because managing multiple ephemeral environments for a single developer introduces complexity. With multiple sandboxes, it can be difficult to keep track of what code version or configuration is deployed where. Sticking to a single sandbox per developer keeps your workflows simpler.

You can create multiple sandboxes if you want to have different features or test environments available in different sandboxes. By default, your sandbox is named based on the local machine username. To override this name, use the

--identifier

option:

Copy

code example

npx ampx sandbox --identifier feature1sandbox

This will start a sandbox named

feature1sandbox

.

Once the deployment completes, exit sandbox and run the following command in the terminal:

Copy

code example

npx ampx sandbox --identifier feature2sandbox

After successful deployment, you will have two sandboxes

feature1sandbox

and

feature2sandbox

. You can switch between them but only one can be running at a time.

Secret management with named sandboxes

When working with multiple sandboxes, secrets must be configured for each one. All of the

sandbox secret

commands accept the

--identifier

argument to manage secrets for named sandboxes. For example, to add a secret to

feature1sandbox

, use:

Copy

code example

npx ampx sandbox --identifier feature1sandbox secret set baz

Stream function logs

Amplify offers the ability to stream function logs directly to your terminal or a file.

Learn more about streaming function logs

.

Generate client config

The client config, or

amplify_outputs.json

file, contains the configuration strings for interacting with AWS resources specific to an environment. The Amplify client libraries need the client config in order to use the library APIs to connect to backend resources. By default, the cloud sandbox generates the client configuration file at the root of the project (such as

@/amplify_outputs.json

). If you want to place the file at a different path (such as for a monorepo or Android app), run the following command in the terminal:

Terminal

Copy

Terminal

code example

npx ampx sandbox --outputs-out-dir ./path/to/config --outputs-format ["json", "dart"]

Alternatively, if you want to generate the config for a branch environment to test against, run the following command in the terminal.

Copy

code example

npx ampx generate outputs --app-id <your-amplify-app-id> --branch main --format ["json", "dart"] --out-dir ./path/to/config

Deployment Environment

Alternatively, if you want to generate the config for a branch environment to test against, you can run the following command below in the terminal:

For Web and React Native, generating the config with the default format and output directory.

Terminal

Copy

Terminal

code example

npx ampx generate outputs --app-id <app-id> --branch main

Generate client codegen

Amplify Gen 2 introduces a fully typed experience for data that no longer requires an explicit codegen step, unlike in Amplify Gen 1. You will only need this command if you are building a mobile app or have Gen 1 requirements.

Codegen generates native code for Swift (iOS), Java (Android), and JavaScript that represents your GraphQL API's data models. It can also generate GraphQL statements (queries, mutations, and subscriptions) so that you don't have to manually code them.

Once your sandbox completes a deployment, you can run the following command in the terminal to generate client code that is specific to your needs:

Copy

code example

npx ampx generate graphql-client-code

--format [choices: "modelgen", "graphql-codegen", "introspection"]

Delete a sandbox

You can delete a cloud sandbox environment in several ways:

Ctrl+C your sandbox and choose to delete resources.

Run

npx ampx sandbox delete

or

npx ampx sandbox delete --name

Visit the Amplify console and

delete sandboxes

.

PREVIOUS

Use cloud sandbox in dev environment

NEXT

Sandbox Seed
