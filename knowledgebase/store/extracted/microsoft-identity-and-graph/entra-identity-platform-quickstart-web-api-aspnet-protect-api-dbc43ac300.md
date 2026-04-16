---
title: Quickstart: Call a web API that is protected by the Microsoft identity platform - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-api-aspnet-protect-api
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:41.312913+00:00
kind: extracted-doc
---

# Quickstart: Call a web API that is protected by the Microsoft identity platform - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-api-aspnet-protect-api

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:41.312913+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-web-api-aspnet-protect-api
- https://learn.microsoft.com/en-us/entra/identity-platform/msal-overview
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/permissions-consent-overview
- https://learn.microsoft.com/en-us/entra/identity-platform/media/web-api-tutorial-01-register-app/add-a-scope.png
- https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-web-api-dotnet-core-build-app

Captured summary:

- Quickstart: Call a web API that is protected by the Microsoft identity platform - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Quickstart: Call a web API that is protected by the Microsoft identity platform Feedback Summarize this article for me Applies to : Workforce tenants External tenants ( learn more ) In this quickstart, you use a sample web app to show you how to protect an ASP.NET web API by using the Microsoft identity platform.
- The sample uses the Microsoft Authentication Library (MSAL) to handle authentication and authorization.

Extracted text:

Quickstart: Call a web API that is protected by the Microsoft identity platform - Microsoft identity platform | Microsoft Learn

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

Quickstart: Call a web API that is protected by the Microsoft identity platform

Feedback

Summarize this article for me

Applies to

:

Workforce tenants

External tenants (

learn more

)

In this quickstart, you use a sample web app to show you how to protect an ASP.NET web API by using the Microsoft identity platform. The sample uses the

Microsoft Authentication Library (MSAL)

to handle authentication and authorization.

Prerequisites

An Azure account with an active subscription.

Create an account for free

.

Register a new app in the

Microsoft Entra admin center

and record its identifiers from the app

Overview

page. For more information, see

Register an application

.

Name

:

NewWebAPI1

Supported account types

:

Accounts in this organizational directory only (Single tenant)

ASP.NET

ASP.NET Core

Visual Studio 2022. Download

Visual Studio for free

.

Visual Studio Code

Expose the API

Once the API is registered, you can configure its permission by defining the scopes that the API exposes to client applications. Client applications request permission to perform operations by passing an access token along with its requests to the protected web API. The web API then performs the requested operation only if the access token it receives contains the required scopes.

ASP.NET

ASP.NET Core

Under

Manage

, select

Expose an API

>

Add a scope

. Accept the proposed Application ID URI (

api://{clientId}

) by selecting

Save and continue

, and then enter the following information:

For

Scope name

, enter

access_as_user

.

For

Who can consent

, ensure that the

Admins and users

option is selected.

In the

Admin consent display name

box, enter

Access TodoListService as a user

.

In the

Admin consent description

box, enter

Accesses the TodoListService web API as a user

.

In the

User consent display name

box, enter

Access TodoListService as a user

.

In the

User consent description

box, enter

Accesses the TodoListService web API as a user

.

For

State

, keep

Enabled

.

Select

Add scope

.

Add delegated permissions (scopes)

An API needs to publish a minimum of one scope, also called

Delegated Permission

, for the client apps to obtain an access token for a user successfully. To publish a scope, follow these steps:

From the

App registrations

page, select the API application that you created (

ciam-ToDoList-api

) to open its

Overview

page.

Under

Manage

, select

Expose an API

.

At the top of the page, next to

Application ID URI

, select the

Add

link to generate a URI that is unique for this app.

Accept the proposed Application ID URI such as

api://{clientId}

, and select

Save

. When your web application requests an access token for the web API, it adds the URI as the prefix for each scope that you define for the API.

Under

Scopes defined by this API

, select

Add a scope

.

Enter the following values that define a read access to the API, then select

Add scope

to save your changes:

Property

Value

Scope name

ToDoList.Read

Who can consent

Admins only

Admin consent display name

Read users ToDo list using the 'TodoListApi'

Admin consent description

Allow the app to read the user's ToDo list using the 'TodoListApi'

.

State

Enabled

Select

Add a scope

again, and enter the following values that define a read and write access scope to the API. Select

Add scope

to save your changes:

Property

Value

Scope name

ToDoList.ReadWrite

Who can consent

Admins only

Admin consent display name

Read and write users ToDo list using the 'ToDoListApi'

Admin consent description

Allow the app to read and write the user's ToDo list using the 'ToDoListApi'

State

Enabled

Learn more about

the principle of least privilege when publishing permissions

for a web API.

Add application permissions (app roles)

