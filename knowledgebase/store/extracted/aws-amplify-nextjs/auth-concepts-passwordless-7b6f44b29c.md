---
title: Passwordless - AWS Amplify Gen 2 Documentation
source_url: https://docs.amplify.aws/nextjs/build-a-backend/auth/concepts/passwordless/
target_id: aws-amplify-nextjs
dependency: AWS Amplify Gen 2 for Next.js
collected_at: 2026-04-16T03:20:06.302921+00:00
kind: extracted-doc
---

# Passwordless - AWS Amplify Gen 2 Documentation

Source URL:

- https://docs.amplify.aws/nextjs/build-a-backend/auth/concepts/passwordless/

Dependency:

- AWS Amplify Gen 2 for Next.js

Collected at:

- 2026-04-16T03:20:06.302921+00:00

Direct links in scope:

- https://docs.amplify.aws/nextjs/how-amplify-works/
- https://docs.amplify.aws/nextjs/frontend/auth/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/concepts/passwordless/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/moving-to-production/
- https://docs.amplify.aws/nextjs/frontend/auth/sign-in/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/manage-users/manage-webauthn-credentials/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/concepts/phone/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/concepts/user-attributes/

Captured summary:

- Passwordless - AWS Amplify Gen 2 Documentation Name: interface Value: Introducing Amplify Gen 2 Dismiss Gen 2 introduction dialog Amplify has re-imagined the way frontend developers build fullstack applications.
- Fullstack TypeScript Write your app's data model, auth, storage, and functions in TypeScript; Amplify will do the rest.
- 🚀 Built with the AWS CDK Use any cloud resource your app needs.
- Back to Gen 1 Docs Learn more about Gen 2 Looking for how to use this in your app?
- See Frontend Libraries → Passwordless ✨ Use with AI Amplify supports the use of passwordless authentication flows using the following methods: SMS-based one-time password (SMS OTP) Email-based one-time password (Email OTP) WebAuthn passkey Passwordless authentication removes the security risks and user friction associated with traditional passwords.

Extracted text:

Passwordless - AWS Amplify Gen 2 Documentation

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

Passwordless

✨

Use with AI

Amplify supports the use of passwordless authentication flows using the following methods:

SMS-based one-time password (SMS OTP)

Email-based one-time password (Email OTP)

WebAuthn passkey

Passwordless authentication removes the security risks and user friction associated with traditional passwords.

Configure passwordless authentication

You can enable passwordless authentication methods directly in your

defineAuth

configuration. Passwordless methods are used alongside traditional password-based authentication, giving users multiple options to sign in.

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

// Enable email OTP

}

}

}

)

;

You can enable multiple passwordless methods simultaneously:

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

// Enable email OTP

}

,

phone

:

{

otpLogin

:

true

// Enable SMS OTP

}

,

webAuthn

:

true

// Enable WebAuthn passkeys

}

}

)

;

SMS OTP

SMS-based authentication uses phone numbers as the identifier and text messages as the verification channel. At a high level end users will perform the following steps to authenticate:

User enters their phone number to sign up/sign in

They receive a text message with a time-limited code

After the user enters their code they are authenticated

Configure SMS OTP

Enable SMS OTP by setting

otpLogin: true

in your phone login configuration:

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

phone

:

{

otpLogin

:

true

}

}

}

)

;

SMS-based one-time password requires your Amazon Cognito user pool to be configured to use Amazon Simple Notification Service (SNS) to send text messages.

Learn how to configure your auth resource with SNS

.

Learn more about using SMS OTP in your application code

.

Email OTP

Email-based authentication uses email addresses for identification and verification. At a high level end users will perform the following steps to authenticate:

User enters their email address to sign up/sign in

They receive an email message with a time-limited code

After the users enters their code they are authenticated

Configure Email OTP

Enable Email OTP by setting

otpLogin: true

in your email login configuration:

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

}

}

}

)

;

Email-based one-time password requires your Amazon Cognito user pool to be configured to use Amazon Simple Email Service (SES) to send email messages.

Learn how to configure your auth resource with SES

.

Learn more about using email OTP in your application code

.

WebAuthn Passkey

WebAuthn uses biometrics or security keys for authentication, leveraging device-specific security features. At a high level end users will perform the following steps to authenticate:

User chooses to register a passkey

Their device prompts for biometric/security key verification

For future logins, they'll authenticate using the same method

Configure WebAuthn

Enable WebAuthn passkeys in your auth configuration. The simplest configuration uses automatic relying party ID resolution:

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

true

,

// Users need a sign-up method

webAuthn

:

true

// Automatically resolves relying party ID

}

}

)

;

When

webAuthn: true

is used, the relying party ID is automatically resolved:

In

sandbox

environments: resolves to

localhost

In

branch

deployments: resolves to your Amplify app domain (e.g.,

[branch].[appId].amplifyapp.com

)

For production environments or custom domains, specify the relying party ID explicitly:

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

true

,

webAuthn

:

{

relyingPartyId

:

'example.com'

,

userVerification

:

'required'

// or 'preferred' (default)

}

}

}

)

;

Learn more about using WebAuthn passkeys in your application code

.

Managing credentials

Passwordless authentication with WebAuthn requires associating one or more credentials with the user's Amazon Cognito account. Amplify provides APIs that integrate with each platform's local authenticator to easily create, view, and delete these credential associations.

Learn more about managing WebAuthn credentials

.

Passwordless authentication

When you enable passwordless authentication methods, traditional password authentication remains available. This gives users flexibility to choose their preferred authentication method:

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

// Email OTP enabled alongside password auth

}

}

}

)

;

In this configuration, users can authenticate using either:

Email and password (traditional)

Email OTP (passwordless)

You can enable multiple passwordless methods to give users even more options:

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

}

,

phone

:

{

otpLogin

:

true

}

,

webAuthn

:

{

relyingPartyId

:

'example.com'

}

}

}

)

;

In this configuration, users can authenticate using:

Email and password

Email OTP

Phone and password

SMS OTP

WebAuthn passkeys

When using WebAuthn, users still need a way to initially sign up (email or phone). WebAuthn credentials are then associated with their account for future sign-ins.

Next steps

Learn how to implement passwordless sign-in in your application

Configure email settings for Email OTP

Configure SMS settings for SMS OTP

Manage WebAuthn credentials

PREVIOUS

Phone

NEXT

User attributes
