---
title: Apply Patch | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/tools-apply-patch
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:38.664026+00:00
kind: extracted-doc
---

# Apply Patch | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/tools-apply-patch

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:38.664026+00:00

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

- Apply Patch | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Cookbook example Build a coding agent with GPT-5.1 and the apply_patch tool Copy Page More page actions Copy Page More page actions The apply_patch tool lets GPT-5.1 create, update, and delete files in your codebase using structured diffs.
- Instead of just suggesting edits, the model emits patch operations that your application applies and then reports back on, enabling iterative, multi-step code editing workflows.
- When to use Some common scenarios where you would use apply_patch: Multi-file refactors – Rename symbols, extract helpers, or reorganize modules across many files at once.
- Bug fixes – Have the model both diagnose issues and emit precise patches.
- Tests & docs generation – Create new test files, fixtures, and documentation alongside code changes.

Extracted text:

Apply Patch | OpenAI API

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

Cookbook example

Build a coding agent with GPT-5.1 and the apply_patch tool

Copy Page

More page actions

Copy Page

More page actions

The

apply_patch

tool lets GPT-5.1 create, update, and delete files in your codebase using structured diffs. Instead of just suggesting edits, the model emits patch operations that your application applies and then reports back on, enabling iterative, multi-step code editing workflows.

When to use

Some common scenarios where you would use apply_patch:

Multi-file refactors

– Rename symbols, extract helpers, or reorganize modules across many files at once.

Bug fixes

– Have the model both diagnose issues and emit precise patches.

Tests & docs generation

– Create new test files, fixtures, and documentation alongside code changes.

Migrations & mechanical edits

– Apply repetitive, structured updates (API migrations, type annotations, formatting fixes, etc.).

If you can describe your repo and desired change in text, apply_patch can usually generate the corresponding diffs.

Use apply patch tool with Responses API

At a high level, using

apply_patch

with the Responses API looks like this:

Call the Responses API with the

apply_patch

tool

Provide the model with context about available files (or a summary) in your

input

, or give the model tools for exploring your file system.

Enable the tool with

tools=[{"type": "apply_patch"}]

.

Let the model return one or more patch operations

The Response output includes one or more

apply_patch_call

objects.

Each call describes a single file operation: create, update, or delete.

Apply patches in your environment

Run a patch harness or script that:

Interprets the

operation

diff for each

apply_patch_call

.

Applies the patch to your working directory or repo.

Records whether each patch succeeded and any logs or error messages.

Report patch results back to the model

Call the Responses API again, either with

previous_response_id

or by passing back your conversation items into

input

.

Include an

apply_patch_call_output

event for each

call_id

, with a

status

and optional

output

string.

Keep

tools=[{"type": "apply_patch"}]

so the model can continue editing if needed.

Let the model continue or explain changes

The model may issue more

apply_patch_call

operations, or

Provide a human-facing explanation of what it changed and why.

Example: Renaming a function with Apply Patch Tool

Step 1: Ask the model to plan and emit patches

Ask the model to plan and emit patches

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

from openai import OpenAI

client = OpenAI()

# For brevity, we are including file context in the example input.

# Most agentic use cases should instead equip the model with tools

# for exploring file system state.

RESPONSE_INPUT =

""

"

The user has the following files:

<BEGIN_FILES>

===== lib/fib.py

def fib(n):

if n <= 1:

return n

return fib(n-1) + fib(n-2)

===== run.py

from lib.fib import fib

def main():

print(fib(42))

<END_FILES>

You are a helpful coding assistant that should assist the user with whatever they

ask.

User query:

Help me rename the fib() function to fibonacci()

"

""

response = client.responses.create(

model=

"gpt-5.1"

,

input=RESPONSE_INPUT,

tools=[{

"type"

:

"apply_patch"

}],

)

# response.output may contain multiple apply_patch_call entries, e.g.:

# - update lib/fib.py

# - update run.py

patch_calls = [

item for item in response.output

if item[

"type"

] ==

"apply_patch_call"

]

Example

apply_patch_call

object

Example apply_patch_call object

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

