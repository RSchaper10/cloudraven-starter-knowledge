---
title: Quickstart - Sign in users in a sample mobile app - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-mobile-app-android-sign-in
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:39.022179+00:00
kind: extracted-doc
---

# Quickstart - Sign in users in a sample mobile app - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-mobile-app-android-sign-in

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:39.022179+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-mobile-app-android-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/single-multi-account
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-configuration
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-android
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-ios

Captured summary:

- Quickstart - Sign in users in a sample mobile app - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Quickstart: Sign in users in a sample mobile app Feedback Summarize this article for me Applies to : Workforce tenants External tenants ( learn more ) Before you begin, use the Choose a tenant type selector at the top of this page to select tenant type.
- Microsoft Entra ID provides two tenant configurations, workforce and external .

Extracted text:

Quickstart - Sign in users in a sample mobile app - Microsoft identity platform | Microsoft Learn

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

Quickstart: Sign in users in a sample mobile app

Feedback

Summarize this article for me

Applies to

:

Workforce tenants

External tenants (

learn more

)

Before you begin, use the

Choose a tenant type

selector at the top of this page to select tenant type. Microsoft Entra ID provides two tenant configurations,

workforce

and

external

. A workforce tenant configuration is for your employees, internal apps, and other organizational resources. An external tenant is for your customer-facing apps.

Android

iOS/macOS

In this quickstart, you download and run a code sample that demonstrates how an Android application can sign in users and get an access token to call the Microsoft Graph API.

Applications must be represented by an app object in Microsoft Entra ID so that the Microsoft identity platform can provide tokens to your application.

In this quickstart, you download and run a code sample that demonstrates how a native iOS or macOS application can sign in users and get an access token to call the Microsoft Graph API.

The quickstart applies to both iOS and macOS apps. Some steps are needed only for iOS apps and will be indicated as such.

Prerequisites

An Azure account with an active subscription. If you don't already have one,

Create an account for free

.

This Azure account must have permissions to manage applications. Any of the following Microsoft Entra roles include the required permissions:

Application Administrator

Application Developer

A workforce tenant. You can use your Default Directory or

set up a new tenant

.

Android

iOS/macOS

Register a new app in the

Microsoft Entra admin center

, configured for

Accounts in any organizational directory and personal Microsoft accounts

. Refer to

Register an application

for more details. Record the following values from the application

Overview

page for later use:

Application (client) ID

Directory (tenant) ID

Android Studio

Android 16+

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

XCode 10+

iOS 10+

macOS 10.12+

Add a redirect URI

You must configure specific redirect URIs in your app registration to ensure compatibility with the downloaded code sample. These URIs are essential for redirecting users back to the app after they successfully sign in.

Android

iOS/macOS

Under

Manage

, select

Authentication

>

Add a platform

>

Android

.

Enter your project's Package Name based on the sample type you downloaded above.

Java sample -

com.azuresamples.msalandroidapp

Kotlin sample -

com.azuresamples.msalandroidkotlinapp

In the

Signature hash

section of the

Configure your Android app

pane, select

Generating a development Signature Hash.

and copy the KeyTool command to your command line.

KeyTool.exe is installed as part of the Java Development Kit (JDK). You must also install the OpenSSL tool to execute the KeyTool command. For more information, see

Android documentation on generating a key

for more information.

Enter the

Signature hash

generated by KeyTool.

Select

Configure

and save the

MSAL Configuration

that appears in the

Android configuration

pane so you can enter it when you configure your app later.

Select

Done

.

Under

Manage

, select

Authentication

>

Add Platform

>

iOS

.

Enter the

Bundle Identifier

for your application. The bundle identifier is a unique string that uniquely identifies your application, for example

com.<yourname>.identitysample.MSALMacOS

. Make a note of the value you use. Note that the iOS configuration is also applicable to macOS applications.

Select

Configure

and save the

MSAL Configuration

details for later in this quickstart.

Select

Done

.

Download the sample app

Android

iOS/macOS

Java:

Download the code

.

Kotlin:

Download the code

.

Download the sample project

Download the code sample for iOS

Download the code sample for macOS

Install dependencies

Extract the zip file.

In a terminal window, navigate to the folder with the downloaded code sample and run

pod install

to install the latest MSAL library.

Configure the sample application

Android

iOS/macOS

In Android Studio's project pane, navigate to

app\src\main\res

.

Right-click

res

and choose

New

>

