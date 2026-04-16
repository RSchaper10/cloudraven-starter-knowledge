---
title: Integrations and observability | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/agents/integrations-observability
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:26.555325+00:00
kind: extracted-doc
---

# Integrations and observability | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/agents/integrations-observability

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:26.555325+00:00

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

- Integrations and observability | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions After the workflow shape is clear, the next questions are which external surfaces should live inside the agent loop and how you will inspect what actually happened at runtime.
- Choose what lives in the SDK Need Start with Why Give an agent access to public, remotely hosted MCP tools Hosted MCP tools in the SDK The model can call the remote MCP server through the hosted surface Connect local or private MCP servers from your runtime SDK-managed MCP servers over stdio or streamable HTTP Your runtime owns the connection, approvals, and network boundaries Debug prompts, tools, handoffs, or approvals Built-in tracing Traces show the end-to-end record before you formalize evals Tool capability semantics still live in Using tools .
- This page focuses on the SDK-specific MCP wiring and observability loop.
- MCP Use hosted MCP tools when the remote server should run through the model surface.
- Attach a hosted MCP server typescript 1 2 3 4 5 6 7 8 9 10 11 12 import { Agent, hostedMcpTool } from "@openai/agents" ; const agent = new Agent({ name : "MCP assistant" , instructions : "Use the MCP tools to answer questions." , tools : [ hostedMcpTool({ serverLabel : "gitmcp" , serverUrl : "https://gitmcp.io/openai/codex" , }), ], }); 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 from agents import Agent, HostedMCPTool agent = Agent( name= "MCP assistant" , instructions= "Use the MCP tools to answer questions." , tools=[ HostedMCPTool( tool_config={ "type" : "mcp" , "server_label" : "gitmcp" , "server_url" : "https://gitmcp.io/openai/codex" , "require_approval" : "never" , } ) ], ) Use local transports when your application should connect to the MCP server directly.

Extracted text:

Integrations and observability | OpenAI API

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

After the workflow shape is clear, the next questions are which external surfaces should live inside the agent loop and how you will inspect what actually happened at runtime.

Choose what lives in the SDK

Need

Start with

Why

Give an agent access to public, remotely hosted MCP tools

Hosted MCP tools in the SDK

The model can call the remote MCP server through the hosted surface

Connect local or private MCP servers from your runtime

SDK-managed MCP servers over stdio or streamable HTTP

Your runtime owns the connection, approvals, and network boundaries

Debug prompts, tools, handoffs, or approvals

Built-in tracing

Traces show the end-to-end record before you formalize evals

Tool capability semantics still live in

Using tools

. This page focuses on the SDK-specific MCP wiring and observability loop.

MCP

Use hosted MCP tools when the remote server should run through the model surface.

Attach a hosted MCP server

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

import

{ Agent, hostedMcpTool }

from

"@openai/agents"

;

const

agent =

new

Agent({

name

:

"MCP assistant"

,

instructions

:

"Use the MCP tools to answer questions."

,

tools

: [

hostedMcpTool({

serverLabel

:

"gitmcp"

,

serverUrl

:

"https://gitmcp.io/openai/codex"

,

}),

],

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

16

from

agents

import

Agent, HostedMCPTool

agent = Agent(

name=

"MCP assistant"

,

instructions=

"Use the MCP tools to answer questions."

,

tools=[

HostedMCPTool(

tool_config={

"type"

:

"mcp"

,

"server_label"

:

"gitmcp"

,

"server_url"

:

"https://gitmcp.io/openai/codex"

,

"require_approval"

:

"never"

,

}

)

],

)

Use local transports when your application should connect to the MCP server directly.

Connect a local MCP server

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

{ Agent, MCPServerStdio, run }

from

"@openai/agents"

;

const

server =

new

MCPServerStdio({

name

:

"Filesystem MCP Server"

,

fullCommand

:

"npx -y @modelcontextprotocol/server-filesystem ./sample_files"

,

});

await

server.connect();

try

{

const

agent =

new

Agent({

name

:

"Filesystem assistant"

,

instructions

:

"Read files with the MCP tools before answering."

,

mcpServers

: [server],

});

const

result =

await

run(agent,

"Read the files and list them."

);

console

.log(result.finalOutput);

}

finally

{

await

server.close();

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

import

asyncio

from

agents

import

Agent, Runner

from

agents.mcp

import

MCPServerStdio

async

def

main

() ->

None

:

async

with

MCPServerStdio(

name=

"Filesystem MCP Server"

,

params={

"command"

:

"npx"

,

"args"

: [

"-y"

,

"@modelcontextprotocol/server-filesystem"

,

"./sample_files"

,

],

},

)

as

server:

agent = Agent(

name=

"Filesystem assistant"

,

instructions=

"Read files with the MCP tools before answering."

,

mcp_servers=[server],

)

result =

await

Runner.run(agent,

"Read the files and list them."

)

print

(result.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

The practical split is:

Use

hosted MCP

for public remote servers that fit the platform trust model.

Use

local or private MCP

when your runtime should own connectivity, filtering, or approvals.

For the platform-wide concept, trust model, and product support story, keep

MCP and Connectors

as the canonical reference.

Tracing

Tracing is built into the Agents SDK and is enabled by default in the normal server-side SDK path. Every run can emit a structured record of model calls, tool calls, handoffs, guardrails, and custom spans, which you can inspect in the

Traces dashboard

.

The default trace usually gives you:

the overall run or workflow

each model call

tool calls and their outputs

handoffs and guardrails

any custom spans you wrap around the workflow

If you need less tracing, use the SDK-level or per-run tracing controls rather than removing all observability from the workflow.

Wrap multiple runs in one trace

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

import

{ Agent, run, withTrace }

from

"@openai/agents"

;

const

agent =

new

Agent({

name

:

"Joke generator"

,

instructions

:

"Tell funny jokes."

,

});

await

withTrace(

"Joke workflow"

,

async

() => {

const

first =

await

run(agent,

"Tell me a joke"

);

const

second =

await

run(agent,

`Rate this joke:

${first.finalOutput}

`

);

console

.log(first.finalOutput);

console

.log(second.finalOutput);

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

16

17

18

19

20

21

22

23

import

asyncio

from

agents

import

Agent, Runner, trace

agent = Agent(

name=

"Joke generator"

,

instructions=

"Tell funny jokes."

,

)

async

def

main

() ->

None

:

with

trace(

"Joke workflow"

):

first =

await

Runner.run(agent,

"Tell me a joke"

)

second =

await

Runner.run(

agent,

f"Rate this joke:

{first.final_output}

"

,

)

print

(first.final_output)

print

(second.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

Use traces for two jobs:

Debug one workflow run and understand what happened.

Feed higher-signal examples into

agent workflow evaluation

once you are ready to score behavior systematically.

Next steps

Once the external surfaces are wired in, continue with the guide that covers capability design, review boundaries, or evaluation.

Using tools

See how hosted tools, function tools, and agents-as-tools fit beside MCP.

Guardrails and human review

Add approval or validation boundaries around sensitive capabilities.

Agent workflow evaluation

Move from one-off traces into repeatable grading once behavior stabilizes.
