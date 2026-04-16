---
title: Quickstart - Sign in users in a sample Desktop app - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-desktop-app-nodejs-electron-sign-in
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:38.401837+00:00
kind: extracted-doc
---

# Quickstart - Sign in users in a sample Desktop app - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-desktop-app-nodejs-electron-sign-in

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:38.401837+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-desktop-app-nodejs-electron-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-nodejs-desktop
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-windows-desktop
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-desktop-app-maui-sign-in-prepare-app
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-desktop-wpf-dotnet-sign-in-build-app

Captured summary:

- Quickstart - Sign in users in a sample Desktop app - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Quickstart: Sign in users in a sample Desktop app Feedback Summarize this article for me Applies to : Workforce tenants External tenants ( learn more ) In this quickstart, you’ll use a sample application to learn how to add authentication to a desktop application.
- The sample application enables users to sign in and sign out and uses the Microsoft Authentication Library (MSAL) to handle authentication.

Extracted text:

Quickstart - Sign in users in a sample Desktop app - Microsoft identity platform | Microsoft Learn

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

Quickstart: Sign in users in a sample Desktop app

Feedback

Summarize this article for me

Applies to

:

Workforce tenants

External tenants (

learn more

)

In this quickstart, you’ll use a sample application to learn how to add authentication to a desktop application. The sample application enables users to sign in and sign out and uses the Microsoft Authentication Library (MSAL) to handle authentication.

Before you begin, use the

Choose a tenant type

selector at the top of this page to select tenant type. Microsoft Entra ID provides two tenant configurations,

workforce

and

external

. A workforce tenant configuration is for your employees, internal apps, and other organizational resources. An external tenant is for your customer-facing apps.

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

Node.js Electron

Windows Presentation Foundation (WPF)

Add the following redirect URIs using the

Mobile and desktop applications

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost

Node.js

Visual Studio Code

or another code editor

Add the following redirect URIs using the

Mobile and desktop applications

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

https://login.microsoftonline.com/common/oauth2/nativeclient

Custom redirect URIs

:

ms-appx-web://microsoft.aad.brokerplugin/{client_id}

where {client_id} is the application (client) ID of your application.

Visual Studio

with the

Universal Windows Platform development

workload installed

Download the sample project

Node.js Electron

Windows Presentation Foundation (WPF)

Note

The Electron sample provided in this tutorial is specifically designed to work with MSAL-node. MSAL-browser is not supported in Electron applications. Ensure you to complete the following steps to set up your project correctly.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-javascript-nodejs-desktop.git

Download the .zip file

. Extract it to a file path where the length of the name is fewer than 260 characters.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/active-directory-dotnet-desktop-msgraph-v2.git

Download the .zip file

Configure the project

Node.js Electron

Windows Presentation Foundation (WPF)

In your code editor, open the

ms-identity-javascript-nodejs-desktop-main/App/authConfig.js

file. Replace the value as follows:

Variable

Description

Example(s)

Enter_the_Cloud_Instance_Id_Here

The Azure cloud instance in which your application is registered

https://login.microsoftonline.com/

(include the trailing forward-slash)

Enter_the_Tenant_Info_Here

Tenant ID or Primary domain

contoso.microsoft.com

or

aaaabbbb-0000-cccc-1111-dddd2222eeee

Enter_the_Application_Id_Here

Client ID of the application you registered

00001111-aaaa-2222-bbbb-3333cccc4444

Enter_the_Graph_Endpoint_Here

The Microsoft Graph API cloud instance that your app will call

https://graph.microsoft.com/

(include the trailing forward-slash)

Your file should look similar to below:

const AAD_ENDPOINT_HOST = "https://login.microsoftonline.com/"; // include the trailing slash const msalConfig = { auth: { clientId: "00001111-aaaa-2222-bbbb-3333cccc4444", authority: `${AAD_ENDPOINT_HOST}/aaaabbbb-0000-cccc-1111-dddd2222eeee`, }, system: { loggerOptions: { loggerCallback(loglevel, message, containsPii) { console.log(message); }, piiLoggingEnabled: false, logLevel: LogLevel.Verbose, } } } const GRAPH_ENDPOINT_HOST = "https://graph.microsoft.com/"; // include the trailing slash const protectedResources = { graphMe: { endpoint: `${GRAPH_ENDPOINT_HOST}v1.0/me`, scopes: ["User.Read"], } }; module.exports = { msalConfig: msalConfig, protectedResources: protectedResources, };

