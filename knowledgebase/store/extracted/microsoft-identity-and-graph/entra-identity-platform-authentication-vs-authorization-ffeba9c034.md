---
title: Authentication vs. authorization - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/authentication-vs-authorization
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:30.218202+00:00
kind: extracted-doc
---

# Authentication vs. authorization - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/authentication-vs-authorization

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:30.218202+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/authentication-vs-authorization
- https://learn.microsoft.com/en-us/entra/identity-platform/developer-glossary
- https://learn.microsoft.com/en-us/entra/identity-platform/identity-videos
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-token-exchange-saml-oauth
- https://learn.microsoft.com/en-us/entra/identity-platform/security-tokens
- https://learn.microsoft.com/en-us/entra/identity-platform/application-model
- https://learn.microsoft.com/en-us/entra/identity-platform/claims-validation

Captured summary:

- authorization - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- authorization Feedback Summarize this article for me This article defines authentication and authorization.
- It also briefly covers multifactor authentication and how you can use the Microsoft identity platform to authenticate and authorize users in your web apps, web APIs, or apps that call protected web APIs.

Extracted text:

Authentication vs. authorization - Microsoft identity platform | Microsoft Learn

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

Authentication vs. authorization

Feedback

Summarize this article for me

This article defines authentication and authorization. It also briefly covers multifactor authentication and how you can use the Microsoft identity platform to authenticate and authorize users in your web apps, web APIs, or apps that call protected web APIs. If you see a term you aren't familiar with, try our

glossary

or our

Microsoft identity platform videos

, which cover basic concepts.

Authentication

Authentication

is the process of proving that you are who you say you are. This is achieved by verification of the identity of a person or device. It's sometimes shortened to

AuthN

. The Microsoft identity platform uses the

OpenID Connect

protocol for handling authentication.

Authorization

Authorization

is the act of granting an authenticated party permission to do something. It specifies what data you're allowed to access and what you can do with that data. Authorization is sometimes shortened to

AuthZ

. The Microsoft identity platform provides resource owners the ability to use the

OAuth 2.0

protocol for handling authorization, but the Microsoft cloud also has other authorization systems such as

Microsoft Entra built-in roles

,

Azure RBAC

, and

Exchange RBAC

.

Multifactor authentication

Multifactor authentication

is the act of providing another factor of authentication to an account. This is often used to protect against brute force attacks. It's sometimes shortened to

MFA

or

2FA

. The

Microsoft Authenticator

can be used as an app for handling two-factor authentication. For more information, see

multifactor authentication

.

Authentication and authorization using the Microsoft identity platform

Creating apps that each maintain their own username and password information incurs a high administrative burden when adding or removing users across multiple apps. Instead, your apps can delegate that responsibility to a centralized identity provider.

Microsoft Entra ID is a centralized identity provider in the cloud. Delegating authentication and authorization to it enables scenarios such as:

Conditional Access policies that require a user to be in a specific location.

Multifactor authentication which requires a user to have a specific device.

Enabling a user to sign in once and then be automatically signed in to all of the web apps that share the same centralized directory. This capability is called

single sign-on (SSO)

.

The Microsoft identity platform simplifies authorization and authentication for application developers by providing identity as a service. It supports industry-standard protocols and open-source libraries for different platforms to help you start coding quickly. It allows developers to build applications that sign in all Microsoft identities, get tokens to call

Microsoft Graph

, access Microsoft APIs, or access other APIs that developers have built.

This video explains the Microsoft identity platform and the basics of modern authentication:

Here's a comparison of the protocols that the Microsoft identity platform uses:

OAuth versus OpenID Connect

: The platform uses OAuth for authorization and OpenID Connect (OIDC) for authentication. OpenID Connect is built on top of OAuth 2.0, so the terminology and flow are similar between the two. You can even both authenticate a user (through OpenID Connect) and get authorization to access a protected resource that the user owns (through OAuth 2.0) in one request. For more information, see

OAuth 2.0 and OpenID Connect protocols

and

OpenID Connect protocol

.

OAuth versus SAML

: The platform uses OAuth 2.0 for authorization and SAML for authentication. For more information on how to use these protocols together to both authenticate a user and get authorization to access a protected resource, see

Microsoft identity platform and OAuth 2.0 SAML bearer assertion flow

.

OpenID Connect versus SAML

: The platform uses both OpenID Connect and SAML to authenticate a user and enable single sign-on. SAML authentication is commonly used with identity providers such as Active Directory Federation Services (AD FS) federated to Microsoft Entra ID, so it's often used in enterprise applications. OpenID Connect is commonly used for apps that are purely in the cloud, such as mobile apps, websites, and web APIs.

Related content

For other articles that cover authentication and authorization basics:

To learn how access tokens, refresh tokens, and ID tokens are used in authorization and authentication, see

Security tokens

.

To learn about the process of registering your application so it can integrate with the Microsoft identity platform, see

Application model

.

To learn about proper authorization using token claims, see

Secure applications and APIs by validating claims

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

2025-03-21
