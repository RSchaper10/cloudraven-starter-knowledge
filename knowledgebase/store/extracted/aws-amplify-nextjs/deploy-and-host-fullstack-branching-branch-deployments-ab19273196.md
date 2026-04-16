---
title: Fullstack branch deployments - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/branch-deployments/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:19:55.564471+00:00
kind: extracted-doc
---

# Fullstack branch deployments - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/branch-deployments/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:19:55.564471+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/branch-deployments/
- https://docs.amplify.aws/nextjs/start/quickstart/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/secrets-and-vars/

Captured summary:

- Fullstack branch deployments - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Fullstack branch deployments ✨ Use with AI Amplify code-first DX (Gen 2) offers fullstack branch deployments that allow you to automatically deploy infrastructure and application code changes from feature branches.
- This enables testing changes in an isolated environment before merging to the main branch.

Extracted text:

Fullstack branch deployments - AWS Amplify Gen 2 Documentation

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

Fullstack branch deployments

✨

Use with AI

Amplify code-first DX (Gen 2) offers fullstack branch deployments that allow you to automatically deploy infrastructure and application code changes from feature branches. This enables testing changes in an isolated environment before merging to the main branch.

Set up feature branch deployments

After you've deployed your

first branch

, you can manually connect more, but the recommended workflow is to use the

branch auto-detection

feature.

Log in to the

Amplify console

and choose your app.

Navigate to

App settings > Branch settings

, select

Edit

and enable

Branch auto-detection

and

Branch auto-disconnection

. The following video uses the default settings, which will connect any branch in your repo automatically. Branch auto-disconnection will ensure that if you delete a branch from your repository, the branch will also be deleted.

You can also define a pattern to connect only certain branches. For example, setting

dev

,

staging

, and

feature/*

will automatically connect all three branch types. Your

dev

and

staging

branches, as well as any branch that begins with

feature/

, will be connected.

Push a commit to your

feature/A

and

staging

branches that match the pattern. You should start seeing deployments on the console page. You will now have three fullstack branches deployed.

Promote changes to production

In Gen 2, promoting changes to production follows the normal Git-based workflow.

Make a change in your

feature/A

branch.

Terminal

Copy

Terminal

code example

git checkout -b feature/A

## make some edits to your code

git commit --am "New data model to track comments for todos added"

git push origin feature/A

Submit a pull request to your

main

branch. Once your team has validated the changes, merge the pull request to

main

. This will initiate a build on your

main

branch and update any frontend or backend resources that you changed.

Generate client config

You can generate the config for a branch environment by running:

For Web and React Native, generating the config with the default format and output directory.

Terminal

Copy

Terminal

code example

npx ampx generate outputs --app-id <your-amplify-app-id> --branch <your-git-branch-name> --out-dir <path/to/config>

NEXT

Secrets and environment vars
