---
title: Sign in users in a React single-page app (SPA) by using native authentication - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-single-page-app-react-sign-in
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:46.398853+00:00
kind: extracted-doc
---

# Sign in users in a React single-page app (SPA) by using native authentication - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-single-page-app-react-sign-in

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:46.398853+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-single-page-app-react-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/reference-native-authentication-api
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-native-authentication-cors-solution-test-environment
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-native-authentication-cors-solution-production-environment
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-single-page-app-react-sign-up

Captured summary:

- Sign in users in a React single-page app (SPA) by using native authentication - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Quickstart: Sign in users in a React single-page app by using native authentication Feedback Summarize this article for me Applies to : External tenants ( learn more ) In this quickstart, you use a React single-page application (SPA) to demonstrate how to authenticate users by using native authentication API .
- The sample app demonstrates user sign-up, sign-in, sign-out, and password reset with an email and a password.

Extracted text:

Sign in users in a React single-page app (SPA) by using native authentication - Microsoft identity platform | Microsoft Learn

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

Quickstart: Sign in users in a React single-page app by using native authentication

Feedback

Summarize this article for me

Applies to

:

External tenants (

learn more

)

In this quickstart, you use a React single-page application (SPA) to demonstrate how to authenticate users by using

native authentication API

. The sample app demonstrates user sign-up, sign-in, sign-out, and password reset with an email and a password.

Prerequisites

An Azure account with an active subscription. If you don't already have one,

Create an account for free

.

This Azure account must have permissions to manage applications. Any of the following Microsoft Entra roles include the required permissions:

Application Administrator

Application Developer

An external tenant. If you don't have one,

create a new external tenant

in the Microsoft Entra admin center.

A user flow. For more information, see

create self-service sign-up user flows for apps in external tenants

. Ensure that the user flow includes the following user attributes:

Given Name

Surname

If you haven't already done so,

Register an application in the Microsoft Entra admin center

. Make sure to:

Record the

Application (client) ID

and

Directory (tenant) ID

for later use.

Grant admin consent

to the app registration.

Associate your app registration with the user flow

Node.js

.

Visual Studio Code

or another code editor.

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

Clone or download sample SPA

To obtain the sample application, you can either clone it from GitHub or download it as a .zip file.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples.git

Alternatively,

Download the sample

, then extract it to a file path where the length of the name is fewer than 260 characters.

Install project dependencies

Open a terminal window and navigate to the directory that contains the React sample app:

cd API\React\ReactAuthSimple

Run the following command to install app dependencies:

npm install

Configure the sample React app

In your code editor, open

src\config.ts

file.

Find the placeholder

Enter_the_Application_Id_Here

then replace it with the Application (client) ID of the app you registered earlier.

Save the changes.

Configure CORS proxy server

The native authentication APIs don't support

Cross-Origin Resource Sharing (CORS)

so you must set up a proxy server between your SPA app and the APIs.

This code sample includes a CORS proxy server that forwards requests to native authentication API URL endpoints. The CORS proxy server is a Node.js server that listens on port 3001.

To configure the proxy server, open the

proxy.config.js

file, then the find the placeholder:

tenantSubdomain

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't have your tenant subdomain, learn how to

read your tenant details

.

tenantId

and replace it with the Directory (tenant) ID. If you don't have your tenant ID, learn how to

read your tenant details

.

Run and test your app

You've now configured the sample app and it's ready to run.

From your terminal window, run the following commands to start the CORS proxy server:

cd API\React\ReactAuthSimple npm run cors

To start your React app, open another terminal window, then run the following commands:

cd API\React\ReactAuthSimple npm start

Open a web browser and go to

http://localhost:3000/

.

To sign up for an account, select

Sign Up

, then follow the prompts.

After you sign up, test sign-in and password reset by selecting

Sign In

and

Reset Password

respectively.

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

Related content

Set up a reverse proxy for a single-page app that uses native authentication API by using Azure Function App

.

Use Azure Front Door as a reverse proxy in production environment for a single-page app that uses native authentication

.

Build a React single-page app that uses native authentication API from scratch

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
