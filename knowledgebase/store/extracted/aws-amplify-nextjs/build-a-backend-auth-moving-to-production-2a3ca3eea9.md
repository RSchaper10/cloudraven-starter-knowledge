---
title: Moving to production - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/build-a-backend/auth/moving-to-production/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:06.890231+00:00
kind: extracted-doc
---

# Moving to production - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/build-a-backend/auth/moving-to-production/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:06.890231+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/frontend/auth/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/moving-to-production/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/modify-resources-with-cdk/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/use-existing-cognito-resources/

Captured summary:

- Moving to production - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Looking for how to use this in your app?
- See Frontend Libraries → Moving to production ✨ Use with AI Amplify Auth provisions Amazon Cognito resources that are provisioned with limited capabilities for sending email and SMS messages.

Extracted text:

Moving to production - AWS Amplify Gen 2 Documentation

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

Moving to production

✨

Use with AI

Amplify Auth provisions

Amazon Cognito

resources that are provisioned with limited capabilities for sending email and SMS messages. In its default state, it is not intended to handle production workloads, but is sufficient for developing your application and associated business logic.

Email

Cognito provides a

default email functionality

that limits how many emails can be sent in one day. When considering production workloads, Cognito can be configured to send emails using

Amazon Simple Email Service (Amazon SES)

.

All new AWS accounts default to a "sandbox" status with Amazon SES. This comes with the primary caveat that you can only send mail

to

verified email addresses and domains

To get started with Amazon SES in production, you must first

request production access

. Once you submit your request the submission cannot be modified, however you will receive a response from AWS within 24 hours.

After you have configured your account for production access and have verified your

sender

email, you can configure your Cognito user pool to send emails using the verified sender:

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

https://docs.amplify.aws/react/build-a-backend/auth

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

senders

:

{

email

:

{

// configure using the email registered and verified in Amazon SES

fromEmail

:

"registrations@example.com"

,

}

,

}

,

}

)

Now when emails are sent on new user sign-ups, password resets, etc., the sending account will be your verified email! To customize further, you can change the display name of the sender, or optionally apply a custom address for your users to reply.

amplify/auth/resource.ts

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

https://docs.amplify.aws/react/build-a-backend/auth

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

senders

:

{

email

:

{

fromEmail

:

"registrations@example.com"

,

Copy

highlighted code example

fromName

:

"MyApp"

,

replyTo

:

"inquiries@example.com"

}

,

}

,

}

)

SMS

In order to send SMS authentication codes, you must

request an origination number

. Authentication codes will be sent from the origination number. If your AWS account is in the SMS sandbox, you must also add a destination phone number, which can be done by going to the

Amazon Pinpoint Console

, selecting SMS and voice in the navigation pane, and selecting Add phone number in the Destination phone numbers tab. To check if your AWS account is in the SMS sandbox, go to the

SNS console

, select the Text messaging (SMS) tab from the navigation pane, and check the status under the Account information section.

PREVIOUS

Modify Amplify-generated Cognito resources with CDK

NEXT

Use existing Cognito resources
