---
title: Local shell | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/tools-local-shell
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:39.232170+00:00
kind: extracted-doc
---

# Local shell | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/tools-local-shell

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:39.232170+00:00

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

- Local shell | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions The local shell tool is outdated.
- For new use cases, use the shell tool with GPT-5.1 instead.
- Local shell is a tool that allows agents to run shell commands locally on a machine you or the user provides.
- It’s designed to work with Codex CLI and codex-mini-latest .
- Commands are executed inside your own runtime, you are fully in control of which commands actually run —the API only returns the instructions, but does not execute them on OpenAI infrastructure.

Extracted text:

Local shell | OpenAI API

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

The local shell tool is outdated. For new use cases, use the

shell

tool with GPT-5.1 instead.

Learn more

.

Local shell is a tool that allows agents to run shell commands locally on a machine you or the user provides. It’s designed to work with

Codex CLI

and

codex-mini-latest

. Commands are executed inside your own runtime,

you are fully in control of which commands actually run

—the API only returns the instructions, but does not execute them on OpenAI infrastructure.

Local shell is available through the

Responses API

for use with

codex-mini-latest

. It is not available on other models, or via the Chat Completions API.

Running arbitrary shell commands can be dangerous. Always sandbox execution or add strict allow- / deny-lists before forwarding a command to the system shell.

See

Codex CLI

for reference implementation.

How it works

The local shell tool enables agents to run in a continuous loop with access to a terminal.

It sends shell commands, which your code executes on a local machine and then returns the output back to the model. This loop allows the model to complete the build-test-run loop without additional intervention by a user.

As part of your code, you’ll need to implement a loop that listens for

local_shell_call

output items and executes the commands they contain. We strongly recommend sandboxing the execution of these commands to prevent any unexpected commands from being executed.

Integrating the local shell tool

These are the high-level steps you need to follow to integrate the computer use tool in your application:

Send a request to the model

: Include the

local_shell

tool as part of the available tools.

Receive a response from the model

: Check if the response has any

local_shell_call

items. This tool call contains an action like

exec

with a command to execute.

Execute the requested action

: Execute through code the corresponding action in the computer or container environment.

Return the action output

: After executing the action, return the command output and metadata like status code to the model.

Repeat

: Send a new request with the updated state as a

local_shell_call_output

, and repeat this loop until the model stops requesting actions or you decide to stop.

Example workflow

Below is a minimal (Python) example showing the request/response loop. For brevity, error handling and security checks are omitted—

do not execute untrusted commands in production without additional safeguards

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

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

import

os

import

shlex

import

subprocess

from

openai

import

OpenAI

client = OpenAI()

# 1) Create the initial response request with the tool enabled

response = client.responses.create(

model=

"codex-mini-latest"

,

tools=[{

"type"

:

"local_shell"

}],

input

=[

{

"role"

:

"user"

,

"content"

: [

{

"type"

:

"input_text"

,

"text"

:

"List files in the current directory"

},

],

}

],

)

while

True

:

# 2) Look for a local_shell_call in the model's output items

shell_calls = []

for

item

in

response.output:

item_type =

getattr

(item,

"type"

,

None

)

if

item_type ==

"local_shell_call"

:

shell_calls.append(item)

elif

item_type ==

"tool_call"

and

getattr

(item,

"tool_name"

,

None

) ==

"local_shell"

:

shell_calls.append(item)

if

not

shell_calls:

# No more commands — the assistant is done.

break

call = shell_calls[

0

]

args =

getattr

(call,

"action"

,

None

)

or

getattr

(call,

"arguments"

,

None

)

# 3) Execute the command locally (here we just trust the command!)

# The command is already split into argv tokens.

def

_get

(

obj, key, default=

None

):

if

isinstance

(obj,

dict

):

return

obj.get(key, default)

return

getattr

(obj, key, default)

timeout_ms = _get(args,

"timeout_ms"

)

command = _get(args,

"command"

)

if

not

command:

break

if

isinstance

(command,

str

):

command = shlex.split(command)

completed = subprocess.run(

command,

cwd=_get(args,

"working_directory"

)

or

os.getcwd(),

env={**os.environ, **(_get(args,

"env"

)

or

{})},

capture_output=

True

,

text=

True

,

timeout=(timeout_ms /

1000

)

if

timeout_ms

else

None

,

)

output_item = {

"type"

:

"local_shell_call_output"

,

"call_id"

:

getattr

(call,

"call_id"

,

None

),

"output"

: completed.stdout + completed.stderr,

}

# 4) Send the output back to the model to continue the conversation

response = client.responses.create(

model=

"codex-mini-latest"

,

tools=[{

"type"

:

"local_shell"

}],

previous_response_id=response.

id

,

input

=[output_item],

)

# Print the assistant's final answer

print

(response.output_text)

Best practices

Sandbox or containerize

execution. Consider using Docker, firejail, or a jailed user account.

Impose resource limits

(time, memory, network). The

timeout_ms

provided by the model is only a hint—you should enforce your own limits.

Filter or scrutinize

high-risk commands (e.g.

rm

,

curl

, network utilities).

Log every command and its output

for auditability and debugging.

Error handling

If the command fails on your side (non-zero exit code, timeout, etc.) you can still send a

local_shell_call_output

; include the error message in the

output

field.

The model can choose to recover or try executing a different command. If you send malformed data (e.g. missing

call_id

) the API returns a standard

400

validation error.