{

"id"

:

"apc_08f3d96c87a585390069118b594f7481a088b16cda7d9415fe"

,

"type"

:

"apply_patch_call"

,

"status"

:

"completed"

,

"call_id"

:

"call_Rjsqzz96C5xzPb0jUWJFRTNW"

,

"operation"

: {

"type"

:

"update_file"

,

"diff"

:

"

@@

-def fib(n):

+def fibonacci(n):

if n <= 1:

return n

- return fib(n-1) + fib(n-2) + return fibonacci(n-1) + fibonacci(n-2),

"

,

"path"

:

"lib/fib.py"

}

}

Step 2: Apply the patch and send results back

Apply the patch and return results

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

from apply_patch_harness import apply_operation # your implementation

results = []

for call in patch_calls:

op = call[

"operation"

]

success, maybe_log_output = apply_operation(op)

results.append({

"type"

:

"apply_patch_call_output"

,

"call_id"

: call[

"call_id"

],

"status"

:

"completed"

if success else

"failed"

,

"output"

: maybe_log_output,

})

followup = client.responses.create(

model=

"gpt-5.1"

,

previous_response_id=response.id,

input=results,

tools=[{

"type"

:

"apply_patch"

}],

)

If a patch fails (for example, file not found), set

status: "failed"

and include a helpful

output

string so the model can recover:

Report a failed apply_patch call

1

2

3

4

5

6

{

"type"

:

"apply_patch_call_output"

,

"call_id"

:

"call_cNWm41dB3RyQcLNOVTIPBWZU"

,

"status"

:

"failed"

,

"output"

:

"Could not apply patch to lib/foo.py — file not found on disk"

}

Apply patch operations

Operation Type

Purpose

Payload

create_file

Create a new file at

path

.

diff

is a V4A diff representing the full file contents.

update_file

Modify an existing file at

path

.

diff

is a V4A diff with additions, deletions, or replacements.

delete_file

Remove a file at

path

.

No

diff

; delete the file entirely.

Your patch harness is responsible for interpreting the V4A diff format and applying changes. For reference implementations, see the

Python Agents SDK

or

TypeScript Agents SDK

code.

Implementing the patch harness

When using the

apply_patch

tool, you don’t provide an input schema; the model knows how to construct

operation

objects. Your job is to:

Parse operations from the Response

Scan the Response for items with

type: "apply_patch_call"

.

For each call, inspect

operation.type

,

operation.path

, and any potential

diff

.

Apply file operations

For

create_file

and

update_file

, apply the V4A diff to the file system or in-memory workspace.

For

delete_file

, remove the file at

path

.

Record whether each operation succeeded and any logs or error messages.

Return

apply_patch_call_output

events

For each

call_id

, emit exactly one

apply_patch_call_output

event with:

status: "completed"

if the operation was applied successfully.

status: "failed"

if you encountered an error (include a short human-readable

output

string).

Safety and robustness

Path validation

: Prevent directory traversal and restrict edits to allowed directories.

Backups

: Consider backing up files (or working in a scratch copy) before applying patches.

Error handling

: Always return a

failed

status with an informative

output

string when patches cannot be applied.

Atomicity

: Decide whether you want “all-or-nothing” semantics (rollback if any patch fails) or per-file success/failure.

Use the apply patch tool with the Agents SDK

Alternatively, you can use the

Agents SDK

to use the apply patch tool. You’ll still have to implement the harness that handles the actual file operations but you can use the

applyDiff

function to handle the diff processing.

Use the apply patch tool with the Agents SDK

javascript

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

import

{ applyDiff, Agent, run, applyPatchTool, Editor }

from

"@openai/agents"

;

class

WorkspaceEditor

implements

Editor

{

async

createFile

(

operation

)

{

// convert the diff to the file content

const

content = applyDiff(

""

, operation.diff,

"create"

);

// write the file content to the file system

return

{

status

:

"completed"

,

output

:

`Created

${operation.path}

`

};

}

async

updateFile

(

operation

)

{

// read the file content from the file system

const

current =

""

;

// convert the diff to the new file content

const

newContent = applyDiff(current, operation.diff);

// write the updated file content to the file system

return

{

status

:

"completed"

,

output

:

`Updated

${operation.path}

`

};

}

async

deleteFile

(

operation

)

{

// delete the file from the file system

return

{

status

:

"completed"

,

output

:

`Deleted

${operation.path}

`

};

}

}

