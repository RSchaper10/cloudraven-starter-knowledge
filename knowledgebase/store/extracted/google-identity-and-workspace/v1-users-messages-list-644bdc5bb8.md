---
title: Method: users.messages.list | Gmail | Google for Developers
source_url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:26.984679+00:00
kind: extracted-doc
---

# Method: users.messages.list | Gmail | Google for Developers

Source URL:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:21:26.984679+00:00

Direct links in scope:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- https://developers.google.com/workspace/gmail/api/reference/rest
- https://developers.google.com/workspace/gmail/api/guides/list-messages
- https://developers.google.com/workspace/gmail/api/guides/labels
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages
- https://developers.google.com/workspace/gmail/api/v1/reference/users/messages/get

Captured summary:

- Method: users.messages.list | Gmail | Google for Developers Skip to main content Workspace / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gmail Home Google Workspace Gmail Reference Send feedback Method: users.messages.list Stay organized with collections Save and categorize content based on your preferences.
- HTTP request Path parameters Query parameters Request body Response body JSON representation Authorization scopes Try it!
- Lists the messages in the user's mailbox.
- For more information, see List Gmail messages .
- HTTP request GET https://gmail.googleapis.com/gmail/v1/users/{userId}/messages The URL uses gRPC Transcoding syntax.

Extracted text:

Method: users.messages.list | Gmail | Google for Developers

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

Method: users.messages.list

Stay organized with collections

Save and categorize content based on your preferences.

HTTP request

Path parameters

Query parameters

Request body

Response body

JSON representation

Authorization scopes

Try it!

Lists the messages in the user's mailbox. For more information, see

List Gmail messages

.

HTTP request

GET https://gmail.googleapis.com/gmail/v1/users/{userId}/messages

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

Query parameters

Parameters

maxResults

integer (

uint32

format)

Maximum number of messages to return. This field defaults to 100. The maximum allowed value for this field is 500.

pageToken

string

Page token to retrieve a specific page of results in the list.

q

string

Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example,

"from:someuser@example.com rfc822msgid:<somemsgid@example.com> is:unread"

. Parameter cannot be used when accessing the api using the gmail.metadata scope.

labelIds[]

string

Only return messages with labels that match all of the specified label IDs. Messages in a thread might have labels that other messages in the same thread don't have. To learn more, see

Manage labels on messages and threads

.

includeSpamTrash

boolean

Include messages from

SPAM

and

TRASH

in the results.

Request body

The request body must be empty.

Response body

If successful, the response body contains data with the following structure:

JSON representation

{

"messages"

:

[

{

object (

Message

)

}

]

,

"nextPageToken"

:

string

,

"resultSizeEstimate"

:

integer

}

Fields

messages[]

object (

Message

)

List of messages. Note that each message resource contains only an

id

and a

threadId

. Additional message details can be fetched using the

messages.get

method.

nextPageToken

string

Token to retrieve the next page of results in the list.

resultSizeEstimate

integer (

uint32

format)

Estimated total number of results.

Authorization scopes

Requires one of the following OAuth scopes:

https://mail.google.com/

https://www.googleapis.com/auth/gmail.modify

https://www.googleapis.com/auth/gmail.readonly

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
