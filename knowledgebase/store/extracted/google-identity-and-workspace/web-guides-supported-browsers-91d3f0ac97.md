# Supported browsers and platforms | Web guides | Google for Developers

Source URL:

- https://developers.google.com/identity/gsi/web/guides/supported-browsers

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-15T19:44:43.529703+00:00

Direct links in scope:

- https://developers.google.com/identity/gsi/web/guides/supported-browsers
- https://developers.google.com/identity/gsi/web/guides/overview
- https://developers.google.com/identity/gsi/web/guides/display-button
- https://developers.google.com/identity/gsi/web/guides/itp
- https://developers.google.com/identity/gsi/web/guides/features
- https://developers.google.com/identity/gsi/web/guides/fedcm-migration
- https://developers.google.com/identity/gsi/web/reference/js-reference
- https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid

Captured summary:

- Supported browsers and platforms | Web guides | Google for Developers Skip to main content Identity Web guides / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Home Products Google Identity Web guides Sign in with Google for Web Send feedback Supported browsers and platforms Stay organized with collections Save and categorize content based on your preferences.
- Page Summary outlined_flag The JavaScript client library for Sign In With Google and Google One Tap is designed for most common browsers and platforms but has limitations and specific requirements for compatibility.
- Support for Sign In With Google and One Tap flows varies across browser and platform combinations, potentially affecting user experience due to features like ITP and FedCM.
- Google Identity Services supports the proposed FedCM API to enhance user privacy and security while aiming to minimize changes to existing websites.
- Enabling FedCM is recommended for new web apps, and migrating existing apps may be required for some sites to accommodate changes in browser-rendered dialogs and potential CSP/COOP issues.

Extracted text:

Supported browsers and platforms | Web guides | Google for Developers

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

Supported browsers and platforms

Stay organized with collections

Save and categorize content based on your preferences.

Page Summary

outlined_flag

The JavaScript client library for Sign In With Google and Google One Tap is designed for most common browsers and platforms but has limitations and specific requirements for compatibility.

Support for Sign In With Google and One Tap flows varies across browser and platform combinations, potentially affecting user experience due to features like ITP and FedCM.

Google Identity Services supports the proposed FedCM API to enhance user privacy and security while aiming to minimize changes to existing websites.

Enabling FedCM is recommended for new web apps, and migrating existing apps may be required for some sites to accommodate changes in browser-rendered dialogs and potential CSP/COOP issues.

The JavaScript client library for Sign In With Google and Google One Tap is designed to be compatible with most common browsers and platforms. It is not guaranteed to work on all browsers or platforms.

Due to security risks the JavaScript client library is only supported on the latest two versions of each browser.

Compatibility

Support for the Sign In With Google button and One Tap sign-in flows varies across browser and platform combinations.

The user experience may differ between browsers based upon availability of these features:

Intelligent Tracking Prevention

(ITP)

Federated Credentials Management API

(FedCM)

Supported sign-in flows and features are shown in the following tables. Not all browsers are available on all platforms, N/A means a supported browser is not available on the platform.

Sign In With Google

Browser / Platform

Android

iOS

*

macOS

Linux

Windows 10

Chrome

Edge

Firefox

Safari

N/A

N/A

N/A

*

Due to ITP

redirect mode

is required for iOS.

One Tap

Browser / Platform

Android

iOS

macOS

Linux

Windows 10

Chrome

†

*

Edge

*

†

Firefox

*

Safari

N/A

N/A

N/A

*

Extra configuration

is necessary to enable the

upgraded One Tap UX

for browsers that require ITP.

†

FedCM is available in Chrome 117 or later, see the MDN

Browser compatibility

chart for more information.

Third-party cookies

As a participant in the W3C

FedID

community group working on

FedCM

, Google Identity Services has been working to increase user privacy and security while also minimizing the changes to existing websites and preserving ease of use for our users. The GIS JavaScript library now supports the proposed FedCM API.

As of August 2023, Google Identity Services fully supports FedCM and recommends its use. Changes to

adopt FedCM

may be required for some existing web apps.

Recommended

Enable FedCM

for new web apps and

migrate

existing apps.

Not Recommended

Disabling FedCM.

As of August 2022, Google Identity Services has conducted a limited

FedCM origin trial

. Approximately 20 websites and 300K users successfully signed in using FedCM APIs and GIS.

We're pleased to say early feedback has demonstrated that for most websites, switching to a more private and secure sign-in process without third-party cookies can occur transparently through backward compatible updates to the existing GIS library.

Minimal to no changes to existing user flows and websites was required.

This is a critical point as widespread adoption of FedCM APIs relies on a trouble-free migration by existing websites.

Based upon this preliminary feedback, GIS plans to expand participation in testing GIS with FedCM.

During trials these issues were discovered and may require some web sites to take action when FedCM is adopted by GIS:

Browser rendered dialogs eliminate the existing ability for sites to use style attributes or intermediate iframes to control sign-in dialog positioning. This may obscure existing site content, some of which may be helpful or critical for users to see before signing in.

Although not yet widely deployed, some sites may use CSP and COOP. In these cases, sites may have to make

changes

to direct browsers to allow popups and to load cross-site resources.

Send feedback

Except as otherwise noted, the content of this page is licensed under the

Creative Commons Attribution 4.0 License

, and code samples are licensed under the

Apache 2.0 License

. For details, see the

Google Developers Site Policies

. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-10 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-10 UTC."],[],[]]
