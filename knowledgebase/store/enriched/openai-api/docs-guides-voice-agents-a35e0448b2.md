---
title: Voice agents | OpenAI API | CloudRaven Enrichment
source_url: https://developers.openai.com/api/docs/guides/voice-agents
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:27.700218+00:00
kind: enriched-doc
tags: openai, llm, responses-api, tools, agentic-doing
---

# Voice agents | OpenAI API | CloudRaven Enrichment

Source URL:

- https://developers.openai.com/api/docs/guides/voice-agents

Dependency:

- OpenAI API

Collection scope:

- Collect API docs and guides only.

What this page is useful for:

- Voice agents | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions Voice agents turn the same agent concepts into spoken, low-latency interactions.
- The key design choice is deciding whether the model should work directly with live audio or whether your application should explicitly chain speech-to-text, text reasoning, and text-to-speech.
- Choose the right architecture Architecture Best for Why Speech-to-speech with live audio sessions Natural, low-latency conversations The model handles live audio input and output directly Chained voice pipeline Predictable workflows or extending an existing text agent Your app keeps explicit control over transcription, text reasoning, and speech output Agent Builder doesn’t currently support voice workflows, so voice stays an SDK-first surface.
- Recommended starting points The two supported languages expose different strengths today: In TypeScript, the fastest path to a browser-based voice assistant is a RealtimeAgent and RealtimeSession .

CloudRaven applicability:

- Use this material when the project needs API-first intelligence layers for research, generation, orchestration, or structured outputs.

Prototype-to-production review:

- High fit for programmable AI workflows that must live inside a custom app or local toolchain.
- Always verify model and tool guidance in the current official docs before implementation.

CloudRaven example paths:

- Build a task researcher that produces structured outputs for downstream automation.
- Add a knowledge assistant that can summarize project artifacts and propose next actions.

Suggested retrieval tags:

- `openai`
- `llm`
- `responses-api`
- `tools`
- `agentic-doing`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/openai-api/docs-guides-voice-agents-a35e0448b2.md`
- Raw source: `knowledgebase/store/raw_html/openai-api/docs-guides-voice-agents-a35e0448b2.html`
