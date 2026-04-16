---
title: Quickstart | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/agents/quickstart
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:21.748481+00:00
kind: extracted-doc
---

# Quickstart | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/agents/quickstart

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:21.748481+00:00

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

- Quickstart | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions Use this page when you want the shortest path to a working SDK-based agent.
- The examples below use the same high-level concepts in both TypeScript and Python: define an agent, run it, then add tools and specialist agents as your workflow grows.
- Install the SDK Create a project, install the SDK, and set your API key.
- Create an API Key 1 2 3 4 5 6 7 # TypeScript npm install @openai/agents zod # Python pip install openai-agents export OPENAI_API_KEY=sk-...
- Create and run your first agent Start with one focused agent and one turn.

Extracted text:

Quickstart | OpenAI API

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

Use this page when you want the shortest path to a working SDK-based agent. The examples below use the same high-level concepts in both TypeScript and Python: define an agent, run it, then add tools and specialist agents as your workflow grows.

Install the SDK

Create a project, install the SDK, and set your API key.

Create an API Key

1

2

3

4

5

6

7

# TypeScript

npm install @openai/agents zod

# Python

pip install openai-agents

export

OPENAI_API_KEY=sk-...

Create and run your first agent

Start with one focused agent and one turn. The SDK handles the model call and returns a result object with the final output plus the run history.

Create and run an agent

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

"History tutor"

,

instructions

:

"You answer history questions clearly and concisely."

,

model

:

"gpt-5.4"

,

});

const

result =

await

run(agent,

"When did the Roman Empire fall?"

);

console

.log(result.finalOutput);

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

asyncio

from

agents

import

Agent, Runner

agent = Agent(

name=

"History tutor"

,

instructions=

"You answer history questions clearly and concisely."

,

model=

"gpt-5.4"

,

)

async

def

main

() ->

None

:

result =

await

Runner.run(agent,

"When did the Roman Empire fall?"

)

print

(result.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

You should see a concise answer in the terminal. Once that loop works, keep the same shape and add capabilities incrementally rather than starting with a large multi-agent design.

Carry state into the next turn

The first run result is also how you decide what the second turn should use as state.

If you want

Start with

Keep the full history in your application

result.history

Let the SDK load and save history for you

A session

Let OpenAI manage continuation state

A server-managed continuation ID

Resume a run that paused for approval or interruption

result.state

, together with

interruptions

After handoffs, reuse

lastAgent

for the next turn when that specialist should stay in control.

Give the agent a tool

The first capability you add is often a function tool or a hosted OpenAI tool such as web search or file search.

Add a function tool

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

23

24

25

import

{ Agent, run, tool }

from

"@openai/agents"

;

import

{ z }

from

"zod"

;

const

historyFunFact = tool({

name

:

"history_fun_fact"

,

description

:

"Return a short history fact."

,

parameters

: z.object({}),

async

execute

(

)

{

return

"Sharks are older than trees."

;

},

});

const

agent =

new

Agent({

name

:

"History tutor"

,

instructions

:

"Answer history questions clearly. Use history_fun_fact when it helps."

,

tools

: [historyFunFact],

});

const

result =

await

run(

agent,

"Tell me something surprising about ancient life on Earth."

,

);

console

.log(result.finalOutput);

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

import

asyncio

from

agents

import

Agent, Runner, function_tool

@function_tool

def

history_fun_fact

() ->

str

:

"""Return a short history fact."""

return

"Sharks are older than trees."

agent = Agent(

name=

"History tutor"

,

instructions=

"Answer history questions clearly. Use history_fun_fact when it helps."

,

tools=[history_fun_fact],

)

async

def

main

() ->

None

:

result =

await

Runner.run(

agent,

"Tell me something surprising about ancient life on Earth."

,

)

print

(result.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

Use the shared

Using tools

guide when you need hosted tools, tool search, or agents-as-tools.

Add specialist agents

A common next step is to split the workflow into specialists and let a router delegate to them with handoffs.

Route to specialist agents

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

23

24

25

import

{ Agent, run }

from

"@openai/agents"

;

const

historyTutor =

new

Agent({

name

:

"History tutor"

,

instructions

:

"Answer history questions clearly and concisely."

,

});

const

mathTutor =

new

Agent({

name

:

"Math tutor"

,

instructions

:

"Explain math step by step and include worked examples."

,

});

const

triageAgent = Agent.create({

name

:

"Homework triage"

,

instructions

:

"Route each homework question to the right specialist."

,

handoffs

: [historyTutor, mathTutor],

});

const

result =

await

run(

triageAgent,

"Who was the first president of the United States?"

,

);

console

.log(result.finalOutput);

console

.log(result.lastAgent?.name);

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

31

32

33

34

import

asyncio

from

agents

import

Agent, Runner

history_tutor = Agent(

name=

"History tutor"

,

handoff_description=

"Specialist for history questions."

,

instructions=

"Answer history questions clearly and concisely."

,

)

math_tutor = Agent(

name=

"Math tutor"

,

handoff_description=

"Specialist for math questions."

,

instructions=

"Explain math step by step and include worked examples."

,

)

triage_agent = Agent(

name=

"Homework triage"

,

instructions=

"Route each homework question to the right specialist."

,

handoffs=[history_tutor, math_tutor],

)

async

def

main

() ->

None

:

result =

await

Runner.run(

triage_agent,

"Who was the first president of the United States?"

,

)

print

(result.final_output)

print

(result.last_agent.name)

if

__name__ ==

"__main__"

:

asyncio.run(main())

Inspect traces early

The normal server-side SDK path includes tracing. As soon as the first run works, open the

Traces dashboard

to inspect model calls, tool calls, handoffs, and guardrails before you start tuning prompts.

Next steps

Once the first run works, continue with the guide that matches the next capability you want to add.

Agent definitions

Shape one specialist cleanly before you scale the workflow.

Using tools

Add hosted tools, function tools, and agents-as-tools.

Running agents

Learn the agent loop, streaming, and continuation strategies.

Orchestration and handoffs

Decide when specialists should take over the conversation.
