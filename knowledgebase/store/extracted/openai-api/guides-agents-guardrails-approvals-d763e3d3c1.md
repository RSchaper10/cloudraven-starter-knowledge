---
title: Guardrails and human review | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:25.392307+00:00
kind: extracted-doc
---

# Guardrails and human review | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/agents/guardrails-approvals

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:25.392307+00:00

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

- Guardrails and human review | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions Use guardrails for automatic checks and human review for approval decisions.
- Together, they define when a run should continue, pause, or stop.
- Guardrails validate input, output, or tool behavior automatically.
- Human review pauses the run so a person or policy can approve or reject a sensitive action.
- Choose the right control Use case Start with Block disallowed user requests before the main model runs Input guardrails Validate or redact the final output before it leaves the system Output guardrails Check arguments or results around a function tool call Tool guardrails Pause before side effects like cancellations, edits, shell commands, or sensitive MCP actions Human-in-the-loop approvals Add a blocking guardrail Use input guardrails when you want a fast validation step to run before the expensive or side-effecting part of the workflow starts.

Extracted text:

Guardrails and human review | OpenAI API

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

Use guardrails for automatic checks and human review for approval decisions. Together, they define when a run should continue, pause, or stop.

Guardrails

validate input, output, or tool behavior automatically.

Human review

pauses the run so a person or policy can approve or reject a sensitive action.

Choose the right control

Use case

Start with

Block disallowed user requests before the main model runs

Input guardrails

Validate or redact the final output before it leaves the system

Output guardrails

Check arguments or results around a function tool call

Tool guardrails

Pause before side effects like cancellations, edits, shell commands, or sensitive MCP actions

Human-in-the-loop approvals

Add a blocking guardrail

Use input guardrails when you want a fast validation step to run before the expensive or side-effecting part of the workflow starts.

Block a request with an input guardrail

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

import

{

Agent,

InputGuardrailTripwireTriggered,

run,

}

from

"@openai/agents"

;

import

{ z }

from

"zod"

;

const

guardrailAgent =

new

Agent({

name

:

"Homework check"

,

instructions

:

"Detect whether the user is asking for math homework help."

,

outputType

: z.object({

isMathHomework

: z.boolean(),

reasoning

: z.string(),

}),

});

const

agent =

new

Agent({

name

:

"Customer support"

,

instructions

:

"Help customers with support questions."

,

inputGuardrails

: [

{

name

:

"Math homework guardrail"

,

runInParallel

:

false

,

async

execute

(

{ input, context }

)

{

const

result =

await

run(guardrailAgent, input, { context });

return

{

outputInfo

: result.finalOutput,

tripwireTriggered

: result.finalOutput?.isMathHomework ===

true

,

};

},

},

],

});

try

{

await

run(agent,

"Can you solve 2x + 3 = 11 for me?"

);

}

catch

(error) {

if

(error

instanceof

InputGuardrailTripwireTriggered) {

console

.log(

"Guardrail blocked the request."

);

}

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

import

asyncio

from

pydantic

import

BaseModel

from

agents

import

(

Agent,

GuardrailFunctionOutput,

InputGuardrailTripwireTriggered,

RunContextWrapper,

Runner,

TResponseInputItem,

input_guardrail,

)

class

MathHomeworkOutput

(

BaseModel

):

is_math_homework:

bool

reasoning:

str

guardrail_agent = Agent(

name=

"Homework check"

,

instructions=

"Detect whether the user is asking for math homework help."

,

output_type=MathHomeworkOutput,

)

@input_guardrail

async

def

math_guardrail

(

ctx: RunContextWrapper[

None

],

agent: Agent,

input

:

str

|

list

[TResponseInputItem],

) -> GuardrailFunctionOutput:

result =

await

Runner.run(guardrail_agent,

input

, context=ctx.context)

return

GuardrailFunctionOutput(

output_info=result.final_output,

tripwire_triggered=result.final_output.is_math_homework,

)

agent = Agent(

name=

"Customer support"

,

instructions=

"Help customers with support questions."

,

input_guardrails=[math_guardrail],

)

async

def

main

() ->

None

:

try

:

await

Runner.run(agent,

"Can you solve 2x + 3 = 11 for me?"

)

except

InputGuardrailTripwireTriggered:

print

(

"Guardrail blocked the request."

)

if

__name__ ==

"__main__"

:

asyncio.run(main())

Use blocking execution when the cost or risk of starting the main agent is too high. Use parallel guardrails when lower latency matters more than avoiding speculative work.

Pause for human review

Approvals are the human-in-the-loop path for tool calls. The model can still decide that an action is needed, but the run pauses until you approve or reject it.

Pause for approval before a sensitive action

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

28

29

30

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

cancelOrder = tool({

name

:

"cancel_order"

,

description

:

"Cancel a customer order."

,

parameters

: z.object({

orderId

: z.number() }),

needsApproval

:

true

,

async

execute

(

{ orderId }

)

{

return

`Cancelled order

${orderId}

`

;

},

});

const

agent =

new

Agent({

name

:

"Support agent"

,

instructions

:

"Handle support requests and ask for approval when needed."

,

tools

: [cancelOrder],

});

let

result =

await

run(agent,

"Cancel order 123."

);

if

(result.interruptions?.length) {

const

state = result.state;

for

(

const

interruption

of

result.interruptions) {

state.approve(interruption);

}

result =

await

run(agent, state);

}

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

import

asyncio

from

agents

import

Agent, Runner, function_tool

@function_tool(

needs_approval=

True

)

async

def

cancel_order

(

order_id:

int

) ->

str

:

return

f"Cancelled order

{order_id}

"

agent = Agent(

name=

"Support agent"

,

instructions=

"Handle support requests and ask for approval when needed."

,

tools=[cancel_order],

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

"Cancel order 123."

)

if

result.interruptions:

state = result.to_state()

for

interruption

in

result.interruptions:

state.approve(interruption)

result =

await

Runner.run(agent, state)

print

(result.final_output)

if

__name__ ==

"__main__"

:

asyncio.run(main())

This same interruption pattern applies even when the approving tool lives deeper in the workflow, such as after a handoff or inside a nested

agent.asTool()

call.

Approval lifecycle

When a tool call needs review, the SDK follows the same pattern every time:

The run records an approval interruption instead of executing the tool.

The result returns

interruptions

plus a resumable

state

.

Your application approves or rejects the pending items.

You resume the same run from

state

instead of starting a new user turn.

If the review might take time, serialize

state

, store it, and resume later. That’s still the same run.

Workflow boundaries matter

Agent-level guardrails don’t run everywhere:

Input guardrails run only for the first agent in the chain.

Output guardrails run only for the agent that produces the final output.

Tool guardrails run on the function tools they’re attached to.

If you need checks around every custom tool call in a manager-style workflow, don’t rely only on agent-level input or output guardrails. Put validation next to the tool that creates the side effect.

Streaming and delayed review use the same state model

Streaming doesn’t create a separate approval system. If a streamed run pauses, wait for it to settle, inspect

interruptions

, resolve the approvals, and resume from the same

state

. If the review happens later, store the serialized state and continue the same run when the decision arrives.

Next steps

Once the control boundaries are clear, continue with the guide that covers the runtime or tool surface around them.

Running agents

See how interruptions and resumptions fit into the runtime loop.

Results and state

Learn which result surfaces paused runs return to your application.

Using tools

Decide which tool surfaces need validation or approval before side effects happen.
