---
title: Running agents | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/agents/running-agents
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:23.351442+00:00
kind: extracted-doc
---

# Running agents | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/agents/running-agents

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:23.351442+00:00

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

- Running agents | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions Defining an agent is only the setup step.
- The runtime questions are what a single run does, how the next turn continues, and how the workflow behaves when it pauses for approvals or tool work.
- The agent loop One SDK run is one application-level turn.
- The runner keeps looping until it reaches a real stopping point: Call the current agent’s model with the prepared input.
- If the model produced tool calls, execute them and continue.

Extracted text:

Running agents | OpenAI API

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

Defining an agent is only the setup step. The runtime questions are what a single run does, how the next turn continues, and how the workflow behaves when it pauses for approvals or tool work.

The agent loop

One SDK run is one application-level turn. The runner keeps looping until it reaches a real stopping point:

Call the current agent’s model with the prepared input.

Inspect the model output.

If the model produced tool calls, execute them and continue.

If the model handed off to another specialist, switch agents and continue.

If the model produced a final answer with no more tool work, return a result.

That loop is the core concept behind the SDK. Tools, handoffs, approvals, and streaming all build on top of it rather than replacing it.

Choose one conversation strategy

There are four common ways to carry state into the next turn:

Strategy

Where state lives

Best for

What you pass on the next turn

result.history

Your application

Small chat loops and maximum control

The replay-ready history

session

Your storage plus the SDK

Persistent chat state, resumable runs, and storage you control

The same session

conversationId

OpenAI Conversations API

Shared server-managed state across workers or services

The same conversation ID and only the new turn

previousResponseId

OpenAI Responses API

The lightest server-managed continuation from one response to the next

The last response ID and only the new turn

In most applications, pick one strategy per conversation. Mixing local replay with server-managed state can duplicate context unless you are deliberately reconciling both layers.

Persist multi-turn state with sessions

typescript

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

import

{ Agent, MemorySession, run }

from

"@openai/agents"

;

const

agent =

new

Agent({

name

:

"Tour guide"

,

instructions

:

"Answer with compact travel facts."

,

});

const

session =

new

MemorySession();

const

firstTurn =

await

run(

agent,

"What city is the Golden Gate Bridge in?"

,

{ session },

);

console

.log(firstTurn.finalOutput);

const

secondTurn =

await

run(agent,

"What state is it in?"

, { session });

console

.log(secondTurn.finalOutput);

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

29

30

import

asyncio

from

agents

import

Agent, Runner, SQLiteSession

agent = Agent(

name=

"Tour guide"

,

instructions=

"Answer with compact travel facts."

,

)

session = SQLiteSession(

"conversation_123"

)

async

def

main

() ->

None

:

first_turn =

await

Runner.run(

agent,

"What city is the Golden Gate Bridge in?"

,

session=session,

)

print

(first_turn.final_output)

second_turn =

await

Runner.run(

agent,

"What state is it in?"

,

session=session,

)

print

(second_turn.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

Sessions are the best default when you want durable memory, resumable approval flows, or storage that your application controls.

Continue with server-managed state

typescript

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

import

{ Agent, run }

from

"@openai/agents"

;

import

OpenAI

from

"openai"

;

const

agent =

new

Agent({

name

:

"Assistant"

,

instructions

:

"Reply very concisely."

,

});

const

client =

new

OpenAI();

const

{

id

: conversationId } =

await

client.conversations.create({});

const

first =

await

run(agent,

"What city is the Golden Gate Bridge in?"

, {

conversationId,

});

console

.log(first.finalOutput);

const

second =

await

run(agent,

"What state is it in?"

, {

conversationId,

});

console

.log(second.finalOutput);

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

import

asyncio

from

agents

import

Agent, Runner

agent = Agent(

name=

"Assistant"

,

instructions=

"Reply very concisely."

,

)

async

def

main

() ->

None

:

first =

await

Runner.run(

agent,

"What city is the Golden Gate Bridge in?"

,

)

print

(first.final_output)

second =

await

Runner.run(

agent,

"What state is it in?"

,

previous_response_id=first.last_response_id,

)

print

(second.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

Use

conversationId

when multiple systems should share one named conversation. Use

previousResponseId

when you want the cheapest response-to-response continuation option.

Stream runs incrementally

Streaming uses the same agent loop and the same state strategies. The only difference is that you consume events while the run is still happening.

Stream a run as text arrives

typescript

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

import

{ Agent, run }

from

"@openai/agents"

;

const

agent =

new

Agent({

name

:

"Planet guide"

,

instructions

:

"Answer with short facts."

,

});

const

stream =

await

run(agent,

"Give me three short facts about Saturn."

, {

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

if

(

event.type ===

"raw_model_stream_event"

&&

event.data.type ===

"response.output_text.delta"

) {

process.stdout.write(event.data.delta);

}

}

await

stream.completed;

console

.log(

"\nFinal:"

, stream.finalOutput);

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

29

30

import

asyncio

from

openai.types.responses

import

ResponseTextDeltaEvent

from

agents

import

Agent, Runner

agent = Agent(

name=

"Planet guide"

,

instructions=

"Answer with short facts."

,

)

async

def

main

() ->

None

:

stream = Runner.run_streamed(

agent,

"Give me three short facts about Saturn."

,

)

async

for

event

in

stream.stream_events():

if

(

event.

type

==

"raw_response_event"

and

isinstance

(event.data, ResponseTextDeltaEvent)

):

print

(event.data.delta, end=

""

, flush=

True

)

print

(

f"\nFinal:

{stream.final_output}

"

)

if

__name__ ==

"__main__"

:

asyncio.run(main())

Three practical rules matter:

Wait for the stream to finish before treating the run as settled.

If the run pauses for approval, resolve

interruptions

and resume from

state

rather than starting a fresh user turn.

If you cancel a stream mid-turn, resume the unfinished turn from

state

if you want the same turn to continue later.

Handle pauses and failures deliberately

Two broad classes of non-happy-path outcomes matter:

Runtime or validation failures

such as max-turn limits, guardrail exceptions, or tool errors.

Expected pauses

such as human approval requests, where the run is intentionally interrupted and should later resume from the same state.

Treat approvals as paused runs, not as new turns. That distinction keeps turn counts, history, and server-managed continuation IDs consistent.

Next steps

Once the runtime loop is clear, move to the guide that matches the next workflow boundary you need to design.

Results and state

Learn which result surfaces your application should carry into the next turn.

Orchestration and handoffs

Decide how multiple specialists behave inside the same runtime loop.

Guardrails and human review

Add validation and approval pauses without breaking turn continuity.
