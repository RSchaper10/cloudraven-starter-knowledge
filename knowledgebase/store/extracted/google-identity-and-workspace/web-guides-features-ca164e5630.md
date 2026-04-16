---
title: Understand the One Tap user experience | Web guides | Google for Developers
source_url: https://developers.google.com/identity/gsi/web/guides/features
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:06.532123+00:00
kind: extracted-doc
---

# Understand the One Tap user experience | Web guides | Google for Developers

Source URL:

- https://developers.google.com/identity/gsi/web/guides/features

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:21:06.532123+00:00

Direct links in scope:

- https://developers.google.com/identity/gsi/web/guides/features
- https://developers.google.com/identity/gsi/web/guides/overview
- https://developers.google.com/identity/gsi/web/reference/html-reference
- https://developers.google.com/identity/gsi/web/guides/itp

Captured summary:

- Understand the One Tap user experience | Web guides | Google for Developers Skip to main content Identity Web guides / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Home Products Google Identity Web guides Sign in with Google for Web Send feedback Understand the One Tap user experience Stay organized with collections Save and categorize content based on your preferences.
- Page Summary outlined_flag Users can opt out of One Tap globally through their Google Account settings or by disabling third-party sign-in prompts in their browser settings.
- If a user manually closes the One Tap prompt, it will be suppressed for increasingly longer periods of time, unless FedCM is enabled in which case browser vendors may define their own cooldowns.
- On mobile browsers without FedCM enabled, Google One Tap will automatically close after 90 seconds if there is no user interaction.
- For browsers that don't support security measures or if the dialog is covered, a pop-up window will be displayed to request user consent for account creation to ensure they understand the action.

Extracted text:

Understand the One Tap user experience | Web guides | Google for Developers

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

Understand the One Tap user experience

Stay organized with collections

Save and categorize content based on your preferences.

Page Summary

outlined_flag

Users can opt out of One Tap globally through their Google Account settings or by disabling third-party sign-in prompts in their browser settings.

If a user manually closes the One Tap prompt, it will be suppressed for increasingly longer periods of time, unless FedCM is enabled in which case browser vendors may define their own cooldowns.

On mobile browsers without FedCM enabled, Google One Tap will automatically close after 90 seconds if there is no user interaction.

For browsers that don't support security measures or if the dialog is covered, a pop-up window will be displayed to request user consent for account creation to ensure they understand the action.

Due to Intelligent Tracking Prevention (ITP) in certain browsers like Safari and Firefox, a different One Tap user experience is provided, often starting with a welcome page and opening a pop-up window for the sign-in process.

This guide contains detailed descriptions of the One Tap user experience, including when One Tap is or is not displayed and user session behaviors.

Globally opt out

Users can opt out of One Tap if they disable the Google Account sign-in prompts flag in the

Apps with access to your account

page. The opted-out sessions aren't shown in One Tap. If all Google sessions are opted out, One Tap doesn't display.

If a user disables third-party sign-in on browsers with

FedCM enabled

, One Tap is not displayed. In Chrome settings under the Privacy and Security section users control the display of

third-party sign-in

prompts either globally or for individual sites.

Exponential cooldown

If the user closes the One Tap prompt manually, the One Tap prompt is suppressed. A user closes One Tap when they tap

Close

close

in the top-right corner of the prompt, after which One Tap wouldn't display in the same browser or the last website visited for a period of time.

The following exponential time periods are used for cooldowns when FedCM is

not

enabled:

Consecutive times closed

Time period that One Tap is disabled

1

Two hours

2

One day

3

One week

4+

Four weeks

The cooldown status resets after a successful sign-in using One Tap or the Sign in with Google button.

When FedCM is enabled, browser vendors may define their own, different, cooldown time periods.

Auto-dismissal on mobile browsers

On

mobile

browsers, and when FedCM is not enabled, Google One Tap closes automatically after a short time period unless the user directly interacts with the One Tap UI.

The threshold for auto-dismissal is 90 seconds. This is subject to change.

Show a dialog to prevent unintended clicks

One Tap now comes with different security measures to enforce the integrity of the dialog, but some browsers don't support these capabilities. Unsupported browsers include non-Chromium-based ones or those before v75. In these cases, or if the dialog is covered with other content, a pop-up window is displayed that requests the user's consent to create an account.

Upgraded UX on ITP browsers

Due to

Intelligent Tracking Prevention

(ITP), the normal One Tap UX doesn't work on Chrome on iOS, Safari, or Firefox. A different UX is provided instead on these browsers. You have the option to disable this UX on ITP browsers by setting the

data-itp_support

attribute.

The upgraded One Tap UX on ITP browsers begins with a welcome page as shown below. After the user selects Continue, a pop-up window is opened. The UX in the pop-up window is very similar to normal One Tap.

When there is no Google session, after the 'Continue' button is clicked, users must first sign in to their Google Account. See

One Tap support on ITP browsers

for more details.

Key user journeys

The user journeys vary based on the following statuses.

Session status on Google websites. The following terms are used to indicate different Google session status when the user journey starts.

Single-session: There is exactly one active session on Google websites.

Multiple-session: There are more than one active sessions on Google websites.

Whether the selected Google Account has approved your website when the user journey starts. The following terms are used to indicate different approval status.

New user: The selected account hasn't approved your website.

Returning user: The selected account has approved your website before.

Single-session new user journey

The new user consent page.

The second confirmation dialog in a pop-up window for non-Chromium browsers.

After users confirm, an ID token is shared with your website.

Single-session returning user journey

The returning user page.

After users click the button, an ID token is shared with your website.

Multiple-session new user journey

The account chooser page.

The consent page.

For non-Chromium browsers, this confirmation dialog is displayed in a pop-up window:

After user consent, an ID token is shared with your website.

Multiple-session returning user journey

The account chooser page.

After users select a returning account, an ID token is shared with your website.

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
