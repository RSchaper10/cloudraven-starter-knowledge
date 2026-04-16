---
title: Set up a test environment for your app - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/test-setup-environment
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:41.719770+00:00
kind: extracted-doc
---

# Set up a test environment for your app - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/test-setup-environment

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:41.719770+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/test-setup-environment
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/configurable-token-lifetimes
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-supported-account-types
- https://learn.microsoft.com/en-us/entra/identity-platform/howto-restrict-your-app-to-a-set-of-users

Captured summary:

- Set up a test environment for your app - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Set up your application's Microsoft Entra test environment Feedback Summarize this article for me To help move your app through the development, test, and production lifecycle, set up a Microsoft Entra test environment.
- You can use your Microsoft Entra test environment during the early stages of app development and long-term as a permanent test environment.

Extracted text:

Set up a test environment for your app - Microsoft identity platform | Microsoft Learn

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

Set up your application's Microsoft Entra test environment

Feedback

Summarize this article for me

To help move your app through the development, test, and production lifecycle, set up a Microsoft Entra test environment. You can use your Microsoft Entra test environment during the early stages of app development and long-term as a permanent test environment.

Choose between a dedicated test tenant or production Microsoft Entra tenant

You need to decide whether to use a dedicated test tenant or your production tenant for testing.

Using a production tenant can simplify some testing aspects but requires proper isolation between test and production resources, especially for high-privilege scenarios.

Avoid using your production tenant if:

Your app requires tenant-wide unique settings, such as app-only permissions needing admin consent.

You can't risk unauthorized access to test resources by tenant members.

Your production environment could be disrupted by configuration changes.

You can't create users or test data in your production tenant.

Your production tenant has policies requiring user interaction during authentication, like mandatory multifactor authentication. In such cases, you can't use automated sign-ins for integration testing.

Your

service or throttling limits

could be exceeded by adding nonproduction resources.

If these restrictions apply, set up a

test environment in a separate tenant

.

If not, you can set up a

test environment in your production tenant

. Users with privileged roles in your production tenant (such as Cloud Application Administrator) can access its resources and change its configuration at any time. To prevent access to any test resources or configuration, put that data in a separate tenant.

Set up a test environment in a separate tenant

Setting up a test environment in a separate tenant ensures that your production environment remains unaffected by changes or configurations made during testing. You need to set up a test tenant, populate it with users, and configure it with policies that match your production tenant.

Get a test tenant

If you don't already have a dedicated test tenant, you can create one for free using the Microsoft 365 Developer Program or manually create one yourself.

Microsoft 365 Developer Program

Create a tenant manually

The recommended approach is to join the

Microsoft 365 Developer Program

. This program is free and can have test user accounts and sample data packs automatically added to the tenant.

Open the

Microsoft 365 Developer Program

page and select

Join now

.

Sign in with a new Microsoft account or use an existing (work) account.

On the sign-up page select your region, enter a company name, and accept the terms and conditions of the program before you select

Next

.

Select on

Set Up Subscription

. Specify the region where you want to create your new tenant, create a username, domain, and enter a password. A new tenant is created and the first administrator of the tenant is added.

Enter the security information, which is needed to protect the administrator account of your new tenant. This sets up multifactor authentication for the account.

You can

manually create a tenant

, which is empty upon creation and needs to be configured with test data.

Populate your tenant with users

For convenience, you can invite yourself and other members of your development team to be guest users in the tenant. This creates separate guest objects in the test tenant, but means you only have to manage one set of credentials for your corporate account and your test account.

Sign in to the

Microsoft Entra admin center

as at least an

Application Developer

.

Browse to

Entra ID

>

Users

.

Select

New user

>

Invite external user

and invite your work account email address.

Repeat for other members of the development and/or testing team for your application.

You can also create test users in your test tenant. If you used one of the Microsoft 365 sample packs, you may already have some test users in your tenant. If not, you should be able to create some yourself as the tenant administrator.

Browse to

Entra ID

>

Users

.

Select

New user

>

Create new user

