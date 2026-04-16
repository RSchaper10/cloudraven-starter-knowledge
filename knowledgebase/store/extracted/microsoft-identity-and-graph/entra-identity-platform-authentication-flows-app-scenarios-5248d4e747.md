# Microsoft identity platform app types and authentication flows - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/authentication-flows-app-scenarios

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-15T19:44:47.088423+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/authentication-flows-app-scenarios
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
- https://learn.microsoft.com/en-us/entra/identity-platform/reference-v2-libraries
- https://learn.microsoft.com/en-us/entra/identity-platform/security-tokens
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-overview
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-supported-account-types
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-app-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-web-app-call-api-app-configuration
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-desktop-acquire-token-username-password
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-desktop-app-configuration
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-mobile-app-configuration
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-protected-web-api-expose-scopes
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-web-api-call-api-app-configuration
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-daemon-acquire-token
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-daemon-app-configuration
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-spa-app-configuration
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-implicit-grant-flow
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth-ropc

Captured summary:

- Microsoft identity platform app types and authentication flows - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Microsoft identity platform app types and authentication flows Feedback Summarize this article for me The Microsoft identity platform supports authentication for different kinds of modern application architectures.
- All of the architectures are based on the industry-standard protocols OAuth 2.0 and OpenID Connect .

Extracted text:

Microsoft identity platform app types and authentication flows - Microsoft identity platform | Microsoft Learn

Table of contents

Exit editor mode

Ask Learn

Ask Learn

Focus mode

Table of contents

Read in English

Add

Add to plan

Edit

Share via

Facebook

x.com

LinkedIn

Email

Copy Markdown

Print

Note

Access to this page requires authorization. You can try

signing in

or

changing directories

.

Access to this page requires authorization. You can try

changing directories

.

Microsoft identity platform app types and authentication flows

Feedback

Summarize this article for me

The Microsoft identity platform supports authentication for different kinds of modern application architectures. All of the architectures are based on the industry-standard protocols

OAuth 2.0 and OpenID Connect

. By using the

authentication libraries for the Microsoft identity platform

, applications authenticate identities and acquire tokens to access protected APIs.

This article describes authentication flows and the application scenarios that they're used in.

Application categories

Security tokens

can be acquired from several types of applications, including:

Web apps

Mobile apps

Desktop apps

Web APIs

Tokens can also be acquired by apps running on devices that don't have a browser or are running on the Internet of Things (IoT).

The following sections describe the categories of applications.

Protected resources vs. client applications

Authentication scenarios involve two activities:

Acquiring security tokens for a protected web API

: We recommend that you use the

Microsoft Authentication Library (MSAL)

, developed and supported by Microsoft.

Protecting a web API or a web app

: One challenge of protecting these resources is validating the security token. On some platforms, Microsoft offers

middleware libraries

.

With users or without users

Most authentication scenarios acquire tokens on behalf of signed-in users.

However, there are also daemon apps. In these scenarios, applications acquire tokens on behalf of themselves with no user.

Single-page, public client, and confidential client applications

Security tokens can be acquired by multiple types of applications. These applications tend to be separated into the following three categories. Each is used with different libraries and objects.

Single-page applications

: Also known as SPAs, these are web apps in which tokens are acquired by a JavaScript or TypeScript app running in the browser. Many modern apps have a single-page application at the front end that's primarily written in JavaScript. The application often uses a framework like Angular, React, or Vue. MSAL.js is the only Microsoft Authentication Library that supports single-page applications.

Public client applications

: Apps in this category, like the following types, always sign in users:

Desktop apps that call web APIs on behalf of signed-in users

Mobile apps

Apps running on devices that don't have a browser, like those running on IoT

Confidential client applications

: Apps in this category include:

Web apps that call a web API

Web APIs that call a web API

Daemon apps, even when implemented as a console service like a Linux daemon or a Windows service

Sign-in audience

The available authentication flows differ depending on the sign-in audience. Some flows are available only for work or school accounts. Others are available both for work or school accounts and for personal Microsoft accounts.

For more information, see

Supported account types

.

Application types

The Microsoft identity platform supports authentication for these app architectures:

Single-page apps

Web apps

Web APIs

Mobile apps

Native apps

Daemon apps

Server-side apps

Applications use the different authentication flows to sign in users and get tokens to call protected APIs.

Single-page application

