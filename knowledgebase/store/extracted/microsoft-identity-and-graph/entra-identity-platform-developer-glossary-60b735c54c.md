---
title: Microsoft Identity Platform Glossary - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/developer-glossary
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:55.041254+00:00
kind: extracted-doc
---

# Microsoft Identity Platform Glossary - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/developer-glossary

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:55.041254+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/developer-glossary
- https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens
- https://learn.microsoft.com/en-us/entra/identity-platform/reference-app-manifest
- https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/application-consent-experience
- https://learn.microsoft.com/en-us/entra/identity-platform/id-tokens
- https://learn.microsoft.com/en-us/entra/identity-platform/howto-convert-app-to-be-multi-tenant
- https://learn.microsoft.com/en-us/entra/identity-platform/refresh-tokens
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols

Captured summary:

- Microsoft Identity Platform Glossary - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Microsoft identity platform glossary Feedback Summarize this article for me This glossary explains key terms in the Microsoft Identity Platform, Microsoft Entra admin center, and Microsoft Graph API.
- Learn about OAuth protocols and authentication concepts to build secure applications.

Extracted text:

Microsoft Identity Platform Glossary - Microsoft identity platform | Microsoft Learn

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

Microsoft identity platform glossary

Feedback

Summarize this article for me

This glossary explains key terms in the Microsoft Identity Platform, Microsoft Entra admin center, and Microsoft Graph API. Learn about OAuth protocols and authentication concepts to build secure applications.

Access token

A type of

security token

issued by an

authorization server

and used by a

client application

to access a

protected resource server

. Typically in the form of a

JSON Web Token (JWT)

, the token embodies the authorization granted to the client by the

resource owner

, for a requested level of access. The token contains all applicable

claims

about the subject, enabling the client application to use it as a form of credential when accessing a given resource. This also eliminates the need for the resource owner to expose credentials to the client.

Access tokens are only valid for a short period of time and can't be revoked. An authorization server may also issue a

refresh token

when the access token is issued. Refresh tokens are typically provided only to confidential client applications.

Access tokens are sometimes referred to as "User+App" or "App-Only", depending on the credentials being represented. For example, when a client application uses the:

"Authorization code" authorization grant

, the end user authenticates first as the resource owner, delegating authorization to the client to access the resource. The client authenticates afterward when obtaining the access token. The token can sometimes be referred to more specifically as a "User+App" token, as it represents both the user that authorized the client application, and the application.

"Client credentials" authorization grant

, the client provides the sole authentication, functioning without the resource-owner's authentication/authorization, so the token can sometimes be referred to as an "App-Only" token.

See the

access tokens reference

for more details.

Actor

Another term for the

client application

. The actor is the party acting on behalf of a subject (

resource owner

).

Application (client) ID

The application ID, or

client ID

, is a value the Microsoft identity platform assigns to your application when you register it in Microsoft Entra ID. The application ID is a GUID value that uniquely identifies the application and its configuration within the identity platform. You add the app ID to your application's code, and authentication libraries include the value in their requests to the identity platform at application runtime. The application (client) ID isn't a secret - don't use it as a password or other credential.

Application manifest

An application manifest is a feature that produces a JSON representation of the application's identity configuration, used as a mechanism for updating its associated

Application

and

ServicePrincipal

entities. See

Understanding the Microsoft Entra application manifest

for more details.

Application object

When you register/update an application, both an application object and a corresponding

service principal object

are created/updated for that tenant. The application object

defines

the application's identity configuration globally (across all tenants where it has access), providing a template from which its corresponding service principal objects are

derived

for use locally at run-time (in a specific tenant).

For more information, see

Application and Service Principal Objects

.

Application registration

In order to allow an application to integrate with and delegate Identity and Access Management functions to Microsoft Entra ID, it must be registered with a Microsoft Entra

tenant

. When you register your application with Microsoft Entra ID, you're providing an identity configuration for your application, allowing it to integrate with Microsoft Entra ID and use features like:

