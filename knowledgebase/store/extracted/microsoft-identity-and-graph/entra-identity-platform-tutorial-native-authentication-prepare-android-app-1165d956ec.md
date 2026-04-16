---
title: Prepare your Android mobile app for native authentication - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-prepare-android-app
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:50.645749+00:00
kind: extracted-doc
---

# Prepare your Android mobile app for native authentication - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-prepare-android-app

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:50.645749+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-prepare-android-app
- https://learn.microsoft.com/en-us/entra/identity-platform/concept-native-authentication-challenge-types
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-logging-android
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-native-authentication-android-sign-up

Captured summary:

- Prepare your Android mobile app for native authentication - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Tutorial: Prepare your Android mobile app for native authentication Feedback Summarize this article for me Applies to : External tenants ( learn more ) This tutorial demonstrates how to add Microsoft Authentication Library (MSAL) native authentication SDK to an Android mobile app.
- In this tutorial, you: Add MSAL dependencies.

Extracted text:

Prepare your Android mobile app for native authentication - Microsoft identity platform | Microsoft Learn

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

Tutorial: Prepare your Android mobile app for native authentication

Feedback

Summarize this article for me

Applies to

:

External tenants (

learn more

)

This tutorial demonstrates how to add Microsoft Authentication Library (MSAL) native authentication SDK to an Android mobile app.

In this tutorial, you:

Add MSAL dependencies.

Create a configuration file.

Create MSAL SDK instance.

Prerequisites

If you haven't already, follow the instructions in

Sign in users in sample Android (Kotlin) mobile app by using native authentication

and register an app in your external tenant. Make sure you complete the following steps:

Register an application.

Enable public client and native authentication flows.

Grant API permissions.

Create a user flow.

Associate the app with the user flow.

An Android project. If you don't have an Android project, create it.

Add MSAL dependencies

Open your project in Android Studio or create a new project.

Open your application's

build.gradle

and add the following dependencies:

allprojects { repositories { //Needed for com.microsoft.device.display:display-mask library maven { url 'https://pkgs.dev.azure.com/MicrosoftDeviceSDK/DuoSDK-Public/_packaging/Duo-SDK-Feed/maven/v1' name 'Duo-SDK-Feed' } mavenCentral() google() } } //... dependencies { implementation 'com.microsoft.identity.client:msal:6.+' //... }

In Android Studio, select

File

>

Sync Project with Gradle Files

.

Create a configuration file

You pass the required tenant identifiers, such as the application (client) ID, to the MSAL SDK through a JSON configuration setting.

Use these steps to create configuration file:

In Android Studio's project pane, navigate to

app\src\main\res

.

Right-click

res

and select

New

>

Directory

. Enter

raw

as the new directory name and select

OK

.

In

app\src\main\res\raw

, create a new JSON file called

auth_config_native_auth.json

.

In the

auth_config_native_auth.json

file, add the following MSAL configurations:

{ "client_id": "Enter_the_Application_Id_Here", "authorities": [ { "type": "CIAM", "authority_url": "https://Enter_the_Tenant_Subdomain_Here.ciamlogin.com/Enter_the_Tenant_Subdomain_Here.onmicrosoft.com/" } ], "challenge_types": ["oob"], "logging": { "pii_enabled": false, "log_level": "INFO", "logcat_enabled": true } } //...

Replace the following placeholders with your tenant values that you obtained from the Microsoft Entra admin center:

Replace the

Enter_the_Application_Id_Here

placeholder with the application (client) ID of the app you registered earlier.

Replace the

Enter_the_Tenant_Subdomain_Here

with the directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't have your tenant name, learn how to

read your tenant details

.

The challenge types are a list of values, which the app uses to notify Microsoft Entra about the authentication method that it supports.

For sign-up and sign-in flows with email one-time passcode, use

["oob"]

.

For sign-up and sign-in flows with email and password, use

["oob","password"]

.

For self-service password reset (SSPR), use

["oob"]

.

Learn more

challenge types

.

Optional: Logging configuration

Turn on logging at app creation by creating a logging callback, so the SDK can output logs.

import com.microsoft.identity.client.Logger fun initialize(context: Context) { Logger.getInstance().setExternalLogger { tag, logLevel, message, containsPII -> Logs.append("$tag $logLevel $message") } }

To configure the logger, you need to add a section in the configuration file,

auth_config_native_auth.json

:

//... { "logging": { "pii_enabled": false, "log_level": "INFO", "logcat_enabled": true } } //...

logcat_enabled

: Enables the logging functionality of the library.

pii_enabled

: Specifies whether messages containing personal data, or organizational data are logged. When set to false, logs won't contain personal data. When set to true, the logs might contain personal data.

log_level

: Use it to decide which level of logging to enable. Android supports the following log levels:

ERROR

WARNING

INFO

VERBOSE

For more information on MSAL logging, see

Logging in MSAL for Android

.

Create native authentication MSAL SDK instance

In the

onCreate()

method, create an MSAL instance so the app can perform authentication with your tenant through native authentication. The

createNativeAuthPublicClientApplication()

method returns an instance called

authClient

. Pass the JSON configuration file that you created earlier as a parameter.

//... authClient = PublicClientApplication.createNativeAuthPublicClientApplication( this, R.raw.auth_config_native_auth ) //...

Your code should look something similar to the following snippet:

class MainActivity : AppCompatActivity() { private lateinit var authClient: INativeAuthPublicClientApplication override fun onCreate(savedInstanceState: Bundle?) { super.onCreate(savedInstanceState) setContentView(R.layout.activity_main) authClient = PublicClientApplication.createNativeAuthPublicClientApplication( this, R.raw.auth_config_native_auth ) getAccountState() } private fun getAccountState() { CoroutineScope(Dispatchers.Main).launch { val accountResult = authClient.getCurrentAccount() when (accountResult) { is GetAccountResult.AccountFound -> { displaySignedInState(accountResult.resultValue) } is GetAccountResult.NoAccountFound -> { displaySignedOutState() } } } } private fun displaySignedInState(accountResult: AccountState) { val accountName = accountResult.getAccount().username val textView: TextView = findViewById(R.id.accountText) textView.text = "Cached account found: $accountName" } private fun displaySignedOutState() { val textView: TextView = findViewById(R.id.accountText) textView.text = "No cached account found" } }

Retrieve the cached account by using the

getCurrentAccount()

, which returns an object,

accountResult

.

If an account is found in persistence, use

GetAccountResult.AccountFound

to display a signed-in state.

Otherwise, use

GetAccountResult.NoAccountFound

to display a signed-out state.

Make sure you include the import statements. Android Studio should include the import statements for you automatically.

Next step

Tutorial: Add sign-up in an Android mobile app using native authentication

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
