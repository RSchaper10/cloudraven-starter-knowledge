---
title: Method: users.messages.modify | Gmail | Google for Developers
source_url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/modify
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:26.160767+00:00
kind: extracted-doc
---

# Method: users.messages.modify | Gmail | Google for Developers

Source URL:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/modify

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:21:26.160767+00:00

Direct links in scope:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/modify
- https://developers.google.com/workspace/gmail/api/reference/rest
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages

Captured summary:

- Method: users.messages.modify | Gmail | Google for Developers Skip to main content Workspace / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gmail Home Google Workspace Gmail Reference Send feedback Method: users.messages.modify Stay organized with collections Save and categorize content based on your preferences.
- HTTP request Path parameters Request body JSON representation Response body Authorization scopes Try it!
- Modifies the labels on the specified message.
- HTTP request POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify The URL uses gRPC Transcoding syntax.
- Path parameters Parameters userId string The user's email address.

Extracted text:

Method: users.messages.modify | Gmail | Google for Developers

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

Reference

Send feedback

Method: users.messages.modify

Stay organized with collections

Save and categorize content based on your preferences.

HTTP request

Path parameters

Request body

JSON representation

Response body

Authorization scopes

Try it!

Modifies the labels on the specified message.

HTTP request

POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}/modify

The URL uses

gRPC Transcoding

syntax.

Path parameters

Parameters

userId

string

The user's email address. The special value

me

can be used to indicate the authenticated user.

id

string

The ID of the message to modify.

Request body

The request body contains data with the following structure:

JSON representation

{

"addLabelIds"

:

[

string

]

,

"removeLabelIds"

:

[

string

]

}

Fields

addLabelIds[]

string

A list of IDs of labels to add to this message. You can add up to 100 labels with each update.

removeLabelIds[]

string

A list IDs of labels to remove from this message. You can remove up to 100 labels with each update.

Response body

If successful, the response body contains an instance of

Message

.

Authorization scopes

Requires one of the following OAuth scopes:

https://mail.google.com/

https://www.googleapis.com/auth/gmail.modify

For more information, see the

Authorization guide

.

Send feedback

Except as otherwise noted, the content of this page is licensed under the

Creative Commons Attribution 4.0 License

, and code samples are licensed under the

Apache 2.0 License

. For details, see the

Google Developers Site Policies

. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-15 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-15 UTC."],[],[]]