Robust management of single sign-on using Microsoft Entra identity management and

OpenID Connect

protocol implementation

Brokered access to

protected resources

by

client applications

, via OAuth 2.0

authorization server

Consent framework

for managing client access to protected resources, based on resource owner authorization.

See

Integrating applications with Microsoft Entra ID

for more details.

Authentication

The act of challenging a party for legitimate credentials, providing the basis for creation of a security principal to be used for identity and access control. During an

OAuth 2.0 authorization grant

for example, the party authenticating is filling the role of either

resource owner

or

client application

, depending on the grant used.

Authorization

The act of granting an authenticated security principal permission to do something. There are two primary use cases in the Microsoft Entra programming model:

During an

OAuth 2.0 authorization grant

flow: when the

resource owner

grants authorization to the

client application

, allowing the client to access the resource owner's resources.

During resource access by the client: as implemented by the

resource server

, using the

claim

values present in the

access token

to make access control decisions based upon them.

Authorization code

A short-lived value provided by the

authorization endpoint

to a

client application

during the OAuth 2.0

authorization code grant flow

, one of the four OAuth 2.0

authorization grants

. Also called an

auth code

, the authorization code is returned to the client application in response to the authentication of a

resource owner

. The auth code indicates the resource owner has delegated authorization to the client application to access their resources. As part of the flow, the auth code is later redeemed for an

access token

.

Authorization endpoint

One of the endpoints implemented by the

authorization server

, used to interact with the

resource owner

to provide an

authorization grant

during an OAuth 2.0 authorization grant flow. Depending on the authorization grant flow used, the actual grant provided can vary, including an

authorization code

or

security token

.

See the OAuth 2.0 specification's

authorization grant types

and

authorization endpoint

sections, and the

OpenIDConnect specification

for more details.

Authorization grant

A credential representing the

resource owner's

authorization

to access its protected resources, granted to a

client application

. A client application can use one of the

four grant types defined by the OAuth 2.0 Authorization Framework

to obtain a grant, depending on client type/requirements: "authorization code grant", "client credentials grant", "implicit grant", and "resource owner password credentials grant". The credential returned to the client is either an

access token

, or an

authorization code

(exchanged later for an access token), depending on the type of authorization grant used.

The resource owner password credentials grant

shouldn't be used

except in scenarios when other flows can't be used. If you're building a SPA, use the

authorization code flow with PKCE instead of implicit grant

.

Authorization server

As defined by the

OAuth 2.0 Authorization Framework

, the server responsible for issuing access tokens to the

client

after successfully authenticating the

resource owner

and obtaining its authorization. A

client application

interacts with the authorization server at runtime via its

authorization

and

token

endpoints, in accordance with the OAuth 2.0 defined

authorization grants

.

In the case of the Microsoft identity platform application integration, the Microsoft identity platform implements the authorization server role for Microsoft Entra applications and Microsoft service APIs, for example

Microsoft Graph APIs

.

Claim

Claims are name/values pairs in a

security token

that provide assertions made by one entity to another. These entities are typically the

client application

or a

resource owner

providing assertions to a

resource server

. Claims relay facts about the token subject like the ID of the security principal that was authenticated by the

authorization server

. The claims present in a token can vary and depend on several factors like the type of token, type of credential used for authenticating the subject, the application configuration, and others.

See the

Microsoft identity platform token reference

for more details.

Client application

Also known as the "

actor

". As defined by the

OAuth 2.0 Authorization Framework

, an application that makes protected resource requests on behalf of the

resource owner

. They receive permissions from the resource owner in the form of scopes. The term "client" doesn't imply any particular hardware implementation characteristics (for instance, whether the application executes on a server, a desktop, or other devices).

A client application requests

authorization

from a resource owner to participate in an

OAuth 2.0 authorization grant

flow, and may access APIs/data on the resource owner's behalf. The OAuth 2.0 Authorization Framework

defines two types of clients

, "confidential" and "public", based on the client's ability to maintain the confidentiality of its credentials. Applications can implement a

