---
title: Sign in users in Android mobile app by using native authentication. - Microsoft identity platform | Microsoft Learn
source_url: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-android-sign-in
target_id: microsoft-identity-and-graph
dependency: Microsoft Entra ID and Graph Change Notifications
collected_at: 2026-04-16T03:21:46.835377+00:00
kind: extracted-doc
---

# Sign in users in Android mobile app by using native authentication. - Microsoft identity platform | Microsoft Learn

Source URL:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-android-sign-in

Dependency:

- Microsoft Entra ID and Graph Change Notifications

Collected at:

- 2026-04-16T03:21:46.835377+00:00

Direct links in scope:

- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-android-sign-in
- https://learn.microsoft.com/en-us/entra/identity-platform/concept-native-authentication
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app
- https://learn.microsoft.com/en-us/entra/identity-platform/media/native-authentication/android/android-email-otp-expanded.png
- https://learn.microsoft.com/en-us/entra/identity-platform/media/native-authentication/android/android-submit-code-expanded.png
- https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication-android-call-api

Captured summary:

- Sign in users in Android mobile app by using native authentication.
- - Microsoft identity platform | Microsoft Learn Table of contents Exit editor mode Ask Learn Ask Learn Focus mode Table of contents Read in English Add Add to plan Edit Share via Facebook x.com LinkedIn Email Copy Markdown Print Note Access to this page requires authorization.
- You can try signing in or changing directories .
- Access to this page requires authorization.
- Sign in users in sample Android (Kotlin) app by using native authentication Feedback Summarize this article for me Applies to : External tenants ( learn more ) In this quickstart you learn how to run an Android sample application that demonstrates sign-up, sign in, sign out, and password reset scenarios using Microsoft Entra's native authentication .

Extracted text:

Sign in users in Android mobile app by using native authentication. - Microsoft identity platform | Microsoft Learn

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

Sign in users in sample Android (Kotlin) app by using native authentication

Feedback

Summarize this article for me

Applies to

:

External tenants (

learn more

)

In this quickstart you learn how to run an Android sample application that demonstrates sign-up, sign in, sign out, and password reset scenarios using Microsoft Entra's

native authentication

.

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

If you haven't already done so,

Register an application in the Microsoft Entra admin center

. Make sure to:

Record the

Application (client) ID

and

Directory (tenant) ID

for later use.

Grant admin consent

to the application.

If you haven't already done so,

Create a user flow in the Microsoft Entra admin center

Associate your app registration with the user flow

Android Studio

.

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

Clone sample Android mobile application

Open Terminal and navigate to a directory where you want to keep the code.

Clone the application from GitHub by running the following command:

git clone https://github.com/Azure-Samples/ms-identity-ciam-native-auth-android-sample

Configure the sample Android mobile application

In Android Studio, open the project that you cloned.

Open

app/src/main/res/raw/native_auth_sample_app_config.json

file.

Find the placeholder:

Enter_the_Application_Id_Here

and replace it with the

Application (client) ID

of the app you registered earlier.

Enter_the_Tenant_Subdomain_Here

and replace it with the Directory (tenant) subdomain. For example, if your tenant primary domain is

contoso.onmicrosoft.com

, use

contoso

. If you don't know your tenant subdomain, learn how to

read your tenant details

.

You've now configured the app and it's ready to run.

Run and test the sample Android mobile application

To build and run your app, follow these steps:

In the toolbar, select your app from the run configurations menu.

In the target device menu, select the device that you want to run your app on.

If you don't have any devices configured, you need to either create an Android Virtual Device to use the Android Emulator or connect a physical Android device.

Select the

Run

button. The app opens the

Email & OTP

screen.

Enter a valid email address and select then

Sign up

button. The app opens the submit code screen and you receive an OTP code in the email address.

Enter the OTP code that you receive in the email inbox and select

Next

. If the sign-up is successful, the app signs you in automatically. If you don't receive the OTP code in your email inbox, you can resend it after a while by selecting

Resend Passcode

.

To sign out, select the

Sign out

button.

Other scenarios that this sample supports

This sample app also supports the following authentication flows:

Email + password

covers sign-in or sign-up flows with an email with password.

Email + password sign-up with user attributes

covers sign-up with email and password, and submitting user attributes.

Password reset

covers self-service password reset (SSPR).

Access Protected API

covers call a protected API after the user successfully signs up or signs in and acquires an access token.

Fallback to web browser

covers the use the browser-based authentication as a fallback mechanism when the user can't complete authentication through native authentication for whatever reason.

Test email with password flow

In this section, you test email with password flow, with its variants such as, email with password sign-up with user attributes and SSPR:

Use the steps in

create a user flow

to create a new user flow, but this time select

Email with password

as your authentication method. You need to configure

Country/Region

and

City

as the user attributes. Alternatively, you can modify the existing user flow to use

Email with password

(Select

External Identities

>

User flows

>

SignInSignUpSample

>

Identity providers

>

Email with password

>

Save

).

Use the steps in

associate the application with the new user flow

to add an app to your new user flow.

Run the sample app, then select the ellipsis menu (

...

) to open more options.

Select the scenario you want to test, such as

Email + password

or

Email + password sign-up with user attributes

or

Password reset

, then follow the prompts. To test

Password reset

, you need to first sign up a user, and

enable email one-time passcode

for all users in your tenant.

Test call a protected API flow

Use the steps in

Call a protected web API in a sample Android mobile app by using native authentication

to call a protected web API from a sample Android mobile app.

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

Next steps

Tutorial: Prepare your Android app for native authentication

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
