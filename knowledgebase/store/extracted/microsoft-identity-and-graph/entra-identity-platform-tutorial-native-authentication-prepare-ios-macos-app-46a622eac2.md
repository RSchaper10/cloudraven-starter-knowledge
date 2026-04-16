---
title: Prepare your iOS/macOS app for native authentication - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-prepare-ios-macos-app
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:51.559322+00:00
kind: extracted-doc
---

# Prepare your iOS/macOS app for native authentication - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-prepare-ios-macos-app

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:51.559322+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-prepare-ios-macos-app
- https://learn.microsoft.com/en-us/entra/identity-platform/concept-native-authentication-challenge-types
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-ios-macos-sign-up

Captured summary:

- Prepare your iOS/macOS app for native authentication - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Tutorial: Prepare your iOS/macOS app for native authentication Feedback Summarize this article for me Applies to : External tenants ( learn more ) This tutorial demonstrates how to add Microsoft Authentication Library (MSAL) native authentication SDK framework to your iOS/macOS Swift app.
- In this tutorial, you: Add the MSAL framework to an iOS/macOS app.

Extracted text:

Prepare your iOS/macOS app for native authentication - Microsoft identity platform | Microsoft Learn

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

Tutorial: Prepare your iOS/macOS app for native authentication

Feedback

Summarize this article for me

Applies to

:

External tenants (

learn more

)

This tutorial demonstrates how to add Microsoft Authentication Library (MSAL) native authentication SDK framework to your iOS/macOS Swift app.

In this tutorial, you:

Add the MSAL framework to an iOS/macOS app.

Create SDK instance.

Prerequisites

Xcode

If you haven't already, follow the instructions in

Sign in users in sample iOS (Swift) mobile app by using native authentication

and register an app in your external tenant. Make sure you complete the following steps:

Register an application.

Enable public client and native authentication flows.

Grant API permissions.

Create a user flow.

Associate the app with the user flow.

iOS/macOS project

Add the MSAL framework to an iOS/macOS app

Open your iOS/macOS project in Xcode.

Select

Add Package Dependencies...

from the

File

menu.

Enter

https://github.com/AzureAD/microsoft-authentication-library-for-objc

as the Package URL and choose

Add Package

.

Add a new keychain group to your project

Capabilities

. Use

com.microsoft.adalcache

on iOS and

com.microsoft.identity.universalstorage

on macOS.

For more information and other mechanisms to add MSAL to your project, see the

project Readme file

.

Create SDK instance

Import the MSAL library into your view controller by adding

import MSAL

at the top of your

ViewController

class.

Add a

nativeAuth

member variable to your

ViewController

class by adding the following code just before the

viewDidLoad()

function:

var nativeAuth: MSALNativeAuthPublicClientApplication!

Next, add the following code to the

viewDidLoad()

function:

do { nativeAuth = try MSALNativeAuthPublicClientApplication( clientId: "Enter_the_Application_Id_Here", tenantSubdomain: "Enter_the_Tenant_Subdomain_Here", challengeTypes: [.OOB] ) print("Initialized Native Auth successfully.") } catch { print("Unable to initialize MSAL \(error)") }

Replace the following values with the values from the Microsoft Entra admin center:

Find the

Enter_the_Application_Id_Here

value and replace it with the

Application (client) ID

of the app you registered earlier.

Find the

Enter_the_Tenant_Subdomain_Here

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't have your Directory (tenant) subdomain, learn how to

read your tenant details

.

The challenge types are a list of values, which the app uses to notify Microsoft Entra about the authentication method that it supports.

For sign-up and sign-in flows with email one-time passcode, use

[.OOB]

.

For sign-up and sign-in flows with email and password, use

[.OOB, .password]

.

For self-service password reset (SSPR), use

[.OOB]

.

Learn more

challenge types

.

To build, select the

Product

>

Build

in your project’s toolbar.

Optional: Logging configuration

MSAL provides a logging API that you can use to enable and configure logging. To see all debug output from MSAL add the following code at the start of the

viewDidLoad()

function:

MSALGlobalConfig.loggerConfig.logLevel = .verbose MSALGlobalConfig.loggerConfig.setLogCallback { logLevel, message, containsPII in if !containsPII { print("MSAL: \(message ?? "")") } }

This outputs all debug logs from MSAL, which can be helpful in diagnosing issues and learning how the native authentication flows work. To learn more about configuring log levels and best practices see

Logging in MSAL for iOS/macOS

.

Next step

Tutorial: Add sign-up in an iOS/macOS app using native authentication

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

2025-03-04