and create some new test users in your directory.

Get a Microsoft Entra subscription (optional)

If you want to fully test Microsoft Entra ID P1 or P2 features on your application, you need to sign up your tenant for a

Premium P1 or Premium P2 license

.

If you signed up using the Microsoft 365 Developer program, your test tenant comes with Microsoft Entra ID P2 licenses. If not, you can still enable a one month

free trial of Microsoft Entra ID P1 or P2

.

Create and configure an app registration

You need to create an app registration to use in your test environment. This should be a separate registration from your eventual production app registration, to maintain security isolation between your test environment and your production environment. How you configure your application depends on the type of app you're building. For more information, see

register an application

.

Populate your tenant with policies

If a single organization (often referred to as single tenant) will primarily use your app, and you have access to the production tenant, reduce the chances of unexpected errors in production by replicating the settings of your production tenant that can affect your app's behavior as much as possible.

Conditional Access policies

Replicating Conditional Access policies ensures you don't encounter unexpected blocked access when moving to production and your application can appropriately handle the errors it's likely to receive.

Viewing your production tenant Conditional Access policies may need to be performed by a

Conditional Access Administrator

.

Go to

Entra ID

>

Enterprise apps

>

Conditional Access

.

View the list of policies in your tenant, and select the first policy.

Navigate to

Cloud apps or actions

.

If the policy only applies to a select group of apps, then move on to the next policy. If not, then it will likely apply to your app as well when you move to production. You should copy the policy over to your test tenant.

In a new tab or browser session, sign in to the

Microsoft Entra admin center

as at least a

Conditional Access Administrator

to access your test tenant.

Browse to

Entra ID

>

Conditional Access

.

Select

Create new policy

Copy the settings from the production tenant policy, identified through the previous steps.

Permission grant policies

Replicating permission grant policies ensures you don't encounter unexpected prompts for admin consent when moving to production.

Browse to

Entra ID

>

Enterprise apps

>

Consent and permissions

>

User consent

settings. Copy the settings there to your test tenant.

Token lifetime policies

Replicating token lifetime policies ensures tokens issued to your application don't expire unexpectedly in production.

Token lifetime policies can currently only be managed through PowerShell. Read about

configurable token lifetimes

to learn about identifying any token lifetime policies that apply to your whole production organization. Copy those policies to your test tenant.

Set up a test environment in your production tenant

If you can safely constrain your test app in your production tenant, then you can configure your tenant for testing purposes.

Create and configure an app registration

You need to create an app registration to use in your test environment. This should be a separate registration from your eventual production app registration, to maintain security isolation between your test environment and your production environment. How you configure your application depends on the type of app you're building. For more information, refer to

Register an application in Microsoft Entra ID

.

Create some test users

You need to create some test users with associated test data to use while testing your scenarios. This step might need to be performed by an admin.

Browse to

Entra ID

>

Users

.

Select

New user

>

Create new user

and create some new test users in your directory.

Add the test users to a group (optional)

For convenience, you can assign all these users to a group, which makes other assignment operations easier.

Browse to

Entra ID

>

Groups

>

All groups

.

Select

New group

.

Select either

Security

or

Microsoft 365

for group type.

Name your group.

Add the test users created in the previous step.

Restrict your test application to specific users

You can restrict the users in your tenant that are allowed to use your test application to specific users or groups, through user assignment. When you

created an app through App registrations

, a representation of your app was created in

Enterprise applications

as well. Use the

Enterprise applications

settings to restrict who can use the application in your tenant.

Important

If your app is a

multitenant app

, this operation doesn't restrict users in other tenants from signing into and using your app. It will only restrict users in the tenant that user assignment is configured in.

For detailed instructions on restricting an app to specific users in a tenant, go to

restricting your app to a set of users

.

Next step

Learn about Microsoft Entra usage constraints and service limits you might hit

here

. General Azure subscription and service limits, quotas, and constraints can be found

here

.

For more detailed information about test environments, read

Securing Azure environments with Microsoft Entra ID

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

2025-04-25
