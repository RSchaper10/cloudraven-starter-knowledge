---
title: Advanced integrations with ChatKit | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/custom-chatkit
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:32.620433+00:00
kind: extracted-doc
---

# Advanced integrations with ChatKit | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/custom-chatkit

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:32.620433+00:00

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

- Advanced integrations with ChatKit | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Sample apps See advanced working examples on GitHub Copy Page More page actions Copy Page More page actions When you need full control—custom authentication, data residency, on‑prem deployment, or bespoke agent orchestration—you can run ChatKit on your own infrastructure.
- Use OpenAI’s advanced self‑hosted option to use your own server and customized ChatKit.
- Our recommended ChatKit integration helps you get started quickly: embed a chat widget, customize its look and feel, let OpenAI host and scale the backend.
- Use simpler integration → Run ChatKit on your own infrastructure At a high level, an advanced ChatKit integration is a process of building your own ChatKit server and adding widgets to build out your chat surface.
- You’ll use OpenAI APIs and your ChatKit server to build a custom chat powered by OpenAI models.

Extracted text:

Advanced integrations with ChatKit | OpenAI API

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

Sample apps

See advanced working examples on GitHub

Copy Page

More page actions

Copy Page

More page actions

When you need full control—custom authentication, data residency, on‑prem deployment, or bespoke agent orchestration—you can run ChatKit on your own infrastructure. Use OpenAI’s advanced self‑hosted option to use your own server and customized ChatKit.

Our recommended ChatKit integration helps you get started quickly: embed a chat widget, customize its look and feel, let OpenAI host and scale the backend.

Use simpler integration →

Run ChatKit on your own infrastructure

At a high level, an advanced ChatKit integration is a process of building your own ChatKit server and adding widgets to build out your chat surface. You’ll use OpenAI APIs and your ChatKit server to build a custom chat powered by OpenAI models.

Set up your ChatKit server

Follow the

server guide on GitHub

to learn how to handle incoming requests, run tools, and stream results back to the client. The snippets below highlight the main components.

1. Install the server package

pip install openai-chatkit

2. Implement a server class

ChatKitServer

drives the conversation. Override

respond

to stream events whenever a user message or client tool output arrives. Helpers like

stream_agent_response

make it simple to connect to the Agents SDK.

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

class

MyChatKitServer

(

ChatKitServer

):

def

__init__

(

self, data_store: Store, file_store: FileStore |

None

=

None

):

super

().__init__(data_store, file_store)

assistant_agent = Agent[AgentContext](

model=

"gpt-4.1"

,

name=

"Assistant"

,

instructions=

"You are a helpful assistant"

,

)

async

def

respond

(

self,

thread: ThreadMetadata,

input

: UserMessageItem | ClientToolCallOutputItem,

context:

Any

,

) -> AsyncIterator[Event]:

agent_context = AgentContext(

thread=thread,

store=self.store,

request_context=context,

)

result = Runner.run_streamed(

self.assistant_agent,

await

to_input_item(

input

, self.to_message_content),

context=agent_context,

)

async

for

event

in

stream_agent_response(agent_context, result):

yield

event

async

def

to_message_content

(

self,

input

: FilePart | ImagePart

) -> ResponseInputContentParam:

raise

NotImplementedError()

3. Expose the endpoint

Use your framework of choice to forward HTTP requests to the server instance. For example, with FastAPI:

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

app = FastAPI()

data_store = SQLiteStore()

file_store = DiskFileStore(data_store)

server = MyChatKitServer(data_store, file_store)

@app.post(

"/chatkit"

)

async

def

chatkit_endpoint

(

request: Request

):

result =

await

server.process(

await

request.body(), {})

if

isinstance

(result, StreamingResult):

return

StreamingResponse(result, media_type=

"text/event-stream"

)

return

Response(content=result.json, media_type=

"application/json"

)

4. Establish data store contract

Implement

chatkit.store.Store

to persist threads, messages, and files using your preferred database. The default example uses SQLite for local development. Consider storing the models as JSON blobs so library updates can evolve the schema without migrations.

5. Provide file store contract

Provide a

FileStore

implementation if you support uploads. ChatKit works with direct uploads (the client POSTs the file to your endpoint) or two-phase uploads (the client requests a signed URL, then uploads to cloud storage). Expose previews to support inline thumbnails and handle deletions when threads are removed.

