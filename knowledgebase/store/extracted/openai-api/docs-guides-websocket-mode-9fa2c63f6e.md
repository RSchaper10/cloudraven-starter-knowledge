---
title: WebSocket Mode | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/websocket-mode
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:42.741601+00:00
kind: extracted-doc
---

# WebSocket Mode | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/websocket-mode

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:42.741601+00:00

Direct links in scope:

- https://developers.openai.com/api/docs/quickstart
- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/pricing
- https://developers.openai.com/api/docs/libraries
- https://developers.openai.com/api/docs/guides/latest-model
- https://developers.openai.com/api/docs/guides/prompt-guidance
- https://developers.openai.com/api/docs/guides/text
- https://developers.openai.com/api/docs/guides/code-generation
- https://developers.openai.com/api/docs/guides/images-vision
- https://developers.openai.com/api/docs/guides/audio
- https://developers.openai.com/api/docs/guides/structured-outputs
- https://developers.openai.com/api/docs/guides/function-calling
- https://developers.openai.com/api/docs/guides/migrate-to-responses
- https://developers.openai.com/api/docs/guides/tools
- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents/quickstart
- https://developers.openai.com/api/docs/guides/agents/define-agents
- https://developers.openai.com/api/docs/guides/agents/models
- https://developers.openai.com/api/docs/guides/agents/running-agents
- https://developers.openai.com/api/docs/guides/agents/sandboxes

Captured summary:

- WebSocket Mode | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions The Responses API supports a WebSocket mode for long-running, tool-call-heavy workflows.
- In this mode, you keep a persistent connection to /v1/responses and continue each turn by sending only new input items plus previous_response_id .
- WebSocket mode is compatible with both Zero Data Retention (ZDR) and store=false .
- Why use WebSocket mode WebSocket mode is most useful when a workflow involves many model-tool round trips (for example, agentic coding or orchestration loops with repeated tool calls).
- Because the connection stays open and each turn sends only incremental input, WebSocket mode reduces per-turn continuation overhead and improves end-to-end latency across long chains.

Extracted text:

WebSocket Mode | OpenAI API

Search the API docs

Search docs

Suggested

responses create

reasoning_effort

realtime

prompt caching

Primary navigation

Search docs

Suggested

responses create

reasoning_effort

realtime

prompt caching

Get started

Overview

Quickstart

Models

Pricing

Libraries

Latest: GPT-5.4

Prompt guidance

Core concepts

Text generation

Code generation

Images and vision

Audio and speech

Structured output

Function calling

Responses API

Using tools

Agents SDK

Overview

Quickstart

Agent definitions

Models and providers

Running agents

Sandbox agents

Orchestration

Guardrails

Results and state

Integrations and observability

Evaluate agent workflows

Voice agents

Agent Builder

Overview

Node reference

Safety in building agents

ChatKit

Overview

Customize

Widgets

Actions

Advanced integrations

Tools

Web search

MCP and Connectors

Skills

Shell

Computer use

File search and retrieval

File search

Retrieval

Tool search

More tools

Apply Patch

Local shell

Image generation

Code interpreter

Run and scale

Conversation state

Background mode

Streaming

WebSocket mode

Webhooks

File inputs

Context management

Compaction

Counting tokens

Prompt caching

Prompting

Overview

Prompt engineering

Citation formatting

Reasoning

Reasoning models

Reasoning best practices

Evaluation

Getting started

Working with evals

Prompt optimizer

External models

Best practices

Realtime API

Overview

Connect

WebRTC

WebSocket

SIP

Usage

Using realtime models

Managing conversations

MCP servers

Webhooks and server-side controls

Managing costs

Realtime transcription

Voice agents

Model optimization

Optimization cycle

Fine-tuning

Supervised fine-tuning

Vision fine-tuning

Direct preference optimization

Reinforcement fine-tuning

RFT use cases

Best practices

Graders

Specialized models

Image generation

Video generation

Text to speech

Speech to text

Deep research

Embeddings

Moderation

Going live

Production best practices

Latency optimization

Overview

Predicted Outputs

Priority processing

Cost optimization

Overview

Batch

Flex processing

Accuracy optimization

Safety

Safety best practices

Safety checks

Cybersecurity checks

Under 18 API Guidance

Legacy APIs

Assistants API

Migration guide

Deep dive

Tools

Resources

Terms and policies

Changelog

Your data

Permissions

Rate limits

Deprecations

MCP for deep research

Developer mode

ChatGPT Actions

Introduction

Getting started

Actions library

Authentication

Production

Data retrieval

Sending files

Docs

Use cases

Getting Started

Overview

Quickstart

Explore use cases

Pricing

Concepts

Prompting

Customization

