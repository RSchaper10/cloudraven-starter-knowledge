---
title: Next.js App Router - Next.js - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:01.491224+00:00
kind: extracted-doc
---

# Next.js App Router - Next.js - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:01.491224+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components/
- https://docs.amplify.aws/nextjs/start/account-setup/
- https://docs.amplify.aws/nextjs/how-amplify-works/concepts/

Captured summary:

- Next.js App Router - Next.js - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Next.js App Router ✨ Use with AI Pre-requisites This Quickstart guide will walk you through how to build a task list application with TypeScript, Next.js App Router with Client Components , and React.
- Before you begin, make sure you have the following installed: Node.js v14.x or later npm v6.14.4 or later git v2.14.1 or later If you are new to these technologies, we recommend you go through the official React , Next.js , and TypeScript tutorials first.

Extracted text:

Next.js App Router - Next.js - AWS Amplify Gen 2 Documentation

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

Next.js App Router

✨

Use with AI

Pre-requisites

This Quickstart guide will walk you through how to build a task list application with TypeScript, Next.js

App Router with Client Components

, and React. Before you begin, make sure you have the following installed:

Node.js

v14.x or later

npm

v6.14.4 or later

git

v2.14.1 or later

If you are new to these technologies, we recommend you go through the official

React

,

Next.js

, and

TypeScript

tutorials first.

Deploy a fullstack app to AWS

We've created a starter "To-do" application to help get started faster. First, you will create a repository in your GitHub account using our starter Next template.

1. Create the repository

Use our starter template to create a repository in your GitHub account. This template scaffolds

create-next-app

with Amplify backend capabilities.

Create repository from template

Use the form in GitHub to finalize your repo's creation.

2. Deploy the starter app

Now that the repository has been created, deploy it with Amplify.

Deploy to AWS

Select

Start with an existing app

>

GitHub

. After you give Amplify access to your GitHub account via the popup window, pick the repository and

main

branch to deploy. Make no other changes and click through the flow to

Save and deploy

.

3. View deployed app

While you are waiting for your app to deploy (~5 mins)

Learn about the project structure

Let's take a tour of the project structure in this starter repository by opening it on GitHub. The starter application has pre-written code for a to-do list app. It gives you a real-time database with a feed of all to-do list items and the ability to add new items.

Copy

code example

├── amplify/ # Folder containing your Amplify backend configuration

│ ├── auth/ # Definition for your auth backend

│ │ └── resource.tsx

│ ├── data/ # Definition for your data backend

│ │ └── resource.ts

| ├── backend.ts

│ └── tsconfig.json

├── src/ # React UI code

│ ├── App.tsx # UI code to sync todos in real-time

│ ├── index.css # Styling for your app

│ └── main.tsx # Entrypoint of the Amplify client library

├── package.json

└── tsconfig.json

Close accordion

When the build completes, visit the newly deployed branch by selecting "View deployed URL". Since the build deployed an API, database, and authentication backend, you will be able to create new to-do items.

In the Amplify console, click into the deployment branch (in this case

main

) > select

Data

in the left-hand menu >

Data manager

to see the data entered in your database.

Make frontend updates

Let's learn how to enhance the app functionality by creating a delete flow for to-do list items.

4. Set up local environment

Now let's set up our local development environment to add features to the frontend. Click on your deployed branch and you will land on the

Deployments

page which shows you your build history and a list of deployed backend resources.

At the bottom of the page you will see a tab for

Deployed backend resources

. Click on the tab and then click the

Download amplify_outputs.json file

button.

Clone the repository locally.

Terminal

Copy

Terminal

code example

git clone https://github.com/<github-user>/amplify-next-template.git

cd amplify-next-template && npm install

Now move the

amplify_outputs.json

file you downloaded above to the root of your project.

Copy

code example

├── amplify

├── src

├── amplify_outputs.json <== backend outputs file

├── package.json

└── tsconfig.json

Learn more

amplify_outputs.json

The

amplify_outputs.json