Directory

. Enter

raw

as the new directory name and select

OK

.

In

app

>

src

>

main

>

res

>

raw

, go to JSON file called

auth_config_single_account.json

and paste the MSAL Configuration that you saved earlier.

Below the redirect URI, paste:

"account_mode" : "SINGLE",

Your config file should resemble this example:

{ "client_id": "00001111-aaaa-bbbb-3333-cccc4444", "authorization_user_agent": "WEBVIEW", "redirect_uri": "msauth://com.azuresamples.msalandroidapp/00001111%cccc4444%3D", "broker_redirect_uri_registered": false, "account_mode": "SINGLE", "authorities": [ { "type": "AAD", "audience": { "type": "AzureADandPersonalMicrosoftAccount", "tenant_id": "common" } } ] }

Open

/app/src/main/AndroidManifest.xml

file.

Find the placeholder:

enter_the_signature_hash

and replace it with the

Signature Hash

that you generated earlier when you added the platform redirect URL.

As this tutorial only demonstrates how to configure an app in Single Account mode, see

single vs. multiple account mode

and

configuring your app

for more information

Run the sample app

Select your emulator, or physical device, from Android Studio's

available devices

dropdown and run the app.

The sample app starts on the

Single Account Mode

screen. A default scope,

user.read

, is provided by default, which is used when reading your own profile data during the Microsoft Graph API call. The URL for the Microsoft Graph API call is provided by default. You can change both of these if you wish.

Use the app menu to change between single and multiple account modes.

In single account mode, sign in using a work or home account:

Select

Get graph data interactively

to prompt the user for their credentials. You'll see the output from the call to the Microsoft Graph API in the bottom of the screen.

Once signed in, select

Get graph data silently

to make a call to the Microsoft Graph API without prompting the user for credentials again. You'll see the output from the call to the Microsoft Graph API in the bottom of the screen.

In multiple account mode, you can repeat the same steps. Additionally, you can remove the signed-in account, which also removes the cached tokens for that account.

If you selected Option 1 above, you can skip these steps.

Open the project in XCode.

Edit

ViewController.swift

and replace the line starting with 'let kClientID' with the following code snippet. Remember to update the value for

kClientID

with the clientID that you saved when you registered your app earlier in this quickstart:

let kClientID = "Enter_the_Application_Id_Here"

If you're building an app for

Microsoft Entra national clouds

, replace the line starting with 'let kGraphEndpoint' and 'let kAuthority' with correct endpoints. For global access, use default values:

let kGraphEndpoint = "https://graph.microsoft.com/" let kAuthority = "https://login.microsoftonline.com/common"

Other endpoints are documented

here

. For example, to run the quickstart with Microsoft Entra Germany, use following:

let kGraphEndpoint = "https://graph.microsoft.de/" let kAuthority = "https://login.microsoftonline.de/common"

Open the project settings. In the

Identity

section, enter the

Bundle Identifier

.

Right-click

Info.plist

and select

Open As

>

Source Code

.

Under the dict root node, replace

Enter_the_bundle_Id_Here

with the

Bundle Id

that you used in the portal. Notice the

msauth.

prefix in the string.

<key>CFBundleURLTypes</key> <array> <dict> <key>CFBundleURLSchemes</key> <array> <string>msauth.Enter_the_Bundle_Id_Here</string> </array> </dict> </array>

Build and run the app!

How the sample works

Android

iOS/macOS

The code is organized into fragments that show how to write a single and multiple accounts MSAL app. The code files are organized as follows:

File

Demonstrates

MainActivity

Manages the UI

MSGraphRequestWrapper

Calls the Microsoft Graph API using the token provided by MSAL

MultipleAccountModeFragment

Initializes a multi-account application, loads a user account, and gets a token to call the Microsoft Graph API

SingleAccountModeFragment

Initializes a single-account application, loads a user account, and gets a token to call the Microsoft Graph API

res/auth_config_multiple_account.json

The multiple account configuration file

res/auth_config_single_account.json

The single account configuration file

Gradle Scripts/build.grade (Module:app)

The MSAL library dependencies are added here

We'll now look at these files in more detail and call out the MSAL-specific code in each.

Next steps

Android

iOS/macOS

Move on to the Android tutorial in which you build an Android app that gets an access token from the Microsoft identity platform and uses it to call the Microsoft Graph API.

Tutorial: Sign in users and call the Microsoft Graph from an Android application

