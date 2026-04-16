---
title: Set up Amplify Auth - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/build-a-backend/auth/set-up-auth/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:19:53.880973+00:00
kind: extracted-doc
---

# Set up Amplify Auth - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/build-a-backend/auth/set-up-auth/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:19:53.880973+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/frontend/auth/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/concepts/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/concepts/passwordless/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/set-up-auth/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/moving-to-production/

Captured summary:

- Set up Amplify Auth - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Looking for how to use this in your app?
- See Frontend Libraries → Set up Amplify Auth ✨ Use with AI Amplify Auth is powered by Amazon Cognito .

Extracted text:

Set up Amplify Auth - AWS Amplify Gen 2 Documentation

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

Set up Amplify Auth

✨

Use with AI

Amplify Auth is powered by

Amazon Cognito

. Cognito is a robust user directory service that handles user registration, authentication, account recovery, and other operations.

Review the concepts to learn more

.

To get started with defining your authentication resource, open or create the auth resource file:

amplify/auth/resource.ts

Copy

amplify/auth/resource.ts

code example

import

{

defineAuth

}

from

"@aws-amplify/backend"

/**

* Define and configure your auth resource

*

@see

https://docs.amplify.aws/gen2/build-a-backend/auth

*/

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

}

,

}

)

By default, your auth resource is scaffolded using

email

as the default login mechanism. You can also configure your auth resource to allow signing in with:

Phone numbers

External providers (Google, Facebook, Amazon, or Sign in with Apple)

Passwordless authentication

(Email OTP, SMS OTP, or WebAuthn passkeys)

Note:

At a minimum you will need to pass a

loginWith

value to set up how your users sign in to your app. Signing in with email and password is configured by default if you do not provide any value.

Enable passwordless authentication

You can enable passwordless authentication methods to provide a more secure and user-friendly experience:

amplify/auth/resource.ts

Copy

amplify/auth/resource.ts

code example

import

{

defineAuth

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

{

otpLogin

:

true

// Enable email-based one-time passwords

}

}

}

)

;

Learn more about passwordless authentication options

.

Deploy auth resource

After you have chosen and defined your authentication resource, run the following command to create your resource in your personal cloud sandbox.

Terminal

Copy

Terminal

code example

npx ampx sandbox

After a successful deployment, this command also generates an outputs file (

amplify_outputs.json

) to enable your frontend app to connect to your backend resources. The values you configure in your backend authentication resource are set in the generated outputs file to automatically configure the frontend

Authenticator connected component

.

Connect your application code to your auth resource

Creating and correctly implementing the sign-in flow can be challenging and time-consuming. Amplify's Authenticator UI component streamlines this by enabling you to rapidly build the entire authentication flow for your app. The component works seamlessly with configuration in

amplify/auth/resource.ts

to automatically connect with your backend resources.

Amplify has pre-built UI components for React, Vue, Angular, React Native, Swift, Android, and Flutter. In this guide, we are focusing on those for web applications.

Once you add the Authenticator component to your app, you can test the sign-up, sign-in, and sign-out functionality. You can also

customize the Authenticator connected component

to adjust colors and styling as needed.

Next steps

Now that you have completed setting up authentication in your Amplify app with email and password, you may also want to add some additional features. We recommend you learn more about:

Learn more about authentication concepts

Moving to production

NEXT

Concepts
