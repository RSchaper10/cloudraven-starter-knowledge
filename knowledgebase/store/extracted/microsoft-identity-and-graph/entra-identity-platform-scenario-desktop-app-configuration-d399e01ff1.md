---
title: Configure desktop apps that call web APIs - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/scenario-desktop-app-configuration
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:45.061897+00:00
kind: extracted-doc
---

# Configure desktop apps that call web APIs - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-desktop-app-configuration

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:45.061897+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-desktop-app-configuration
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-desktop-acquire-token-wam
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-ios
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-windows-uwp
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-windows-desktop
- https://learn.microsoft.com/en-us/entra/identity-platform/scenario-desktop-acquire-token

Captured summary:

- Configure desktop apps that call web APIs - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Desktop app that calls web APIs: Code configuration Feedback Summarize this article for me Applies to : Workforce tenants ( learn more ) This article contains instructions to help you configure the code with the application's coordinates.
- Prerequisites Register a new app in the Microsoft Entra admin center , configured for Accounts in this organizational directory only .

Extracted text:

Configure desktop apps that call web APIs - Microsoft identity platform | Microsoft Learn

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

Desktop app that calls web APIs: Code configuration

Feedback

Summarize this article for me

Applies to

:

Workforce tenants (

learn more

)

This article contains instructions to help you configure the code with the application's coordinates.

Prerequisites

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

Add a platform redirect URI

To specify your app type to your app registration, follow these steps:

Under

Manage

, select

Authentication

>

Add a platform

>

Mobile and desktop applications

Depending on the authentication method you're using, choose one of the following options:

For apps using embedded browsers, use the exact value:

https://login.microsoftonline.com/common/oauth2/nativeclient

For apps using system browsers, use the exact value:

http://localhost

Objective-C or Swift apps for macOS:

msauth.<your.app.bundle.id>://auth

.

Node.js Electron apps:

msal{Your_Application/Client_Id}://auth

Note

For

Web Authentication Manager (WAM)

apps, no redirect URI is needed in MSAL.

Enable public client flow

To distinguish device code flow, integrated Windows authentication, and a username and a password from a confidential client application using a client credential flow used in daemon applications, none of which requires a redirect URI, configure it as a public client application. To achieve this configuration

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

Microsoft libraries supporting desktop apps

The following Microsoft libraries support desktop apps:

Language / framework

Project on

GitHub

Package

Getting

started

Sign in users

Access web APIs

Generally available (GA)

or

Public preview

1

Electron

MSAL Node.js

msal-node

—

Public preview

Java

MSAL4J

msal4j

—

GA

macOS (Swift/Obj-C)

MSAL for iOS and macOS

MSAL

Tutorial

GA

UWP

MSAL.NET

Microsoft.Identity.Client

Tutorial

GA

WPF

MSAL.NET

Microsoft.Identity.Client

Tutorial

GA

1

Universal License Terms for Online Services

apply to libraries in

Public preview

.

Public client application

From a code point of view, desktop applications are public client applications. The configuration will be a bit different based on whether you use interactive authentication or not.

.NET

Java

MacOS

Node.js

Python

You'll need to build and manipulate MSAL.NET

IPublicClientApplication

.

Exclusively by code

The following code instantiates a public client application and signs in users in the Microsoft Azure public cloud with a work or school account or a personal Microsoft account.

IPublicClientApplication app = PublicClientApplicationBuilder.Create(clientId) .Build();

If you intend to use interactive authentication or device code flow, as seen previously, use the

.WithRedirectUri

modifier.

IPublicClientApplication app; app = PublicClientApplicationBuilder.Create(clientId) .WithDefaultRedirectUri() .Build();

Use configuration files

The following code instantiates a public client application from a configuration object, which could be filled in programmatically or read from a configuration file.

PublicClientApplicationOptions options = GetOptions(); // your own method IPublicClientApplication app = PublicClientApplicationBuilder.CreateWithApplicationOptions(options) .WithDefaultRedirectUri() .Build();