Many modern web apps are built as client-side single-page applications. These applications use JavaScript or a framework like Angular, Vue, and React. These applications run in a web browser.

Single-page applications differ from traditional server-side web apps in terms of authentication characteristics. By using the Microsoft identity platform, single-page applications can sign in users and get tokens to access back-end services or web APIs. The Microsoft identity platform offers two grant types for JavaScript applications:

MSAL.js (2.x)

MSAL.js (1.x)

Web app that signs in a user

To help protect a web app that signs in a user:

If you develop in .NET, you use ASP.NET or ASP.NET Core with the ASP.NET OpenID Connect middleware. Protecting a resource involves validating the security token, which is done by the

IdentityModel extensions for .NET

and not MSAL libraries.

If you develop in Node.js, you use

MSAL Node

.

For more information, see

Sign in users in a sample web app

.

Web app that signs in a user and calls a web API on behalf of the user

To call a web API from a web app on behalf of a user, use the authorization code flow and store the acquired tokens in the token cache. When needed, MSAL refreshes tokens and the controller silently acquires tokens from the cache.

For more information, see

Web app that calls web APIs

.

Desktop app that calls a web API on behalf of a signed-in user

For a desktop app to call a web API that signs in users, use the interactive token-acquisition methods of MSAL. With these interactive methods, you can control the sign-in UI experience. MSAL uses a web browser for this interaction.

There's another possibility for Windows-hosted applications on computers joined either to a Windows domain or by Microsoft Entra ID. These applications can silently acquire a token by using

integrated Windows authentication

.

Applications running on a device without a browser can still call an API on behalf of a user. To authenticate, the user must sign in on another device that has a web browser. This scenario requires that you use the

device code flow

.

Though we don't recommend that you use it, the

username/password flow

is available in public client applications. This flow is still needed in some scenarios like DevOps.

Using the username/password flow constrains your applications and is no longer considered secure. For instance, applications can't sign in a user who needs to use multifactor authentication or the Conditional Access tool in Microsoft Entra ID. Your applications also don't benefit from single sign-on. Authentication with the username/password flow goes against the principles of modern authentication and is provided only for legacy reasons.

In desktop apps, if you want the token cache to persist, you can customize the

token cache serialization

. By implementing dual token cache serialization, you can use backward-compatible and forward-compatible token caches.

For more information, see

Desktop app that calls web APIs

.

Mobile app that calls a web API on behalf of an interactive user

Similar to a desktop app, a mobile app calls the interactive token-acquisition methods of MSAL to acquire a token for calling a web API.

MSAL iOS and MSAL Android use the system web browser by default. However, you can direct them to use the embedded web view instead. There are specificities that depend on the mobile platform: iOS, or Android.

Some scenarios, like those that involve Conditional Access related to a device ID or a device enrollment, require a broker to be installed on the device. Examples of brokers are Microsoft Company Portal on Android and Microsoft Authenticator on Android and iOS.

For more information, see

Mobile app that calls web APIs

.

Note

A mobile app that uses MSAL iOS or MSAL Android can have app protection policies applied to it. For instance, the policies might prevent a user from copying protected text. The mobile app is managed by Intune and is recognized by Intune as a managed app. For more information, see

Microsoft Intune App SDK overview

.

The

Intune App SDK

is separate from MSAL libraries and interacts with Microsoft Entra ID on its own.

Protected web API

You can use the Microsoft identity platform endpoint to secure web services like your app's RESTful API. A protected web API is called through an access token. The token helps secure the API's data and authenticate incoming requests. The caller of a web API appends an access token in the authorization header of an HTTP request.

If you want to protect your ASP.NET or ASP.NET Core web API, validate the access token. For this validation, you use the ASP.NET JWT middleware. The validation is done by the

IdentityModel extensions for .NET

library and not by MSAL.NET.

For more information, see

Protected web API

.

Web API that calls another web API on behalf of a user

For your protected web API to call another web API on behalf of a user, your app needs to acquire a token for the downstream web API. Such calls are sometimes referred to as

service-to-service

calls. Web APIs that call other web APIs need to provide custom cache serialization.

For more information, see

Web API that calls web APIs

.

Daemon app that calls a web API in the daemon's name

Apps that have long-running processes or that operate without user interaction also need a way to access secure web APIs. Such an app can authenticate and get tokens by using the app's identity. The app proves its identity by using a client secret or certificate.

