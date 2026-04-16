---
title: REST Resource: users.drafts | Gmail | Google for Developers
source_url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:08.157747+00:00
kind: extracted-doc
---

# REST Resource: users.drafts | Gmail | Google for Developers

Source URL:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:21:08.157747+00:00

Direct links in scope:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts
- https://developers.google.com/workspace/gmail/api/reference/rest
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts/create
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts/delete
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts/get
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts/list
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts/send
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts/update

Captured summary:

- REST Resource: users.drafts | Gmail | Google for Developers Skip to main content Workspace / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gmail Home Google Workspace Gmail Reference Send feedback REST Resource: users.drafts Stay organized with collections Save and categorize content based on your preferences.
- Resource: Draft JSON representation Methods Resource: Draft A draft email in the user's mailbox.
- JSON representation { "id" : string , "message" : { object ( Message ) } } Fields id string The immutable ID of the draft.
- message object ( Message ) The message content of the draft.
- Methods create Creates a draft with the DRAFT label.

Extracted text:

REST Resource: users.drafts | Gmail | Google for Developers

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

REST Resource: users.drafts

Stay organized with collections

Save and categorize content based on your preferences.

Resource: Draft

JSON representation

Methods

Resource: Draft

A draft email in the user's mailbox.

JSON representation

{

"id"

:

string

,

"message"

:

{

object (

Message

)

}

}

Fields

id

string

The immutable ID of the draft.

message

object (

Message

)

The message content of the draft.

Methods

create

Creates a draft with the

DRAFT

label.

delete

Immediately and permanently deletes the specified draft.

get

Gets the specified draft.

list

Lists the drafts in the user's mailbox.

send

Sends the specified, existing draft to the recipients in the

To

,

Cc

, and

Bcc

headers.

update

Replaces a draft's content.

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