const

editor =

new

WorkspaceEditor();

const

agent =

new

Agent({

name

:

"Patch Assistant"

,

model

:

"gpt-5.1"

,

instructions

:

"You can edit files inside the /tmp directory using the apply_patch tool."

,

tools

: [

applyPatchTool({

editor,

// could also be a function for you to determine if approval is needed

needsApproval

:

true

,

onApproval

:

async

(_ctx, _approvalItem) => {

// create your own approval logic

return

{

approve

:

true

};

},

}),

],

});

const

result =

await

run(

agent,

"Create tasks.md with a shopping checklist of 5 entries."

);

console

.log(

`\nFinal response:\n

${result.finalOutput}

`

);

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

from

agents

import

Agent, ApplyPatchTool, Runner, apply_diff

class

WorkspaceEditor

:

async

def

create_file

(

self, operation

):

# convert the diff to the file content

content = apply_diff(

""

, operation.diff, create=

True

)

# write the file content to the file system

return

{

"status"

:

"completed"

,

"output"

:

f"Created

{operation.path}

"

}

async

def

update_file

(

self, operation

):

# read the file content from the file system

current =

""

# convert the diff to the new file content

new_content = apply_diff(current, operation.diff)

# write the updated file content to the file system

return

{

"status"

:

"completed"

,

"output"

:

f"Updated

{operation.path}

"

}

async

def

delete_file

(

self, operation

):

# delete the file from the file system

return

{

"status"

:

"completed"

,

"output"

:

f"Deleted

{operation.path}

"

}

editor = WorkspaceEditor()

agent = Agent(

name=

"Patch Assistant"

,

model=

"gpt-5.1"

,

instructions=

"You can edit files inside the /tmp directory using the apply_patch tool."

,

tools=[

ApplyPatchTool(

editor=editor,

# could also be a function for you to determine if approval is needed

needs_approval=

True

,

# Implement your own approval logic

on_approval=

lambda

_ctx, _approval_item: {

"approve"

:

True

},

),

],

)

async

def

main

():

result =

await

Runner.run(

agent,

input

=

"Create tasks.md with a shopping checklist of 5 entries."

,

)

print

(

f"\nFinal response:\n

{result.final_output}

"

)

if

__name__ ==

"__main__"

:

import

asyncio

asyncio.run(main())

You can find full working examples on GitHub.

Apply patch tool example - TypeScript

Example of how to use the apply patch tool with the Agents SDK in TypeScript

Apply patch tool example - Python

Example of how to use the apply patch tool with the Agents SDK in Python

Handling common errors

Use

status: "failed"

plus a clear

output

message to help the model recover.

File not found

Patch conflict

File not found

File not found error

1

2

3

4

5

6

{

"type"

:

"apply_patch_call_output"

,

"call_id"

:

"call_abc"

,

"status"

:

"failed"

,

"output"

:

"Error: File not found at path 'lib/baz.py'"

}

Patch conflict

Patch conflict error

1

2

3

4

5

6

{

"type"

:

"apply_patch_call_output"

,

"call_id"

:

"call_abc"

,

"status"

:

"failed"

,

"output"

:

"Error: Invalid Context:\n@@ def fib(n):"

}

The model can then adjust future diffs (for example, by re-reading a file in your prompt or simplifying a change) based on these error messages.

Best practices

Give clear file context

When you call the Responses API, include either an inline snapshot of your files (as in the example), or give the model tools for exploring your filesystem (like the

shell

tool).

Consider using with the

shell

tool

When used in conjunction with the

shell

tool, the model can explore file system directories, read files, and grep for keywords, enabling agentic file discovery and editing.

Encourage small, focused diffs

In your system instructions, nudge the model toward minimal, targeted edits rather than huge rewrites.

Make sure changes apply cleanly

After a series of patches, run your tests or linters and share failures back in the next

input

so the model can fix them.

Usage notes

API Availability

Supported models

Responses

Chat Completions

Assistants

GPT-5.4

GPT-5.2

GPT-5.1