web client (confidential)

which runs on a web server, a

native client (public)

installed on a device, or a

user-agent-based client (public)

which runs in a device's browser.

Consent

The process of a

resource owner

granting authorization to a

client application

, to access protected resources under specific

permissions

, on behalf of the resource owner. Depending on the permissions requested by the client, an administrator or user will be asked for consent to allow access to their organization/individual data respectively. Note, in a

multitenant

scenario, the application's

service principal

is also recorded in the tenant of the consenting user.

See

consent framework

for more information.

Identity provider

An identity provider (IdP) is a service that creates, maintains, and manages identity information for users while providing authentication services to applications. In the context of Microsoft Entra, identity providers can include Microsoft accounts and social identity providers like Google or Facebook depending on your tenant configuration. When a user attempts to sign in, the application redirects the user to the appropriate identity provider for authentication.

ID token

An

OpenID Connect

security token

provided by an

authorization server's

authorization endpoint

, which contains

claims

pertaining to the authentication of an end user

resource owner

. Like an access token, ID tokens are also represented as a digitally signed

JSON Web Token (JWT)

. Unlike an access token though, an ID token's claims aren't used for purposes related to resource access and specifically access control.

See the

ID token reference

for more details.

Managed identities

Eliminate the need for developers to manage credentials. Managed identities provide an identity for applications to use when connecting to resources that support Microsoft Entra authentication. Applications may use the managed identity to obtain Microsoft identity platform tokens. For example, an application may use a managed identity to access resources like Azure Key Vault where developers can store credentials in a secure manner or to access storage accounts. For more information, see

managed identities overview

.

Microsoft identity platform

The Microsoft identity platform is an evolution of the Microsoft Entra identity service and developer platform. It allows developers to build applications that sign in all Microsoft identities, get tokens to call Microsoft Graph, other Microsoft APIs, or APIs that developers have built. It's a full-featured platform that consists of an authentication service, libraries, application registration and configuration, full developer documentation, code samples, and other developer content. The Microsoft identity platform supports industry standard protocols such as OAuth 2.0 and OpenID Connect.

Multitenant application

A class of application that enables sign in and

consent

by users provisioned in any Microsoft Entra

tenant

, including tenants other than the one where the client is registered.

Native client

applications are multitenant by default, whereas

web client

and

web resource/API

applications have the ability to select between single or multitenant. By contrast, a web application registered as single-tenant, would only allow sign-ins from user accounts provisioned in the same tenant as the one where the application is registered.

See

How to sign in any Microsoft Entra user using the multitenant application pattern

for more details.

Native client

A type of

client application

that is installed natively on a device. Since all code is executed on a device, it's considered a "public" client due to its inability to store credentials privately/confidentially. See

OAuth 2.0 client types and profiles

for more details.

Permissions

A

client application

gains access to a

resource server

by declaring permission requests. Two types are available:

"Delegated" permissions, which specify

scope-based

access using delegated authorization from the signed-in

resource owner

, are presented to the resource at run-time as

"scp" claims

in the client's

access token

. These indicate the permission granted to the

actor

by the

subject

.

"Application" permissions, which specify

role-based

access using the client application's credentials/identity, are presented to the resource at run-time as

"roles" claims

in the client's access token. These indicate permissions granted to the

subject

by the tenant.

They also surface during the

consent

process, giving the administrator or resource owner the opportunity to grant/deny the client access to resources in their tenant.

Permission requests are configured on the

API permissions

page for an application, by selecting the desired "Delegated Permissions" and "Application Permissions" (the latter requires membership in the Global Administrator role). Because a

public client

can't securely maintain credentials, it can only request delegated permissions, while a

confidential client

has the ability to request both delegated and application permissions. The client's

application object

stores the declared permissions in its

requiredResourceAccess property

.

Refresh token

A type of

security token

issued by an

authorization server

. Before an access token expires, a

client application

includes its associated refresh token when it requests a new

access token

