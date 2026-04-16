---
title: Code samples for authentication and authorization - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/sample-v2-code
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:31.596052+00:00
kind: extracted-doc
---

# Code samples for authentication and authorization - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/sample-v2-code

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:31.596052+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/sample-v2-code
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-app-types
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-single-page-app-react-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-single-page-app-react-prepare-app
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-single-page-app-angular-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-angular-auth-code
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-single-page-app-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-single-page-app-blazor-wasm-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-app-dotnet-core-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-app-dotnet-prepare-app
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-app-java-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-app-nodejs-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-nodejs-webapp-msal
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-app-python-flask
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-app-python-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-api-aspnet-protect-api
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-api-aspnet-core-protect-api
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-api-dotnet-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-desktop-app-nodejs-electron-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-nodejs-desktop

Captured summary:

- Code samples for authentication and authorization - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Microsoft identity platform code samples for authentication and authorization Feedback Summarize this article for me These code samples are built and maintained by Microsoft to demonstrate usage of our authentication libraries with the Microsoft identity platform.
- Common authentication and authorization scenarios are implemented in several application types , development languages, and frameworks.

Extracted text:

Code samples for authentication and authorization - Microsoft identity platform | Microsoft Learn

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

Microsoft identity platform code samples for authentication and authorization

Feedback

Summarize this article for me

These code samples are built and maintained by Microsoft to demonstrate usage of our authentication libraries with the Microsoft identity platform. Common authentication and authorization scenarios are implemented in several

application types

, development languages, and frameworks.

Sign in users to web applications and provide authorized access to protected web APIs.

Protect a web API by requiring an access token to perform API operations.

Each code sample includes a

README.md

file describing how to build the project (if applicable) and run the sample application. Comments in the code help you understand how these libraries are used in the application to perform authentication and authorization by using the identity platform.

Samples and guides

Use the tabs to sort the samples by application type, or your preferred language/framework.

By app type

By language/framework

Single-page applications

These samples show how to write a single-page application secured with Microsoft identity platform. These samples use one of the flavors of MSAL.js.

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

React

•

Sign in users

MSAL React

Authorization code with PKCE

Quickstart

Tutorial

Angular

•

Sign in users

MSAL Angular

Authorization code with PKCE

Quickstart

Tutorial

JavaScript

•

Sign in users

•

Call Microsoft Graph

•

Call Node.js web API

•

Deploy to Azure Storage and App Service

MSAL.js

Authorization code with PKCE

Quickstart

Blazor WebAssembly

•

Sign in users

•

Call Microsoft Graph

•

Deploy to Azure App Service

MSAL.js

Authorization code with PKCE

Quickstart

Web applications

The following samples illustrate web applications that sign in users. Some samples also demonstrate the application calling Microsoft Graph, or your own web API with the user's identity.

Language / Platform

Code sample(s) on GitHub

Auth libraries

Auth flow

Quickstart

Tutorial

ASP.NET

•

Microsoft Graph Training Sample

•

Sign in users and call Microsoft Graph with admin restricted scope

•

MSAL.NET

•

Microsoft.Identity.Web

•

Advanced Token Cache Scenarios

• OpenID connect

• Authorization code

• On-Behalf-Of (OBO)

Quickstart

ASP.NET Core

•

Sign in users

•

Call Microsoft Graph

•

Customize token cache

•

Use the Conditional Access auth context to perform step-up authentication

•

Call Graph (multitenant)

•

Call Azure REST APIs

•

Protect web API

•

Protect multitenant web API

•

Use App Roles for access control

•

Use Security Groups for access control

•

Deploy to Azure Storage and App Service

•

Active Directory Federation Services to Microsoft Entra migration

Microsoft.Identity.Web

• OpenID connect

• Authorization code

• On-Behalf-Of Flow (OBO)

Quickstart

Tutorial

Blazor

•

Sign in users

•

Call Microsoft Graph

•

Call web API

MSAL.NET

Hybrid flow

Java Spring

•

Sign in users

•

Call Microsoft Graph

•

Use App Roles for access control

•

Use Groups for access control

•

Protect a web API

•

Deploy to Azure App Service

MSAL Java

Authorization code

Tutorial

Java Servlets

•

Sign in users

•

Call Microsoft Graph

•

Use App Roles for access control

•

Use Security Groups for access control

•

Deploy to Azure App Service

MSAL Java

