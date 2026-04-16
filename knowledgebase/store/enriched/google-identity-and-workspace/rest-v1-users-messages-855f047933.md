---
title: REST Resource: users.messages | Gmail | Google for Developers | CloudRaven Enrichment
source_url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:11.923761+00:00
kind: enriched-doc
tags: google, auth, gmail, calendar, webhooks, notifications
---

# REST Resource: users.messages | Gmail | Google for Developers | CloudRaven Enrichment

Source URL:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages

Dependency:

- Google Identity and Workspace Events

Collection scope:

- Collect social sign-in plus Gmail and Calendar push event guidance.

What this page is useful for:

- REST Resource: users.messages | Gmail | Google for Developers Skip to main content Workspace / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gmail Home Google Workspace Gmail Reference Send feedback REST Resource: users.messages Stay organized with collections Save and categorize content based on your preferences.
- Resource: Message JSON representation MessagePart JSON representation Header JSON representation ClassificationLabelValue JSON representation ClassificationLabelFieldValue JSON representation Methods Resource: Message An email message.
- JSON representation { "id" : string , "threadId" : string , "labelIds" : [ string ] , "snippet" : string , "historyId" : string , "internalDate" : string , "payload" : { object ( MessagePart ) } , "sizeEstimate" : integer , "raw" : string , "classificationLabelValues" : [ { object ( ClassificationLabelValue ) } ] } Fields id string The immutable ID of the message.
- threadId string The ID of the thread the message belongs to.

CloudRaven applicability:

- Use this material for consumer sign-in and Google Workspace-driven notification workflows.

Prototype-to-production review:

- Strong fit for assistant workflows that need mailbox or calendar awareness.
- Watch channel renewal and scope management must be part of the design.

CloudRaven example paths:

- Link Google sign-in with inbox listeners to automate lead or support flows.
- Use calendar push channels to trigger follow-up actions around scheduling changes.

Suggested retrieval tags:

- `google`
- `auth`
- `gmail`
- `calendar`
- `webhooks`
- `notifications`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/google-identity-and-workspace/rest-v1-users-messages-855f047933.md`
- Raw source: `knowledgebase/store/raw_html/google-identity-and-workspace/rest-v1-users-messages-855f047933.html`