More elaborated configuration

You can elaborate the application building by adding a number of modifiers. For instance, if you want your application to be a multitenant application in a national cloud, such as US Government shown here, you could write:

IPublicClientApplication app; app = PublicClientApplicationBuilder.Create(clientId) .WithDefaultRedirectUri() .WithAadAuthority(AzureCloudInstance.AzureUsGovernment, AadAuthorityAudience.AzureAdMultipleOrgs) .Build();

MSAL.NET also contains a modifier for Active Directory Federation Services 2019:

IPublicClientApplication app; app = PublicClientApplicationBuilder.Create(clientId) .WithAdfsAuthority("https://consoso.com/adfs") .Build();

Finally, if you want to acquire tokens for an Azure Active Directory (Azure AD) B2C tenant, specify your tenant as shown in the following code snippet:

IPublicClientApplication app; app = PublicClientApplicationBuilder.Create(clientId) .WithB2CAuthority("https://fabrikamb2c.b2clogin.com/tfp/{tenant}/{PolicySignInSignUp}") .Build();

Learn more

To learn more about how to configure an MSAL.NET desktop application:

For a list of all modifiers available on

PublicClientApplicationBuilder

, see the reference documentation

PublicClientApplicationBuilder

.

For a description of all the options exposed in

PublicClientApplicationOptions

, see

PublicClientApplicationOptions

in the reference documentation.

Complete example with configuration options

Imagine a .NET console application that has the following

appsettings.json

configuration file:

{ "Authentication": { "AzureCloudInstance": "AzurePublic", "AadAuthorityAudience": "AzureAdMultipleOrgs", "ClientId": "00001111-aaaa-2222-bbbb-3333cccc4444" }, "WebAPI": { "MicrosoftGraphBaseEndpoint": "https://graph.microsoft.com" } }

You have little code to read in this file by using the .NET-provided configuration framework:

public class SampleConfiguration { /// <summary> /// Authentication options /// </summary> public PublicClientApplicationOptions PublicClientApplicationOptions { get; set; } /// <summary> /// Base URL for Microsoft Graph (it varies depending on whether the application runs /// in Microsoft Azure public clouds or national or sovereign clouds) /// </summary> public string MicrosoftGraphBaseEndpoint { get; set; } /// <summary> /// Reads the configuration from a JSON file /// </summary> /// <param name="path">Path to the configuration json file</param> /// <returns>SampleConfiguration as read from the json file</returns> public static SampleConfiguration ReadFromJsonFile(string path) { // .NET configuration IConfigurationRoot Configuration; var builder = new ConfigurationBuilder() .SetBasePath(Directory.GetCurrentDirectory()) .AddJsonFile(path); Configuration = builder.Build(); // Read the auth and graph endpoint configuration SampleConfiguration config = new SampleConfiguration() { PublicClientApplicationOptions = new PublicClientApplicationOptions() }; Configuration.Bind("Authentication", config.PublicClientApplicationOptions); config.MicrosoftGraphBaseEndpoint = Configuration.GetValue<string>("WebAPI:MicrosoftGraphBaseEndpoint"); return config; } }

Now, to create your application, write the following code:

SampleConfiguration config = SampleConfiguration.ReadFromJsonFile("appsettings.json"); var app = PublicClientApplicationBuilder.CreateWithApplicationOptions(config.PublicClientApplicationOptions) .WithDefaultRedirectUri() .Build();

Before the call to the

.Build()

method, you can override your configuration with calls to

.WithXXX

methods, as seen previously.

Here's the class used in MSAL Java development samples to configure the samples:

TestData

.

PublicClientApplication pca = PublicClientApplication.builder(CLIENT_ID) .authority(AUTHORITY) .build();

The following code instantiates a public client application and signs in users in the Microsoft Azure public cloud with a work or school account or a personal Microsoft account.

Quick configuration

Objective-C:

NSError *msalError = nil; MSALPublicClientApplicationConfig *config = [[MSALPublicClientApplicationConfig alloc] initWithClientId:@"<your-client-id-here>"]; MSALPublicClientApplication *application = [[MSALPublicClientApplication alloc] initWithConfiguration:config error:&msalError];

Swift:

let config = MSALPublicClientApplicationConfig(clientId: "<your-client-id-here>") if let application = try? MSALPublicClientApplication(configuration: config){ /* Use application */}

More elaborated configuration

You can elaborate the application building by adding a number of modifiers. For instance, if you want your application to be a multitenant application in a national cloud, such as US Government shown here, you could write:

Objective-C:

MSALAADAuthority *aadAuthority = [[MSALAADAuthority alloc] initWithCloudInstance:MSALAzureUsGovernmentCloudInstance audienceType:MSALAzureADMultipleOrgsAudience rawTenant:nil error:nil]; MSALPublicClientApplicationConfig *config = [[MSALPublicClientApplicationConfig alloc] initWithClientId:@"<your-client-id-here>" redirectUri:@"<your-redirect-uri-here>" authority:aadAuthority]; NSError *applicationError = nil; MSALPublicClientApplication *application = [[MSALPublicClientApplication alloc] initWithConfiguration:config error:&applicationError];

Swift:

let authority = try? MSALAADAuthority(cloudInstance: .usGovernmentCloudInstance, audienceType: .azureADMultipleOrgsAudience, rawTenant: nil) let config = MSALPublicClientApplicationConfig(clientId: "<your-client-id-here>", redirectUri: "<your-redirect-uri-here>", authority: authority) if let application = try? MSALPublicClientApplication(configuration: config) { /* Use application */}

Configuration parameters can be loaded from many sources, like a JavaScript file or from environment variables. Below, an

authConfig.js

file is used.

/* * Copyright (c) Microsoft Corporation. All rights reserved. * Licensed under the MIT License. */ const { LogLevel } = require("@azure/msal-node"); /** * Configuration object to be passed to MSAL instance on creation. * For a full list of MSAL.js configuration parameters, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-node/docs/configuration.md */ const AAD_ENDPOINT_HOST = "Enter_the_Cloud_Instance_Id_Here"; // include the trailing slash const msalConfig = { auth: { clientId: "Enter_the_Application_Id_Here", authority: `${AAD_ENDPOINT_HOST}Enter_the_Tenant_Info_Here`, }, system: { loggerOptions: { loggerCallback(loglevel, message, containsPii) { console.log(message); }, piiLoggingEnabled: false, logLevel: LogLevel.Verbose, }, }, }; /** * Add here the endpoints and scopes when obtaining an access token for protected web APIs. For more information, see: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/resources-and-scopes.md */ const GRAPH_ENDPOINT_HOST = "Enter_the_Graph_Endpoint_Here"; // include the trailing slash const protectedResources = { graphMe: { endpoint: `${GRAPH_ENDPOINT_HOST}v1.0/me`, scopes: ["User.Read"], } }; module.exports = { msalConfig: msalConfig, protectedResources: protectedResources, };

Import the configuration object from

authConfig.js

file. MSAL Node can be initialized minimally as below. See the available

configuration options

.

const { PublicClientApplication } = require('@azure/msal-node'); const { msalConfig } = require('./authConfig') /** * Initialize a public client application. For more information, visit: * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-node/docs/initialize-public-client-application.md */ clientApplication = new PublicClientApplication(msalConfig);

config = json.load(open(sys.argv[1])) app = msal.PublicClientApplication( config["client_id"], authority=config["authority"], # token_cache=... # Default cache is in memory only. # You can learn how to use SerializableTokenCache from # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache )

Next steps

Move on to the next article in this scenario,

Acquire a token for the desktop app

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

2025-09-11
