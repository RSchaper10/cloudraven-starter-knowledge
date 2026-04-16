---
title: Tutorial: Prepare a web application for authentication - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-app-dotnet-prepare-app
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:48.932631+00:00
kind: extracted-doc
---

# Tutorial: Prepare a web application for authentication - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-app-dotnet-prepare-app

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:48.932631+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-app-dotnet-prepare-app
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri
- https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-self-signed-certificate
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-app-dotnet-sign-in-users
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-app-dotnet-sign-in-users?toc=/entra/external-id/toc.json&bc=/entra/external-id/breadcrumb/toc.json&tabs=external-tenant

Captured summary:

- Tutorial: Prepare a web application for authentication - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Tutorial: Set up an ASP.NET Core web app that authenticates users Feedback Summarize this article for me Applies to : Workforce tenants External tenants ( learn more ) In this tutorial, you create an ASP.NET Core web app and configure it for authentication.
- This is part 1 of a series that demonstrates how to build an ASP.NET Core web application and prepare it for authentication using the Microsoft Entra admin center.

Extracted text:

Tutorial: Prepare a web application for authentication - Microsoft identity platform | Microsoft Learn

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

Tutorial: Set up an ASP.NET Core web app that authenticates users

Feedback

Summarize this article for me

Applies to

:

Workforce tenants

External tenants (

learn more

)

In this tutorial, you create an ASP.NET Core web app and configure it for authentication. This is part 1 of a series that demonstrates how to build an ASP.NET Core web application and prepare it for authentication using the Microsoft Entra admin center. This application can be used for employees in a workforce tenant or for customers using an external tenant

In this tutorial, you:

Create an ASP.NET Core web app

Create a self-signed certificate

Configure the settings for the application

Define platform settings and URLs

Prerequisites

An Azure account with an active subscription.

Create an account for free

. This account must have permissions to manage applications. Use any of the following roles needed to register the application:

Application Administrator

Application Developer

Although any integrated development environment (IDE) that supports ASP.NET Core applications can be used, this tutorial uses

Visual Studio Code

. You can download it

here

.

A minimum requirement of

.NET 8.0 SDK

.

An ASP.NET Core developer certificate. Install one using

dotnet dev-certs

Workforce tenant

External tenant

Register a new app in the

Microsoft Entra admin center

, configured for

Accounts in this organizational directory only

. Refer to

Register an application

for more details. Record the following values from the application

Overview

page for later use:

Application (client) ID

Directory (tenant) ID

Add the following redirect URIs using the

Web

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

https://localhost:5001/signin-oidc

Front channel logout URL

:

https://localhost:5001/signout-oidc

For development purposes,

create a self signed certificate

. Refer to

add credentials

to upload the certificate and record the certificate

Thumbprint

.

Do not use a self signed certificate

for production apps. Use a trusted certificate authority.

An external tenant. If you don't have one,

create a new external tenant

in the Microsoft Entra admin center.

Register a new app in the

Microsoft Entra admin center

, configured for

Accounts in this organizational directory only

. Refer to

Register an application

for more details. Record the following values from the application

Overview

page for later use:

Application (client) ID

Directory (tenant) ID

Add the following redirect URIs using the

Web

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

https://localhost:5001/signin-oidc

Front channel logout URL

:

https://localhost:5001/signout-oidc

For development purposes,

create a self signed certificate

. Refer to

add credentials

to upload the certificate and record the certificate

Thumbprint

.

Do not use a self signed certificate

for production apps. Use a trusted certificate authority.

Associate your app with a user flow in the Microsoft Entra admin center. This user flow can be used across multiple applications. For more information, see

Create self-service sign-up user flows for apps in external tenants

and

Add your application to the user flow

.

Create an ASP.NET Core project

In this section, you create an ASP.NET Core project in Visual Studio Code.

Open Visual Studio Code and select

File > Open Folder...

. Navigate to and select the location in which to create your project.

Open a new terminal by selecting

Terminal > New Terminal

.

Enter the following command to make a Model View Controller (MVC) ASP.NET Core project.

dotnet new mvc -n identity-client-web-app

Install identity packages

This application uses

Microsoft.Identity.Web

and the related NuGet package must be installed.

Use the following snippet to change into the new

identity-client-web-app

