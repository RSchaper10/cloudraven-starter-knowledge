---
title: Migrate to the Microsoft Authentication Library (MSAL) - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/msal-migration
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:32.826434+00:00
kind: extracted-doc
---

# Migrate to the Microsoft Authentication Library (MSAL) - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/msal-migration

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:32.826434+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/msal-migration
- https://learn.microsoft.com/en-us/entra/identity-platform/app-resilience-continuous-access-evaluation
- https://learn.microsoft.com/en-us/entra/identity-platform/howto-get-list-of-all-auth-library-apps
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-compare-msal-js-and-adal-js
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-node-migration
- https://learn.microsoft.com/en-us/entra/identity-platform/migrate-android-adal-msal
- https://learn.microsoft.com/en-us/entra/identity-platform/reference-v2-libraries
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-overview
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-acquire-cache-tokens
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration

Captured summary:

- Migrate to the Microsoft Authentication Library (MSAL) - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Migrate applications to the Microsoft Authentication Library (MSAL) Feedback Summarize this article for me If any of your applications use the Azure Active Directory Authentication Library (ADAL) for authentication and authorization capabilities, it's time to migrate them to the Microsoft Authentication Library (MSAL) .
- All Microsoft support and development for ADAL, including security fixes, ended on June 30, 2023.

Extracted text:

Migrate to the Microsoft Authentication Library (MSAL) - Microsoft identity platform | Microsoft Learn

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

Migrate applications to the Microsoft Authentication Library (MSAL)

Feedback

Summarize this article for me

If any of your applications use the Azure Active Directory Authentication Library (ADAL) for authentication and authorization capabilities, it's time to migrate them to the

Microsoft Authentication Library (MSAL)

.

All Microsoft support and development for ADAL, including security fixes, ended on June 30, 2023.

There were no ADAL feature releases or new platform version releases planned before the deprecation date.

No new features have been added to ADAL since June 30, 2020.

Warning

Azure Active Directory Authentication Library (ADAL) has been deprecated. While existing apps that use ADAL will continue to work, Microsoft will no longer release security fixes on ADAL. Use the

Microsoft Authentication Library (MSAL)

to avoid putting your app's security at risk.

Why switch to MSAL?

If you've developed apps using the Azure AD (v1.0) endpoint, you're likely using ADAL. Since Microsoft identity platform (v2.0) endpoint has changed significantly, the new library (MSAL) was entirely built for the new endpoint.

MSAL is designed to enable a secure solution without developers having to worry about the implementation details. It simplifies and manages acquiring, managing, caching, and refreshing tokens, and uses best practices for resilience. We recommend you use MSAL to

increase the resilience of authentication and authorization in client applications that you develop

.

MSAL provides multiple benefits over ADAL, including the following features:

Features

MSAL

ADAL

Security

Security fixes beyond June 2023

Proactively refresh and revoke tokens based on policy or critical events for Microsoft Graph and other APIs that support

Continuous Access Evaluation (CAE)

.

Standards compliant with OAuth v2.0 and OpenID Connect (OIDC)

User accounts and experiences

Microsoft Entra accounts

Microsoft account (MSA)

Azure AD B2C accounts

Best single sign-on experience

Authentication experiences

Continuous access evaluation through proactive token refresh

Throttling

Auth broker support

Token protection

Additional capabilities of MSAL over ADAL

Proof of possession tokens

Microsoft Entra certificate-based authentication (CBA) on mobile

System browsers on mobile devices

Where ADAL had only authentication context class, MSAL exposes the notion of a collection of client apps (public client and confidential client).

Active Directory Federation Services (AD FS) support in MSAL

You can use MSAL.NET, MSAL Java, MSAL.js, and MSAL Python to get tokens from Active Directory Federation Services (AD FS) 2019 or later. Earlier versions of AD FS, including AD FS 2016, are unsupported by MSAL.

If you need to continue using AD FS, you should upgrade to AD FS 2019 or later before you update your applications from ADAL to MSAL.

How to migrate to MSAL

Before you start the migration, you need to identify which of your apps are using ADAL for authentication. Follow the steps in this article to get a list by using the Azure portal:

How to: Get a complete list of apps using ADAL in your tenant

After identifying applications that use ADAL, migrate them to MSAL depending on your app type:

Single-page app (SPA)

ADAL.js to MSAL.js

Web app

ADAL Node to MSAL Node

ADAL.NET to MSAL.NET

Web API

ADAL Java to MSAL Java

ADAL Python to MSAL Python

ADAL.NET to MSAL.NET

Desktop app

ADAL Java to MSAL Java

ADAL Python to MSAL Python

ADAL.NET to MSAL.NET

Mobile app

ADAL.Android to MSAL.Android

ADAL.iOS to MSAL.iOS

Service / daemon app

ADAL Python to MSAL Python

ADAL.NET to MSAL.NET

ADAL Node to MSAL Node

ADAL Java to MSAL Java

MSAL Supports a wide range of application types and scenarios. Refer to

Microsoft Authentication Library support for several application types

.

ADAL to MSAL migration guide for different platforms are available in the following links:

Migrate to MSAL iOS and macOS

Migrate to MSAL Java

Migrate to MSAL.js

Migrate to MSAL .NET

Migrate to MSAL Node

Migrate to MSAL Python

Migration help

If you have questions about migrating your app from ADAL to MSAL, here are some options:

Post your question on

Microsoft Q&A

and tag it with

[azure-ad-adal-deprecation]

.

Open an issue in the library's GitHub repository. See the

Languages and frameworks

section of the MSAL overview article for links to each library's repo.

If you partnered with an Independent Software Vendor (ISV) in the development of your application, we recommend that you contact them directly to understand their migration journey to MSAL.

Next steps

For more information about MSAL, including usage information and which libraries are available for different programming languages and application types, see:

Acquire and cache tokens using MSAL

Application configuration options

MSAL authentication libraries

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

2025-02-28
