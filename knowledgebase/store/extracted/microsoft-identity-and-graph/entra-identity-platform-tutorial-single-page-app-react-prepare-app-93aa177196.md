---
title: Tutorial: Prepare a React single-page application for authentication - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-single-page-app-react-prepare-app
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:48.587424+00:00
kind: extracted-doc
---

# Tutorial: Prepare a React single-page application for authentication - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-single-page-app-react-prepare-app

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:48.587424+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-single-page-app-react-prepare-app
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri
- https://learn.microsoft.com/en-us/entra/identity-platform/authentication-national-cloud
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-single-page-app-react-configure-authentication

Captured summary:

- Tutorial: Prepare a React single-page application for authentication - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Tutorial: Create a React single-page application and prepare it for authentication Feedback Summarize this article for me Applies to : Workforce tenants External tenants ( learn more ) In this tutorial you'll build a React single-page application (SPA) and prepare it for authentication using the Microsoft identity platform.
- This tutorial demonstrates how to create a React SPA using npm , create files needed for authentication and authorization and add your tenant details to the source code.

Extracted text:

Tutorial: Prepare a React single-page application for authentication - Microsoft identity platform | Microsoft Learn

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

Tutorial: Create a React single-page application and prepare it for authentication

Feedback

Summarize this article for me

Applies to

:

Workforce tenants

External tenants (

learn more

)

In this tutorial you'll build a React single-page application (SPA) and prepare it for authentication using the Microsoft identity platform. This tutorial demonstrates how to create a React SPA using

npm

, create files needed for authentication and authorization and add your tenant details to the source code. The application can be used for employees in a workforce tenant or for customers using an external tenant.

In this tutorial, you:

Create a new React project

Install packages required for authentication

Create your file structure and add code to the server file

Add your tenant details to the authentication configuration file

Prerequisites

Workforce tenant

External tenant

A workforce tenant. You can use your

Default Directory

or set up a new tenant.

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

.

An external tenant. To create one, choose from the following methods:

(Recommended) Use the

Microsoft Entra External ID extension

to set up an external tenant directly in Visual Studio Code.

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

Add the following redirect URIs using the

Single-page application

platform configuration. Refer to

How to add a redirect URI in your application

for more details.

Redirect URI

:

http://localhost:3000/

.

Associate your app with a user flow in the Microsoft Entra admin center. This user flow can be used across multiple applications. For more information, see

Create self-service sign-up user flows for apps in external tenants

and

Add your application to the user flow

.

Node.js

.

Visual Studio Code

or another code editor.

Create a new React project

Open Visual Studio Code, select

File

>

Open Folder...

. Navigate to and select the location in which to create your project.

Open a new terminal by selecting

Terminal

>

New Terminal

.

Run the following commands to create a new React project with the name

reactspalocal

, change to the new directory and start the React project. A web browser will open with the address

http://localhost:3000/

by default. The browser remains open and re-renders for every saved change.

npx create-react-app reactspalocal cd reactspalocal npm start

Create additional folders and files to achieve the following folder structure:

├─── public │ └─── index.html └───src └─── styles │ └─── App.css │ └─── index.css ├─── utils │ └─── claimUtils.js ├─── components │ └─── DataDisplay.jsx │ └─── NavigationBar.jsx │ └─── PageLayout.jsx └── App.jsx └── authConfig.js └── index.js

Install identity and bootstrap packages

Identity related

npm

packages must be installed in the project to enable user authentication. For project styling,

Bootstrap

will be used.

In the

Terminal

bar, select the

+

icon to create a new terminal. A separate terminal window will open with the previous node terminal continuing to run in the background.

Ensure that the correct directory is selected (

reactspalocal

) then enter the following into the terminal to install the relevant

msal

and

bootstrap

packages.

npm install @azure/msal-browser @azure/msal-react npm install react-bootstrap bootstrap

Add your tenant details to the MSAL configuration

The

authConfig.js

file contains the configuration settings for the authentication flow and is used to configure

MSAL.js

with the required settings for authentication.

Workforce tenant

External tenant

In the

src

folder, open

authConfig.js

and add the following code snippet:

