---
title: Manage delegates | Gmail | Google for Developers
source_url: https://developers.google.com/workspace/gmail/api/guides/delegate_settings
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:07.212062+00:00
kind: extracted-doc
---

# Manage delegates | Gmail | Google for Developers

Source URL:

- https://developers.google.com/workspace/gmail/api/guides/delegate_settings

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:21:07.212062+00:00

Direct links in scope:

- https://developers.google.com/workspace/gmail/api/guides/delegate_settings
- https://developers.google.com/workspace/gmail/api/guides
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.settings.delegates
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.settings.delegates/create
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.settings.delegates/list
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.settings.delegates/get
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.settings.delegates/delete

Captured summary:

- Manage delegates | Gmail | Google for Developers Skip to main content Workspace / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gmail Home Google Workspace Gmail Guides Send feedback Manage delegates Stay organized with collections Save and categorize content based on your preferences.
- This document explains how to delegate and collaborate on email using the Gmail API.
- A Gmail user can grant mailbox access to one or more users in the same Google Workspace organization.
- The user granting access is the delegator and the user receiving access is the delegate .
- Delegates can read, send, and delete email messages in your account.

Extracted text:

Manage delegates | Gmail | Google for Developers

Skip to main content

Workspace

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

Gmail

Home

Google Workspace

Gmail

Guides

Send feedback

Manage delegates

Stay organized with collections

Save and categorize content based on your preferences.

This document explains how to delegate and collaborate on email using the Gmail API.

A Gmail user can grant mailbox access to one or more users in the same Google Workspace organization. The user granting access is the

delegator

and the user receiving access is the

delegate

.

Delegates can read, send, and delete email messages in your account. They can also view and add contacts. When a delegate sends a message from your account, their email address appears. For more information, see

Delegate & collaborate on email

.

Google Workspace organizations can use the

settings.delegates

resource to manage delegates within Gmail accounts in their organization. This requires a

service account

that has been delegated with

domain-wide authority

.

A delegate user must be referred to by their primary email address and not an email alias. Gmail limits the number of delegates for each user in a Google Workspace organization to a maximum of 25 delegates.

The

settings.delegates

resource contains more information on how to

create

,

list

,

get

, or

delete

delegates.

The

settings.delegates

resource includes a

VerificationStatus

object to indicate if ownership of an email address is verified for delegation. When creating a delegate using the

settings.delegates.create

method, the

verificationStatus

field is set to

accepted

without sending a verification email.

Send feedback

Except as otherwise noted, the content of this page is licensed under the

Creative Commons Attribution 4.0 License

, and code samples are licensed under the

Apache 2.0 License

. For details, see the

Google Developers Site Policies

. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-01 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-01 UTC."],[],[]]