file contains backend endpoint information, publicly-viewable API keys, authentication flow information, and more. The Amplify client library uses this outputs file to connect to your Amplify Backend. You can review how the outputs file is imported within the

main.tsx

file and then passed into the

Amplify.configure(...)

function of the Amplify client library.

Close accordion

5. Implement delete functionality

Go to the

app/page.tsx

file and add in a new

deleteTodo

functionality and pass function into the

<li>

element's

onClick

handler.

app/page.tsx

function

App

(

)

{

// ...

Copy

highlighted code example

function

deleteTodo

(

id

:

string

)

{

client

.

models

.

Todo

.

delete

(

{

id

}

)

}

return

(

<

main

>

<

h1

>

My todos

</

h1

>

<

button

onClick

=

{

createTodo

}

>

+ new

</

button

>

<

ul

>

{

todos

.

map

(

todo

=>

<

li

Copy

highlighted code example

onClick

=

{

(

)

=>

deleteTodo

(

todo

.

id

)

}

key

=

{

todo

.

id

}

>

{

todo

.

content

}

</

li

>

)

}

</

ul

>

<

div

>

🥳 App successfully hosted. Try creating a new todo.

<

br

/>

<

a

href

=

"

https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components/

"

>

Review next step of this tutorial.

</

a

>

</

div

>

</

main

>

)

}

See the complete amplify/data/resources.ts

Open the

amplify/data/resource.ts

file in your text editor, and you will see a default data model generated for you.

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

// API Key is used for allow.publicApiKey() rules

apiKeyAuthorizationMode

:

{

expiresInDays

:

30

}

}

}

)

;

The schema generated by Amplify is for a to-do app. A schema is a blueprint for how our app's data will be organized. Within the schema, we will define models that will correspond to a database table—

Todo

in the above code. Finally, we will define fields, which are attributes that each data instance will have—in the generated code, the field is

content

. Each field will have a type attached to it—in the above examples, we are stating that the

content

field is a string.

Close accordion

Try out the deletion functionality now by starting the local dev server:

Terminal

Copy

Terminal

code example

npm run dev

This should start a local dev server at

http://localhost:3000

.

6. Implement login UI

The starter application already has a pre-configured auth backend defined in the

amplify/auth/resource.ts

file. We've configured it to support email and password login but you can extend it to support a variety of login mechanisms, including Google, Amazon, Sign In With Apple, and Facebook.

The fastest way to get your login experience up and running is to use our Authenticator UI component. To properly integrate it with Next.js App Router, we'll create a client component wrapper and use it in the layout.

First, create an AuthenticatorWrapper.tsx file in your app directory:

app/AuthenticatorWrapper.tsx

Copy

app/AuthenticatorWrapper.tsx

code example

"use client"

import

{

Authenticator

}

from

"@aws-amplify/ui-react"

;

export

default

function

AuthenticatorWrapper

(

{

children

,

}

:

{

children

:

React

.

ReactNode

;

}

)

{

return

<

Authenticator

>

{

children

}

</

Authenticator

>

;

}

Next, update your app/layout.tsx file to import and use the AuthenticatorWrapper component:

app/layout.tsx

import

React

from

"react"

;

import

{

Amplify

}

from

"aws-amplify"

;

import

"./app.css"

;

Copy

highlighted code example

import

AuthenticatorWrapper

from

"./AuthenticatorWrapper"

;

import

"@aws-amplify/ui-react/styles.css"

;

import

outputs

from

"@/amplify_outputs.json"

;

Amplify

.

configure

(

outputs

)

;

export

default

function

RootLayout

(

{

children

,

}

:

{

children

:

React

.

ReactNode

;

}

)

{

return

(

Copy

highlighted code example

<

html

lang

=

"

en

"

>

<

body

>

<

AuthenticatorWrapper

>

{

children

}

</

AuthenticatorWrapper

>

</

body

>

</

html

>

)

;

}

The Authenticator component auto-detects your auth backend settings and renders the correct UI state based on the auth backend's authentication flow.

In your

app/page.tsx

file, add a button to enable users to sign out of the application. Import the

