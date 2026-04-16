---
title: Understand the One Tap user experience | Web guides | Google for Developers | CloudRaven Enrichment
source_url: https://developers.google.com/identity/gsi/web/guides/features
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:06.532123+00:00
kind: enriched-doc
tags: google, auth, gmail, calendar, webhooks, notifications
---

# Understand the One Tap user experience | Web guides | Google for Developers | CloudRaven Enrichment

Source URL:

- https://developers.google.com/identity/gsi/web/guides/features

Dependency:

- Google Identity and Workspace Events

Collection scope:

- Collect social sign-in plus Gmail and Calendar push event guidance.

What this page is useful for:

- Understand the One Tap user experience | Web guides | Google for Developers Skip to main content Identity Web guides / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Home Products Google Identity Web guides Sign in with Google for Web Send feedback Understand the One Tap user experience Stay organized with collections Save and categorize content based on your preferences.
- Page Summary outlined_flag Users can opt out of One Tap globally through their Google Account settings or by disabling third-party sign-in prompts in their browser settings.
- If a user manually closes the One Tap prompt, it will be suppressed for increasingly longer periods of time, unless FedCM is enabled in which case browser vendors may define their own cooldowns.
- On mobile browsers without FedCM enabled, Google One Tap will automatically close after 90 seconds if there is no user interaction.

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

- Extracted page: `knowledgebase/store/extracted/google-identity-and-workspace/web-guides-features-ca164e5630.md`
- Raw source: `knowledgebase/store/raw_html/google-identity-and-workspace/web-guides-features-ca164e5630.html`
