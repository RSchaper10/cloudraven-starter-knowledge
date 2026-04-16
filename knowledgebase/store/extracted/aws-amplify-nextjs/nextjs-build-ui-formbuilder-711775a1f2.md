---
title: Connected forms - Next.js - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/build-ui/formbuilder/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:07.634069+00:00
kind: extracted-doc
---

# Connected forms - Next.js - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/build-ui/formbuilder/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:07.634069+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/build-ui/formbuilder/
- https://docs.amplify.aws/nextjs/start/quickstart/

Captured summary:

- Connected forms - Next.js - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Connected forms ✨ Use with AI Connected Forms are bound to a model in your app's data schema.
- Whenever a connected form is submitted, a record is automatically created or updated in the bound data model, with some or all of the form's input fields mapping to fields in the data model.

Extracted text:

Connected forms - Next.js - AWS Amplify Gen 2 Documentation

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

Connected forms

✨

Use with AI

Connected Forms are bound to a model in your app's data schema. Whenever a connected form is submitted, a record is automatically created or updated in the bound data model, with some or all of the form's input fields mapping to fields in the data model. Connected forms automatically work with any Amplify GraphQL API, and no

onSubmit

handling is required.

Generate forms

First, install the Amplify UI library.

Terminal

Copy

Terminal

code example

npm add @aws-amplify/ui-react

To use connected forms, you first need to deploy a data model from your sandbox environment. We will use the same example as in the getting started

tutorial

. To get started run the following command from your project root:

Terminal

Copy

Terminal

code example

npx ampx generate forms

This will generate create and update forms for each model defined in your schema in a folder called

ui-components

.

Terminal

Copy

Terminal

code example

File written: ui-components/graphql/subscriptions.ts

File written: ui-components/graphql/mutations.ts

File written: ui-components/graphql/queries.ts

File written: ui-components/TodoCreateForm.jsx

File written: ui-components/TodoCreateForm.d.ts

File written: ui-components/TodoUpdateForm.jsx

File written: ui-components/TodoUpdateForm.d.ts

File written: ui-components/utils.js

File written: ui-components/index.js

Re-generating forms

In Gen 2, we automatically generate the form UI for you, which you can then customize and manage. If you decide to update your data model and need to regenerate the forms, please ensure you back up the original

ui-components

folder before executing the

npx ampx generate forms

command again.

Render React form in your app

In your application's entrypoint file (e.g.

src/index.js

for create-react-app or

src/main.jsx

for Vite), add the following imports and configuration

Copy

highlighted code example

import

'@aws-amplify/ui-react/styles.css'

;

import

{

ThemeProvider

}

from

'@aws-amplify/ui-react'

;

import

{

Amplify

}

from

'aws-amplify'

;

import

outputs

from

'./amplify_outputs.json'

;

Amplify

.

configure

(

outputs

)

;

In your application's entrypoint file (e.g.

src/main.jsx

for Vite), wrap the

<App />

component with the following:

Copy

code example

<

ThemeProvider

>

<

App

/>

</

ThemeProvider

>

Import your form by name. For a form named

TodoCreateForm

, you would use the following code:

Copy

code example

import

{

TodoCreateForm

}

from

'./ui-components'

;

Place your form in code. For a form named

ProductCreateForm

in a React project, you could use the following App code:

Copy

code example

function

App

(

)

{

return

<

TodoCreateForm

/>

;

}

export

default

App

;

Types of forms

All connected and unconnected forms are either a

Create

form or an

Update

form.

Create forms

Create forms render a form with empty inputs. If a create form is connected to a data model, will always generate a new record upon submission.

Update forms

Update forms expect an input value in order to pre-populate the form.

For update forms that are connected to a data model, you can use the

id

prop, or the model prop:

id

prop: id string of the record you want to update. For example:

Copy

code example

<

AuthorUpdateForm

id

=

"

ac74af5c-3aab-4274-8f41-23e1e6576af5

"

/>

Model prop: if your form is bound to a data model named

Author

, your form will have a prop named

author

as well, which can receive a record. For example:

Copy

code example

<

AuthorUpdateForm

author

=

{

authorRecord

}

>