Sandboxing

Subagents

Workflows

Models

Cyber Safety

Using Codex

App

Overview

Features

Settings

Review

Automations

Worktrees

Local Environments

Commands

Windows

Troubleshooting

IDE Extension

Overview

Features

Settings

IDE Commands

Slash commands

CLI

Overview

Features

Command Line Options

Slash commands

Web

Overview

Environments

Internet Access

Integrations

GitHub

Slack

Linear

Codex Security

Overview

Setup

Improving the threat model

FAQ

Configuration

Config File

Config Basics

Advanced Config

Config Reference

Sample Config

Speed

Rules

Hooks

AGENTS.md

MCP

Plugins

Overview

Build plugins

Skills

Subagents

Administration

Authentication

Agent approvals & security

Enterprise

Admin Setup

Governance

Managed configuration

Windows

Automation

Non-interactive Mode

Codex SDK

App Server

MCP Server

GitHub Action

Learn

Best practices

Videos

Community

Blog

Using skills to accelerate OSS maintenance

Building frontend UIs with Codex and Figma

View all

Cookbooks

Codex Prompting Guide

Modernizing your Codebase with Codex

View all

Building AI Teams

Releases

Changelog

Feature Maturity

Open Source

Home

Apps SDK

Commerce

Home

Quickstart

Core Concepts

MCP Apps in ChatGPT

MCP Server

UX principles

UI guidelines

Plan

Research use cases

Define tools

Design components

Build

Set up your server

Build your ChatGPT UI

Authenticate users

Manage state

Monetize your app

Examples

Deploy

Deploy your app

Connect from ChatGPT

Test your integration

Submit your app

Guides

Optimize Metadata

Security & Privacy

Troubleshooting

Resources

Changelog

App submission guidelines

Reference

Home

Guides

Get started

Best practices

File Upload

Overview

Products

API

Overview

Feeds

Products

Promotions

Showcase

Blog

Cookbook

Learn

Community

Home

All posts

Recent

How Perplexity Brought Voice Search to Millions Using the Realtime API

Designing delightful frontends with GPT-5.4

From prompts to products: One year of Responses

Using skills to accelerate OSS maintenance

Building frontend UIs with Codex and Figma

Topics

General

API

Apps SDK

Audio

Codex

Home

Topics

Agents

Evals

Multimodal

Text

Guardrails

Optimization

ChatGPT

Codex

gpt-oss

Contribute

Cookbook on GitHub

Home

Docs MCP

Categories

Demo apps

Videos

Topics

Agents

Audio & Voice

Computer use

Codex

Evals

gpt-oss

Fine-tuning

Image generation

Scaling

Tools

Video generation

Community

Programs

Codex Ambassadors

Codex for Students

Codex for Open Source

Events

Meetups

Hackathon Support

Forum

Discord

API Dashboard

Copy Page

More page actions

Copy Page

More page actions

The Responses API supports a WebSocket mode for long-running, tool-call-heavy workflows. In this mode, you keep a persistent connection to

/v1/responses

and continue each turn by sending only new input items plus

previous_response_id

.

WebSocket mode is compatible with both Zero Data Retention (ZDR) and

store=false

.

Why use WebSocket mode

WebSocket mode is most useful when a workflow involves many model-tool round trips (for example, agentic coding or orchestration loops with repeated tool calls).

Because the connection stays open and each turn sends only incremental input, WebSocket mode reduces per-turn continuation overhead and improves end-to-end latency across long chains. For rollouts with 20+ tool calls, we have seen up to roughly 40% faster end-to-end execution.

Connect and create responses

In WebSocket mode, start each turn by sending a

response.create

event from the client. The payload mirrors the normal

Responses create body

, except that transport-specific fields like

stream

and

background

are not used.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

from

websocket

import

create_connection

import

json

import

os

ws = create_connection(

"wss://api.openai.com/v1/responses"

,

header=[

f"Authorization: Bearer

{os.environ[

'OPENAI_API_KEY'

]}

"

,

],

)

ws.send(

json.dumps(

{

"type"

:

"response.create"

,

"model"

:

"gpt-5.4"

,

"store"

:

False

,

"input"

: [

{

"type"

:

"message"

,

"role"

:

"user"

,

"content"

: [{

"type"

:

"input_text"

,

"text"

:

"Find fizz_buzz()"

}],

}

],

"tools"

: [],

}

)

)

Clients can optionally warm up request state by sending

response.create

with

generate: false

. This is useful when you already know the tools, instructions, and/or custom messages you plan to send with an upcoming turn.

generate: false

does not return a model output, but prepares request state so the next generated turn can start faster. The warmup request returns a response ID that you can chain from with

previous_response_id

