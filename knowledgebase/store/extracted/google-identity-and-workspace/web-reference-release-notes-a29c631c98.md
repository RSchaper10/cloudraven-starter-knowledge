---
title: Sign In With Google Release Notes | Web guides | Google for Developers
source_url: https://developers.google.com/identity/gsi/web/reference/release-notes
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:05.244368+00:00
kind: extracted-doc
---

# Sign In With Google Release Notes | Web guides | Google for Developers

Source URL:

- https://developers.google.com/identity/gsi/web/reference/release-notes

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:21:05.244368+00:00

Direct links in scope:

- https://developers.google.com/identity/gsi/web/reference/release-notes
- https://developers.google.com/identity/gsi/web/guides/overview
- https://developers.google.com/identity/gsi/web/guides/personalized-button
- https://developers.google.com/identity/gsi/web/guides/supported-browsers
- https://developers.google.com/identity/gsi/web/amp/amp
- https://developers.google.com/identity/gsi/web/guides/features

Captured summary:

- Sign In With Google Release Notes | Web guides | Google for Developers Skip to main content Identity Web guides / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Home Products Google Identity Web guides Sign in with Google for Web Send feedback Sign In With Google Release Notes Stay organized with collections Save and categorize content based on your preferences.
- Page Summary outlined_flag Recent updates to the Sign in with Google button support Federated Credential Management (FedCM), Family Link, and adhere to Google Workspace policies.
- Federated Credential Management (FedCM) Beta launched for Google Identity Services, with updates to the automatic sign-in flow UX in Chrome M121 to reduce disruption to conversion rates before third-party cookie restrictions are fully implemented.
- The Federated Credential Management API (FedCM) is now supported, while Accelerated Mobile Pages (AMP) is unsupported when FedCM is enabled.
- One Tap UX on ITP browsers and the Sign In With Google button are supported features.

Extracted text:

Sign In With Google Release Notes | Web guides | Google for Developers

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

Sign In With Google Release Notes

Stay organized with collections

Save and categorize content based on your preferences.

Page Summary

outlined_flag

Recent updates to the Sign in with Google button support Federated Credential Management (FedCM), Family Link, and adhere to Google Workspace policies.

Federated Credential Management (FedCM) Beta launched for Google Identity Services, with updates to the automatic sign-in flow UX in Chrome M121 to reduce disruption to conversion rates before third-party cookie restrictions are fully implemented.

The Federated Credential Management API (FedCM) is now supported, while Accelerated Mobile Pages (AMP) is unsupported when FedCM is enabled.

One Tap UX on ITP browsers and the Sign In With Google button are supported features.

This page contains a list of the new features and significant changes to the Google Identity Services JavaScript library.

2025-03-17

Sign in with Google button

supports

Federated Credential Management (FedCM)

and adhere to

Google Workspace

policies set by the organization's administrator.

2024-12-01

Sign in with Google button

supports

Family Link

and adhere to

Google Workspace

policies set by the organization's administrator.

2023-12-21

Federated Credential Management (FedCM) Beta

for Google Identity Services was launched in August 2023. Many developers tested the API and have provided valuable feedback.

One response Google heard from developers is about the FedCM automatic sign-in flow user gesture requirement. For improved privacy, Chrome requires users to reconfirm that they want to sign in to the website with Google Account in each Chrome instance even if the user approved the website prior to the FedCM rollout. This one-time reconfirmation is achieved through a single click of the One Tap prompt to demonstrate user intent to sign-in. This change may cause an initial disruption in automatic sign-in conversion rates for some websites.

Recently in M121, Chrome made a

change

to the FedCM automatic sign-in flow UX. The reconfirmation is only required when third-party cookies are restricted. This means:

Before third-party cookie restrictions are ramped up to 100% (see Privacy Sandbox

News and Update

page for latest timeline), FedCM automatic sign-in does not require reconfirmation for returning users. If users reconfirm with FedCM UI, this reconfirmation will count toward the user gesture requirement.

FedCM automatic sign-in will check the confirmation status when the third-party cookies are manually restricted by users today, or by default in future Chrome.

With this change, we recommend all automatic sign-in developers migrate to FedCM as soon as possible, to reduce disruption to automatic sign-in conversion rates.

For the automatic sign-in flow, GIS JavaScript won't trigger FedCM on an older Chrome (before M121), even if your website chooses to opt-in to FedCM.

2023-08-15

Added

support

for the Federated Credential Management API (FedCM).

Accelerated Mobile Pages

is unsupported. AMP is not available when FedCM is enabled.

2022-04-12

Upgraded One Tap UX on ITP browsers

is supported.

2021-4-13

Sign In With Google button

is supported.

2021-03-17

Accelerated Mobile Pages

is supported.

2020-3-24

Exponential Cool Down

is supported.

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
