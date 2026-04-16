---
title: Run automated integration tests - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/test-automate-integration-testing
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:42.619498+00:00
kind: extracted-doc
---

# Run automated integration tests - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/test-automate-integration-testing

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:42.619498+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/test-automate-integration-testing
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth-ropc
- https://learn.microsoft.com/en-us/entra/identity-platform/test-setup-environment
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-overview

Captured summary:

- Run automated integration tests - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Run automated integration tests Feedback Summarize this article for me As a developer, you want to run automated integration tests on the apps you develop.
- Calling your API protected by Microsoft identity platform (or other protected APIs such as Microsoft Graph ) in automated integration tests is a challenge.

Extracted text:

Run automated integration tests - Microsoft identity platform | Microsoft Learn

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

Run automated integration tests

Feedback

Summarize this article for me

As a developer, you want to run automated integration tests on the apps you develop. Calling your API protected by Microsoft identity platform (or other protected APIs such as

Microsoft Graph

) in automated integration tests is a challenge. Microsoft Entra ID often requires an interactive user sign-in prompt, which is difficult to automate. This article describes how you can use a non-interactive flow, called

Resource Owner Password Credential Grant (ROPC)

, to automatically sign in users for testing.

To prepare for your automated integration tests, create some test users, create and configure an app registration, and potentially make some configuration changes to your tenant. Some of these steps require admin privileges.

Create a separate test tenant

that you are an administrator of so you can safely and effectively run your automated integration tests.

Warning

Microsoft recommends that you

do not

use the ROPC flow in a production environment. Use a more trusted method such as the

authorization code flow

. In most production scenarios, more secure alternatives are available and recommended. The ROPC flow requires a very high degree of trust in the application, and carries risks which aren't present in other authentication flows. You should only use this flow for testing purposes in a

separate test tenant

, and only with test users.

Important

The Microsoft identity platform only supports ROPC within Microsoft Entra tenants, not personal accounts. This means that you must use a tenant-specific endpoint (

https://login.microsoftonline.com/{TenantId_or_Name}

) or the

organizations

endpoint.

Personal accounts that are invited to a Microsoft Entra tenant can't use ROPC.

Accounts that don't have passwords can't sign in with ROPC, which means features like SMS sign-in, FIDO, and the Authenticator app won't work with that flow.

If users need to use

multifactor authentication (MFA)

to sign in to the application, they are blocked instead.

ROPC isn't supported in

hybrid identity federation

scenarios (for example, Microsoft Entra ID and Active Directory Federation Services (AD FS) used to authenticate on-premises accounts). If users are full-page redirected to an on-premises identity provider, Microsoft Entra ID isn't able to test the username and password against that identity provider.

Pass-through authentication

is supported with ROPC, however.

An exception to a hybrid identity federation scenario would be the following: Home Realm Discovery policy with

AllowCloudPasswordValidation

set to TRUE will enable ROPC flow to work for federated users when on-premises password is synced to cloud. For more information, see

Enable direct ROPC authentication of federated users for legacy applications

.

Create a separate test tenant

Using the ROPC authentication flow is risky in a production environment, so

create a separate tenant

to test your applications. You can use an existing test tenant, but you need to be an admin in the tenant since some of the following steps require admin privileges.

Create and configure a key vault

We recommend you securely store the test usernames and passwords as

secrets

in Azure Key Vault. When you run the tests later, the tests run in the context of a security principal. The security principal is a Microsoft Entra user if you're running tests locally (for example, in Visual Studio or Visual Studio Code), or a service principal or managed identity if you're running tests in Azure Pipelines or another Azure resource. The security principal must have

Read

and

List

secrets permissions so the test runner can get the test usernames and passwords from your key vault. For more information, read

Authentication in Azure Key Vault

.

Create a new key vault

if you don't have one already.

Take note of the

Vault URI

property value (similar to

https://<your-unique-keyvault-name>.vault.azure.net/

) which is used in the example test later in this article.

Assign an access policy

for the security principal running the tests. Grant the user, service principal, or managed identity

Get

and

List

secrets permissions in the key vault.

Create test users