import { LogLevel } from '@azure/msal-browser'; /** * Configuration object to be passed to MSAL instance on creation. * For a full list of MSAL.js configuration parameters, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/configuration.md */ export const msalConfig = { auth: { clientId: 'Enter_the_Application_Id_Here', // This is the ONLY mandatory field that you need to supply. authority: 'https://login.microsoftonline.com/Enter_the_Tenant_Info_Here', // Replace the placeholder with your tenant info redirectUri: 'http://localhost:3000', // Points to window.location.origin. You must register this URI on Microsoft Entra admin center/App Registration. postLogoutRedirectUri: '/', // Indicates the page to navigate after logout. navigateToLoginRequestUrl: false, // If "true", will navigate back to the original request location before processing the auth code response. }, cache: { cacheLocation: 'sessionStorage', // Configures cache location. "sessionStorage" is more secure, but "localStorage" gives you SSO between tabs. storeAuthStateInCookie: false, // Set this to "true" if you are having issues on IE11 or Edge }, system: { loggerOptions: { loggerCallback: (level, message, containsPii) => { if (containsPii) { return; } switch (level) { case LogLevel.Error: console.error(message); return; case LogLevel.Info: console.info(message); return; case LogLevel.Verbose: console.debug(message); return; case LogLevel.Warning: console.warn(message); return; default: return; } }, }, }, }; /** * Scopes you add here will be prompted for user consent during sign-in. * By default, MSAL.js will add OIDC scopes (openid, profile, email) to any login request. * For more information about OIDC scopes, visit: * https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#openid-connect-scopes */ export const loginRequest = { scopes: [], }; /** * An optional silentRequest object can be used to achieve silent SSO * between applications by providing a "login_hint" property. */ // export const silentRequest = { // scopes: ["openid", "profile"], // loginHint: "example@domain.net" // };

Replace the following values with the values from the Microsoft Entra admin center.

clientId

- The identifier of the application, also referred to as the client. Replace

Enter_the_Application_Id_Here

with the

Application (client) ID

value that was recorded earlier from the overview page of the registered application.

authority

- This is composed of two parts:

The

Instance

is endpoint of the cloud provider. Check with the different available endpoints in

National clouds

.

The

Tenant ID

is the identifier of the tenant where the application is registered. Replace

Enter_the_Tenant_Info_Here

with the

Directory (tenant) ID

value that was recorded earlier from the overview page of the registered application.

Save the file.

In the

src

folder, open

authConfig.js

and add the following code snippet:

import { LogLevel } from '@azure/msal-browser'; /** * Configuration object to be passed to MSAL instance on creation. * For a full list of MSAL.js configuration parameters, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/configuration.md */ export const msalConfig = { auth: { clientId: 'Enter_the_Application_Id_Here', // This is the ONLY mandatory field that you need to supply. authority: 'https://Enter_the_Tenant_Subdomain_Here.ciamlogin.com/', // Replace the placeholder with your tenant subdomain redirectUri: '/', // Points to window.location.origin. You must register this URI on Azure Portal/App Registration. postLogoutRedirectUri: '/', // Indicates the page to navigate after logout. navigateToLoginRequestUrl: false, // If "true", will navigate back to the original request location before processing the auth code response. }, cache: { cacheLocation: 'sessionStorage', // Configures cache location. "sessionStorage" is more secure, but "localStorage" gives you SSO between tabs. storeAuthStateInCookie: false, // Set this to "true" if you are having issues on IE11 or Edge }, system: { loggerOptions: { loggerCallback: (level, message, containsPii) => { if (containsPii) { return; } switch (level) { case LogLevel.Error: console.error(message); return; case LogLevel.Info: console.info(message); return; case LogLevel.Verbose: console.debug(message); return; case LogLevel.Warning: console.warn(message); return; default: return; } }, }, }, }; /** * Scopes you add here will be prompted for user consent during sign-in. * By default, MSAL.js will add OIDC scopes (openid, profile, email) to any login request. * For more information about OIDC scopes, visit: * https://docs.microsoft.com/azure/active-directory/develop/v2-permissions-and-consent#openid-connect-scopes */ export const loginRequest = { scopes: [], }; /** * An optional silentRequest object can be used to achieve silent SSO * between applications by providing a "login_hint" property. */ // export const silentRequest = { // scopes: ["openid", "profile"], // loginHint: "example@domain.net" // };

Replace the following values with the values from the Entra admin center:

Enter_the_Application_Id_Here

and replace it with the Application (client) ID in the Microsoft Entra admin center.

Enter_the_Tenant_Subdomain_Here

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't have your tenant name, learn how to

read your tenant details

.

Save the file.

Use custom URL domain (Optional)

Applies to

:

External tenants (

learn more

)

Use a custom domain to fully brand the authentication URL. From a user perspective, users remain on your domain during the authentication process, rather than being redirected to

ciamlogin.com

domain name.

Use the following steps to use a custom domain:

Use the steps in

Enable custom URL domains for apps in external tenants

to enable custom URL domain for your external tenant.

In your

authConfig.js

file, locate then

auth

object, then:

Update the value of the

authority

property to

https://Enter_the_Custom_Domain_Here/Enter_the_Tenant_ID_Here

. Replace

Enter_the_Custom_Domain_Here

with your custom URL domain and

Enter_the_Tenant_ID_Here

with your tenant ID. If you don't have your tenant ID, learn how to

read your tenant details

.

Add

knownAuthorities

property with a value

[Enter_the_Custom_Domain_Here]

.

After you make the changes to your

authConfig.js

file, if your custom URL domain is

login.contoso.com

, and your tenant ID is

aaaabbbb-0000-cccc-1111-dddd2222eeee

, then your file should look similar to the following snippet:

//... const msalConfig = { auth: { authority: process.env.AUTHORITY || 'https://login.contoso.com/aaaabbbb-0000-cccc-1111-dddd2222eeee', knownAuthorities: ["login.contoso.com"], //Other properties }, //... };

Add the authentication provider

The

msal

packages are used to provide authentication in the application. The

msal-browser

package is used to handle the authentication flow and the

msal-react

package is used to integrate

msal-browser

with React.

addEventCallback

is used to listen for events that occur during the authentication process, such as when a user successfully logs in. The

setActiveAccount

method is used to set the active account for the application, which is used to determine which user's information to display.

In the

src

folder, open

index.js

and replace the contents of the file with the following code snippet to use the

msal

packages and bootstrap styling:

import React from 'react'; import { createRoot } from 'react-dom/client'; import App from './App'; import { PublicClientApplication, EventType } from '@azure/msal-browser'; import { msalConfig } from './authConfig'; import 'bootstrap/dist/css/bootstrap.min.css'; import './styles/index.css'; /** * MSAL should be instantiated outside of the component tree to prevent it from being re-instantiated on re-renders. * For more, visit: https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-react/docs/getting-started.md */ const msalInstance = new PublicClientApplication(msalConfig); // Default to using the first account if no account is active on page load if (!msalInstance.getActiveAccount() && msalInstance.getAllAccounts().length > 0) { // Account selection logic is app dependent. Adjust as needed for different use cases. msalInstance.setActiveAccount(msalInstance.getAllAccounts()[0]); } // Listen for sign-in event and set active account msalInstance.addEventCallback((event) => { if (event.eventType === EventType.LOGIN_SUCCESS && event.payload.account) { const account = event.payload.account; msalInstance.setActiveAccount(account); } }); const root = createRoot(document.getElementById('root')); root.render( <App instance={msalInstance}/> );

Save the file.

To learn more about these packages refer to the documentation in

msal-browser

and

msal-react

.

Add the main application component

All parts of the app that require authentication must be wrapped in the

MsalProvider

component. You set a an

instance

variable that calls the

useMsal

hook to get the

PublicClientApplication

instance, and then pass it to

MsalProvider

. The

MsalProvider

component makes the

PublicClientApplication

instance available throughout your app via React's Context API. All components underneath

MsalProvider

will have access to the

PublicClientApplication

instance via context as well as all hooks and components provided by

msal-react

.

In the

src

folder, open

App.jsx

and replace the contents of the file with the following code snippet:

import { MsalProvider, AuthenticatedTemplate, useMsal, UnauthenticatedTemplate } from '@azure/msal-react'; import { Container, Button } from 'react-bootstrap'; import { PageLayout } from './components/PageLayout'; import { IdTokenData } from './components/DataDisplay'; import { loginRequest } from './authConfig'; import './styles/App.css'; /** * Most applications will need to conditionally render certain components based on whether a user is signed in or not. * msal-react provides 2 easy ways to do this. AuthenticatedTemplate and UnauthenticatedTemplate components will * only render their children if a user is authenticated or unauthenticated, respectively. For more, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-react/docs/getting-started.md */ const MainContent = () => { /** * useMsal is hook that returns the PublicClientApplication instance, * that tells you what msal is currently doing. For more, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-react/docs/hooks.md */ const { instance } = useMsal(); const activeAccount = instance.getActiveAccount(); const handleRedirect = () => { instance .loginRedirect({ ...loginRequest, prompt: 'create', }) .catch((error) => console.log(error)); }; return ( <div className="App"> <AuthenticatedTemplate> {activeAccount ? ( <Container> <IdTokenData idTokenClaims={activeAccount.idTokenClaims} /> </Container> ) : null} </AuthenticatedTemplate> <UnauthenticatedTemplate> <Button className="signInButton" onClick={handleRedirect} variant="primary"> Sign up </Button> </UnauthenticatedTemplate> </div> ); }; /** * msal-react is built on the React context API and all parts of your app that require authentication must be * wrapped in the MsalProvider component. You will first need to initialize an instance of PublicClientApplication * then pass this to MsalProvider as a prop. All components underneath MsalProvider will have access to the * PublicClientApplication instance via context as well as all hooks and components provided by msal-react. For more, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-react/docs/getting-started.md */ const App = ({ instance }) => { return ( <MsalProvider instance={instance}> <PageLayout> <MainContent /> </PageLayout> </MsalProvider> ); }; export default App;

Save the file.

Next steps

Tutorial: Create components for sign in and sign out in a React single-page app

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

2025-05-25
