---
title: Quickstart - Sign in users in a single-page app (SPA) and call the Microsoft Graph API - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-single-page-app-sign-in
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:37.207204+00:00
kind: extracted-doc
---

# Quickstart - Sign in users in a single-page app (SPA) and call the Microsoft Graph API - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-single-page-app-sign-in

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:37.207204+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-single-page-app-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-overview
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri
- https://learn.microsoft.com/en-us/entra/identity-platform/media/quickstarts/js-spa/quickstart-js-spa-sign-in.png
- https://learn.microsoft.com/en-us/entra/identity-platform/media/common-spa/react-spa/display-api-call-results-react-spa.png
- https://learn.microsoft.com/en-us/entra/identity-platform/media/quickstarts/angular-spa/quickstart-angular-spa-sign-in.png
- https://learn.microsoft.com/en-us/entra/identity-platform/media/common-spa/blazor-spa/display-api-call-results-blazor-spa.png
- https://learn.microsoft.com/en-us/entra/identity-platform/media/common-spa/angular-spa/customer-display-api-call-results-angular-spa.png
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-api-aspnet-core-protect-api
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-single-page-app-react-prepare-app

Captured summary:

- Quickstart - Sign in users in a single-page app (SPA) and call the Microsoft Graph API - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Quickstart: Sign in users in a single-page app (SPA) and call the Microsoft Graph API Feedback Summarize this article for me Applies to : Workforce tenants External tenants ( learn more ) In this quickstart, you use a sample single-page app (SPA) to show you how to sign in users by using the authorization code flow with Proof Key for Code Exchange (PKCE) and call the Microsoft Graph API.
- The sample uses the Microsoft Authentication Library to handle authentication.

Extracted text:

Quickstart - Sign in users in a single-page app (SPA) and call the Microsoft Graph API - Microsoft identity platform | Microsoft Learn

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

Quickstart: Sign in users in a single-page app (SPA) and call the Microsoft Graph API

Feedback

Summarize this article for me

Applies to

:

Workforce tenants

External tenants (

learn more

)

In this quickstart, you use a sample single-page app (SPA) to show you how to sign in users by using the

authorization code flow

with Proof Key for Code Exchange (PKCE) and call the Microsoft Graph API. The sample uses the

Microsoft Authentication Library

to handle authentication.

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

Visual Studio Code

or another code editor.

JavaScript

React

Angular

Blazor

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

Single-page application

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost:3000/

Node.js

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

Single-page application

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost:3000/

Node.js

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

Add the following redirect URI using the

Single-page application

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost:4200/

Node.js

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

Single-page application

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost:5000/authentication/login-callback.

.NET SDK

Clone or download the sample application

To obtain the sample application, you can either clone it from GitHub or download it as a .zip file.

JavaScript

React

Angular

Blazor

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-docs-code-javascript.git

Download the .zip file

. Extract it to a file path where the length of the name is fewer than 260 characters.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-docs-code-javascript.git

Download the .zip file

. Extract it to a file path where the length of the name is fewer than 260 characters.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-docs-code-javascript.git

Download the .zip file

. Extract it to a file path where the length of the name is fewer than 260 characters.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-docs-code-dotnet.git

Download the .zip file

. Extract it to a file path where the length of the name is fewer than 260 characters.

Configure the project

JavaScript

React

Angular

Blazor

In your IDE, open the project folder,

ms-identity-docs-code-javascript

, containing the sample.

Open

vanillajs-spa/App/public/authConfig.js

and update the following values with the information recorded in the admin center.