Move on to the step-by-step tutorial in which you build an iOS or macOS app that gets an access token from the Microsoft identity platform and uses it to call the Microsoft Graph API.

Tutorial: Sign in users and call Microsoft Graph from an iOS or macOS app

The quickstart guides you in configuring sample Android, .NET MAUI Android, and iOS/macOS apps to sign in users by registering applications, setting up redirect URLs, updating configurations, and testing the app.

Prerequisites

An Azure account with an active subscription. If you don't already have one,

Create an account for free

.

This Azure account must have permissions to manage applications. Any of the following Microsoft Entra roles include the required permissions:

Application Administrator

Application Developer

An external tenant. To create one, choose from the following methods:

Use the

Microsoft Entra External ID extension

to set up an external tenant directly in Visual Studio Code.

(Recommended)

Create a new external tenant

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

Android

Android(.NET MAUI)

iOS/macOS

Android Studio

.

A user flow. For more information, refer to

create self-service sign-up user flows for apps in external tenants

. This user flow can be used for multiple applications.

Add your application to the user flow

.

.NET 7.0 SDK

Visual Studio 2022

with the MAUI workload installed:

Instructions for Windows

Instructions for macOS

Xcode

.

Add a platform redirect URL

You must configure specific redirect URIs in your app registration to ensure compatibility with the downloaded code sample. These URIs are essential for redirecting users back to the app after they successfully sign in.

Android

Android(.NET MAUI)

iOS/macOS

To specify your app type to your app registration, follow these steps:

Under

Manage

, select

Authentication

.

On the

Platform configurations

page, select

Add a platform

, and then select

Android

option.

Enter your project's Package Name. If you downloaded the

sample code

, this value is

com.azuresamples.msaldelegatedandroidkotlinsampleapp

.

In the

Signature hash

section of the

Configure your Android app

pane, select

Generating a development Signature Hash. This will change for each development environment.

Copy and run the KeyTool command for your operating system in your Terminal.

Enter the

Signature hash

generated by KeyTool.

Select

Configure

.

Copy the

MSAL Configuration

from the

Android configuration

pane and save it for later app configuration.

Select

Done

.

Enable public client flow

To identify your app as a public client, follow these steps:

Under

Manage

, select

Authentication

.

Under

Advanced settings

, for

Allow public client flows

, select

Yes

.

Select

Save

to save your changes.

To specify your app type to your app registration, follow these steps:

Under

Manage

, select

Authentication

.

On the

Platform configurations

page, select

Add a platform

, and then select

Mobile and Desktop applications

option.

For the

Redirect URIs

enter

msal{client_id}://auth

. Ensure that the

{client_id}

matches the value of your app registration. Select

Configure

.

Select

Save

to save the changes.

To specify your app type to your app registration, follow these steps:

Under

Manage

, select

Authentication

.

On the

Platform configurations

page, select

Add a platform

, and then select

iOS / macOS

option.

Enter your project's Bundle ID. If you downloaded the

sample code

, this value is

com.microsoft.identitysample.ciam.MSALiOS

.

Select

Configure

and save the

MSAL Configuration

that appears in the

iOS / macOS configuration

pane so you can enter it when you configure your app later.

Select

Done

.

Enable public client flow

To identify your app as a public client, follow these steps:

Under

Manage

, select

Authentication

.

Under

Advanced settings

, for

Allow public client flows

, select

Yes

.

Select

Save

to save your changes.

Clone sample application

Android

Android(.NET MAUI)

iOS/macOS

To obtain the sample application, you can either clone it from GitHub or

download it as a .zip file

.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-browser-delegated-android-sample

To get the .NET MAUI Android application sample code,

download the .zip file

or clone the sample .NET MAUI Android application from GitHub by running the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-dotnet-tutorial.git

To obtain the sample application, you can either clone it from GitHub or download it as a .zip file.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-browser-delegated-ios-sample.git

Configure the sample application

Android

Android(.NET MAUI)

iOS/macOS

To enable authentication and access to Microsoft Graph resources, configure the sample by following these steps:

In Android Studio, open the project that you cloned.

Open

/app/src/main/res/raw/auth_config_ciam.json

file.

Find the placeholder:

Enter_the_Application_Id_Here

and replace it with the

Application (client) ID

of the app you registered earlier.

Enter_the_Redirect_Uri_Here

and replace it with the value of

redirect_uri

