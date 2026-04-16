---
title: Theming and customization in ChatKit | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/chatkit-themes
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:30.769305+00:00
kind: extracted-doc
---

# Theming and customization in ChatKit | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/chatkit-themes

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:30.769305+00:00

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

- Theming and customization in ChatKit | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions After following the ChatKit quickstart , learn how to change themes and add customization to your chat embed.
- Match your app’s aesthetic with light and dark themes, setting an accent color, controlling the density, and rounded corners.
- Overview At a high level, customize the theme by passing in an options object.
- If you followed the ChatKit quickstart to embed ChatKit in your frontend, use the React syntax below.
- React : Pass options to useChatKit({...}) Advanced integrations : Set options with chatkit.setOptions({...}) In both integration types, the shape of the options object is the same.

Extracted text:

Theming and customization in ChatKit | OpenAI API

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

After following the

ChatKit quickstart

, learn how to change themes and add customization to your chat embed. Match your app’s aesthetic with light and dark themes, setting an accent color, controlling the density, and rounded corners.

Overview

At a high level, customize the theme by passing in an options object. If you followed the

ChatKit quickstart

to embed ChatKit in your frontend, use the React syntax below.

React

: Pass options to

useChatKit({...})

Advanced integrations

: Set options with

chatkit.setOptions({...})

In both integration types, the shape of the options object is the same.

Explore customization options

Visit

ChatKit Studio

to see working implementations of ChatKit and interactive builders. If you like building by trying things rather than reading, these resources are a good starting point.

Explore ChatKit UI

chatkit.world

Play with an interactive demo of ChatKit.

Widget builder

Browse available widgets.

ChatKit playground

Play with an interactive demo to learn by doing.

See working examples

Samples on GitHub

See working examples of ChatKit and get inspired.

Starter app repo

Clone a repo to start with a fully working template.

Change the theme

Match the look and feel of your product by specifying colors, typography, and more. Below, we set to dark mode, change colors, round the corners, adjust the information density, and set the font.

For all theming options, see the

API reference

.

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

const options: Partial<ChatKitOptions> = {

theme: {

colorScheme:

"dark"

,

color: {

accent: {

primary:

"#2D8CFF"

,

level:

2

}

},

radius:

"round"

,

density:

"compact"

,

typography: { fontFamily:

"'Inter', sans-serif"

},

},

};

Customize the start screen text

Let users know what to ask or guide their first input by changing the composer’s placeholder text.

1

2

3

4

5

6

7

8

const options: Partial<ChatKitOptions> = {

composer: {

placeholder:

"Ask anything about your data…"

,

},

startScreen: {

greeting:

"Welcome to FeedbackBot!"

,

},

};

Show starter prompts for new threads

Guide users on what to ask or do by suggesting prompt ideas when starting a conversation.

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

const options: Partial<ChatKitOptions> = {

startScreen: {

greeting:

"What can I help you build today?"

,

prompts: [

{

name:

"Check on the status of a ticket"

,

prompt:

"Can you help me check on the status of a ticket?"

,

icon:

"search"

},

{

name:

"Create Ticket"

,

prompt:

"Can you help me create a new support ticket?"

,

icon:

"write"

},

],

},

};

Add custom buttons to the header

Custom header buttons help you add navigation, context, or actions relevant to your integration.

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

const options: Partial<ChatKitOptions> = {

header: {

customButtonLeft: {

icon:

"settings-cog"

,

onClick: () => openProfileSettings(),

},

customButtonRight: {

icon:

"home"

,

onClick: () => openHomePage(),

},

},

};

Enable file attachments

Attachments are disabled by default. To enable them, add attachments configuration. Unless you are doing a custom backend, you must use the

hosted

upload strategy. See the Python SDK docs for more information on other upload strategies work with a custom backend.

You can also control the number, size, and types of files that users can attach to messages.

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

const options: Partial<ChatKitOptions> = {

composer: {

attachments: {

uploadStrategy: { type: 'hosted' },

maxSize:

20

*

1024

*

1024

,

// 20MB per file

maxCount:

3

,

accept: {

"application/pdf"

: [

".pdf"

],

"image/*"

: [

".png"

,

".jpg"

] },

},

},

}

Enable @mentions in the composer with entity tags

Let users tag custom “entities” with @-mentions. This enables richer conversation context and interactivity.

Use

onTagSearch

to return a list of entities based on the input query.

Use

onClick

to handle the click event of an entity.

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

const options: Partial<ChatKitOptions> = {

entities: {

async onTagSearch(query) {

return [

{

id:

"user_123"

,

title:

"Jane Doe"

,

group:

"People"

,

interactive:

true

,

},

{

id:

"document_123"

,

title:

"Quarterly Plan"

,

group:

"Documents"

,

interactive:

true

,

},

]

},

onClick: (entity) => {

navigateToEntity(entity.id);

},

},

};

Customize how entity tags appear

You can customize the appearance of entity tags on mouseover using widgets. Show rich previews such as a business card, document summary, or image when the user hovers over an entity tag.

Widget builder

Browse available widgets.

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

const options: Partial<ChatKitOptions> = {

entities: {

async onTagSearch() {

/* ... */

},

onRequestPreview: async (entity) => ({

preview: {

type:

"Card"

,

children: [

{ type:

"Text"

, value: `Profile: ${entity.title}` },

{ type:

"Text"

, value:

"Role: Developer"

},

],

},

}),

},

};

Add custom tools to the composer

Enhance productivity by letting users trigger app-specific actions from the composer bar. The selected tool will be sent to the model as a tool preference.

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

const options: Partial<ChatKitOptions> = {

composer: {

tools: [

{

id: 'add-note',

label: 'Add Note',

icon: 'write',

pinned:

true

,

},

],

},

};

Toggle UI regions and features

Disable major UI regions and features if you need more customization over the options available in the header and want to implement your own instead. Disabling history can be useful when the concept of threads and history doesn’t make sense for your use case—e.g., in a support chatbot.

1

2

3

4

const options: Partial<ChatKitOptions> = {

history: { enabled:

false

},

header: { enabled:

false

},

};

Override the locale

Override the default locale if you have an app-wide language setting. By default, the locale is set to the browser’s locale.

1

2

3

const options: Partial

<ChatKitOptions>

= {

locale:

'de-DE'

,

};