Authorization code

Quickstart

Node.js Express

•

Sign in users

•

Express web application built with MSAL Node and Microsoft identity platform

•

Call Microsoft Graph

•

Call Microsoft Graph via BFF proxy

•

Use App Roles for access control

•

Use Security Groups for access control

•

Deploy to Azure App Service

MSAL Node

• Authorization code

• Backend-for-Frontend (BFF) proxy

Quickstart

Tutorial

Python Flask

•

Sign in users

•

Template to sign in Microsoft Entra ID, and optionally call a downstream API (Microsoft Graph)

MSAL Python

Authorization code

Quickstart

Tutorial

Python Django

•

Sign in users

MSAL Python

Authorization code

Ruby

•

Sign in users and call Microsoft Graph

OmniAuth OAuth2

Authorization code

Web API

The following samples show how to protect a web API with the Microsoft identity platform, and how to call a downstream API from the web API.

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

ASP.NET

•

Call Microsoft Graph

MSAL.NET

On-Behalf-Of (OBO)

Quickstart

ASP.NET Core

•

Access control (protected routes) with the Microsoft identity platform

MSAL.NET

On-Behalf-Of (OBO)

Quickstart

Tutorial

Java

•

Protect your Java Spring Boot web API with the Microsoft identity platform

MSAL Java

On-Behalf-Of (OBO)

Node.js

•

Protect a Node.js web API

MSAL Node

Authorization bearer

Desktop

The following samples show public client desktop applications that access the Microsoft Graph API, or your own web API in the name of the user. Apart from the

Desktop (Console) with Web Authentication Manager (WAM)

sample, all these client applications use the Microsoft Authentication Library (MSAL).

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

.NET Core

•

Call Microsoft Graph

•

Call Microsoft Graph with token cache

•

Call Microsoft Graph with custom web UI HTML

•

Call Microsoft Graph with custom web browser

•

Sign in users with device code flow

•

Call Microsoft Graph by signing in users using username/password

MSAL.NET

• Authorization code with PKCE

• Device code

• Resource owner password credentials

Java

•

Call Microsoft Graph

MSAL Java

Integrated Windows authentication

Node.js

•

Sign in users

MSAL Node

Authorization code with PKCE

Quickstart

Tutorial

Python

•

Sign in users

MSAL Python

Resource owner password credentials

Windows Presentation Foundation (WPF)

•

Sign in users and call Microsoft Graph

•

Windows Presentation Foundation (WPF) user sign-in, protected web API access (Microsoft Graph)

•

Sign in users and call ASP.NET Core web API

•

Sign in users and call Microsoft Graph

MSAL.NET

Authorization code with PKCE

Quickstart

Tutorial

Mobile

The following samples show public client mobile applications that access the Microsoft Graph API. These client applications use the Microsoft Authentication Library (MSAL).

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

.NET Core

•

Call Microsoft Graph using MAUI

•

Call Microsoft Graph using MAUI with broker

MSAL.NET

Authorization code with PKCE

iOS

•

Call Microsoft Graph native

MSAL iOS

Authorization code with PKCE

Quickstart

Tutorial

Java

•

Sign in users and call Microsoft Graph

MSAL Android

Authorization code with PKCE

Quickstart

Tutorial

Kotlin

•

Sign in users and call Microsoft Graph

MSAL Android

Authorization code with PKCE

Service / daemon

The following samples show an application that accesses the Microsoft Graph API with its own identity (with no user).

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

.NET

•

.NET console app that accesses a protected web API

•

Multitenant with Microsoft identity platform endpoint

MSAL.NET

Client credentials grant

Quickstart

Tutorial

.NET Core

•

Call Microsoft Graph

•

Call web API

•

Using managed identity to call MSGraph

•

Using managed identity to call an API

•

Worker role calling an API

Microsoft.Identity.Web

Client credentials grant

Java

•

Call Microsoft Graph with Secret

•

Call Microsoft Graph with Certificate

MSAL Java

Client credentials grant

Quickstart

Node.js

•

Call Microsoft Graph with secret

MSAL Node

Client credentials grant

Quickstart

Tutorial

Python

•

Call Microsoft Graph with secret

•

Call Microsoft Graph with certificate

MSAL Python

Client credentials grant

Quickstart

Browserless (Headless)