An API needs to publish a minimum of one app role for applications, also called

Application permission

, for the client apps to obtain an access token as themselves. Application permissions are the type of permissions that APIs should publish when they want to enable client applications to successfully authenticate as themselves and not need to sign-in users. To publish an application permission, follow these steps:

From the

App registrations

page, select the application that you created (such as

ciam-ToDoList-api

) to open its

Overview

page.

Under

Manage

, select

App roles

.

Select

Create app role

, then enter the following values, then select

Apply

to save your changes:

Property

Value

Display name

ToDoList.Read.All

Allowed member types

Applications

Value

ToDoList.Read.All

Description

Allow the app to read every user's ToDo list using the 'TodoListApi'

Do you want to enable this app role?

Keep it checked

Select

Create app role

again, then enter the following values for the second app role, then select

Apply

to save your changes:

Property

Value

Display name

ToDoList.ReadWrite.All

Allowed member types

Applications

Value

ToDoList.ReadWrite.All

Description

Allow the app to read and write every user's ToDo list using the 'ToDoListApi'

Do you want to enable this app role?

Keep it checked

Clone or download the sample application

To obtain the sample application, you can either clone it from GitHub or download it as a

.zip

file.

ASP.NET

ASP.NET Core

git clone https://github.com/AzureADQuickStarts/AppModelv2-NativeClient-DotNet.git

Download it as a ZIP file

.

Tip

To avoid errors caused by path length limitations in Windows, we recommend extracting the archive or cloning the repository into a directory near the root of your drive.

git clone https://github.com/Azure-Samples/ms-identity-ciam-dotnet-tutorial.git

Download the .zip file

. Extract it to a file path where the length of the name is fewer than 260 characters.

Configure the sample application

Configure the code sample to match the registered web API.

ASP.NET

ASP.NET Core

Open the solution in Visual Studio, and then open the

appsettings.json

file under the root of the TodoListService project.

Replace the value of the

Enter_the_Application_Id_here

by the Client ID (Application ID) value from the application you registered in the

App registrations

portal both in the

ClientID

and the

Audience

properties.

Add the new scope to the app.config file

To add the new scope to the TodoListClient

app.config

file, follow these steps:

In the TodoListClient project root folder, open the

app.config

file.

Paste the Application ID from the application that you registered for your TodoListService project in the

TodoListServiceScope

parameter, replacing the

{Enter the Application ID of your TodoListService from the app registration portal}

string.

Note

Make sure that the Application ID uses the following format:

api://{TodoListService-Application-ID}/access_as_user

(where

{TodoListService-Application-ID}

is the GUID representing the Application ID for your TodoListService app).

Register the web app (TodoListClient)

Register your TodoListClient app in

App registrations

in the Microsoft Entra admin center, and then configure the code in the TodoListClient project. If the client and server are considered the same application, you can reuse the application registered in step 2. Use the same application if you want users to sign in with a personal Microsoft account.

Register the app

To register the TodoListClient app, follow these steps:

Sign in to the

Microsoft Entra admin center

as at least a

Cloud Application Administrator

.

Browse to

Entra ID

>

App registrations

and select

New registration

.

Select

New registration

.

When the

Register an application page

opens, enter your application's registration information:

In the

Name

section, enter a meaningful application name that will be displayed to users of the app (for example,

NativeClient-DotNet-TodoListClient

).

For

Supported account types

, select

Accounts in any organizational directory

.

Select

Register

to create the application.

Note

In the TodoListClient project

app.config

file, the default value of

ida:Tenant

is set to

common

. The possible values are:

common

: You can sign in by using a work or school account or a personal Microsoft account (because you selected

Accounts in any organizational directory

in a previous step).

organizations

: You can sign in by using a work or school account.

consumers

: You can sign in only by using a Microsoft personal account.

On the app

Overview

page, select

Authentication

, and then complete these steps to add a platform:

Under

Platform configurations

, select the

Add a platform

button.

For

Mobile and desktop applications

, select

Mobile and desktop applications

.

For

Redirect URIs

, select the

https://login.microsoftonline.com/common/oauth2/nativeclient

check box.

Select

Configure

.

Select

API permissions

, and then complete these steps to add permissions:

Select the

Add a permission

button.

Select the

My APIs

tab.

In the list of APIs, select

AppModelv2-NativeClient-DotNet-TodoListService API

or the name you entered for the web API.

Select the

access_as_user

permission check box if it's not already selected. Use the Search box if necessary.

Select the

Add permissions

button.

Configure your project

Configure your TodoListClient project by adding the Application ID to the

app.config

file.

In the

App registrations

portal, on the

Overview

page, copy the value of the

Application (client) ID