/** * Configuration object to be passed to MSAL instance on creation. * For a full list of MSAL.js configuration parameters, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/configuration.md */ const msalConfig = { auth: { clientId: "Enter_the_Application_Id_Here", // WORKFORCE TENANT authority: "https://login.microsoftonline.com/Enter_the_Tenant_Info_Here", // Replace the placeholder with your tenant info // EXTERNAL TENANT // authority: "https://Enter_the_Tenant_Subdomain_Here.ciamlogin.com/", // Replace the placeholder with your tenant subdomain redirectUri: '/', // You must register this URI on App Registration. Defaults to window.location.href e.g. http://localhost:3000/ navigateToLoginRequestUrl: true, // If "true", will navigate back to the original request location before processing the auth code response. }, cache: { cacheLocation: 'sessionStorage', // Configures cache location. "sessionStorage" is more secure, but "localStorage" gives you SSO. storeAuthStateInCookie: false, // set this to true if you have to support IE }, system: { loggerOptions: { loggerCallback: (level, message, containsPii) => { if (containsPii) { return; } switch (level) { case msal.LogLevel.Error: console.error(message); return; case msal.LogLevel.Info: console.info(message); return; case msal.LogLevel.Verbose: console.debug(message); return; case msal.LogLevel.Warning: console.warn(message); return; } }, }, }, }; /** * Scopes you add here will be prompted for user consent during sign-in. * By default, MSAL.js will add OIDC scopes (openid, profile, email) to any login request. * For more information about OIDC scopes, visit: * https://learn.microsoft.com/en-us/entra/identity-platform/permissions-consent-overview#openid-connect-scopes */ const loginRequest = { scopes: ["User.Read"], }; /** * An optional silentRequest object can be used to achieve silent SSO * between applications by providing a "login_hint" property. */ // const silentRequest = { // scopes: ["openid", "profile"], // loginHint: "example@domain.net" // }; // exporting config object for jest if (typeof exports !== 'undefined') { module.exports = { msalConfig: msalConfig, loginRequest: loginRequest, }; }

clientId

- The identifier of the application, also referred to as the client. Replace the text in quotes with the

Application (client) ID

value that was recorded earlier.

authority

- The authority is a URL that indicates a directory that MSAL can request tokens from. Replace

Enter_the_Tenant_Info_Here

with the

Directory (tenant) ID

value that was recorded earlier.

redirectUri

- The

Redirect URI

of the application. If necessary, replace the text in quotes with the redirect URI that was recorded earlier.

In your IDE, open the project folder,

ms-identity-docs-code-javascript/react-spa

, containing the sample.

Open

react-spa/src/authConfig.js

and update the following values with the information recorded in the admin center.

/* * Copyright (c) Microsoft Corporation. All rights reserved. * Licensed under the MIT License. */ import { LogLevel } from "@azure/msal-browser"; /** * Configuration object to be passed to MSAL instance on creation. * For a full list of MSAL.js configuration parameters, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/configuration.md */ export const msalConfig = { auth: { clientId: "Enter_the_Application_Id_Here", authority: "https://login.microsoftonline.com/Enter_the_Tenant_Info_Here", redirectUri: "http://localhost:3000", }, cache: { cacheLocation: "sessionStorage", // This configures where your cache will be stored storeAuthStateInCookie: false, // Set this to "true" if you are having issues on IE11 or Edge }, system: { loggerOptions: { loggerCallback: (level, message, containsPii) => { if (containsPii) { return; } switch (level) { case LogLevel.Error: console.error(message); return; case LogLevel.Info: console.info(message); return; case LogLevel.Verbose: console.debug(message); return; case LogLevel.Warning: console.warn(message); return; default: return; } } } } }; /** * Scopes you add here will be prompted for user consent during sign-in. * By default, MSAL.js will add OIDC scopes (openid, profile, email) to any login request. * For more information about OIDC scopes, visit: * https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#openid-connect-scopes */ export const loginRequest = { scopes: ["User.Read"] }; /** * Add here the scopes to request when obtaining an access token for MS Graph API. For more information, see: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/resources-and-scopes.md */ export const graphConfig = { graphMeEndpoint: "https://graph.microsoft.com/v1.0/me", };

clientId

- The identifier of the application, also referred to as the client. Replace the text in quotes with the

Application (client) ID

value that was recorded earlier.

authority

- The authority is a URL that indicates a directory that MSAL can request tokens from. Replace

Enter_the_Tenant_Info_Here

with the

Directory (tenant) ID

value that was recorded earlier.

redirectUri

- The

Redirect URI

of the application. If necessary, replace the text in quotes with the redirect URI that was recorded earlier.

In your IDE, open the project folder,

ms-identity-docs-code-javascript/angular-spa

, containing the sample.

Open

angular-spa/src/app/app.module.ts

and update the following values with the information recorded in the admin center.

// Required for Angular multi-browser support import { BrowserModule } from '@angular/platform-browser'; // Required for Angular import { NgModule } from '@angular/core'; // Required modules and components for this application import { AppRoutingModule } from './app-routing.module'; import { AppComponent } from './app.component'; import { ProfileComponent } from './profile/profile.component'; import { HomeComponent } from './home/home.component'; // HTTP modules required by MSAL import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http'; // Required for MSAL import { IPublicClientApplication, PublicClientApplication, InteractionType, BrowserCacheLocation, LogLevel } from '@azure/msal-browser'; import { MsalGuard, MsalInterceptor, MsalBroadcastService, MsalInterceptorConfiguration, MsalModule, MsalService, MSAL_GUARD_CONFIG, MSAL_INSTANCE, MSAL_INTERCEPTOR_CONFIG, MsalGuardConfiguration, MsalRedirectComponent } from '@azure/msal-angular'; const isIE = window.navigator.userAgent.indexOf('MSIE ') > -1 || window.navigator.userAgent.indexOf('Trident/') > -1; export function MSALInstanceFactory(): IPublicClientApplication { return new PublicClientApplication({ auth: { // 'Application (client) ID' of app registration in the Microsoft Entra admin center - this value is a GUID clientId: "Enter_the_Application_Id_Here", // Full directory URL, in the form of https://login.microsoftonline.com/<tenant> authority: "https://login.microsoftonline.com/Enter_the_Tenant_Info_Here", // Must be the same redirectUri as what was provided in your app registration. redirectUri: "http://localhost:4200", }, cache: { cacheLocation: BrowserCacheLocation.LocalStorage, storeAuthStateInCookie: isIE } }); } // MSAL Interceptor is required to request access tokens in order to access the protected resource (Graph) export function MSALInterceptorConfigFactory(): MsalInterceptorConfiguration { const protectedResourceMap = new Map<string, Array<string>>(); protectedResourceMap.set('https://graph.microsoft.com/v1.0/me', ['user.read']); return { interactionType: InteractionType.Redirect, protectedResourceMap }; } // MSAL Guard is required to protect routes and require authentication before accessing protected routes export function MSALGuardConfigFactory(): MsalGuardConfiguration { return { interactionType: InteractionType.Redirect, authRequest: { scopes: ['user.read'] } }; } // Create an NgModule that contains the routes and MSAL configurations @NgModule({ declarations: [ AppComponent, HomeComponent, ProfileComponent ], imports: [ BrowserModule, AppRoutingModule, HttpClientModule, MsalModule ], providers: [ { provide: HTTP_INTERCEPTORS, useClass: MsalInterceptor, multi: true }, { provide: MSAL_INSTANCE, useFactory: MSALInstanceFactory }, { provide: MSAL_GUARD_CONFIG, useFactory: MSALGuardConfigFactory }, { provide: MSAL_INTERCEPTOR_CONFIG, useFactory: MSALInterceptorConfigFactory }, MsalService, MsalGuard, MsalBroadcastService ], bootstrap: [AppComponent, MsalRedirectComponent] }) export class AppModule { }

clientId

- The identifier of the application, also referred to as the client. Replace the text in quotes with the

Application (client) ID

value that was recorded earlier.

authority

- The authority is a URL that indicates a directory that MSAL can request tokens from. Replace

Enter_the_Tenant_Info_Here

with the

Directory (tenant) ID

value that was recorded earlier.

redirectUri

- The

Redirect URI

of the application. If necessary, replace the text in quotes with the redirect URI that was recorded earlier.

In your IDE, open the project folder,

ms-identity-docs-code-dotnet/spa-blazor-wasm

, containing the sample.

Open

spa-blazor-wasm/wwwroot/appsettings.json

and update the following values with the information recorded earlier in the admin center.

{ "AzureAd": { "Authority": "https://login.microsoftonline.com/<Enter the tenant ID obtained from the Microsoft Entra admin center>", "ClientId": "Enter the client ID obtained from the Microsoft Entra admin center", "ValidateAuthority": true } }

Authority

- The authority is a URL that indicates a directory that MSAL can request tokens from. Replace

Enter_the_Tenant_Info_Here

with the

Directory (tenant) ID

value that was recorded earlier.

ClientId

- The identifier of the application, also referred to as the client. Replace the text in quotes with the

Application (client) ID

value that was recorded earlier.

Run the application and sign in and sign out

JavaScript

React

Angular

Blazor

Run the project with a web server by using Node.js:

To start the server, run the following commands from within the project directory:

cd vanillajs-spa/App npm install npm start

Copy the

https

URL that appears in the terminal, for example,

https://localhost:3000

, and paste it into a browser. We recommend using a private or incognito browser session.

Follow the steps and enter the necessary details to sign in with your Microsoft account. You'll be requested an email address so a one time passcode can be sent to you. Enter the code when prompted.

The application will request permission to maintain access to data you have given it access to, and to sign you in and read your profile. Select

Accept

. The following screenshot appears, indicating that you have signed in to the application and have accessed your profile details from the Microsoft Graph API.

Run the project with a web server by using Node.js:

To start the server, run the following commands from within the project directory:

cd react-spa npm install npm start

Copy the

https

URL that appears in the terminal, for example,

https://localhost:3000

, and paste it into a browser. We recommend using a private or incognito browser session.

Follow the steps and enter the necessary details to sign in with your Microsoft account. You're requested an email address so a one time passcode can be sent to you. Enter the code when prompted.

The application requests permission to maintain access to data you have given it access to, and to sign you in and read your profile. Select

Accept

. The following screenshot appears, indicating that you have signed in to the application and have accessed your profile details from the Microsoft Graph API.

Run the project with a web server by using Node.js:

To start the server, run the following commands from within the project directory:

cd angular-spa npm install npm start

Copy the

https

URL that appears in the terminal, for example,

https://localhost:4200

, and paste it into a browser address bar. We recommend using a private or incognito browser session.

Follow the steps and enter the necessary details to sign in with your Microsoft account. You'll be requested an email address so a one time passcode can be sent to you. Enter the code when prompted.

The application will request permission to maintain access to data you have given it access to, and to sign you in and read your profile. Select

Accept

. The following screenshot appears, indicating that you have signed in to the application and have accessed your profile details from the Microsoft Graph API.

Run the project with a web server by using dotnet:

To start the server, run the following commands from within the project directory:

cd spa-blazor-wasm dotnet workload install wasm-tools dotnet run

Copy the

http

URL that appears in the terminal, for example,

http://localhost:5000

, and paste it into a browser. We recommend using a private or incognito browser session.

Follow the steps and enter the necessary details to sign in with your Microsoft account. You'll be requested an email address so a one time passcode can be sent to you. Enter the code when prompted.

The application will request permission to maintain access to data you have given it access to, and to sign you in and read your profile. Select

Accept

. The following screenshot appears, indicating that you have signed in to the application and have accessed your profile details from the Microsoft Graph API.

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

A user flow. For more information, refer to

create self-service sign-up user flows for apps in external tenants

. This user flow can be used for multiple applications.

Visual Studio Code

or another code editor.

JavaScript

React

Angular

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

Single-page application

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost:3000/

Add your application to the user flow

Node.js

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

Single-page application

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost:3000/

Add your application to the user flow

Node.js

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

Single-page application

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost:4200/

Add your application to the user flow

Node.js

Clone or download sample SPA

To obtain the sample application, you can either clone it from GitHub or download it as a .zip file.

JavaScript

React

Angular

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-javascript-tutorial.git

Download the sample

. Extract it to a file path where the length of the name is fewer than 260 characters.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-javascript-tutorial.git

Download the sample

. Extract it to a file path where the length of the name is fewer than 260 characters.

To clone the sample, open a command prompt and navigate to where you wish to create the project, and enter the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-javascript-tutorial.git

Download the sample

. Extract it to a file path where the length of the name is fewer than 260 characters.

Configure the sample SPA

JavaScript

React

Angular

Open

App/public/authConfig.js

and replace the following with the values obtained from the Microsoft Entra admin center:

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

Save the file.

Open

SPA\src\authConfig.js

and replace the following with the values obtained from the Microsoft Entra admin center:

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

Save the file.

Open

SPA/src/app/auth-config.ts

and replace the following with the values obtained from the Microsoft Entra admin center:

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

Save the file.

Run your project and sign in

JavaScript

React

Angular

To start the server, run the following commands from within the project directory:

cd 1-Authentication\0-sign-in-vanillajs\App npm install npm start

Copy the

https

URL that appears in the terminal, for example,

https://localhost:3000

, and paste it into a browser. We recommend using a private or incognito browser session.

Sign-in with an account registered to the tenant.

The following screenshot appears, indicating that you have signed in to the application and have accessed your profile details from the Microsoft Graph API.

To start the server, run the following commands from within the project directory:

cd 1-Authentication\1-sign-in-react\SPA npm install npm start

Copy the

https

URL that appears in the terminal, for example,

https://localhost:3000

, and paste it into a browser. We recommend using a private or incognito browser session.

Sign-in with an account registered to the external tenant.

The following screenshot appears, indicating that you have signed in to the application and have accessed your profile details from the Microsoft Graph API.

To start the server, run the following commands from within the project directory:

cd 1-Authentication\2-sign-in-angular\SPA npm install npm start

Copy the

https

URL that appears in the terminal, for example,

https://localhost:4200

, and paste it into a browser. We recommend using a private or incognito browser session.

Sign-in with an account registered to the external tenant.

The following screenshot appears, indicating that you have signed in to the application and have accessed your profile details from the Microsoft Graph API.

Sign out from the application

Find the

Sign out

button on the page, and select it.

You'll be prompted to pick an account to sign out from. Select the account you used to sign in.

A message appears indicating that you have signed out. You can now close the browser window.

Related content

Quickstart: Protect an ASP.NET Core web API with the Microsoft identity platform

.

Learn more by building a React SPA that signs in users in the following multi-part tutorial series

.

Enable password reset

.

Customize the default branding

.

Configure sign-in with Google

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