from the authorization server. Refresh tokens are typically formatted as a

JSON Web Token (JWT)

.

Unlike access tokens, refresh tokens can be revoked. An authorization server denies any request from a client application that includes a refresh token that has been revoked. When the authorization server denies a request that includes a revoked refresh token, the client application loses the permission to access the

resource server

on behalf of the

resource owner

.

See the

refresh tokens

for more details.

Resource owner

As defined by the

OAuth 2.0 Authorization Framework

, an entity capable of granting access to a protected resource. When the resource owner is a person, it's referred to as an end user. For example, when a

client application

wants to access a user's mailbox through the

Microsoft Graph API

, it requires permission from the resource owner of the mailbox. The "resource owner" is also sometimes called the

subject

.

Every

security token

represents a resource owner. The resource owner is what the subject

claim

, object ID claim, and personal data in the token represent. Resource owners are the party that grants delegated permissions to a client application, in the form of scopes. Resource owners are also the recipients of

roles

that indicate expanded permissions within a tenant or on an application.

Resource server

As defined by the

OAuth 2.0 Authorization Framework

, a server that hosts protected resources, capable of accepting and responding to protected resource requests by

client applications

that present an

access token

. Also known as a protected resource server, or resource application.

A resource server exposes APIs and enforces access to its protected resources through

scopes

and

roles

, using the OAuth 2.0 Authorization Framework. Examples include the

Microsoft Graph API

, which provides access to Microsoft Entra tenant data, and the Microsoft 365 APIs that provide access to data such as mail and calendar.

Just like a client application, resource application's identity configuration is established via

registration

in a Microsoft Entra tenant, providing both the application and service principal object. Some Microsoft-provided APIs, such as the Microsoft Graph API, have preregistered service principals made available in all tenants during provisioning.

Roles

Like

scopes

, app roles provide a way for a

resource server

to govern access to its protected resources. Unlike scopes, roles represent privileges that the

subject

has been granted beyond the baseline - this is why reading your own email is a scope, while being an email administrator that can read everyone's email is a role.

App roles can support two assignment types: "user" assignment implements role-based access control for users/groups that require access to the resource, while "application" assignment implements the same for

client applications

that require access. An app role can be defined as user-assignable, app-assignable, or both.

Roles are resource-defined strings (for example "Expense approver", "Read-only", "Directory.ReadWrite.All"), managed via the resource's

application manifest

, and stored in the resource's

appRoles property

. Users can be assigned to "user" assignable roles and client

application permissions

can be configured to request "application" assignable roles.

For a detailed discussion of the application roles exposed by the Microsoft Graph API, see

Graph API Permission Scopes

. For a step-by-step implementation example, see

Add or remove Azure role assignments

.

Scopes

Like

roles

, scopes provide a way for a

resource server

to govern access to its protected resources. Scopes are used to implement

scope-based

access control, for a

client application

that has been given delegated access to the resource by its owner.

Scopes are resource-defined strings (for example "Mail.Read", "Directory.ReadWrite.All"), managed via the resource's

application manifest

, and stored in the resource's

oauth2Permissions property

. Client application

delegated permissions

can be configured to access a scope.

A best practice naming convention, is to use a "resource.operation.constraint" format. For a detailed discussion of the scopes exposed by Microsoft Graph API, see

Graph API Permission Scopes

. For scopes exposed by Microsoft 365 services, see

Microsoft 365 API permissions reference

.

Security token

A signed document containing claims, such as an OAuth 2.0 token or SAML 2.0 assertion. For an OAuth 2.0

authorization grant

, an

access token

(OAuth2),

refresh token

, and an

ID Token

are types of security tokens, all of which are implemented as a

JSON Web Token (JWT)

.

Service principal object

When you register/update an application, both an

application object

and a corresponding service principal object are created/updated for that tenant. The application object

defines

the application's identity configuration globally (across all tenants where the associated application has been granted access), and is the template from which its corresponding service principal object(s) are

derived

for use locally at run-time (in a specific tenant).