.

From the TodoListClient project root folder, open the

app.config

file, and then paste the Application ID value in the

ida:ClientId

parameter.

In your IDE, open the project folder,

ms-identity-ciam-dotnet-tutorial/2-Authorization/3-call-own-api-dotnet-core-daemon/ToDoListAPI

, containing the sample.

Open

appsettings.json

file, which contains the following code snippet:

{ "AzureAd": { "Instance": "Enter_the_Authority_URL_Here", //For external tenants, use instance in the form of "https://Enter_the_Tenant_Subdomain_Here.ciamlogin.com/" "TenantId": "Enter_the_Tenant_Id_Here", "ClientId": "Enter_the_Application_Id_Here", "Scopes": { "Read": ["ToDoList.Read", "ToDoList.ReadWrite"], "Write": ["ToDoList.ReadWrite"] }, "AppPermissions": { "Read": ["ToDoList.Read.All", "ToDoList.ReadWrite.All"], "Write": ["ToDoList.ReadWrite.All"] } }, "Logging": {...}, "AllowedHosts": "*" }

Find the following values:

ClientId

- The identifier of the application, also referred to as the client. Replace the

value

text in quotes with

Application (client) ID

that was recorded earlier from the

Overview

page of the registered application.

TenantId

- The identifier of the tenant where the application is registered. Replace the

value

text in quotes with

Directory (tenant) ID

value that was recorded earlier from the

Overview

page of the registered application.

Instance

- It specifies the directory from which the Microsoft Authentication Library (MSAL) can request tokens from. Replace

Enter_the_Authority_URL_Here

with either of the following values depending on your scenario:

For workforce tenants, use

https://login.microsoftonline.com/

as the instance.

For external tenants, add an authority URL in the form of

https://<Enter_the_Tenant_Subdomain_Here>.ciamlogin.com/

Run the sample application

ASP.NET

ASP.NET Core

Start both projects. For Visual Studio users;

Right click on the Visual Studio solution and select

Properties

In the

Common Properties

, select

Startup Project

and then

Multiple startup projects

.

For both projects choose

Start

as the action

Ensure the TodoListService service starts first by moving it to the first position in the list, using the up arrow.

Sign in to run your TodoListClient project.

Press F5 to start the projects. The service page opens, as well as the desktop application.

In the TodoListClient, at the upper right, select

Sign in

, and then sign in with the same credentials you used to register your application, or sign in as a user in the same directory.

If you're signing in for the first time, you might be prompted to consent to the TodoListService web API.

To help you access the TodoListService web API and manipulate the

To-Do

list, the sign-in also requests an access token to the

access_as_user

scope.

Pre-authorize your client application

You can allow users from other directories to access your web API by pre-authorizing the client application to access your web API. You do this by adding the Application ID from the client app to the list of preauthorized applications for your web API. By adding a preauthorized client, you're allowing users to access your web API without having to provide consent.

In the

App registrations

portal, open the properties of your TodoListService app.

In the

Expose an API

section, under

Authorized client applications

, select

Add a client application

.

In the

Client ID

box, paste the Application ID of the TodoListClient app.

In the

Authorized scopes

section, select the scope for the

api://<Application ID>/access_as_user

web API.

Select

Add application

.

Run your project

Press

F5

to run your project. Your TodoListClient app opens.

At the upper right, select

Sign in

, and then sign in by using a personal Microsoft account, such as a

live.com

or

hotmail.com

account, or a work or school account.

Optional: Limit sign-in access to certain users

By default, any personal accounts, such as

outlook.com

or

live.com

accounts, or work or school accounts from organizations that are integrated with Microsoft Entra ID can request tokens and access your web API.

To specify who can sign in to your application, by changing the

TenantId

property in the

appsettings.json

file.

Run the following command from the root of your web API project directory to start the app:

dotnet run

If everything worked correctly, your terminal displays an output similar to the following:

Building... info: Microsoft.Hosting.Lifetime[14] Now listening on: https://localhost:{port} info: Microsoft.Hosting.Lifetime[0] Application started. Press Ctrl+C to shut down. info: Microsoft.Hosting.Lifetime[0] Hosting environment: Development ...

Record the port number in the

https://localhost:{port}

URL.

To verify the endpoint is protected, update the base URL in the following cURL command to match the one you received in the previous step, and then run the command:

curl -k -X GET https://localhost:<your-api-port>/api/todolist -w "%{http_code}\n"

The expected response is 401 Unauthorized.

Next steps

Learn how to protect an ASP.NET Core web API with the Microsoft identity platform.

Tutorial: Build and secure an ASP.NET Core web API with the Microsoft identity platform

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

2025-04-04
