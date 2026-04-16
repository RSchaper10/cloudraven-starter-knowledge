---
title: Fullstack previews - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/pr-previews/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:09.945647+00:00
kind: extracted-doc
---

# Fullstack previews - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/pr-previews/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:09.945647+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/pr-previews/
- https://docs.amplify.aws/nextjs/start/quickstart/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/monorepos/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/custom-pipelines/

Captured summary:

- Fullstack previews - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Fullstack previews ✨ Use with AI With fullstack previews, you can set up ephemeral fullstack environments on every pull request.
- This allows you to test features in isolation from production.

Extracted text:

Fullstack previews - AWS Amplify Gen 2 Documentation

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

Fullstack previews

✨

Use with AI

With fullstack previews, you can set up ephemeral fullstack environments on every pull request. This allows you to test features in isolation from production. Once fullstack previews are enabled, your typical workflow would look like the following diagram:

Your

main

(production branch) and

featureA

branch are deployed on Amplify.

You and your team work on

featureA

until it's ready.

The

featureA

branch is updated to

main

HEAD and then a pull request to

main

is opened.

The pull request preview is deployed on Amplify and available at

pr-1.appid.amplifyapp.com

.

Once the pull request is merged into

main

, the request is closed and the fullstack environment is also automatically torn down.

Prerequisites

Before you get started, make sure you have the following:

A fullstack Amplify app deployed

Ensure that your git repository is private. For security purposes, fullstack previews are disabled for public repositories with Amplify backend templates.

Enable fullstack previews

To enable fullstack web previews for your Amplify app, follow these steps:

Login to the

Amplify console

and select your app.

Navigate to

Hosting > Previews

. Select the

main

branch and click on

Edit settings

.

Click on the

Pull request previews

toggle button and choose

Confirm

to enable previews.

Done! You have successfully enabled previews on the production branch.

Ship updates to the

dev

branch. Now, when you create a pull request for the

main

branch, Amplify will build and deploy your fullstack PR and provide you with a preview URL.

For

GitHub repositories only

, you can access your preview URL directly on the pull request from the Amplify Hosting's bot comment:

After the pull request is merged or closed, the preview URL is deleted and any ephemeral fullstack environment is also deleted.

Share backend resources across Preview branches

Fullstack previews allow teams a way to preview changes from pull requests before merging code to a production branch. Pull requests let you tell others about changes you’ve pushed to a branch in a repository and the changes can be reviewed by accessing the preview URL. When previews are enabled on a git branch, by default every pull request created against the git branch creates an ephemeral fullstack environment.

In some instances, you may not want to deploy new resources for every preview branch. For example, you might want all your preview branches to point to the backend resources deployed by the

dev

branch so you can reuse seed data, users, and groups.

To achieve this, you can update your app build settings to reuse backend resources across your preview branches. In the Amplify console, select your app on the

All apps

page. From the

App overview

page, select

Hosting > Build settings

to view your app's build specification YAML file.

Update the build settings for the

backend

phase to run

npx ampx generate outputs --branch dev app-id $AWS_APP_ID

to generate the

amplify_outputs.json

file for all preview branches. After this update, any new deployed preview branches will not deploy backend resources as part of the build and instead will use the deployed backend resources from the

dev

branch.

amplify.yml

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

Copy

highlighted code example

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

npx ampx generate outputs --branch dev --app-id $AWS_APP_ID

;;

*)

echo "Deploying to staging branch..."

npx ampx generate outputs --branch staging --app-id $AWS_APP_ID

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

.amplify

-

hosting

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

Monorepo setup

NEXT

Custom pipelines