You can write such daemon apps that acquire a token for the calling app by using the

client credential

acquisition methods in MSAL. These methods require a client secret that you add to the app registration in Microsoft Entra ID. The app then shares the secret with the called daemon. Examples of such secrets include application passwords, certificate assertion, and client assertion.

For more information, see

Daemon application that calls web APIs

.

Scenarios and supported authentication flows

You use authentication flows to implement the application scenarios that are requesting tokens. There isn't a one-to-one mapping between application scenarios and authentication flows.

Scenarios that involve acquiring tokens also map to OAuth 2.0 authentication flows. For more information, see

OAuth 2.0 and OpenID Connect protocols on the Microsoft identity platform

.

Scenario

Detailed scenario walk-through

OAuth 2.0 flow and grant

Audience

Single-page app

Authorization code

with PKCE

Work or school accounts, personal accounts, and Azure Active Directory B2C (Azure AD B2C)

Single-page app

Implicit

Work or school accounts, personal accounts, and Azure Active Directory B2C (Azure AD B2C)

Web app that signs in users

Authorization code

Work or school accounts, personal accounts, and Azure AD B2C

Web app that calls web APIs

Authorization code

Work or school accounts, personal accounts, and Azure AD B2C

Desktop app that calls web APIs

Interactive by using

authorization code

with PKCE

Work or school accounts, personal accounts, and Azure AD B2C

Integrated Windows authentication

Work or school accounts

Resource owner password

Work or school accounts and Azure AD B2C

Browserless app

Device code

Work or school accounts, personal accounts, but not Azure AD B2C

Mobile app that calls web APIs

Interactive by using

authorization code

with PKCE

Work or school accounts, personal accounts, and Azure AD B2C

Resource owner password

Work or school accounts and Azure AD B2C

Daemon app that calls web APIs

Client credentials

App-only permissions that have no user and are used only in Microsoft Entra organizations

Web API that calls web APIs

On-behalf-of

Work or school accounts and personal accounts

Scenarios and supported platforms and languages

Microsoft Authentication Libraries support multiple platforms:

.NET

.NET Framework

Java

JavaScript

macOS

Native Android

Native iOS

Node.js

Python

You can also use various languages to build your applications.

In the Windows column of the following table, each time .NET is mentioned, .NET Framework is also possible. The latter is omitted to avoid cluttering the table.

Scenario

Windows

Linux

Mac

iOS

Android

Single-page app

MSAL.js

MSAL.js

MSAL.js

MSAL.js

MSAL.js

Single-page app

MSAL.js

MSAL.js

MSAL.js

MSAL.js

MSAL.js

Web app that signs in users

ASP.NET Core

MSAL Node

ASP.NET Core

MSAL Node

ASP.NET Core

MSAL Node

Web app that calls web APIs

ASP.NET Core + MSAL.NET

MSAL Java

Flask + MSAL Python

MSAL Node

ASP.NET Core + MSAL.NET

MSAL Java

Flask + MSAL Python

MSAL Node

ASP.NET Core + MSAL.NET

MSAL Java

Flask + MSAL Python

MSAL Node

Desktop app that calls web APIs

MSAL.NET

MSAL Java

MSAL Python

MSAL Node

MSAL.NET

MSAL Java

MSAL Python

MSAL Node

MSAL.NET

MSAL Java

MSAL Python

MSAL Node

MSAL.objc

Mobile app that calls web APIs

MSAL.NET

MSAL.objc

MSAL.Android

Daemon app

MSAL.NET

MSAL Java

MSAL Python

MSAL Node

MSAL.NET

MSAL Java

MSAL Python

MSAL Node

MSAL.NET

MSAL Java

MSAL Python

MSAL Node

Web API that calls web APIs

ASP.NET Core + MSAL.NET

MSAL Java

MSAL Python

MSAL Node

ASP.NET Core + MSAL.NET

MSAL Java

MSAL Python

MSAL Node

ASP.NET Core + MSAL.NET

MSAL Java

MSAL Python

MSAL Node

For more information, see

Microsoft identity platform authentication libraries

.

Next steps

For more information about authentication, see:

Authentication vs. authorization.

Microsoft identity platform access tokens.

Securing access to IoT apps.

Feedback

Was this page helpful?

Yes

No

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

Ask Learn

Ask Learn

Suggest a fix?

Additional resources

Last updated on

2025-04-14
