---
title: Agent definitions | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/agents/define-agents
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:22.313114+00:00
kind: extracted-doc
---

# Agent definitions | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/agents/define-agents

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:22.313114+00:00

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

- Agent definitions | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions An agent is the core unit of an SDK-based workflow.
- It packages a model, instructions, and optional runtime behavior such as tools, guardrails, MCP servers, handoffs, and structured outputs.
- What belongs on an agent Use agent configuration for decisions that are intrinsic to that specialist: Property Use it for Read next name Human-readable identity in traces and tool/handoff surfaces This page instructions The job, constraints, and style for that agent This page prompt Stored prompt configuration for Responses-based runs Models and providers model and model settings Choosing the model and tuning behavior Models and providers tools Capabilities the agent can call directly Using tools handoffDescription Hinting when another agent should delegate here Orchestration and handoffs handoffs Delegating to another agent Orchestration and handoffs outputType Returning structured output instead of plain text This page Guardrails and approvals Validation, blocking, and review flows Guardrails and human review MCP servers and hosted MCP tools Attaching MCP-backed capabilities Integrations and observability Start with one focused agent Define the smallest agent that can own a clear task.
- Add more agents only when you need separate ownership, different instructions, different tool surfaces, or different approval policies.
- Define a single agent typescript 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 import { Agent, tool } from "@openai/agents" ; import { z } from "zod" ; const getWeather = tool({ name : "get_weather" , description : "Return the weather for a given city." , parameters : z.object({ city : z.string() }), async execute ( { city } ) { return `The weather in ${city} is sunny.` ; }, }); const agent = new Agent({ name : "Weather bot" , instructions : "You are a helpful weather bot." , model : "gpt-5.4" , tools : [getWeather], }); 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 from agents import Agent, function_tool @function_tool def get_weather ( city: str ) -> str : """Return the weather for a given city.""" return f"The weather in {city} is sunny." agent = Agent( name= "Weather bot" , instructions= "You are a helpful weather bot." , model= "gpt-5.4" , tools=[get_weather], ) Shape instructions, handoffs, and outputs Three configuration choices deserve extra care: Start with static instructions .

Extracted text:

Agent definitions | OpenAI API

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

An agent is the core unit of an SDK-based workflow. It packages a model, instructions, and optional runtime behavior such as tools, guardrails, MCP servers, handoffs, and structured outputs.

What belongs on an agent

Use agent configuration for decisions that are intrinsic to that specialist:

Property

Use it for

Read next

name

Human-readable identity in traces and tool/handoff surfaces

This page

instructions

The job, constraints, and style for that agent

This page

prompt

Stored prompt configuration for Responses-based runs

Models and providers

model

and model settings

Choosing the model and tuning behavior

Models and providers

tools

Capabilities the agent can call directly

Using tools

handoffDescription

Hinting when another agent should delegate here

Orchestration and handoffs

handoffs

Delegating to another agent

Orchestration and handoffs

outputType

Returning structured output instead of plain text

This page

Guardrails and approvals

Validation, blocking, and review flows

Guardrails and human review

MCP servers and hosted MCP tools

Attaching MCP-backed capabilities

Integrations and observability

Start with one focused agent

Define the smallest agent that can own a clear task. Add more agents only when you need separate ownership, different instructions, different tool surfaces, or different approval policies.

Define a single agent

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

{ Agent, tool }

from

"@openai/agents"

;

import

{ z }

from

"zod"

;

const

getWeather = tool({

name

:

"get_weather"

,

description

:

"Return the weather for a given city."

,

parameters

: z.object({

city

: z.string() }),

async

execute

(

{ city }

)

{

return

`The weather in

${city}

is sunny.`

;

},

});

const

agent =

new

Agent({

name

:

"Weather bot"

,

instructions

:

"You are a helpful weather bot."

,

model

:

"gpt-5.4"

,

tools

: [getWeather],

});

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

from

agents

import

Agent, function_tool

@function_tool

def

get_weather

(

city:

str

) ->

str

:

"""Return the weather for a given city."""

return

f"The weather in

{city}

is sunny."