The following sample shows a public client application running on a device without a web browser. The app can be a command-line tool, an app running on Linux or Mac, or an IoT application. The sample features an app accessing the Microsoft Graph API, in the name of a user who signs in interactively on another device (such as a mobile phone). This client application uses the Microsoft Authentication Library (MSAL).

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

.NET Core

•

Invoke protected API from text-only device

MSAL.NET

Device code

Java

•

Sign in users and invoke protected API from text-only device

MSAL Java

Device code

Python

•

Call Microsoft Graph

MSAL Python

Device code

Azure Functions as web APIs

The following samples show how to protect an Azure Function using HttpTrigger and exposing a web API with the Microsoft identity platform, and how to call a downstream API from the web API.

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Python

•

Python Azure function web API secured by Microsoft Entra ID

MSAL Python

Authorization code

Microsoft Teams applications

The following sample illustrates Microsoft Teams Tab application that signs in users. Additionally it demonstrates how to call Microsoft Graph API with the user's identity using the Microsoft Authentication Library (MSAL).

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Node.js

•

Teams Tab app: single sign-on (SSO) and call Microsoft Graph

MSAL Node

On-Behalf-Of (OBO)

Multitenant SaaS

The following samples show how to configure your application to accept sign-ins from any Microsoft Entra tenant. Configuring your application to be

multitenant

means that you can offer a

Software as a Service

(SaaS) application to many organizations, allowing their users to be able to sign-in to your application after providing consent.

Language /

Platform

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

ASP.NET Core

•

ASP.NET Core MVC web application calls Microsoft Graph API

•

ASP.NET Core MVC web application calls ASP.NET Core web API

MSAL.NET

• OpenID connect

• Authorization code

C#

The following samples show how to build applications using the C# language and frameworks

.NET Core

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Desktop

•

Call Microsoft Graph

•

Call Microsoft Graph with token cache

•

Call Microsoft Graph with custom web UI HTML

•

Call Microsoft Graph with custom web browser

•

Sign in users with device code flow

•

Call Microsoft Graph by signing in users using username/password

MSAL.NET

• Authorization code with PKCE

• Device code

Mobile

•

Call Microsoft Graph using MAUI

•

Call Microsoft Graph using MAUI with broker

MSAL.NET

Authorization code with PKCE

Service/daemon

•

Call Microsoft Graph

•

Call web API

•

Using managed identity and Azure key vault

MSAL.NET

Client credentials grant

Headless

•

Invoke protected API from text-only device

MSAL.NET

Device code

ASP.NET

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web application

•

Microsoft Graph Training Sample

•

Sign in users and call Microsoft Graph with admin restricted scope

MSAL.NET

• OpenID connect

• Authorization code

Quickstart

Web API

•

Call Microsoft Graph

MSAL.NET

On-Behalf-Of (OBO)

Service/

daemon

•

Multitenant with Microsoft identity platform endpoint

MSAL.NET

Client credentials grant

ASP.NET Core

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web application

•

Sign in users

•

Call Microsoft Graph

•

Customize token cache

•

Use the Conditional Access auth context to perform step-up authentication

•

Call Graph (multitenant)

•

Call Azure REST APIs

•

Protect web API

•

Protect multitenant web API

•

Use App Roles for access control

•

Use Security Groups for access control

•

Deploy to Azure Storage and App Service

•

Active Directory Federation Services to Microsoft Entra migration

•

Active Directory Federation Services to Microsoft Entra migration

Use the Conditional Access auth context to perform step-up authentication

Advanced Token Cache Scenarios

Microsoft.Identity.Web

• OpenID connect

• Authorization code

• On-Behalf-Of

Quickstart

Tutorial

Web API

•

Sign in users and call Microsoft Graph

MSAL.NET

On-Behalf-Of (OBO)

Quickstart

Tutorial

Multitenant SaaS

•

ASP.NET Core MVC web application calls Microsoft Graph API

•

ASP.NET Core MVC web application calls ASP.NET Core web API

MSAL.NET

OpenID connect

Blazor

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Single-page application

•

Sign in users

•

Call Microsoft Graph

•

Deploy to Azure App Service

MSAL.js

Implicit Flow

Quickstart

Web application

•

Sign in users

•

Call Microsoft Graph

•

Call web API

MSAL.NET

Implicit/Hybrid flow

iOS

The following samples show how to build applications for the iOS platform.

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Mobile

•

Call Microsoft Graph native