Create some test users in your tenant for testing. Since the test users aren't actual humans, we recommend you assign complex passwords and securely store these passwords as

secrets

in Azure Key Vault.

Sign in to the

Microsoft Entra admin center

as at least a

Cloud Application Administrator

.

Browse to

Entra ID

>

Users

.

Select

New user

and create one or more test user accounts in your directory.

The example test later in this article uses a single test user.

Add the test username and password as secrets

in the key vault you created previously. Add the username as a secret named "TestUserName" and the password as a secret named "TestPassword".

Create and configure an app registration

Register an application that acts as your client app when calling APIs during testing. This shouldn't* be the same application you may already have in production. You should have a separate app to use only for testing purposes.

Register an application

Create an app registration. You can follow the steps in the

app registration quickstart

and take note of the

Application (client) ID

, which is used in the example test later in this article.

Enable your app for public client flows

ROPC is a public client flow, so you need to enable your app for public client flows. From your app registration in the

Microsoft Entra admin center

, go to

Authentication

>

Advanced settings

>

Allow public client flows

. Set the toggle to

Yes

.

Consent to the permissions you want to use while testing

Since ROPC isn't an interactive flow, you won't be prompted with a consent screen to consent to these at runtime. Preconsent to the permissions to avoid errors when acquiring tokens.

Add the permissions to your app. Don't add any sensitive or high-privilege permissions to the app, we recommend you scope your testing scenarios to basic integration scenarios around integrating with Microsoft Entra ID.

From your app registration in the

Microsoft Entra admin center

, go to

API Permissions

>

Add a permission

. Add the permissions you need to call the APIs you're using. A test example further in this article uses the

https://graph.microsoft.com/User.Read

and

https://graph.microsoft.com/User.ReadBasic.All

permissions.

Once the permissions are added, you need to consent to them. The way you consent to the permissions depends on if your test app is in the same tenant as the app registration and whether you're an admin in the tenant.

App and app registration are in the same tenant and you're an admin

If you plan on testing your app in the same tenant you registered it in and you're an administrator in that tenant, you can consent to the permissions from the

Microsoft Entra admin center

. In your app registration in the Azure portal, go to

API Permissions

and select the

Grant admin consent for <your_tenant_name>

button next to the

Add a permission

button and then

Yes

to confirm.

App and app registration are in different tenants, or you're not an admin

If you don't plan on testing your app in the same tenant you registered it in, or you aren't an administrator in your tenant, you can't consent to the permissions from the

Microsoft Entra admin center

. You can still consent to some permissions, however, by triggering a sign-in prompt in a web browser.

Go to

Microsoft Entra admin center

, Navigate to

Entra ID

>

App registrations

> Select your application from the list. > go to

Authentication

>

Platform configurations

>

Add a platform

>

Web

. Add the redirect URI "https://localhost" and select

Configure

.

There's no way for non-admin users to preconsent through the Azure portal, so send the following request in a browser. When you're prompted with the login screen, sign in with a test account you created in a previous step. Consent to the permissions you are prompted with. You may need to repeat this step for each API you want to call and test user you want to use.

// Line breaks for legibility only https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize? client_id={your_client_ID} &response_type=code &redirect_uri=https://localhost &response_mode=query &scope={resource_you_want_to_call}/.default &state=12345

Replace

{tenant}

with your tenant ID,

{your_client_ID}

with the client ID of your application, and

{resource_you_want_to_call}

with the identifier URI (for example, "https://graph.microsoft.com") or app ID of the API you're trying to access.

Exclude test apps and users from your MFA policy

Your tenant likely has a Conditional Access policy that

requires multifactor authentication (MFA) for all users

, as recommended by Microsoft. MFA won't work with ROPC, so you need to exempt your test applications and test users from this requirement.

To exclude user accounts:

Sign in to the

Microsoft Entra admin center

as at least a

Cloud Application Administrator

.

Browse to

Entra ID

>

Conditional Access

>

Policies

.

Select the Conditional Access policy that requires MFA.

Select

Users or workload identities

.

Select the

Exclude

tab and then the

Users and groups

checkbox.

Select the user account to exclude in

Select excluded users

.

Select the

Select

button and then

Save

.

To exclude a test application:

In

Policies

, select the Conditional Access policy that requires MFA.

Select

Cloud apps or actions

.

Select the

Exclude

tab and then

Select excluded cloud apps

.

Select the app(s) you want to exclude in

Select excluded cloud apps

.

Select the

Select

button and then

Save

.

Write your application tests

Now that you're set up, you can write your automated tests. The following are tests for:

.NET example code uses

Microsoft Authentication Library (MSAL)

and

xUnit

, a common testing framework.

JavaScript example code uses

Microsoft Authentication Library (MSAL)

and

Playwright

, a common testing framework.

.NET

JavaScript

Set up your appsettings.json file

Add the client ID of the test app you previously created, the necessary scopes, and the key vault URI to the

appsettings.json

file of your test project.

{ "Authentication": { "AzureCloudInstance": "AzurePublic", //Will be different for different Azure clouds, like US Gov "AadAuthorityAudience": "AzureAdMultipleOrgs", "ClientId": <your_client_ID> }, "WebAPI": { "Scopes": [ //For this Microsoft Graph example. Your value(s) will be different depending on the API you're calling "https://graph.microsoft.com/User.Read", //For this Microsoft Graph example. Your value(s) will be different depending on the API you're calling "https://graph.microsoft.com/User.ReadBasic.All" ] }, "KeyVault": { "KeyVaultUri": "https://<your-unique-keyvault-name>.vault.azure.net//" } }

Set up your client for use across all your test classes

Use

SecretClient()

to get the test username and password secrets from Azure Key Vault. The code uses exponential back-off for retries in case Key Vault is being throttled.

DefaultAzureCredential()

authenticates with Azure Key Vault by getting an access token from a service principal configured by environment variables or a managed identity (if the code is running on an Azure resource with a managed identity). If the code is running locally,

DefaultAzureCredential

uses the local user's credentials. Read more in the

Azure Identity client library

content.

Use Microsoft Authentication Library (MSAL) to authenticate using the ROPC flow and get an access token. The access token is passed along as a bearer token in the HTTP request.

using Xunit; using System.Threading.Tasks; using Microsoft.Identity.Client; using System.Security; using System.Net; using System.Net.Http; using System.Net.Http.Headers; using Microsoft.Extensions.Configuration; using Azure.Identity; using Azure.Security.KeyVault.Secrets; using Azure.Core; using System; public class ClientFixture : IAsyncLifetime { public HttpClient httpClient; public async Task InitializeAsync() { var builder = new ConfigurationBuilder().AddJsonFile("<path-to-json-file>"); IConfigurationRoot Configuration = builder.Build(); var PublicClientApplicationOptions = new PublicClientApplicationOptions(); Configuration.Bind("Authentication", PublicClientApplicationOptions); var app = PublicClientApplicationBuilder.CreateWithApplicationOptions(PublicClientApplicationOptions) .Build(); SecretClientOptions options = new SecretClientOptions() { Retry = { Delay= TimeSpan.FromSeconds(2), MaxDelay = TimeSpan.FromSeconds(16), MaxRetries = 5, Mode = RetryMode.Exponential } }; string keyVaultUri = Configuration.GetValue<string>("KeyVault:KeyVaultUri"); var client = new SecretClient(new Uri(keyVaultUri), new DefaultAzureCredential(), options); KeyVaultSecret userNameSecret = client.GetSecret("TestUserName"); KeyVaultSecret passwordSecret = client.GetSecret("TestPassword"); string password = passwordSecret.Value; string username = userNameSecret.Value; string[] scopes = Configuration.GetSection("WebAPI:Scopes").Get<string[]>(); SecureString securePassword = new NetworkCredential("", password).SecurePassword; AuthenticationResult result = null; httpClient = new HttpClient(); try { result = await app.AcquireTokenByUsernamePassword(scopes, username, securePassword) .ExecuteAsync(); } catch (MsalException) { } string accessToken = result.AccessToken; httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("bearer", accessToken); } public Task DisposeAsync() => Task.CompletedTask; }

Use in your test classes

The following example is a test that calls Microsoft Graph. Replace this test with whatever you'd like to test on your own application or API.

public class ApiTests : IClassFixture<ClientFixture> { ClientFixture clientFixture; public ApiTests(ClientFixture clientFixture) { this.clientFixture = clientFixture; } [Fact] public async Task GetRequestTest() { var testClient = clientFixture.httpClient; HttpResponseMessage response = await testClient.GetAsync("https://graph.microsoft.com/v1.0/me"); var responseCode = response.StatusCode.ToString(); Assert.Equal("OK", responseCode); } }

Set up your authConfig.json file

Add the client ID and the tenant ID of the test app you previously created, the key vault URI, and the secret name to the authConfig.js file of your test project.

export const msalConfig = { auth: { clientId: 'Enter_the_Application_Id_Here', authority: 'https://login.microsoftonline.com/Enter_the_Tenant_Id_Here', }, }; export const keyVaultConfig = { keyVaultUri: 'https://<your-unique-keyvault-name>.vault.azure.net', secretName: 'Enter_the_Secret_Name', };

Initialize MSAL.js and fetch the user credentials from Key Vault

Initialize the MSAL.js authentication context by instantiating a

PublicClientApplication

with a

Configuration

object.The minimum required configuration property is the

clientID

of the application.

Use

SecretClient()

to get the test username and password secrets from Azure Key Vault.

DefaultAzureCredential()

authenticates with Azure Key Vault by getting an access token from a service principal configured by environment variables or a managed identity (if the code is running on an Azure resource with a managed identity). If the code is running locally,

DefaultAzureCredential

uses the local user's credentials. Read more in the

Azure Identity client library

content.

Use Microsoft Authentication Library (MSAL) to authenticate using the ROPC flow and get an access token. The access token is passed along as a bearer token in the HTTP request.

import { test, expect } from '@playwright/test'; import { DefaultAzureCredential } from '@azure/identity'; import { SecretClient } from '@azure/keyvault-secrets'; import { PublicClientApplication, CacheKVStore } from '@azure/msal-node'; import { msalConfig, keyVaultConfig } from '../authConfig'; let tokenCache; const KVUri = keyVaultConfig.keyVaultUri; const secretName = keyVaultConfig.secretName; async function getCredentials() { try { const credential = new DefaultAzureCredential(); const secretClient = new SecretClient(KVUri, credential); const secret = await secretClient.getSecret(keyVaultConfig.secretName); const password = secret.value; return [secretName, password]; } catch (error) { console.log(error); } } test.beforeAll(async () => { const pca = new PublicClientApplication(msalConfig); const [username, password] = await getCredentials(); const usernamePasswordRequest = { scopes: ['user.read', 'User.ReadBasic.All'], username: username, password: password, }; await pca.acquireTokenByUsernamePassword(usernamePasswordRequest); tokenCache = pca.getTokenCache().getKVStore(); });

Run the test suite

In the same file, add the tests as shown below:

/** * Stores the token in the session storage and reloads the page */ async function setSessionStorage(page, tokens) { const cacheKeys = Object.keys(tokens); for (let key of cacheKeys) { const value = JSON.stringify(tokenCache[key]); await page.context().addInitScript( (arr) => { window.sessionStorage.setItem(arr[0], arr[1]); }, [key, value] ); } await page.reload(); } test.describe('Testing Authentication with MSAL.js ', () => { test('Test user has signed in successfully', async ({ page }) => { await page.goto('http://localhost:<port>/'); let signInButton = page.getByRole('button', { name: /Sign In/i }); let signOutButton = page.getByRole('button', { name: /Sign Out/i }); let welcomeDev = page.getByTestId('WelcomeMessage'); expect(await signInButton.count()).toBeGreaterThan(0); expect(await signOutButton.count()).toBeLessThanOrEqual(0); expect(await welcomeDev.innerHTML()).toEqual('Please sign-in to see your profile and read your mails'); await setSessionStorage(page, tokenCache); expect(await signInButton.count()).toBeLessThanOrEqual(0); expect(await signOutButton.count()).toBeGreaterThan(0); expect(await welcomeDev.innerHTML()).toContain(`Welcome`); }); });

For more information, please check the following code sample

MSAL.js Testing Example

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

2025-06-11