agent = Agent(

name=

"Weather bot"

,

instructions=

"You are a helpful weather bot."

,

model=

"gpt-5.4"

,

tools=[get_weather],

)

Shape instructions, handoffs, and outputs

Three configuration choices deserve extra care:

Start with static

instructions

. When the guidance depends on the current user, tenant, or runtime context, switch to a dynamic instructions callback instead of stitching strings together at the call site.

Keep

handoffDescription

short and concrete so routing agents know when to pick this specialist.

Use

outputType

when downstream code needs typed data rather than free-form prose.

Return structured output

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

import

{ Agent, run }

from

"@openai/agents"

;

import

{ z }

from

"zod"

;

const

calendarEvent = z.object({

name

: z.string(),

date

: z.string(),

participants

: z.array(z.string()),

});

const

agent =

new

Agent({

name

:

"Calendar extractor"

,

instructions

:

"Extract calendar events from text."

,

outputType

: calendarEvent,

});

const

result =

await

run(

agent,

"Dinner with Priya and Sam on Friday."

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

29

30

import

asyncio

from

pydantic

import

BaseModel

from

agents

import

Agent, Runner

class

CalendarEvent

(

BaseModel

):

name:

str

date:

str

participants:

list

[

str

]

agent = Agent(

name=

"Calendar extractor"

,

instructions=

"Extract calendar events from text."

,

output_type=CalendarEvent,

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

"Dinner with Priya and Sam on Friday."

,

)

print

(result.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

Use

prompt

when you want to reference a stored prompt configuration from the Responses API instead of embedding the entire system prompt in code.

Keep local context separate from model context

The SDK lets you pass application state and dependencies into a run without sending them to the model. Use this for data like authenticated user info, database clients, loggers, and helper functions.

Pass local context to tools

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

26

27

import

{ Agent, RunContext, run, tool }

from

"@openai/agents"

;

import

{ z }

from

"zod"

;

interface

UserInfo {

name

:

string

;

uid:

number

;

}

const

fetchUserAge = tool({

name

:

"fetch_user_age"

,

description

:

"Return the age of the current user."

,

parameters

: z.object({}),

async

execute

(

_args, runContext?: RunContext<UserInfo>

)

{

return

`User

${runContext?.context.name}

is 47 years old`

;

},

});

const

agent =

new

Agent<UserInfo>({

name

:

"Assistant"

,

tools

: [fetchUserAge],

});

const

result =

await

run(agent,

"What is the age of the user?"

, {

context

: {

name

:

"John"

,

uid

:

123

},

});

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

29

30

31

32

33

34

35

import

asyncio

from

dataclasses

import

dataclass

from

agents

import

Agent, RunContextWrapper, Runner, function_tool

@dataclass

class

UserInfo

:

name:

str

uid:

int

@function_tool

async

def

fetch_user_age

(

wrapper: RunContextWrapper[UserInfo]

) ->

str

:

"""Fetch the age of the current user."""

return

f"The user

{wrapper.context.name}

is 47 years old."

agent = Agent[UserInfo](

name=

"Assistant"

,

tools=[fetch_user_age],

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

"What is the age of the user?"

,

context=UserInfo(name=

"John"

, uid=

123

),

)

print

(result.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

The important boundary is:

Conversation history is what the model sees.

Run context is what your code sees.

If the model needs a fact, put it in instructions, input, retrieval, or a tool. If only your runtime needs it, keep it in local context.

When to split one agent into several

Split an agent when one specialist shouldn’t own the full reply or when separate capabilities are materially different. Common reasons are:

A specialist needs a different tool or MCP surface.

A specialist needs a different approval policy or guardrail.

One branch of the workflow needs a different model or output style.

You want explicit routing in traces rather than a single large prompt.

Next steps

Once one specialist is defined cleanly, move to the guide that matches the next design question.

Models and providers

Choose models, defaults, and transport strategy for this agent.

Using tools

Add capabilities the agent can call directly.

Orchestration and handoffs

Choose how specialists collaborate once one agent is no longer enough.

Running agents

Understand the runtime loop, state, and streaming behavior.
