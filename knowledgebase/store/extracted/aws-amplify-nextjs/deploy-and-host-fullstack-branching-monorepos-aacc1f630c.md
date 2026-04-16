---
title: Monorepo setup - Next.js - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/monorepos/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:11.422482+00:00
kind: extracted-doc
---

# Monorepo setup - Next.js - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/monorepos/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:11.422482+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/monorepos/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/mono-and-multi-repos/
- https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/pr-previews/

Captured summary:

- Monorepo setup - Next.js - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Monorepo setup ✨ Use with AI Some teams choose a monorepo approach, or single repositories that contain multiple packages or components to simplify the deployment process for shared libraries and components.
- Without a monorepo, you have to deploy each package individually, keep track of package versions and dependencies across packages, and ensure version compatibility.

Extracted text:

Monorepo setup - Next.js - AWS Amplify Gen 2 Documentation

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

Monorepo setup

✨

Use with AI

Some teams choose a monorepo approach, or single repositories that contain multiple packages or components to simplify the deployment process for shared libraries and components. Without a monorepo, you have to deploy each package individually, keep track of package versions and dependencies across packages, and ensure version compatibility. This can become exponentially more complex as the number of packages grows. With a monorepo, all packages and dependencies are contained within a single repository.

Amplify Gen 2 supports monorepo workflows for fullstack builds with monorepo tools such as Nx and yarn workspaces. When building with Gen 2, we recommend creating the

amplify/

folder in a shared workspace. We will use the following example for this guide:

Copy

code example

├── apps/

│ ├── admin-dashboard/

│ │ ├── next.config.mjs

│ │ └── package.json

│ └── marketing-site/

│ ├── astro.config.mjs

│ └── package.json

├── packages/

│ └── my-shared-backend/

│ ├── amplify/

│ │ ├── auth/

│ │ │ └── resource.ts

│ │ ├── data/

│ │ │ └── resource.ts

│ │ └── backend.ts

│ |── package.json

└── tsconfig.json

└── package.json

Monorepos require a slightly different setup. We are going to deploy 3 Amplify apps:

my-shared-backend

admin-dashboard

marketing-site

Deploy backend app

The first app,

my-shared-backend

, will be the only app that updates changes to the backend. The other apps will only run frontend builds that point to the shared backend.

To get started, deploy the shared backend Amplify app. With Gen 2, you can now setup backend-only CI/CD apps. Navigate to the Amplify console and select

Create new app

.

Once you connect your repository, select your monorepo project. Check the box that says

My app is a monorepo

and enter the path to your amplify backend.

Your build settings should be automatically detected. Save and deploy.

Deploy frontend apps

For the frontend apps, connect the frontend projects in the Amplify console separately, and update the build commands to include:

Terminal

Copy

Terminal

code example

npx ampx generate outputs --branch main --app-id BACKEND-APP-ID

To locate the

App ID

for your backend application, navigate to the Amplify console and select your

backend-app

. On the Overview page, the

App ID

is displayed under the project name.

Terminal

Copy

Terminal

code example

npx ampx generate outputs --branch main --app-id BACKEND-APP-ID

Sharing schema type definitions

If you're using Amplify Data, we recommend adding a

paths

entry in your

tsconfig.json

file that points to the

amplify/data/resource.ts

file to easily access your schema type definitions from your frontend apps.

tsconfig.json

Copy

tsconfig.json

code example

{

"compilerOptions": {

"paths": {

"@/data-schema": ["./packages/my-shared-backend/amplify/data/resource"]

}

}

}

You can then import the

Schema

type from this path in your frontend code to get code completion and strong typing for your API calls:

apps/admin-dashboard/page.tsx

Copy

apps/admin-dashboard/page.tsx

code example

import

{

generateClient

}

from

"aws-amplify/data"

;

import

type

{

Schema

}

from

"@/data-schema"

;

const

client

=

generateClient

<

Schema

>

(

)

;

const

createTodo

=

async

(

)

=>

{

await

client

.

models

.

Todo

.

create

(

{

content

:

window

.

prompt

(

"Todo content?"

)

,

isDone

:

false

,

}

)

;

}

PREVIOUS

Separate frontend and backend teams

NEXT

Fullstack previews