For more information, see

Application and Service Principal Objects

.

Sign-in

The process of a

client application

initiating end-user authentication and capturing related state for requesting a

security token

and scoping the application session to that state. State can include artifacts like user profile information, and information derived from token claims.

The sign-in function of an application is typically used to implement single-sign-on (SSO). It may also be preceded by a "sign-up" function, as the entry point for an end user to gain access to an application (upon first sign-in). The sign-up function is used to gather and persist additional state specific to the user, and may require

user consent

.

Sign-out

The process of unauthenticating an end user, detaching the user state associated with the

client application

session during

sign-in

Subject

Also known as the

resource owner

.

Tenant

An instance of a Microsoft Entra directory is referred to as a Microsoft Entra tenant. It provides several features, including:

a registry service for integrated applications

authentication of user accounts and registered applications

REST endpoints required to support various protocols including OAuth 2.0 and SAML, including the

authorization endpoint

,

token endpoint

and the "common" endpoint used by

multi-tenant applications

.

Microsoft Entra tenants are created/associated with Azure and Microsoft 365 subscriptions during sign-up, providing Identity & Access Management features for the subscription. Azure subscription administrators can also create additional Microsoft Entra tenants. See

How to get a Microsoft Entra tenant

for details on the various ways you can get access to a tenant. See

Associate or add an Azure subscription to your Microsoft Entra tenant

for details on the relationship between subscriptions and a Microsoft Entra tenant, and for instructions on how to associate or add a subscription to a Microsoft Entra tenant.

Tenants can be configured for either workforce or external scenarios. The tenant configuration you choose depends on the type of users you want to authenticate and authorize in your application. For more information, see

Supported features in workforce and external tenants

.

Token endpoint

One of the endpoints implemented by the

authorization server

to support OAuth 2.0

authorization grants

. Depending on the grant, it can be used to acquire an

access token

(and related "refresh" token) to a

client

, or

ID token

when used with the

OpenID Connect

protocol.

User-agent-based client

A type of

client application

that downloads code from a web server and executes within a user-agent (for instance, a web browser), such as a single-page application (SPA). Since all code is executed on a device, it's considered a "public" client due to its inability to store credentials privately/confidentially. For more information, see

OAuth 2.0 client types and profiles

.

User flow (External tenants only)

A user flow is a predefined, configurable policy that defines the steps a user goes through to sign up or sign in. User flows are used in Microsoft Entra External to provide a customizable experience for end users. They allow you to define the user journey, including the identity providers used, the attributes collected, and the UI customization options available. For more information, see

Create a User Flow in Microsoft Entra External ID

.

User principal

Similar to the way a service principal object is used to represent an application instance, a user principal object is another type of security principal, which represents a user. The Microsoft Graph

User

resource type

defines the schema for a user object, including user-related properties like first and last name, user principal name, directory role membership, and so on. This provides the user identity configuration for Microsoft Entra ID to establish a user principal at run-time. The user principal is used to represent an authenticated user for single sign-on, recording

consent

delegation, making access control decisions, and so on.

Web client

A type of

client application

that executes all code on a web server, functioning as a

confidential client

because it can securely store its credentials on the server. For more information, see

OAuth 2.0 client types and profiles

.

Workload identity

An identity used by a software workload like an application, service, script, or container to authenticate and access other services and resources. In Microsoft Entra ID, workload identities are apps, service principals, and managed identities. For more information, see

workload identity overview

.

Workload identity federation

Allows you to securely access Microsoft Entra protected resources from external apps and services without needing to manage secrets (for supported scenarios). For more information, see

workload identity federation

.

Next steps

Many of the terms in this glossary are related to the OAuth 2.0 and OpenID Connect protocols. Though you don't need to know how the protocols work "on the wire" to use the identity platform, knowing some protocol basics can help you more easily build and debug authentication and authorization in your apps:

OAuth 2.0 and OpenID Connect (OIDC) in the Microsoft identity platform

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

2025-05-12