6. Trigger client tools from the server

Client tools must be registered both in the client options and on your agent. Use

ctx.context.client_tool_call

to enqueue a call from an Agents SDK tool.

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

@function_tool(

description_override=

"Add an item to the user's todo list."

)

async

def

add_to_todo_list

(

ctx: RunContextWrapper[AgentContext], item:

str

) ->

None

:

ctx.context.client_tool_call = ClientToolCall(

name=

"add_to_todo_list"

,

arguments={

"item"

: item},

)

assistant_agent = Agent[AgentContext](

model=

"gpt-4.1"

,

name=

"Assistant"

,

instructions=

"You are a helpful assistant"

,

tools=[add_to_todo_list],

tool_use_behavior=StopAtTools(stop_at_tool_names=[add_to_todo_list.name]),

)

7. Use thread metadata and state

Use

thread.metadata

to store server-side state such as the previous Responses API run ID or custom labels. Metadata is not exposed to the client but is available in every

respond

call.

8. Get tool status updates

Long-running tools can stream progress to the UI with

ProgressUpdateEvent

. ChatKit replaces the progress event with the next assistant message or widget output.

9. Using server context

Pass a custom context object to

server.process(body, context)

to enforce permissions or propagate user identity through your store and file store implementations.

Add inline interactive widgets

Widgets let agents surface rich UI inside the chat surface. Use them for cards, forms, text blocks, lists, and other layouts. The helper

stream_widget

can render a widget immediately or stream updates as they arrive.

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

async

def

respond

(

self,

thread: ThreadMetadata,

input

: UserMessageItem | ClientToolCallOutputItem,

context:

Any

,

) -> AsyncIterator[Event]:

widget = Card(

children=[Text(

id

=

"description"

,

value=

"Generated summary"

,

)]

)

async

for

event

in

stream_widget(

thread,

widget,

generate_id=

lambda

item_type: self.store.generate_item_id(item_type, thread, context),

):

yield

event

ChatKit ships with a wide set of widget nodes (cards, lists, forms, text, buttons, and more). See

widgets guide on GitHub

for all components, props, and streaming guidance.

See the

Widget Builder

to explore and create widgets in an interactive UI.

Use actions

Actions let the ChatKit UI trigger work without sending a user message. Attach an

ActionConfig

to any widget node that supports it—buttons, selects, and other controls can stream new thread items or update widgets in place. When a widget lives inside a

Form

, ChatKit includes the collected form values in the action payload.

On the server, implement the

action

method on

ChatKitServer

to process the payload and optionally stream additional events. You can also handle actions on the client by setting

handler="client"

and responding in JavaScript before forwarding follow-up work to the server.

See the

actions guide on GitHub

for patterns like chaining actions, creating strongly typed payloads, and coordinating client/server handlers.

Resources

Use the following resources and reference to complete your integration.

Design resources

Download

OpenAI Sans Variable

.

Duplicate the file and customize components for your product.

Events reference

ChatKit emits

CustomEvent

instances from the Web Component. The payload shapes are:

1

2

3

4

5

6

7

type Events = {

"chatkit.error"

: CustomEvent<{ error: Error }>;

"chatkit.response.start"

: CustomEvent<void>;

"chatkit.response.end"

: CustomEvent<void>;

"chatkit.thread.change"

: CustomEvent<{ threadId: string |

null

}>;

"chatkit.log"

: CustomEvent<{ name: string; data?: Record<string, unknown> }>;

};

Options reference

Option

Type

Description

Default

apiURL

string

Endpoint that implements the ChatKit server protocol.

required

fetch

typeof fetch

Override fetch calls (for custom headers or auth).

window.fetch

theme

"light" | "dark"

UI theme.

"light"

initialThread

string | null

Thread to open on mount;

null

shows the new thread view.

null

clientTools

Record<string, Function>

Client-executed tools exposed to the model.

header

object | boolean

Header configuration or

false

to hide the header.

true

newThreadView

object

Customize greeting text and starter prompts.

messages

object

Configure message affordances (feedback, annotations, etc.).

composer

object

Control attachments, entity tags, and placeholder text.

entities

object

Callbacks for entity lookup, click handling, and previews.
