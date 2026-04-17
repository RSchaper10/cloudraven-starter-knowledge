# Dependency Manifest

This is the starter collection manifest for the current CloudRaven dependency set.

Collection date:

- April 15, 2026

Status legend:

- `seeded`
- `curated`
- `ready-for-agent-use`

## Foundation Stack

| Dependency | Role | Status | Official entry points |
| --- | --- | --- | --- |
| Next.js App Router | server-first route boundaries, route handlers, and data-fetching runtime for the app | seeded | https://nextjs.org/docs/app ; https://nextjs.org/docs/app/building-your-application/routing/route-handlers |
| AWS Amplify Gen 2 for Next.js | backend, auth, data, storage foundation for App Router projects | ready-for-agent-use | https://docs.amplify.aws/nextjs/ ; https://docs.amplify.aws/nextjs/build-a-backend/auth/grant-access-to-auth-resources/ ; https://docs.amplify.aws/nextjs/build-a-backend/storage/set-up-storage/ |
| AWS SDK for JavaScript v3 | direct service clients for handlers, orchestration, secrets, mail, and storage | seeded | https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-nodejs.html ; https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_sfn_code_examples.html |
| AWS CDK v2 | backend assembly, IAM wiring, and workflow infrastructure customization | seeded | https://docs.aws.amazon.com/cdk/v2/guide/home.html ; https://docs.aws.amazon.com/cdk/v2/guide/work-with-stepfunctions.html |
| HeroUI React | design system and component primitives | curated | https://heroui.com/docs/guide/introduction ; https://heroui.com/docs/guide/installation |
| Tailwind CSS | utility-first styling foundation | curated | https://tailwindcss.com/docs/installation/framework-guides/nextjs ; https://tailwindcss.com/docs/styling-with-utility-classes |
| Iconify React | repo-wide icon system for the marketing site and workspace UI | seeded | https://iconify.design/docs/icon-components/react/ |

## AI and Media

| Dependency | Role | Status | Official entry points |
| --- | --- | --- | --- |
| OpenAI API | models, Responses API, tools, research and agent capabilities through API use | ready-for-agent-use | https://developers.openai.com/api/docs/quickstart ; https://developers.openai.com/api/docs/models ; https://developers.openai.com/api/docs/guides/tools |
| ElevenLabs API | speech, voice, and conversational audio workflows | curated | https://elevenlabs.io/docs/quickstart ; https://elevenlabs.io/docs/api-reference/introduction |
| Pexels API | stock photo and video retrieval, not native image generation | curated | https://www.pexels.com/api/documentation/ |

## Identity, Messaging, and Eventing

| Dependency | Role | Status | Official entry points |
| --- | --- | --- | --- |
| Google Identity Services | social sign-in for web | curated | https://developers.google.com/identity/gsi/web/guides/overview |
| Gmail API | mailbox integration and push notifications | curated | https://developers.google.com/workspace/gmail/api/guides/push |
| Google Calendar API | calendar integration and watch channels | curated | https://developers.google.com/workspace/calendar/api/guides/push |
| Amazon SES email receiving and S3 delivery | inbound email receipt rules, S3 delivery, and permissions for workspace-agent ingress | curated | https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html ; https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-s3.html ; https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html |
| Microsoft Entra ID | Microsoft identity for workforce or external tenants | seeded | https://learn.microsoft.com/en-us/entra/identity-platform/ |
| Microsoft Graph change notifications | inbox and calendar webhooks for Microsoft 365 | seeded | https://learn.microsoft.com/en-us/graph/change-notifications-overview |
| HubSpot Developer Platform | OAuth, mailbox connection, and transactional delivery workflows | seeded | https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/oauth ; https://developers.hubspot.com/docs/api-reference/marketing-transactional-single-send-v3/guide |
| Outbound email considerations for marketing outreach dynamics | internal operational guidance for research outreach, staged sending, deliverability risk, and restrained upsell behavior | curated | internal brief: `knowledgebase/dependencies/important-outbound-email-considerations-for-marketing-outreach-dynamics.md` |
| Stripe API | billing, subscriptions, checkout, payments | curated | https://docs.stripe.com/api ; https://docs.stripe.com/payments/checkout |
| Stripe Event Destinations to AWS EventBridge | event routing into AWS workflows | seeded | https://docs.stripe.com/event-destinations/eventbridge |

## Spatial, Visualization, and Rich UI

| Dependency | Role | Status | Official entry points |
| --- | --- | --- | --- |
| MapLibre GL JS | open-source web mapping | curated | https://maplibre.org/maplibre-gl-js/docs/API/ ; https://maplibre.org/maplibre-gl-js/docs/examples/ |
| react-map-gl | React wrapper used for controlled map surfaces in the workspace UI | seeded | https://visgl.github.io/react-map-gl/docs ; https://visgl.github.io/react-map-gl/docs/api-reference/maplibre/map |
| Apache ECharts | charting and dashboards | seeded | https://echarts.apache.org/handbook/en/get-started/ |
| Three.js | 3D rendering for web experiences | curated | https://threejs.org/docs/ ; https://threejs.org/manual/en/creating-a-scene.html |

## Publishing And Artifact Automation

| Dependency | Role | Status | Official entry points |
| --- | --- | --- | --- |
| Markdown publishing stack | frontmatter parsing, rendering, TOC, anchors, and syntax-highlighting for blog content | curated | internal brief: `knowledgebase/dependencies/content-publishing-and-markdown.md` |
| PptxGenJS | editable deck generation for slide and briefing workflows | seeded | https://gitbrent.github.io/PptxGenJS/docs/introduction/ ; https://gitbrent.github.io/PptxGenJS/docs/api-text/ |
| Sharp | deterministic image composition and export for generated collateral | seeded | https://sharp.pixelplumbing.com/ ; https://sharp.pixelplumbing.com/api-composite/ |
| Artifact automation helper stack | supporting packages for text layout, QR generation, syntax rendering, and canvas-based asset workflows | curated | internal brief: `knowledgebase/dependencies/artifact-automation-and-print.md` |

## Collection Priorities

Priority 1:

- Amplify Gen 2 with Next.js App Router
- OpenAI API
- Identity and eventing flows
- Stripe plus EventBridge

Priority 2:

- HeroUI
- Tailwind
- ElevenLabs
- MapLibre

Priority 3:

- ECharts
- Three.js
- Pexels

## Notes

- The current manifest is intentionally narrow and official-doc-first.
- Several URLs are broad entry points because those ecosystems are large and should be narrowed per feature request.
- Pexels is best treated as a licensed media source, not as an image generation provider.
