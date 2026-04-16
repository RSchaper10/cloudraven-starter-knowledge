---
title: Method: users.watch | Gmail | Google for Developers
source_url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users/watch
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:20:56.540890+00:00
kind: extracted-doc
---

# Method: users.watch | Gmail | Google for Developers

Source URL:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users/watch

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:20:56.540890+00:00

Direct links in scope:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users/watch
- https://developers.google.com/workspace/gmail/api/reference/rest
- https://developers.google.com/workspace/gmail/api/guides/push

Captured summary:

- Method: users.watch | Gmail | Google for Developers Skip to main content Workspace / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gmail Home Google Workspace Gmail Reference Send feedback Method: users.watch Stay organized with collections Save and categorize content based on your preferences.
- HTTP request Path parameters Request body JSON representation Response body JSON representation Authorization scopes LabelFilterAction Set up or update a push notification watch on the given user mailbox.
- For more information, see Configure push notifications in Gmail API .
- HTTP request POST https://gmail.googleapis.com/gmail/v1/users/{userId}/watch The URL uses gRPC Transcoding syntax.
- Path parameters Parameters userId string The user's email address.

Extracted text:

Method: users.watch | Gmail | Google for Developers

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

Method: users.watch

Stay organized with collections

Save and categorize content based on your preferences.

HTTP request

Path parameters

Request body

JSON representation

Response body

JSON representation

Authorization scopes

LabelFilterAction

Set up or update a push notification watch on the given user mailbox. For more information, see

Configure push notifications in Gmail API

.

HTTP request

POST https://gmail.googleapis.com/gmail/v1/users/{userId}/watch

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

The request body contains data with the following structure:

JSON representation

{

"labelIds"

:

[

string

]

,

"labelFilterAction"

:

enum (

LabelFilterAction

)

,

"labelFilterBehavior"

:

enum (

LabelFilterAction

)

,

"topicName"

:

string

}

Fields

labelIds[]

string

List of labelIds to restrict notifications about. By default, if unspecified, all changes are pushed out. If specified then dictates which labels are required for a push notification to be generated.

labelFilterAction

(deprecated)

enum (

LabelFilterAction

)

Filtering behavior of

labelIds list

specified. This field is deprecated because it caused incorrect behavior in some cases; use

labelFilterBehavior

instead.

labelFilterBehavior

enum (

LabelFilterAction

)

Filtering behavior of

labelIds list

specified. This field replaces

labelFilterAction

; if set,

labelFilterAction

is ignored.

topicName

string

A fully qualified Google Cloud Pub/Sub API topic name to publish the events to. This topic name

must

already exist in Cloud Pub/Sub and you

must

have already granted gmail "publish" permission on it. For example, "projects/my-project-identifier/topics/my-topic-name" (using the Cloud Pub/Sub "v1" topic naming format).

Note that the "my-project-identifier" portion must exactly match your Google developer project id (the one executing this watch request).

Response body

Push notification watch response.

If successful, the response body contains data with the following structure:

JSON representation

{

"historyId"

:

string

,

"expiration"

:

string

}

Fields

historyId

string

The ID of the mailbox's current history record.

expiration

string (

int64

format)

When Gmail will stop sending notifications for mailbox updates (epoch millis). Call

watch

again before this time to renew the watch.

Authorization scopes

Requires one of the following OAuth scopes:

https://mail.google.com/

https://www.googleapis.com/auth/gmail.modify

https://www.googleapis.com/auth/gmail.readonly

https://www.googleapis.com/auth/gmail.metadata

For more information, see the

Authorization guide

.

LabelFilterAction

Filtering behavior of labelIds list specified.

Enums

include

Only get push notifications for message changes relating to labelIds specified.

exclude

Get push notifications for all message changes except those relating to labelIds specified.

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
