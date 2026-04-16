---
title: How to register an app in Microsoft Entra ID - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:33.171764+00:00
kind: extracted-doc
---

# How to register an app in Microsoft Entra ID - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:33.171764+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/media/quickstart-register-app/portal-02-app-reg-01.png
- https://learn.microsoft.com/en-us/entra/identity-platform/media/quickstart-register-app/portal-03-app-reg-02.png
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-expose-web-apis
- https://learn.microsoft.com/en-us/entra/identity-platform/sample-v2-code

Captured summary:

- How to register an app in Microsoft Entra ID - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Register an application in Microsoft Entra ID Feedback Summarize this article for me In this how-to guide, you learn how to register an application in Microsoft Entra ID.
- This process is essential for establishing a trust relationship between your application and the Microsoft identity platform.

Extracted text:

How to register an app in Microsoft Entra ID - Microsoft identity platform | Microsoft Learn

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

Register an application in Microsoft Entra ID

Feedback

Summarize this article for me

In this how-to guide, you learn how to register an application in Microsoft Entra ID. This process is essential for establishing a trust relationship between your application and the Microsoft identity platform. By completing this quickstart, you enable identity and access management (IAM) for your app, allowing it to securely interact with Microsoft services and APIs.

Prerequisites

An Azure account that has an active subscription.

Create an account for free

.

The Azure account must be at least a

Application Developer

.

A workforce or external tenant. You can use your

Default Directory

for this quickstart. If you need an external tenant, complete

set up an external tenant

.

Register an application

Registering your application in Microsoft Entra establishes a trust relationship between your app and the Microsoft identity platform. The trust is unidirectional. Your app trusts the Microsoft identity platform, and not the other way around. Once created, the application object can't be moved between different tenants.

Follow these steps to create the app registration:

Sign in to the

Microsoft Entra admin center

as at least an

Application Developer

.

If you have access to multiple tenants, use the

Settings

icon

in the top menu to switch to the tenant in which you want to register the application.

Browse to

Entra ID

>

App registrations

and select

New registration

.

Enter a meaningful

Name

for your app, for example

identity-client-app

. App users can see this name, and it can be changed at any time. You can have multiple app registrations with the same name.

Under

Supported account types

, specify who can use the application. We recommend you select

Accounts in this organizational directory only

for most applications. Refer to the table for more information on each option.

Supported account types

Description

Accounts in this organizational directory only

For

single-tenant

apps for use only by users (or guests) in

your

tenant.

Accounts in any organizational directory

For

multitenant

apps and you want users in

any

Microsoft Entra tenant to be able to use your application. Ideal for software-as-a-service (SaaS) applications that you intend to provide to multiple organizations.

Accounts in any organizational directory and personal Microsoft accounts

For

multitenant

apps that support both organizational and personal Microsoft accounts (for example, Skype, Xbox, Live, Hotmail).

Personal Microsoft accounts

For apps used only by personal Microsoft accounts (for example, Skype, Xbox, Live, Hotmail).

Select

Register

to complete the app registration.

The application's

Overview

page is displayed. Record the

Application (client) ID

, which uniquely identifies your application and is used in your application's code as part of validating the security tokens it receives from the Microsoft identity platform.

Important

New app registrations are hidden to users by default. When you're ready for users to see the app on their

My Apps page

you can enable it. To enable the app, in the Microsoft Entra admin center navigate to

Entra ID

>

Enterprise apps

and select the app. Then on the

Properties

page, set

Visible to users?

to

Yes

.

Grant admin consent (external tenants only)

Once you register your application, it gets assigned the

User.Read

permission. However, for external tenants, the customer users themselves can't consent to permissions themselves. You as the admin must consent to this permission on behalf of all the users in the tenant:

From the

Overview

page of your app registration, under

Manage

select

API permissions

.

Select

Grant admin consent for < tenant name >

, then select

Yes

.

Select

Refresh

, then verify that

Granted for < tenant name >

appears under

Status

for the permission.

Related content

Add a redirect URI to your application

Add credentials to your application

Configure an application to expose a web API

Microsoft identity platform code samples

Add your application to a user flow

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

2025-04-08
