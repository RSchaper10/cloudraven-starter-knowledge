---
title: Method: users.labels.list | Gmail | Google for Developers
source_url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels/list
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:19.097726+00:00
kind: extracted-doc
---

# Method: users.labels.list | Gmail | Google for Developers

Source URL:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels/list

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:21:19.097726+00:00

Direct links in scope:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels/list
- https://developers.google.com/workspace/gmail/api/reference/rest
- https://developers.google.com/workspace/gmail/api/guides/labels
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.labels
- https://developers.google.com/workspace/gmail/api/v1/reference/users/labels/get

Captured summary:

- Method: users.labels.list | Gmail | Google for Developers Skip to main content Workspace / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gmail Home Google Workspace Gmail Reference Send feedback Method: users.labels.list Stay organized with collections Save and categorize content based on your preferences.
- HTTP request Path parameters Request body Response body JSON representation Authorization scopes Try it!
- For more information, see Manage labels .
- HTTP request GET https://gmail.googleapis.com/gmail/v1/users/{userId}/labels The URL uses gRPC Transcoding syntax.
- Path parameters Parameters userId string The user's email address.

Extracted text:

Method: users.labels.list | Gmail | Google for Developers

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

Method: users.labels.list

Stay organized with collections

Save and categorize content based on your preferences.

HTTP request

Path parameters

Request body

Response body

JSON representation

Authorization scopes

Try it!

Lists all labels in the user's mailbox. For more information, see

Manage labels

.

HTTP request

GET https://gmail.googleapis.com/gmail/v1/users/{userId}/labels

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

Request body

The request body must be empty.

Response body

If successful, the response body contains data with the following structure:

JSON representation

{

"labels"

:

[

{

object (

Label

)

}

]

}

Fields

labels[]

object (

Label

)

List of labels. Note that each label resource only contains an

id

,

name

,

messageListVisibility

,

labelListVisibility

, and

type

. The

labels.get

method can fetch additional label details.

Authorization scopes

Requires one of the following OAuth scopes:

https://mail.google.com/

https://www.googleapis.com/auth/gmail.modify

https://www.googleapis.com/auth/gmail.readonly

https://www.googleapis.com/auth/gmail.labels

https://www.googleapis.com/auth/gmail.metadata

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
