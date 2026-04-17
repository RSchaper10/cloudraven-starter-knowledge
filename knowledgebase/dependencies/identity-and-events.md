# Identity and Events

This brief covers Google sign-in, Microsoft identity, inbox and calendar listeners, and Stripe eventing.

Related internal operating note:

- `knowledgebase/dependencies/important-outbound-email-considerations-for-marketing-outreach-dynamics.md`
- `knowledgebase/dependencies/aws-ses-inbound-email-and-s3.md`

## Google Identity Services

Role:

- Social sign-in for web applications.

Priority docs:

- https://developers.google.com/identity/gsi/web/guides/overview

Why it fits CloudRaven:

- Good for low-friction account creation and return visits in consumer-facing experiences.

Production cautions:

- use current Google Identity Services guidance rather than older Google Sign-In patterns
- account-linking and consent flows should be documented before mixing local auth and social auth

Suggested tags:

- `google`
- `social-sign-in`
- `auth`

## Gmail API and Google Calendar API

Role:

- mailbox and calendar integration with push-based update models.

Priority docs:

- https://developers.google.com/workspace/gmail/api/guides/push
- https://developers.google.com/workspace/calendar/api/guides/push

Why it fits CloudRaven:

- Supports assistant workflows, scheduling automation, and event-driven collaboration features.

Production cautions:

- webhooks and watch channels expire and require renewal logic
- scopes should be minimized and consent language should be explicit
- event listeners need idempotency and replay-safe handling

Suggested tags:

- `gmail`
- `calendar`
- `webhooks`
- `notifications`

## Amazon SES Email Receiving And S3 Delivery

Role:

- inbound email receiving, receipt-rule execution, and raw-email delivery into S3 for workflow automation

Priority docs:

- https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html
- https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-s3.html
- https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html

Why it fits CloudRaven:

- CloudRaven's workspace-agent ingress path uses SES receipt rules plus S3 delivery before the inbound email state machine begins.

Production cautions:

- SES validates S3 delivery permissions when the receipt rule is created, so CloudFormation ordering matters
- the bucket policy and, if present, KMS key policy must match the documented SES permission contract
- region, MX, verified identity, and active receipt-rule-set prerequisites are separate from app code and can fail a deploy even when the repo logic is correct

Suggested tags:

- `ses`
- `email-receiving`
- `s3`
- `receipt-rules`
- `aws-events`

## Microsoft Entra ID and Microsoft Graph Change Notifications

Role:

- Microsoft identity plus inbox and calendar event notifications for Microsoft 365 scenarios.

Priority docs:

- https://learn.microsoft.com/en-us/entra/identity-platform/
- https://learn.microsoft.com/en-us/graph/change-notifications-overview

Why it fits CloudRaven:

- Essential for B2B collaboration, enterprise sign-in, Outlook inbox automation, and calendar-aware workflows.

Production cautions:

- tenant type matters early because workforce and external tenant capabilities differ
- notification subscriptions have lifecycle and validation requirements
- enterprise identity projects need earlier environment and consent planning than consumer social auth

Suggested tags:

- `entra-id`
- `microsoft-graph`
- `outlook`
- `calendar`
- `enterprise-auth`

Operational note:

- Use `knowledgebase/dependencies/important-outbound-email-considerations-for-marketing-outreach-dynamics.md` when evaluating research outreach, staged drafts, deliverability behavior, or upsell language in Microsoft 365-adjacent workflows.

## Stripe and Stripe to AWS EventBridge

Role:

- billing and payment workflows, plus event delivery into AWS-native systems.

Priority docs:

- https://docs.stripe.com/api
- https://docs.stripe.com/payments/checkout
- https://docs.stripe.com/event-destinations/eventbridge

Why it fits CloudRaven:

- Supports monetization, subscription experiments, and event-driven back-office automation.

Production cautions:

- payment flows, entitlement rules, and webhook/event semantics must stay aligned
- EventBridge is powerful when Stripe events need to feed broader AWS workflows, not just a single webhook endpoint

Suggested tags:

- `stripe`
- `billing`
- `payments`
- `eventbridge`
- `aws-events`
