---
title: Amplify Docs - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:19:51.415364+00:00
kind: extracted-doc
---

# Amplify Docs - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:19:51.415364+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/start/quickstart/
- https://docs.amplify.aws/nextjs/how-amplify-works/concepts/
- https://docs.amplify.aws/nextjs/build-a-backend/data/set-up-data/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/set-up-auth/
- https://docs.amplify.aws/nextjs/build-ui/
- https://docs.amplify.aws/nextjs/deploy-and-host/hosting/
- https://docs.amplify.aws/nextjs/deploy-and-host/sandbox-environments/setup/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/branch-deployments/
- https://docs.amplify.aws/nextjs/build-a-backend/add-aws-services/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/custom-pipelines/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/mono-and-multi-repos/

Captured summary:

- Amplify Docs - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Amplify Documentation for Next.js AWS Amplify is everything you need to build web and mobile apps.
- You can build a fullstack app using Amplify backend building capabilities, or you can deploy your React and Next.js web apps using Amplify Hosting.

Extracted text:

Amplify Docs - AWS Amplify Gen 2 Documentation

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

Amplify Documentation for

Next.js

AWS Amplify is everything you need to build web and mobile apps. Easy to start, easy to scale.

You can build a fullstack app using Amplify backend building capabilities, or you can deploy your React and Next.js web apps using Amplify Hosting.

Build a new app

Toggle getting started guides navigation

React

Next.js

Angular

Vue

JavaScript

React Native

Flutter

Android

Swift

Deploy your app

How Amplify works >

Build fullstack apps with your framework of choice

You can use AWS Amplify with popular web and mobile frameworks like JavaScript, Flutter, Swift, and React. Build, connect, and host fullstack apps on AWS. Get started by selecting your preferred framework.

Features

Code-first DX

The fullstack TypeScript developer experience lets you focus on your app code instead of infrastructure.

Fullstack Git deployments

Deploy your frontend and backend together on every code commit. Your Git branch is the source of truth.

Faster local development

Per-developer cloud sandbox environments let you quickly iterate during development.

Develop

TypeScript-first fullstack experience

Write TypeScript across your app's frontend and backend. Get schema validation, dot completion, and end-to-end types while you code.

Real-time data for modern apps

Sync frontend state to real-time backend updates. Just write TypeScript without thinking about WebSockets.

Authn and authz for secure apps

Choose the auth strategy (such as passwords, social, email links) and control data access based on users and groups.

Auto-generate CRUD forms wired to data

Map CRUD forms to your data model with form-level validations and error states built in.

Deploy

SSR/SSG/ISR hosting support

Deploy Next.js, Nuxt, React, Vue.js, Angular (and more) apps by simply connecting your Git repository.

Faster iterations with per-developer sandboxes

Per-developer cloud sandboxes provide high fidelity and faster deployment times to make local iteration quick.

Zero-config fullstack branches

Fullstack deployments from your Git branch. Autodeploy Git branches to set up staging, development, and production environments.

GUI to manage your data

Manage your app data, users and groups, and files in a single console.

Customize

Add any AWS service with CDK

Extend or customize with the AWS CDK to access 200+ AWS services.

Bring your own pipelines

Use your own pipelines to set up cross-account or multi-region, stage-based deployments.

Monorepo and multi-repo support

Enable support for all types of fullstack team workflows: monorepos, micro frontends, multi-repos, and more.

amplify/backend.ts

Copy

amplify/backend.ts

code example

import

*

as

sns

from

'aws-cdk-lib/aws-sns'

;

import

*

as

sqs

from

'aws-cdk-lib/aws-sqs'

;

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

'./auth/resource.js'

;

import

{

data

}

from

'./data/resource.js'

;

const

backend

=

defineBackend

(

{

auth

,

data

}

)

;

const

customResourceStack

=

backend

.

createStack

(

'MyCustomResources'

)

;

new

sqs

.

Queue

(

customResourceStack

,

'CustomQueue'

)

;

new

sns

.

Topic

(

customResourceStack

,

'CustomTopic'

)

;
