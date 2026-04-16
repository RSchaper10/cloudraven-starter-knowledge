---
title: Sign in users in sample macOS (Swift) app by using native authentication - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-macos-sign-in
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:48.074915+00:00
kind: extracted-doc
---

# Sign in users in sample macOS (Swift) app by using native authentication - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-macos-sign-in

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:48.074915+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-macos-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/media/native-authentication/macos/native-auth-sign-in-sign-up-password-expanded-macos.png
- https://learn.microsoft.com/en-us/entra/identity-platform/media/native-authentication/macos/enter-one-time-pass-code-expanded-macos.png

Captured summary:

- Sign in users in sample macOS (Swift) app by using native authentication - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Sign in users in sample macOS app by using native authentication Feedback Summarize this article for me Applies to : External tenants ( learn more ) This guide shows how to run an macOS sample application that demonstrates sign-up and sign in scenarios using Microsoft Entra External ID.
- In this article, you learn how to: Enable public client and native authentication flows.

Extracted text:

Sign in users in sample macOS (Swift) app by using native authentication - Microsoft identity platform | Microsoft Learn

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

Sign in users in sample macOS app by using native authentication

Feedback

Summarize this article for me

Applies to

:

External tenants (

learn more

)

This guide shows how to run an macOS sample application that demonstrates sign-up and sign in scenarios using Microsoft Entra External ID.

In this article, you learn how to:

Enable public client and native authentication flows.

Update a sample native macOS application to use your own external tenant details.

Run and test the sample native macOS application.

Prerequisites

An Azure account with an active subscription. If you don't already have one,

Create an account for free

This Azure account must have permissions to manage applications. Any of the following Microsoft Entra roles include the required permissions:

Application Administrator

Application Developer

An external tenant. If you don't have one,

create a new external tenant

in the Microsoft Entra admin center.

If you haven't already done so,

Register an application in the Microsoft Entra admin center

. Make sure to:

Record the

Application (client) ID

and

Directory (tenant) ID

for later use.

Grant admin consent

to the application.

If you haven't already done so,

Create a user flow in the Microsoft Entra admin center

Associate your app registration with the user flow

Xcode

Enable public client and native authentication flows

To specify that this app is a public client and can use native authentication, enable public client and native authentication flows:

From the app registrations page, select the app registration for which you want to enable public client and native authentication flows.

Under

Manage

, select

Authentication

.

Under

Advanced settings

, allow public client flows:

For

Enable the following mobile and desktop flows

select

Yes

.

For

Enable native authentication

, select

Yes

.

Select

Save

button.

Clone sample macOS application

Open Terminal and navigate to a directory where you want to keep the code.

Clone the macOS application from GitHub by running the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-native-auth-macos-sample.git

Navigate to the directory where the repo was cloned:

cd ms-identity-ciam-native-auth-macos-sample

Configure the sample macOS application

In Xcode, open

NativeAuthSampleAppMacOS.xcodeproj

project.

Open

NativeAuthSampleAppMacOS/Configuration.swift

file.

Find the placeholder:

Enter_the_Application_Id_Here

and replace it with the

Application (client) ID

of the app you registered earlier.

Enter_the_Tenant_Subdomain_Here

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use contoso. If you don't have your tenant subdomain, learn how to

read your tenant details

.

Note

Remember to select a scheme to build and destination where you run the built products. Each scheme contains a list of real or simulated devices that represent the available destinations.

Run and test sample macOS application

To build and run your code, select

Run

from the

Product

menu in Xcode. After a successful build, Xcode will launch the sample app in the Simulator.

This guide tests

Email and password

usage. Enter a valid email address and password, select

Sign Up

, and launch the submit code screen:

After you enter your email address on the previous screen, the application will send a verification code to it. Once you submit the received code, the application takes you back to the previous screen and automatically signs you in.

Enable sign-in with an alias or username

You can allow users who sign in with an email address and password to also sign in with a username and password. The username also called an alternate sign-in identifier, can be a customer ID, account number, or another identifier that you choose to use as a username.

You can assign usernames to the user account manually via the Microsoft Entra admin center or automate it in your app via the Microsoft Graph API.

Use the steps in

Sign in with an alias or username

article to allow your users to sign-in using a username in your application:

Enable username in sign-in

.

Create users with username in the admin center

or

update existing users to by adding a username

. Alternatively, you can also

automate user creation and updating in your app by using the Microsoft Graph API

.

Next steps

Tutorial: Prepare your iOS/macOS app for native authentication

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

2025-11-21
