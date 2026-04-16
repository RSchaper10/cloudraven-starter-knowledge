---
title: Text generation | OpenAI API | CloudRaven Enrichment
source_url: https://developers.openai.com/api/docs/guides/text
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:16.527664+00:00
kind: enriched-doc
tags: openai, llm, responses-api, tools, agentic-doing
---

# Text generation | OpenAI API | CloudRaven Enrichment

Source URL:

- https://developers.openai.com/api/docs/guides/text

Dependency:

- OpenAI API

Collection scope:

- Collect API docs and guides only.

What this page is useful for:

- Text generation | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions With the OpenAI API, you can use a large language model to generate text from a prompt, as you might using ChatGPT .
- Models can generate almost any kind of text response—like code, mathematical equations, structured JSON data, or human-like prose.
- Use the Responses API for direct model requests like this text-generation call.
- Generate text from a simple prompt javascript 1 2 3 4 5 6 7 8 9 import OpenAI from "openai" ; const client = new OpenAI(); const response = await client.responses.create({ model : "gpt-5.4" , input : "Write a one-sentence bedtime story about a unicorn." }); console .log(response.output_text); 1 2 3 4 5 6 7 8 9 from openai import OpenAI client = OpenAI() response = client.responses.create( model= "gpt-5.4" , input = "Write a one-sentence bedtime story about a unicorn." ) print (response.output_text) 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 using System; using System.Threading.Tasks; using OpenAI; class Program { static async Task Main ( ) { var client = new OpenAIClient( Environment.GetEnvironmentVariable( "OPENAI_API_KEY" ) ); var response = await client.Responses.CreateAsync( new ResponseCreateRequest { Model = "gpt-5.4" , Input = "Say 'this is a test.'" }); Console.WriteLine( $"[ASSISTANT]: {response.OutputText()} " ); } } 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 import com.openai.client.OpenAIClient; import com.openai.client.okhttp.OpenAIOkHttpClient; import com.openai.models.responses.Response; import com.openai.models.responses.ResponseCreateParams; public class Main { public static void main (String[] args) { OpenAIClient client = OpenAIOkHttpClient.fromEnv(); ResponseCreateParams params = ResponseCreateParams.builder() .input( "Say this is a test" ) .model( "gpt-5.4" ) .build(); Response response = client.responses().create(params); System.out.println(response.outputText()); } } 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 package main import ( "context" "fmt" "github.com/openai/openai-go/v3" "github.com/openai/openai-go/v3/option" "github.com/openai/openai-go/v3/responses" ) func main () { client := openai.NewClient( option.WithAPIKey( "My API Key" ), // or set OPENAI_API_KEY in your env ) resp, err := client.Responses.New(context.TODO(), openai.ResponseNewParams{ Model: "gpt-5.4" , Input: responses.ResponseNewParamsInputUnion{OfString: openai.String( "Say this is a test" )}, }) if err != nil { panic (err.Error()) } fmt.Println(resp.OutputText()) } 1 2 3 4 5 6 7 curl "https://api.openai.com/v1/responses" \ -H "Content-Type: application/json" \ -H "Authorization: Bearer $OPENAI_API_KEY " \ -d '{ "model": "gpt-5.4", "input": "Write a one-sentence bedtime story about a unicorn." }' An array of content generated by the model is in the output property of the response.

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

- Extracted page: `knowledgebase/store/extracted/openai-api/docs-guides-text-2bf0a925bd.md`
- Raw source: `knowledgebase/store/raw_html/openai-api/docs-guides-text-2bf0a925bd.html`
