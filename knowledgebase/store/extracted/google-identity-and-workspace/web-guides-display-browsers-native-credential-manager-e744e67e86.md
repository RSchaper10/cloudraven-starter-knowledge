# Display the browser's native credential manager | Web guides | Google for Developers

Source URL:

- https://developers.google.com/identity/gsi/web/guides/display-browsers-native-credential-manager

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-15T19:44:42.833150+00:00

Direct links in scope:

- https://developers.google.com/identity/gsi/web/guides/display-browsers-native-credential-manager
- https://developers.google.com/identity/gsi/web/guides/overview

Captured summary:

- Display the browser's native credential manager | Web guides | Google for Developers Skip to main content Identity Web guides / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Home Products Google Identity Web guides Sign in with Google for Web Send feedback Display the browser's native credential manager Stay organized with collections Save and categorize content based on your preferences.
- A browser's native credential manager stores a user's password credentials.
- To enable the browser's native credential manager, set the data-native_login_uri attribute.
- The One Tap prompt and the native credential manager dialog aren't displayed together on the same page.
- The native dialog is only displayed when the One Tap prompt isn't displayed.

Extracted text:

Display the browser's native credential manager | Web guides | Google for Developers

Skip to main content

Identity

Web guides

/

English

Deutsch

Español

Español – América Latina

Français

Indonesia

Italiano

Polski

Português – Brasil

Tiếng Việt

Türkçe

Русский

עברית

العربيّة

فارسی

हिंदी

বাংলা

ภาษาไทย

中文 – 简体

中文 – 繁體

日本語

한국어

Sign in

Home

Products

Google Identity

Web guides

Sign in with Google for Web

Send feedback

Display the browser's native credential manager

Stay organized with collections

Save and categorize content based on your preferences.

A browser's native credential manager stores a user's password credentials. To enable the browser's native credential manager, set the

data-native_login_uri

attribute.

The One Tap prompt and the native credential manager dialog aren't displayed together on the same page. The native dialog is only displayed when the One Tap prompt isn't displayed. See the following code example:

<div id="g_id_onload" data-client_id="

YOUR_GOOGLE_CLIENT_ID

" data-login_uri="

https://your.domain/your_login_endpoint

" data-native_login_uri="

https://your.domain/your_password_login_endpoint

"> </div>

Send feedback

Except as otherwise noted, the content of this page is licensed under the

Creative Commons Attribution 4.0 License

, and code samples are licensed under the

Apache 2.0 License

. For details, see the

Google Developers Site Policies

. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]]
