---
title: Increase application security using Zero Trust principles - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/zero-trust-for-developers
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:43.029648+00:00
kind: extracted-doc
---

# Increase application security using Zero Trust principles - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/zero-trust-for-developers

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:43.029648+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/zero-trust-for-developers
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview
- https://learn.microsoft.com/en-us/entra/identity-platform/reference-v2-libraries
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols
- https://learn.microsoft.com/en-us/entra/identity-platform/developer-guide-conditional-access-authentication-context
- https://learn.microsoft.com/en-us/entra/identity-platform/claims-challenge
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-app-types
- https://learn.microsoft.com/en-us/entra/identity-platform/authentication-flows-app-scenarios
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-android-single-sign-on
- https://learn.microsoft.com/en-us/entra/identity-platform/secure-least-privileged-access
- https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc
- https://learn.microsoft.com/en-us/entra/identity-platform/howto-add-app-roles-in-apps
- https://learn.microsoft.com/en-us/entra/identity-platform/security-best-practices-for-app-registration
- https://learn.microsoft.com/en-us/entra/identity-platform/identity-platform-integration-checklist

Captured summary:

- Increase application security using Zero Trust principles - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Increase application security using Zero Trust principles Feedback Summarize this article for me A secure network perimeter around the applications that are developed can't be assumed.
- Nearly every developed application, by design, will be accessed from outside the network perimeter.

Extracted text:

Increase application security using Zero Trust principles - Microsoft identity platform | Microsoft Learn

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

Increase application security using Zero Trust principles

Feedback

Summarize this article for me

A secure network perimeter around the applications that are developed can't be assumed. Nearly every developed application, by design, will be accessed from outside the network perimeter. Applications can't be guaranteed to be secure when they're developed or will remain so after they're deployed. It's the responsibility of the application developer to not only maximize the security of the application, but also minimize the damage the application can cause if it's compromised.

Additionally, the responsibility includes supporting the evolving needs of the customers and users, who expect that the application meets Zero Trust security requirements. Learn the principles of the

Zero Trust model

and adopt the practices. By learning and adopting the principles, applications can be developed that are more secure and that minimize the damage they could cause if there's a break in security.

The Zero Trust model prescribes a culture of explicit verification rather than implicit trust. The model is anchored on three key

guiding principles

:

Verify explicitly

Use least privileged access

Assume breach

Zero Trust best practices

Follow these best practices to build Zero Trust-ready applications with the

Microsoft identity platform

and its tools.

Verify explicitly

The Microsoft identity platform offers authentication mechanisms for verifying the identity of the person or service accessing a resource. Apply the best practices described below to

verify explicitly

any entities that need to access data or resources.

Best practice

Benefits to application security

Use the

Microsoft Authentication Libraries (MSAL)

.

MSAL is a set of Microsoft Authentication Libraries for developers. With MSAL, users and applications can be authenticated, and tokens can be acquired to access corporate resources using just a few lines of code. MSAL uses modern protocols (

OpenID Connect and OAuth 2.0

) that remove the need for applications to ever handle a user's credentials directly. This handling of credentials vastly improves the security for both users and applications as the identity provider becomes the security perimeter. Also, these protocols continuously evolve to address new paradigms, opportunities, and challenges in identity security.

Adopt enhanced security extensions like

Continuous Access Evaluation (CAE)

and Conditional Access authentication context when appropriate.

In Microsoft Entra ID, some of the most used extensions include

Conditional Access

,

Conditional Access authentication context

and CAE. Applications that use enhanced security features like CAE and Conditional Access authentication context must be coded to handle claims challenges. Open protocols enable the

claims challenges and claims requests

to be used to invoke extra client capabilities. The capabilities might be to continue interaction with Microsoft Entra ID, such as when there was an anomaly or if the user authentication conditions change. These extensions can be coded into an application without disturbing the primary code flows for authentication.

Use the correct

authentication flow

by

application type

. For web applications, always try to use

confidential client flows

. For mobile applications, try to use

brokers

or the

system browser

for authentication.

The flows for web applications that can hold a secret (confidential clients) are considered more secure than public clients (for example: Desktop and Console applications). When the system web browser is used to authenticate a mobile application, a secure

single sign-on (SSO)

experience enables the use of application protection policies.

Use least privileged access

A developer uses the Microsoft identity platform to grant permissions (scopes) and verify that a caller has been granted proper permission before allowing access. Enforce least privileged access in applications by enabling fine-grained permissions that allow the smallest amount of access necessary to be granted. Consider the following practices to make sure of adherence to the

principle of least privilege

:

Evaluate the permissions that are requested to make sure that the absolute least privileged is set to get the job done. Don't create "catch-all" permissions with access to the entire API surface.

When designing APIs, provide granular permissions to allow least-privileged access. Start with dividing the functionality and data access into sections that can be controlled by using

scopes

and

App roles

. Don't add APIs to existing permissions in a way that changes the semantics of the permission.

Offer

read-only

permissions.

Write

access, includes privileges for create, update, and delete operations. A client should never require write access to only read data.

Offer both

delegated and application

permissions. Skipping application permissions can create hard requirement for clients to achieve common scenarios like automation, microservices and more.

Consider "standard" and "full" access permissions if working with sensitive data. Restrict the sensitive properties so that they can't be accessed using a "standard" access permission, for example

Resource.Read

. And then implement a "full" access permission, for example

Resource.ReadFull

that returns all available properties including sensitive information.

Assume breach

The Microsoft identity platform application registration portal is the primary entry point for applications intending to use the platform for their authentication and associated needs. When registering and configuring applications, follow the practices described below to minimize the damage they could cause if there's a security breach. For more information, see

Microsoft Entra application registration security best practices

.

Consider the following actions prevent breaches in security:

Properly define the redirect URIs for the application. Don't use the same application registration for multiple applications.

Verify redirect URIs used in the application registration for ownership and to avoid domain takeovers. Don't create the application as a multitenant unless it's intended to be.

Make sure application and service principal owners are always defined and maintained for the applications registered in the tenant.

See also

Zero Trust

Guidance Center

Microsoft identity platform

best practices and recommendations

.

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

2023-10-23
