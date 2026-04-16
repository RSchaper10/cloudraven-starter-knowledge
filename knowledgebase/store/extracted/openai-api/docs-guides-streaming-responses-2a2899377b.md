---
title: Streaming API responses | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/streaming-responses
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:41.948356+00:00
kind: extracted-doc
---

# Streaming API responses | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/streaming-responses

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:41.948356+00:00

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

- Streaming API responses | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Responses Copy Page More page actions Responses Copy Page More page actions By default, when you make a request to the OpenAI API, we generate the model’s entire output before sending it back in a single HTTP response.
- When generating long outputs, waiting for a response can take time.
- Streaming responses lets you start printing or processing the beginning of the model’s output while it continues generating the full response.
- This guide focuses on HTTP streaming ( stream=true ) over server-sent events (SSE).
- For persistent WebSocket transport with incremental inputs via previous_response_id , see the Responses API WebSocket mode .

Extracted text:

Streaming API responses | OpenAI API

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

Responses

Copy Page

More page actions

Responses

Copy Page

More page actions

By default, when you make a request to the OpenAI API, we generate the model’s entire output before sending it back in a single HTTP response. When generating long outputs, waiting for a response can take time. Streaming responses lets you start printing or processing the beginning of the model’s output while it continues generating the full response.

This guide focuses on HTTP streaming (

stream=true

) over server-sent events (SSE). For persistent WebSocket transport with incremental inputs via

previous_response_id

, see

the Responses API WebSocket mode

.

Enable streaming

To start streaming responses, set

stream=True

in your request to the Responses endpoint:

python

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

import

{ OpenAI }

from

"openai"

;

const

client =

new

OpenAI();

const

stream =

await

client.responses.create({

model

:

"gpt-5"

,

input

: [

{

role

:

"user"

,

content

:

"Say 'double bubble bath' ten times fast."

,

},

],

stream

:

true

,

});

for

await

(

const

event

of

stream) {

console

.log(event);

}

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

from

openai

import

OpenAI

client = OpenAI()

stream = client.responses.create(

model=

"gpt-5"

,

input

=[

{

"role"

:

"user"

,

"content"

:

"Say 'double bubble bath' ten times fast."

,

},

],

stream=

True

,

)

for

event

in

stream:

print

(event)

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

using

OpenAI.Responses;

string

key = Environment.GetEnvironmentVariable(

"OPENAI_API_KEY"

)!;

OpenAIResponseClient client =

new

(model:

"gpt-5"

, apiKey: key);

var

responses = client.CreateResponseStreamingAsync([

ResponseItem.CreateUserMessageItem([

ResponseContentPart.CreateInputTextPart(

"Say 'double bubble bath' ten times fast."

),

]),

]);

await

foreach

(

var

response

in

responses)

{

if

(response

is

StreamingResponseOutputTextDeltaUpdate delta)

{

Console.Write(delta.Delta);

}

}

The Responses API uses semantic events for streaming. Each event is typed with a predefined schema, so you can listen for events you care about.

For a full list of event types, see the

API reference for streaming

. Here are a few examples:

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

type

StreamingEvent =

| ResponseCreatedEvent

| ResponseInProgressEvent

| ResponseFailedEvent

| ResponseCompletedEvent

| ResponseOutputItemAdded

| ResponseOutputItemDone

| ResponseContentPartAdded

| ResponseContentPartDone

| ResponseOutputTextDelta

| ResponseOutputTextAnnotationAdded

| ResponseTextDone

| ResponseRefusalDelta

| ResponseRefusalDone

| ResponseFunctionCallArgumentsDelta

| ResponseFunctionCallArgumentsDone

| ResponseFileSearchCallInProgress

| ResponseFileSearchCallSearching

| ResponseFileSearchCallCompleted

| ResponseCodeInterpreterInProgress

| ResponseCodeInterpreterCallCodeDelta

| ResponseCodeInterpreterCallCodeDone

| ResponseCodeInterpreterCallInterpreting

| ResponseCodeInterpreterCallCompleted

| Error

Streaming Chat Completions is fairly straightforward. However, we recommend using the

Responses API for streaming

, as we designed it with streaming in mind. The Responses API uses semantic events for streaming and is type-safe.

Stream a chat completion

To stream completions, set

stream=True

when calling the Chat Completions or legacy Completions endpoints. This returns an object that streams back the response as data-only server-sent events.

The response is sent back incrementally in chunks with an event stream. You can iterate over the event stream with a

for

loop, like this:

python

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

import

OpenAI

from

"openai"

;

const

openai =

new

OpenAI();

const

stream =

await

openai.chat.completions.create({

model

:

"gpt-5"

,

messages

: [

{

role

:

"user"

,

content

:

"Say 'double bubble bath' ten times fast."

,

}

],

stream

:

true

,

});

for

await

(

const

chunk

of

stream) {

console

.log(chunk);

console

.log(chunk.choices[

0

].delta);

console

.log(

"****************"

);

}

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

from

openai

import

OpenAI

client = OpenAI()

stream = client.chat.completions.create(

model=

"gpt-5"

,

messages=[

{

"role"

:

"user"

,

"content"

:

"Say 'double bubble bath' ten times fast."

,

},

],

stream=

True

,

)

for

chunk

in

stream:

print

(chunk)

print

(chunk.choices[

0

].delta)

print

(

"****************"

)

Read the responses

If you’re using our SDK, every event is a typed instance. You can also identity individual events using the

type

property of the event.

Some key lifecycle events are emitted only once, while others are emitted multiple times as the response is generated. Common events to listen for when streaming text are:

1

2

3

4

- `response.created`

- `response.output_text.delta`

- `response.completed`

- `error`

For a full list of events you can listen for, see the

API reference for streaming

.

When you stream a chat completion, the responses has a

delta

field rather than a

message

field. The

delta

field can hold a role token, content token, or nothing.

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

{ role: 'assistant', content: '', refusal: null }

****************

{ content: 'Why' }

****************

{ content: " don't" }

****************

{ content: ' scientists' }

****************

{ content: ' trust' }

****************

{ content: ' atoms' }

****************

{ content: '?\n\n' }

****************

{ content: 'Because' }

****************

{ content: ' they' }

****************

{ content: ' make' }

****************

{ content: ' up' }

****************

{ content: ' everything' }

****************

{ content: '!' }

****************

{}

****************

To stream only the text response of your chat completion, your code would like this:

python

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

import

OpenAI

from

"openai"

;

const

client =

new

OpenAI();

const

stream =

await

client.chat.completions.create({

model

:

"gpt-5"

,

messages

: [

{

role

:

"user"

,

content

:

"Say 'double bubble bath' ten times fast."

,

},

],

stream

:

true

,

});

for

await

(

const

chunk

of

stream) {

process.stdout.write(chunk.choices[

0

]?.delta?.content ||

""

);

}

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

from

openai

import

OpenAI

client = OpenAI()

stream = client.chat.completions.create(

model=

"gpt-5"

,

messages=[

{

"role"

:

"user"

,

"content"

:

"Say 'double bubble bath' ten times fast."

,

},

],

stream=

True

,

)

for

chunk

in

stream:

if

chunk.choices[

0

].delta.content

is

not

None

:

print

(chunk.choices[

0

].delta.content, end=

""

)

Advanced use cases

For more advanced use cases, like streaming tool calls, check out the following dedicated guides:

Streaming function calls

Streaming structured output

Moderation risk

Note that streaming the model’s output in a production application makes it more difficult to moderate the content of the completions, as partial completions may be more difficult to evaluate. This may have implications for approved usage.