Extract the zip file to a local folder close to the root of the disk, for example,

C:\Azure-Samples

.

Open the project in Visual Studio.

Edit

active-directory-wpf-msgraph-v2/App.xaml.cs

and replace the values of the fields

ClientId

and

Tenant

with the following code:

private static string ClientId = "Enter_the_Application_Id_here"; private static string Tenant = "Enter_the_Tenant_Info_Here";

Where:

Enter_the_Application_Id_here

- is the

Application (client) ID

for the application you registered.

To find the value of

Application (client) ID

, go to the app's

Overview

page in the Microsoft Entra admin center.

Enter_the_Tenant_Info_Here

- is set to one of the following options:

If your application supports

Accounts in this organizational directory

, replace this value with the

Tenant Id

or

Tenant name

(for example, contoso.microsoft.com)

If your application supports

Accounts in any organizational directory

, replace this value with

organizations

If your application supports

Accounts in any organizational directory and personal Microsoft accounts

, replace this value with

common

.

To find the values of

Directory (tenant) ID

and

Supported account types

, go to the app's

Overview

page in the Microsoft Entra admin center.

Run the application

Node.js Electron

Windows Presentation Foundation (WPF)

You'll need to install the dependencies of this sample once:

cd ms-identity-javascript-nodejs-desktop-main npm install

Then, run the application via command prompt or console:

npm start

Select

Sign in

to start the sign-in process.

The first time you sign in, you're prompted to provide your consent to allow the application to sign you in and access your profile. After you're signed in successfully, you'll be redirected back to the application.

To build and run the sample application in Visual Studio, follow these steps:

Select the

Debug menu

>

Start Debugging

, or press the F5 key. Your application's

MainWindow

is displayed.

Select the

Call Microsoft Graph API

button.

Sign in using your Microsoft Entra account (work or school account) or Microsoft account (live.com, outlook.com) credentials.

If you're running the application for the first time, you'll be prompted to provide consent to allow the application to access your user profile and sign you in. After consenting to the requested permissions, the application displays that you've successfully logged in.

You should see some basic token information and user data obtained from the call to the Microsoft Graph API.

Next step

Node.js Electron

Windows Presentation Foundation (WPF)

To learn more about Electron desktop app development with MSAL Node, see the tutorial:

Tutorial: Sign in users and call the Microsoft Graph API in an Electron desktop app

Try out the Windows desktop tutorial for a complete step-by-step guide on building applications and new features, including a full explanation of this quickstart.

Call Graph API tutorial

Prerequisites

An Azure account with an active subscription. If you don't already have one,

Create an account for free

.

This Azure account must have permissions to manage applications. Any of the following Microsoft Entra roles include the required permissions:

Application Administrator

Application Developer

Cloud Application Administrator

An external tenant. To create one, choose from the following methods:

(Recommended) Use the

Microsoft Entra External ID extension

to set up an external tenant directly in Visual Studio Code

Create a new external tenant

in the Microsoft Entra admin center

A user flow. For more information, refer to

create self-service sign-up user flows for apps in external tenants

. This user flow can be used for multiple applications.

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

Add your application to the user flow

Node.js Electron

.NET (MAUI)

.NET (MAUI) WPF

Add the following redirect URIs using the

Mobile and desktop applications

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost

Node.js

Visual Studio Code

or another code editor*

Add the following redirect URIs using the

Mobile and desktop applications

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

msal{client_id}://auth

where {client_id} is the application (client) ID of your application.

.NET 7.0 SDK

or later

Visual Studio 2022

with the MAUI workload installed:

Instructions for Windows

Instructions for macOS

Add your application to the user flow

Add the following redirect URIs using the

Mobile and desktop applications

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Custom redirect URI

:

https://login.microsoftonline.com/common/oauth2/nativeclient

. This needs to be entered manually.

Visual Studio Code

or another code editor

.NET 7.0

or later

Add your application to the user flow

Download the sample project

Node.js Electron

.NET (MAUI)

.NET (MAUI) WPF

Note

The Electron sample provided in this tutorial is specifically designed to work with MSAL-node. MSAL-browser is not supported in Electron applications. Ensure you complete the following steps to set up your project correctly.

To get the desktop app sample code,

download the .zip file

