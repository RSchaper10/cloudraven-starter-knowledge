---
title: Background mode | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/background
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:41.389005+00:00
kind: extracted-doc
---

# Background mode | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/background

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:41.389005+00:00

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

- Background mode | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions Agents like Codex and Deep Research show that reasoning models can take several minutes to solve complex problems.
- Background mode enables you to execute long-running tasks on models like GPT-5.2 and GPT-5.2 pro reliably, without having to worry about timeouts or other connectivity issues.
- Background mode kicks off these tasks asynchronously, and developers can poll response objects to check status over time.
- To start response generation in the background, make an API request with background set to true : Because background mode stores response data for roughly 10 minutes to enable polling, it is not Zero Data Retention (ZDR) compatible.
- Requests from ZDR projects are still accepted with background=true for legacy reasons, but using it breaks ZDR guarantees.

Extracted text:

Background mode | OpenAI API

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

Agents like

Codex

and

Deep Research

show that reasoning models can take several minutes to solve complex problems. Background mode enables you to execute long-running tasks on models like GPT-5.2 and GPT-5.2 pro reliably, without having to worry about timeouts or other connectivity issues.

Background mode kicks off these tasks asynchronously, and developers can poll response objects to check status over time. To start response generation in the background, make an API request with

background

set to

true

:

Because background mode stores response data for roughly 10 minutes to enable polling, it is not Zero Data Retention (ZDR) compatible. Requests from ZDR projects are still accepted with

background=true

for legacy reasons, but using it breaks ZDR guarantees. Modified Abuse Monitoring (MAM) projects can safely rely on background mode.

Generate a response in the background

python

1

2

3

4

5

6

7

8

curl https://api.openai.com/v1/responses \

-H

"Content-Type: application/json"

\

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

\

-d

'{

"model": "gpt-5.4",

"input": "Write a very long novel about otters in space.",

"background": true

}'

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

resp =

await

client.responses.create({

model

:

"gpt-5.4"

,

input

:

"Write a very long novel about otters in space."

,

background

:

true

,

});

console

.log(resp.status);

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

from

openai

import

OpenAI

client = OpenAI()

resp = client.responses.create(

model=

"gpt-5.4"

,

input

=

"Write a very long novel about otters in space."

,

background=

True

,

)

print

(resp.status)

Polling background responses

To check the status of background requests, use the GET endpoint for Responses. Keep polling while the request is in the queued or in_progress state. When it leaves these states, it has reached a final (terminal) state.

Retrieve a response executing in the background

python

1

2

3

curl https://api.openai.com/v1/responses/resp_123 \

-H

"Content-Type: application/json"

\

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

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

import

OpenAI

from

"openai"

;

const

client =

new

OpenAI();

let

resp =

await

client.responses.create({

model

:

"gpt-5.4"

,

input

:

"Write a very long novel about otters in space."

,

background

:

true

,

});

while

(resp.status ===

"queued"

|| resp.status ===

"in_progress"

) {

console

.log(

"Current status: "

+ resp.status);

await

new

Promise

(

resolve

=>

setTimeout

(resolve,

2000

));

// wait 2 seconds

resp =

await

client.responses.retrieve(resp.id);

}

console

.log(

"Final status: "

+ resp.status +

"\nOutput:\n"

+ resp.output_text);

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

from

time

import

sleep

client = OpenAI()

resp = client.responses.create(

model=

"gpt-5.4"

,

input

=

"Write a very long novel about otters in space."

,

background=

True

,

)

while

resp.status

in

{

"queued"

,

"in_progress"

}:

print

(

f"Current status:

{resp.status}

"

)

sleep(

2

)

resp = client.responses.retrieve(resp.

id

)

print

(

f"Final status:

{resp.status}

\nOutput:\n

{resp.output_text}

"

)

Cancelling a background response

You can also cancel an in-flight response like this:

Cancel an ongoing response

python

1

2

3

curl -X POST https://api.openai.com/v1/responses/resp_123/cancel \

-H

"Content-Type: application/json"

\

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

1

2

3

4

5

6

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

resp =

await

client.responses.cancel(

"resp_123"

);

console

.log(resp.status);

1

2

3

4

5

6

from

openai

import

OpenAI

client = OpenAI()

resp = client.responses.cancel(

"resp_123"

)

print

(resp.status)

Cancelling twice is idempotent - subsequent calls simply return the final

Response

object.

Streaming a background response

You can create a background Response and start streaming events from it right away. This may be helpful if you expect the client to drop the stream and want the option of picking it back up later. To do this, create a Response with both

background

and

stream

set to

true

. You will want to keep track of a “cursor” corresponding to the

sequence_number

you receive in each streaming event.

Currently, the time to first token you receive from a background response is higher than what you receive from a synchronous one. We are working to reduce this latency gap in the coming weeks.

Generate and stream a background response

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

curl https://api.openai.com/v1/responses \

-H

"Content-Type: application/json"

\

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

\

-d

'{

"model": "gpt-5.4",

"input": "Write a very long novel about otters in space.",

"background": true,

"stream": true

}'

// To resume:

curl

"https://api.openai.com/v1/responses/resp_123?stream=true&starting_after=42"

\

-H

"Content-Type: application/json"

\

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

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

client =

new

OpenAI();

const

stream =

await

client.responses.create({

model

:

"gpt-5.4"

,

input

:

"Write a very long novel about otters in space."

,

background

:

true

,

stream

:

true

,

});

let

cursor =

null

;

for

await

(

const

event

of

stream) {

console

.log(event);

cursor = event.sequence_number;

}

// If the connection drops, you can resume streaming from the last cursor (SDK support coming soon):

// const resumedStream = await client.responses.stream(resp.id, { starting_after: cursor });

// for await (const event of resumedStream) { ... }

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

from

openai

import

OpenAI

client = OpenAI()

# Fire off an async response but also start streaming immediately

stream = client.responses.create(

model=

"gpt-5.4"

,

input

=

"Write a very long novel about otters in space."

,

background=

True

,

stream=

True

,

)

cursor =

None

for

event

in

stream:

print

(event)

cursor = event.sequence_number

# If your connection drops, the response continues running and you can reconnect:

# SDK support for resuming the stream is coming soon.

# for event in client.responses.stream(resp.id, starting_after=cursor):

# print(event)

Limits

Background sampling requires

store=true

; stateless requests are rejected.

To cancel a synchronous response, terminate the connection

You can only start a new stream from a background response if you created it with

stream=true

.