, including on later turns in a response chain. The next section explains how to continue a session using

previous_response_id

and incremental inputs.

Continue with incremental inputs

To continue a run, send another

response.create

with:

previous_response_id

set to the prior response ID.

input

containing only new items (for example, tool outputs and the next user message).

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

ws.send(

json.dumps(

{

"type"

:

"response.create"

,

"model"

:

"gpt-5.4"

,

"store"

:

False

,

"previous_response_id"

:

"resp_123"

,

"input"

: [

{

"type"

:

"function_call_output"

,

"call_id"

:

"call_123"

,

"output"

:

"tool result"

,

},

{

"type"

:

"message"

,

"role"

:

"user"

,

"content"

: [{

"type"

:

"input_text"

,

"text"

:

"Now optimize it."

}],

},

],

"tools"

: [],

}

)

)

How continuation works

WebSocket mode uses the same

previous_response_id

chaining semantics as HTTP mode, but it adds a lower-latency continuation path on the active socket.

On an active WebSocket connection, the service keeps one previous-response state in a connection-local in-memory cache (the most recent response). Continuing from that most recent response is fast because the service can reuse connection-local state. Because the previous-response state is retained only in memory and is not written to disk, you can use WebSocket mode in a way that is compatible with

store=false

and Zero Data Retention (ZDR).

If a

previous_response_id

is not in the in-memory cache, behavior depends on whether you store responses:

With

store=true

, the service may hydrate older response IDs from persisted state when available. Continuation can still work, but it usually loses the in-memory latency benefit.

With

store=false

(including ZDR), there is no persisted fallback. If the ID is uncached, the request returns

previous_response_not_found

.

If a turn fails (

4xx

or

5xx

), the service evicts the referenced

previous_response_id

from the connection-local cache. This prevents reusing stale cached state for that failed continuation.

Compaction and creating new responses

If you are using compaction, there are two different continuation patterns:

Server-side compaction (

context_management

)

When you enable server-side compaction (

context_management

with

compact_threshold

), compaction happens during normal

/responses

generation. In WebSocket mode, you continue the same way you normally do: send the next

response.create

with the latest

previous_response_id

and only new input items.

Standalone

/responses/compact

The standalone

/responses/compact

endpoint

returns a new compacted input window, not a response ID. After compaction, create a new response on your WebSocket connection using the compacted window as

input

(plus the next user/tool items).

Start a new chain by omitting

previous_response_id

or setting it to

null

. Pass the compacted output as-is; do not prune the returned window.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

# Compact your current window (HTTP call)

compacted = client.responses.compact(

model=

"gpt-5.4"

,

input

=long_input_items_array,

)

# Start a new response on the WebSocket using the compacted window

ws.send(

json.dumps(

{

"type"

:

"response.create"

,

"model"

:

"gpt-5.4"

,

"store"

:

False

,

"input"

: [

*compacted.output,

{

"type"

:

"message"

,

"role"

:

"user"

,

"content"

: [{

"type"

:

"input_text"

,

"text"

:

"Continue from here."

}],

},

],

"tools"

: [],

}

)

)

Connection behavior and limits

Server events and ordering match the existing Responses streaming event model.

A single WebSocket connection can receive multiple

response.create

messages, but it runs them sequentially (one in-flight response at a time).

No multiplexing support today. Use multiple connections if you need parallel runs.

Connection duration is limited to 60 minutes. Reconnect when the limit is reached.

Reconnect and recover

When a connection closes (or hits the 60-minute limit), open a new WebSocket connection and continue with one of these patterns:

If your prior response is persisted (

store=true

) and you have a valid response ID, continue with

previous_response_id

and new input items.

If you cannot continue the chain (for example,

store=false

/ZDR or

previous_response_not_found

), start a new response by setting

previous_response_id

to

null

(or omitting it) and send the full input context for the next turn.

If you compacted context with

/responses/compact

, use the returned compacted window as the base

input

for that new response, then append the latest user/tool items.

Errors to handle

previous_response_not_found

1

2

3

4

5

6

7

8

9

{

"type"

:

"error"

,

"status"

:

400

,

"error"

: {

"code"

:

"previous_response_not_found"

,

"message"

:

"Previous response with id 'resp_abc' not found."

,

"param"

:

"previous_response_id"

}

}

websocket_connection_limit_reached

1

2

3

4

5

6

7

8

9

{

"type"

:

"error"

,

"error"

: {

"type"

:

"invalid_request_error"

,

"code"

:

"websocket_connection_limit_reached"

,

"message"

:

"Responses websocket connection limit reached (60 minutes). Create a new websocket connection to continue."

},

"status"

:

400

}

Related guides

Conversation state

Streaming API responses

Responses streaming events reference