MSAL iOS

Authorization code with PKCE

Quickstart

Tutorial

JavaScript

Vanilla JavaScript

The following samples show how to build applications for the JavaScript language and platform.

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Single-page application

•

Sign in users

•

Call Microsoft Graph

•

Call Node.js web API

•

Deploy to Azure Storage and App Service

MSAL.js

Authorization code with PKCE

Quickstart

Angular

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Single-page application

•

Sign in users

MSAL Angular

Authorization code with PKCE

Quickstart

Tutorial

Node.js

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web API

•

Protect a Node.js web API

MSAL Node

Authorization bearer

Desktop

•

Sign in users

MSAL Node

Authorization code with PKCE

Tutorial

Service, daemon

•

Call Microsoft Graph with secret

MSAL Node

Client credentials grant

Quickstart

Microsoft Teams applications

•

Teams Tab app: single sign-on (SSO) and call Microsoft Graph

MSAL Node

On-Behalf-Of (OBO)

Node.js (Express)

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web application

•

Sign in users

•

Call Microsoft Graph

•

Deploy to Azure App Service

•

Use App Roles for access control

•

Use Security Groups for access control

•

Web app that sign in users

MSAL Node

Authorization code

Quickstart

Tutorial

React

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Single-page application

•

Sign in users

MSAL React

• Authorization code with PKCE

Quickstart

Tutorial

Java

The following samples show how to build applications for the Java language and platform.

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web API

•

Sign in users

MSAL Java

On-Behalf-Of (OBO)

Desktop

•

Call Microsoft Graph

MSAL Java

Integrated Windows authentication

Mobile

•

Sign in users and call Microsoft Graph

MSAL Android

Authorization code with PKCE

Service/

daemon

•

Call Microsoft Graph with Secret

•

Call Microsoft Graph with Certificate

MSAL Java

Client credentials grant

Quickstart

Java Spring

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web application

Microsoft Entra Spring Boot Starter Series

•

Sign in users

•

Call Microsoft Graph

•

Use App Roles for access control

•

Use Groups for access control

•

Deploy to Azure App Service

•

Protect a web API

•

MSAL Java

• Microsoft Entra ID Boot Starter

Authorization code

Tutorial

Java Servlet

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web application

Spring-less Servlet Series

•

Sign in users

•

Call Microsoft Graph

•

Use App Roles for access control

•

Use Security Groups for access control

•

Deploy to Azure App Service

MSAL Java

Authorization code

Python

The following samples show how to build applications for the Python language and platform.

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Azure Functions as web APIs

•

Python Azure function web API secured by Microsoft Entra ID

MSAL Python

Authorization code

Desktop

•

Sign in users

MSAL Python

Resource owner password credentials

Headless

•

Call Microsoft Graph

MSAL Python

Device code

Daemon

•

Call Microsoft Graph with secret

•

Call Microsoft Graph with certificate

MSAL Python

Client credentials grant

Quickstart

Flask

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web application

•

Sign in users

•

A template to sign in Microsoft Entra ID, and optionally call a downstream API (Microsoft Graph)

MSAL Python

Authorization code

Quickstart

Tutorial

Django

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web application

•

Sign in users

•

Integrating Microsoft Entra ID with a Python web application written in Django

MSAL Python

Authorization code

Kotlin

The following samples show how to build applications with Kotlin.

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Mobile

•

Sign in users and call Microsoft Graph

MSAL Android

Authorization code with PKCE

Ruby

The following samples show how to build applications with Ruby.

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Web application

Graph Training

•

Sign in users and call Microsoft Graph

OmniAuth OAuth2

Authorization code

Windows Presentation Foundation (WPF)

The following samples show how to build applications with Windows Presentation Foundation (WPF).

App type

Code sample(s)

on GitHub

Auth

libraries

Auth flow

Quickstart

Tutorial

Desktop

•

Sign in users and call Microsoft Graph

MSAL.NET

Authorization code with PKCE

Desktop

•

Sign in users and call ASP.NET Core web API

•

Sign in users and call Microsoft Graph

MSAL.NET

Authorization code with PKCE

Quickstart

Tutorial

Related content

If you'd like to delve deeper into more sample code, see:

Sign in users and call the Microsoft Graph API from an Angular

Sign in users in a Node.js and Express web app

Call the Microsoft Graph API from a Universal Windows Platform

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

2025-01-27