in the Microsoft Authentication Library (MSAL) configuration file you downloaded earlier when you added the platform redirect URL.

Enter_the_Tenant_Subdomain_Here

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't know your tenant subdomain, learn how to

read your tenant details

.

Open

/app/src/main/AndroidManifest.xml

file.

Find the placeholder:

ENTER_YOUR_SIGNATURE_HASH_HERE

and replace it with the

Signature Hash

that you generated earlier when you added the platform redirect URL.

Open

/app/src/main/java/com/azuresamples/msaldelegatedandroidkotlinsampleapp/MainActivity.kt

file.

Find property named

scopes

and set the scopes recorded in

Grant admin consent

. If you haven't recorded any scopes, you can leave this scope list empty.

private const val scopes = "" // Developers should set the respective scopes of their Microsoft Graph resources here. For example, private const val scopes = "api://{clientId}/{ToDoList.Read} api://{clientId}/{ToDoList.ReadWrite}"

You've configured the app and it's ready to run.

In Visual Studio, open

ms-identity-ciam-dotnet-tutorial-main/1-Authentication/2-sign-in-maui/appsettings.json

file.

Find the placeholder:

Enter_the_Tenant_Subdomain_Here

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't have your tenant name, learn how to

read your tenant details

.

Enter_the_Application_Id_Here

and replace it with the

Application (client) ID

of the app you registered earlier.

In Visual Studio, open

ms-identity-ciam-dotnet-tutorial-main/1-Authentication/2-sign-in-maui/Platforms/Android/AndroidManifest.xml

file.

Find the placeholder:

Enter_the_Application_Id_Here

and replace it with the

Application (client) ID

of the app you registered earlier.

To enable authentication and access to Microsoft Graph resources, configure the sample by following these steps:

In Xcode, open the project that you cloned.

Open

/MSALiOS/Configuration.swift

file.

Find the placeholder:

Enter_the_Application_Id_Here

and replace it with the

Application (client) ID

of the app you registered earlier.

Enter_the_Redirect_URI_Here

and replace it with the value of

kRedirectUri

in the Microsoft Authentication Library (MSAL) configuration file you downloaded earlier when you added the platform redirect URL.

Enter_the_Protected_API_Scopes_Here

and replace it with the scopes recorded in

Grant admin consent

. If you haven't recorded any scopes, you can leave this scope list empty.

Enter_the_Tenant_Subdomain_Here

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't know your tenant subdomain, learn how to

read your tenant details

.

You've configured the app and it's ready to run.

Run and test the sample app

Android

Android(.NET MAUI)

iOS/macOS

To build and run your app, follow these steps:

In the toolbar, select your app from the run configurations menu.

In the target device menu, select the device that you want to run your app on.

If you don't have any devices configured, you need to either create an Android Virtual Device to use the Android Emulator or connect a physical Android device.

Select the

Run

button.

Select

Acquire Token Interactively

to request an access token.

If you select

API - Perform GET

to call a protected ASP.NET Core web API, you will get an error.

For more information about calling a protected web API, see our

next steps

.NET MAUI apps are designed to run on multiple operating systems and devices. You'll need to select which target you want to test and debug your app with.

Set the

Debug Target

in the Visual Studio toolbar to the device you want to debug and test with. The following steps demonstrate setting the

Debug Target

to

Android

:

Select

Debug Target

drop-down.

Select

Android Emulators

.

Select emulator device.

Run the app by pressing

F5

or select the

play button

at the top of Visual Studio.

You can now test the sample .NET MAUI Android app. After you run the app, the Android app window appears in an emulator:

On the Android window that appears, select the

Sign In

button. A browser window opens, and you're prompted to sign in.

During the sign in process, you're prompted to grant various permissions (to allow the application to access your data). Upon successful sign in and consent, the application screen displays the main page.

To build and run your app, follow these steps:

To build and run your code, select

Run

from the

Product

menu in Xcode. After a successful build, Xcode will launch the sample app in the Simulator.

Select

Acquire Token Interactively

to request an access token.

If you select

API - Perform GET

to call a protected ASP.NET Core web API, you will get an error.

For more information about calling a protected web API, see our

Next steps

Next steps

Android

Android(.NET MAUI)

iOS/macOS

Sign in users and call a protected web API in sample Android (Kotlin) app

.

Customize the default branding

.

Configure sign-in with Google

.

Sign in users and call a protected web API in sample iOS (Swift) app

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

2025-04-08