or clone the sample web application from GitHub by running the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-javascript-tutorial.git

If you choose to download the

.zip

file, extract the sample app file to a folder where the total length of the path is 260 or fewer characters.

Install project dependencies

Open a console window, and change to the directory that contains the Electron sample app:

cd 1-Authentication\3-sign-in-electron\App

Run the following commands to install app dependencies:

npm install && npm update

To get the .NET MAUI desktop application sample code,

download the .zip file

or clone the sample .NET MAUI desktop application from GitHub by running the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-dotnet-tutorial.git

To obtain the sample application, you can either clone it from GitHub or download it as a .zip file.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-dotnet-tutorial.git

Download the .zip file

. Extract it to a file path where the length of the name is fewer than 260 characters.

Configure the sample web app

Node.js Electron

.NET (MAUI)

.NET (MAUI) WPF

In your code editor, open

App\authConfig.js

file.

Find the placeholder:

Enter_the_Application_Id_Here

and replace it with the Application (client) ID of the app you registered earlier.

Enter_the_Tenant_Subdomain_Here

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't have your tenant name, learn how to

read your tenant details

.

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

and replace it with the Application (client) ID of the app you registered earlier.

Open the project in your IDE (like Visual Studio or Visual Studio Code) to configure the code.

In your code editor, open the

appsettings.json

file in the

ms-identity-ciam-dotnet-tutorial

>

1-Authentication

>

5-sign-in-dotnet-wpf

folder.

Replace

Enter_the_Application_Id_Here

with the Application (client) ID of the app you registered earlier.

Replace

Enter_the_Tenant_Subdomain_Here

with the Directory (tenant) subdomain. For example, if your primary domain is

contoso.onmicrosoft.com

, replace

Enter_the_Tenant_Subdomain_Here

with

contoso

. If you don't have your primary domain, learn how to

read tenant details

.

Run and test the sample web app

Node.js Electron

.NET (MAUI)

.NET (MAUI) WPF

You can now test the sample Electron desktop app. After you run the app, the desktop app window appears automatically:

In your terminal, run the following command:

npm start

On the desktop window that appears, select the

Sign In

or

Sign up

button. A browser window opens, and you're prompted to sign in.

On the browser sign-in page, type your

Email address

, select

Next

, type your

Password

, then select

Sign in

. If you don't have an account, select

No account? Create one

link, which starts the sign-up flow.

If you choose the sign-up option, after filling in your email, one-time passcode, new password and more account details, you complete the whole sign-up flow. You see a page similar to the following screenshot. You see a similar page if you choose the sign-in option. The page displays token ID claims.

.NET MAUI apps are designed to run on multiple operating systems and devices. You'll need to select which target you want to test and debug your app with.

Set the

Debug Target

in the Visual Studio toolbar to the device you want to debug and test with. The following steps demonstrate setting the

Debug Target

to

Windows

:

Select

Debug Target

drop-down.

Select

Framework

Select

net7.0-windows...

Run the app by pressing

F5

or select the

play button

at the top of Visual Studio.

You can now test the sample .NET MAUI desktop application. After you run the application, the desktop application window appears automatically:

On the desktop window that appears, select the

Sign In

button. A browser window opens, and you're prompted to sign in.

During the sign in process, you're prompted to grant various permissions (to allow the application to access your data). Upon successful sign in and consent, the application screen displays the main page.

Open a console window, and change to the directory that contains the WPF desktop sample app:

cd 1-Authentication\5-sign-in-dotnet-wpf

In your terminal, run the app by running the following command:

dotnet run

After you launch the sample, you should see a window with a

Sign-In

button. Select the

Sign-In

button.

On the sign-in page, enter your account email address. If you don't have an account, select

No account? Create one

, which starts the sign-up flow. Follow through this flow to create a new account and sign in.

Once you sign in, you'll see a screen displaying successful sign-in and basic information about your user account stored in the retrieved token. The basic information is displayed in the

Token Info

section of the sign-in screen

Related content

Node.js Electron

.NET (MAUI)

.NET (MAUI) WPF

Enable password reset

.

Customize the default branding

.

Explore the Electron desktop app sample code

.

Tutorial: Create a .NET MAUI app

.

Enable password reset

.

Customize the default branding

.

Tutorial: Authenticate users to your WPF desktop application

Enable password reset

.

Customize the default branding

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