useAuthenticator

hook from the Amplify UI library to hook into the state of the Authenticator.

app/page.tsx

import

type

{

Schema

}

from

"@/amplify/data/resource"

;

Copy

highlighted code example

import

{

useAuthenticator

}

from

"@aws-amplify/ui-react"

;

import

{

useState

,

useEffect

}

from

"react"

;

import

{

generateClient

}

from

"aws-amplify/data"

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

export

default

function

HomePage

(

)

{

Copy

highlighted code example

const

{

signOut

}

=

useAuthenticator

(

)

;

// ...

return

(

<

main

>

{

/* ... */

}

Copy

highlighted code example

<

button

onClick

=

{

signOut

}

>

Sign out

</

button

>

</

main

>

)

;

}

Try out your application in your localhost environment again. You should be presented with a login experience now.

To get these changes to the cloud, commit them to git and push the changes upstream.

Terminal

Copy

Terminal

code example

git commit -am "added authenticator"

git push

Amplify automatically deploys the latest version of your app based on your git commits. In just a few minutes, when the application rebuilds, the hosted app will be updated to support the deletion functionality.

Make backend updates

Let's update our backend to implement per-user authorization rules, allowing each user to only access their own to-dos.

7. Set up local AWS credentials

To make backend updates, we are going to require AWS credentials to deploy backend updates from our local machine.

Skip ahead to step 8

, if you already have an AWS profile with credentials on your local machine, and your AWS profile has the

AmplifyBackendDeployFullAccess

permission policy.

Otherwise,

set up local AWS credentials

that grant Amplify permissions to deploy backend updates from your local machine.

8. Deploy cloud sandbox

To update your backend without affecting the production branch, use Amplify's cloud sandbox. This feature provides a separate backend environment for each developer on a team, ideal for local development and testing.

To start your cloud sandbox, run the following command in a

new Terminal window

:

Terminal

Copy

Terminal

code example

npx ampx sandbox

Once the cloud sandbox has been fully deployed (~5 min), you'll see the

amplify_outputs.json

file updated with connection information to a new isolated authentication and data backend.

The

npx ampx sandbox

command should run concurrently to your

npm run dev

. You can think of the cloud sandbox as the "localhost-equivalent for your app backend".

9. Implement per-user authorization

The to-do items in the starter are currently shared across all users, but, in most cases, you want data to be isolated on a per-user basis.

To isolate the data on a per-user basis, you can use an "owner-based authorization rule". Let's apply the owner-based authorization rule to your to-do items:

amplify/data/resource.ts

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

,

Copy

highlighted code example

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

,

authorizationModes

:

{

// This tells the data client in your app (generateClient())

// to sign API requests with the user authentication token.

Copy

highlighted code example

defaultAuthorizationMode

:

'userPool'

,

}

,

}

)

;

In the application client code, let's also render the username to distinguish different users once they're logged in. Go to your

app/page.tsx

file and render the

user

property from the

useAuthenticator

hook.

app/page.tsx

// ... imports

function

HomePage

(

)

{

Copy

highlighted code example

const

{

user

,

signOut

}

=

useAuthenticator

(

)

;

// ...

return

(

<

main

>

Copy

highlighted code example

<

h1

>

{

user

?.

signInDetails

?.

loginId

}

's todos

</

h1

>

{

/* ... */

}

</

main

>

)

}

Now, let's go back to your local application and test out the user isolation of the to-do items.

You will need to sign up new users again because now you're working with the cloud sandbox instead of your production backend.

To get these changes to the cloud, commit them to git and push the changes upstream.

Terminal

Copy

Terminal

code example

git commit -am "added per-user data isolation"

git push

Once your build completes in the Amplify Console, the

main

backend will update to support the changes made within the cloud sandbox. The data in the cloud sandbox is fully isolated and won't pollute your production database.

🥳 Success

That's it! You have successfully built a fullstack app on AWS Amplify. If you want to learn more about how to work with Amplify, here's the conceptual guide for

how Amplify works

.
