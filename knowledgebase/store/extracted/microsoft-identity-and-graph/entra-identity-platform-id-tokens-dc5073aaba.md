---
title: ID tokens in the Microsoft identity platform - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/id-tokens
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:53.614881+00:00
kind: extracted-doc
---

# ID tokens in the Microsoft identity platform - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/id-tokens

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:53.614881+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/id-tokens
- https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens
- https://learn.microsoft.com/en-us/entra/identity-platform/id-token-claims-reference
- https://learn.microsoft.com/en-us/entra/identity-platform/claims-validation
- https://learn.microsoft.com/en-us/entra/identity-platform/configurable-token-lifetimes
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc

Captured summary:

- ID tokens in the Microsoft identity platform - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- ID tokens in the Microsoft identity platform Feedback Summarize this article for me ID tokens are a security token that serves as proof of authentication, confirming that a user is successfully authenticated.
- Information in ID tokens enables the client to verify that a user is who they claim to be, similar to name tags at a conference.

Extracted text:

ID tokens in the Microsoft identity platform - Microsoft identity platform | Microsoft Learn

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

ID tokens in the Microsoft identity platform

Feedback

Summarize this article for me

ID tokens are a security token that serves as proof of authentication, confirming that a user is successfully authenticated. Information in ID tokens enables the client to verify that a user is who they claim to be, similar to name tags at a conference. The authorization server issues ID tokens that contain claims that carry information about the user. They can be sent alongside or instead of an access token, and are always JWT (JSON Web Token) format.

ID tokens differ from

access tokens

, which serve as proof of authorization. Confidential clients should validate ID tokens. You shouldn't use an ID token to call an API.

Third-party applications are intended to understand ID tokens. Do not use ID tokens for authorization purposes. Access tokens are used for authorization. The claims provided by ID tokens can be used for UX inside your application, as keys in a database, and providing access to the client application. For more information about the claims used in an ID token, see the

ID token claims reference

. For more information about claims-based authorization, see

Secure applications and APIs by validating claims

.

Token formats

There are two versions of ID tokens available in the Microsoft identity platform: v1.0 and v2.0. These versions determine the claims that are in the token. The v1.0 and v2.0 ID tokens have differences in the information they carry. The version is based on the endpoint from where it was requested. New applications should use the v2.0.

v1.0:

https://login.microsoftonline.com/common/oauth2/authorize

v2.0:

https://login.microsoftonline.com/common/oauth2/v2.0/authorize

Sample v1.0 ID token

[REDACTED_SECRET]

View this v1.0 sample token in

jwt.ms

.

Sample v2.0 ID token

[REDACTED_SECRET]

View this v2.0 sample token in

jwt.ms

.

Token lifetime

By default, an ID token is valid for one hour - after one hour, the client must acquire a new ID token.

You can adjust the lifetime of an ID token to control how often the client application expires the application session, and how often it requires the user to authenticate again either silently or interactively. For more information, read

Configurable token lifetimes

.

Validate tokens

To validate an ID token, your client can check whether the token has been tampered with. It can also validate the issuer to ensure that the correct issuer has sent back the token. Because ID tokens are always a JWT token, many libraries exist to validate these tokens - you should use one of these libraries rather than doing it yourself. Only confidential clients should validate ID tokens. For more information, see

Secure applications and APIs by validating claims

.

Public applications (code running entirely on a device or network you don't control such as a user's browser or their home network) don't benefit from validating the ID token. In this instance, a malicious user can intercept and edit the keys used for validation of the token.

The following JWT claims should be validated in the ID token after validating the signature on the token. Your token validation library may also validate the following claims:

Timestamps: the

iat

,

nbf

, and

exp

timestamps should all fall before or after the current time, as appropriate.

Audience: the

aud

claim should match the app ID for your application.

Nonce: the

nonce

claim in the payload must match the nonce parameter passed into the

/authorize

endpoint during the initial request.

Related content

ID token claims reference

OAuth 2.0 and OpenID Connect protocols

OpenID Connect on the Microsoft identity platform

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

2025-05-14
