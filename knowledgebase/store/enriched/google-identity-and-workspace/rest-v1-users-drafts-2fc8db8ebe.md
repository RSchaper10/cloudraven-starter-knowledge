---
title: REST Resource: users.drafts | Gmail | Google for Developers | CloudRaven Enrichment
source_url: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:08.157747+00:00
kind: enriched-doc
tags: google, auth, gmail, calendar, webhooks, notifications
---

# REST Resource: users.drafts | Gmail | Google for Developers | CloudRaven Enrichment

Source URL:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.drafts

Dependency:

- Google Identity and Workspace Events

Collection scope:

- Collect social sign-in plus Gmail and Calendar push event guidance.

What this page is useful for:

- REST Resource: users.drafts | Gmail | Google for Developers Skip to main content Workspace / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Gmail Home Google Workspace Gmail Reference Send feedback REST Resource: users.drafts Stay organized with collections Save and categorize content based on your preferences.
- Resource: Draft JSON representation Methods Resource: Draft A draft email in the user's mailbox.
- JSON representation { "id" : string , "message" : { object ( Message ) } } Fields id string The immutable ID of the draft.
- message object ( Message ) The message content of the draft.

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

- Extracted page: `knowledgebase/store/extracted/google-identity-and-workspace/rest-v1-users-drafts-2fc8db8ebe.md`
- Raw source: `knowledgebase/store/raw_html/google-identity-and-workspace/rest-v1-users-drafts-2fc8db8ebe.html`
