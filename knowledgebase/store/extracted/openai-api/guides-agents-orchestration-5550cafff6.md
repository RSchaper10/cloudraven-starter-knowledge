---
title: Orchestration and handoffs | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:24.728098+00:00
kind: extracted-doc
---

# Orchestration and handoffs | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/agents/orchestration

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:24.728098+00:00

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

- Orchestration and handoffs | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions Multi-agent workflows are useful when specialists should own different parts of the job.
- The first design choice is deciding who owns the final user-facing answer at each branch of the workflow.
- Choose the orchestration pattern Pattern Use it when What happens Handoffs A specialist should take over the conversation for that branch of the work Control moves to the specialist agent Agents as tools A manager should stay in control and call specialists as bounded capabilities The manager keeps ownership of the reply Use handoffs for delegated ownership Handoffs are the clearest fit when a specialist should own the next response rather than merely helping behind the scenes.
- Delegate with handoffs typescript 1 2 3 4 5 6 7 8 9 import { Agent, handoff } from "@openai/agents" ; const billingAgent = new Agent({ name : "Billing agent" }); const refundAgent = new Agent({ name : "Refund agent" }); const triageAgent = Agent.create({ name : "Triage agent" , handoffs : [billingAgent, handoff(refundAgent)], }); 1 2 3 4 5 6 7 8 9 from agents import Agent, handoff billing_agent = Agent(name= "Billing agent" ) refund_agent = Agent(name= "Refund agent" ) triage_agent = Agent( name= "Triage agent" , handoffs=[billing_agent, handoff(refund_agent)], ) Keep the routing surface legible: Give each specialist a narrow job.
- Keep handoffDescription short and concrete.

Extracted text:

Orchestration and handoffs | OpenAI API

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

Multi-agent workflows are useful when specialists should own different parts of the job. The first design choice is deciding who owns the final user-facing answer at each branch of the workflow.

Choose the orchestration pattern

Pattern

Use it when

What happens

Handoffs

A specialist should take over the conversation for that branch of the work

Control moves to the specialist agent

Agents as tools

A manager should stay in control and call specialists as bounded capabilities

The manager keeps ownership of the reply

Use handoffs for delegated ownership

Handoffs are the clearest fit when a specialist should own the next response rather than merely helping behind the scenes.

Delegate with handoffs

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

import

{ Agent, handoff }

from

"@openai/agents"

;

const

billingAgent =

new

Agent({

name

:

"Billing agent"

});

const

refundAgent =

new

Agent({

name

:

"Refund agent"

});

const

triageAgent = Agent.create({

name

:

"Triage agent"

,

handoffs

: [billingAgent, handoff(refundAgent)],

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

from

agents

import

Agent, handoff

billing_agent = Agent(name=

"Billing agent"

)

refund_agent = Agent(name=

"Refund agent"

)

triage_agent = Agent(

name=

"Triage agent"

,

handoffs=[billing_agent, handoff(refund_agent)],

)

Keep the routing surface legible:

Give each specialist a narrow job.

Keep

handoffDescription

short and concrete.

Split only when the next branch truly needs different instructions, tools, or policy.

At the advanced end, handoffs can also carry structured metadata or filtered history. Those exact APIs stay in the SDK docs because the wiring differs by language.

Use agents as tools for manager-style workflows

Use

agent.asTool()

when the main agent should stay responsible for the final answer and call specialists as helpers.

Call a specialist as a tool

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

import

{ Agent }

from

"@openai/agents"

;

const

summarizer =

new

Agent({

name

:

"Summarizer"

,

instructions

:

"Generate a concise summary of the supplied text."

,

});

const

mainAgent =

new

Agent({

name

:

"Research assistant"

,

tools

: [

summarizer.asTool({

toolName

:

"summarize_text"

,

toolDescription

:

"Generate a concise summary of the supplied text."

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

Agent

summarizer = Agent(

name=

"Summarizer"

,

instructions=

"Generate a concise summary of the supplied text."

,

)

main_agent = Agent(

name=

"Research assistant"

,

tools=[

summarizer.as_tool(

tool_name=

"summarize_text"

,

tool_description=

"Generate a concise summary of the supplied text."

,

)

],

)

This is usually the better fit when:

the manager should synthesize the final answer

the specialist is doing a bounded task like summarization or classification

you want one stable outer workflow with nested specialist calls instead of ownership transfer

Add specialists only when the contract changes

Start with one agent whenever you can. Add specialists only when they materially improve capability isolation, policy isolation, prompt clarity, or trace legibility.

Splitting too early creates more prompts, more traces, and more approval surfaces without necessarily making the workflow better.

Next steps

Once the ownership pattern is clear, continue with the guide that covers the adjacent runtime or state question.

Agent definitions

Refine each specialist’s instructions, tools, and output contract.

Running agents

Understand how handoffs and tools behave inside a run.

Results and state

See how

lastAgent

and resumable state affect the next turn.