folder and install the relevant NuGet package:

cd identity-client-web-app dotnet add package Microsoft.Identity.Web.UI

Configure the application for authentication

Web applications that sign in users by using the Microsoft identity platform are configured through a configuration file,

appsettings.json

. In ASP.NET Core, it must specify the following values:

Workforce tenant

External tenant

Setting

Description

Instance

The authentication endpoint to run your app in national clouds. Use one of:

-

https://login.microsoftonline.com/

(Azure public cloud)

-

https://login.microsoftonline.us/

(Azure US government)

-

https://login.microsoftonline.de/

(Microsoft Entra Germany)

-

https://login.partner.microsoftonline.cn/

(Microsoft Entra China operated by 21Vianet)

TenantId

The identifier of the tenant where the app is registered.

Recommended:

use the tenant ID from the app registration.

Alternatives:

-

organizations

(any work or school account)

-

common

(work/school or Microsoft personal account)

-

consumers

(Microsoft personal accounts only).

ClientId

Identifier of the application (client) obtained from the application registration.

CertificateThumbprint

Thumbprint of the certificate uploaded in the Microsoft Entra admin center (see

add credentials

).

CallbackPath

Path used to redirect responses; set to

/signin-oidc

for this tutorial.

DownstreamApi

Identifier that defines an endpoint for accessing Microsoft Graph. Combine the application URI with the required scope (for example,

user.read

).

Setting

Description

Authority

URL of the external tenant where the application is registered. Format:

https://<tenant_subdomain>.ciamlogin.com/

. To obtain your tenant subdomain details, see

Create an external tenant

.

ClientId

Identifier of the application (client) obtained from the application registration.

CertificateThumbprint

Thumbprint of the certificate obtained from

add credentials

in the Microsoft Entra admin center.

Update the configuration file

In your IDE, open

appsettings.json

and replace the file contents with the following snippet. Replace the text in quotes with the values that were recorded earlier.

Workforce tenant

External tenant

{ "AzureAd": { "Instance": "https://login.microsoftonline.com/", "TenantId": "Enter_the_Tenant_Id_Here", "ClientId": "Enter_the_Application_Id_Here", "ClientCertificates": [ { "SourceType": "StoreWithThumbprint", "CertificateStorePath": "CurrentUser/My", "CertificateThumbprint": "Enter the certificate thumbprint obtained the Microsoft Entra admin center" } ], "CallbackPath": "/signin-oidc" }, "DownstreamApi": { "BaseUrl": "https://graph.microsoft.com/v1.0/", "RelativePath": "me", "Scopes": [ "user.read" ] }, "Logging": { "LogLevel": { "Default": "Information", "Microsoft.AspNetCore": "Warning" } }, "AllowedHosts": "*" }

{ "AzureAd": { "Authority": "https://Enter_the_Tenant_Subdomain_Here.ciamlogin.com/", "ClientId": "Enter_the_Application_Id_Here", "ClientCertificates": [ { "SourceType": "StoreWithThumbprint", "CertificateStorePath": "CurrentUser/My", "CertificateThumbprint": "Enter the certificate thumbprint obtained the Microsoft Entra admin center" } ], "CallbackPath": "/signin-oidc", "SignedOutCallbackPath": "/signout-callback-oidc" }, "DownstreamApi": { "BaseUrl": "https://graph.microsoft.com/v1.0/", "RelativePath": "me", "Scopes": [ "user.read" ] }, "Logging": { "LogLevel": { "Default": "Information", "Microsoft.AspNetCore": "Warning" } }, "AllowedHosts": "*" }

Update the redirect URI

From the

prerequisites

, the redirect URI is set to

https://localhost:5001/signin-oidc

. This needs to be updated in the application launch settings. You can use the redirect URI that is created during the local application setup, or any other available port number, provided it matches the redirect URI in the application registration.

In the

Properties

folder, open the

launchSettings.json

file.

Find the

https

object, and update the value of

applicationURI

with the correct port number, in this case,

5001

. The line should look similar to the following snippet:

"applicationUrl": "https://localhost:5001;http://localhost:{port}",

Next step

Workforce tenant

External tenant

Configure an ASP.NET Core web app for authorization and authentication

Configure an ASP.NET Core web app for authorization and authentication

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

2025-12-01
