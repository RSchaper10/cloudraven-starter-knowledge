---
title: Share resources across branches - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/share-resources/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:10.891511+00:00
kind: extracted-doc
---

# Share resources across branches - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/share-resources/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:10.891511+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/secrets-and-vars/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/mono-and-multi-repos/

Captured summary:

- Share resources across branches - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Share resources across branches ✨ Use with AI In some instances, you may not want to deploy new resources for every branch.
- For example, you might want all your feature branches to point to the backend resources deployed by the dev branch so you can reuse seed data, users, and groups.

Extracted text:

Share resources across branches - AWS Amplify Gen 2 Documentation

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

Share resources across branches

✨

Use with AI

In some instances, you may not want to deploy new resources for every branch. For example, you might want all your

feature

branches to point to the backend resources deployed by the

dev

branch so you can reuse seed data, users, and groups.

You can update your app build settings to share resources across branches. From the Amplify console, go to your

App overview

page, select

Build settings

under the

Hosting

for viewing your app's build specification YAML file.

Update the build settings for the

backend

phase to run

npx ampx generate outputs --branch dev app-id $AWS_APP_ID

to generate the

amplify_outputs.json

file for all branches other than

main

or

dev

. After this update, any new deployed branches will not deploy backend resources as part of the build and instead will use the deployed backend resources from the

dev

branch. Update the build settings for the

backend

phase to run

npx ampx generate outputs --branch dev app-id $AWS_APP_ID

to generate the

amplify_outputs.json

file for all branches other than

main

or

dev

. After this update, any new deployed branches will not deploy backend resources as part of the build and instead will use the deployed backend resources from the

dev

branch.

amplify.yml

Copy

amplify.yml

code example

version

:

1

backend

:

phases

:

build

:

commands

:

-

'npm ci --cache .npm --prefer-offline'

-

'echo $AWS_BRANCH'

-

|

case "${AWS_BRANCH}" in

main)

echo "Deploying main branch..."

npx ampx pipeline-deploy --branch $AWS_BRANCH --app-id $AWS_APP_ID

;;

dev)

echo "Deploying dev branch..."

npx ampx pipeline-deploy --branch $AWS_BRANCH --app-id $AWS_APP_ID

;;

pr-*)

echo "Deploying pull request branch..."

npx ampx generate outputs --branch previews --app-id $AWS_APP_ID

;;

*)

echo "Deploying to staging branch..."

npx ampx generate outputs --branch dev --app-id $AWS_APP_ID

;;

esac

frontend

:

phases

:

build

:

commands

:

-

'npm run build'

artifacts

:

baseDirectory

:

.next

files

:

-

'**/*'

cache

:

paths

:

-

.next/cache/

**/*

-

.npm/

**/*

-

node_modules/

**/*

PREVIOUS

Secrets and environment vars

NEXT

Separate frontend and backend teams
