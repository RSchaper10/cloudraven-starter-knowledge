---
title: Code Interpreter | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/tools-code-interpreter
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:40.350590+00:00
kind: extracted-doc
---

# Code Interpreter | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/tools-code-interpreter

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:40.350590+00:00

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

- Code Interpreter | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions The Code Interpreter tool allows models to write and run Python code in a sandboxed environment to solve complex problems in domains like data analysis, coding, and math.
- Use it for: Processing files with diverse data and formatting Generating files with data and images of graphs Writing and running code iteratively to solve problems—for example, a model that writes code that fails to run can keep rewriting and running that code until it succeeds Boosting visual intelligence in our latest reasoning models (like o3 and o4-mini ).
- The model can use this tool to crop, zoom, rotate, and otherwise process and transform images.
- Here’s an example of calling the Responses API with a tool call to Code Interpreter: Use the Responses API with Code Interpreter python 1 2 3 4 5 6 7 8 9 10 11 12 curl https://api.openai.com/v1/responses \ -H "Content-Type: application/json" \ -H "Authorization: Bearer $OPENAI_API_KEY " \ -d '{ "model": "gpt-4.1", "tools": [{ "type": "code_interpreter", "container": { "type": "auto", "memory_limit": "4g" } }], "instructions": "You are a personal math tutor.
- When asked a math question, write and run code using the python tool to answer the question.", "input": "I need to solve the equation 3x + 11 = 14.

Extracted text:

Code Interpreter | OpenAI API

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

The Code Interpreter tool allows models to write and run Python code in a sandboxed environment to solve complex problems in domains like data analysis, coding, and math. Use it for:

Processing files with diverse data and formatting

Generating files with data and images of graphs

Writing and running code iteratively to solve problems—for example, a model that writes code that fails to run can keep rewriting and running that code until it succeeds

Boosting visual intelligence in our latest reasoning models (like

o3

and

o4-mini

). The model can use this tool to crop, zoom, rotate, and otherwise process and transform images.

Here’s an example of calling the

Responses API

with a tool call to Code Interpreter:

Use the Responses API with Code Interpreter

python

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

curl https://api.openai.com/v1/responses \

-H

"Content-Type: application/json"

\

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

\

-d

'{

"model": "gpt-4.1",

"tools": [{

"type": "code_interpreter",

"container": { "type": "auto", "memory_limit": "4g" }

}],

"instructions": "You are a personal math tutor. When asked a math question, write and run code using the python tool to answer the question.",

"input": "I need to solve the equation 3x + 11 = 14. Can you help me?"

}'

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

OpenAI

from

"openai"

;

const

client =

new

OpenAI();

const

instructions =

`

You are a personal math tutor. When asked a math question,

write and run code using the python tool to answer the question.

`

;

const

resp =

await

client.responses.create({

model

:

"gpt-4.1"

,

tools

: [

{

type

:

"code_interpreter"

,

container

: {

type

:

"auto"

,

memory_limit

:

"4g"

},

},

],

instructions,

input

:

"I need to solve the equation 3x + 11 = 14. Can you help me?"

,

});

console

.log(

JSON

.stringify(resp.output,

null

,

2

));

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

from

openai

import

OpenAI

client = OpenAI()

instructions =

"""

You are a personal math tutor. When asked a math question,

write and run code using the python tool to answer the question.

"""

resp = client.responses.create(

model=

"gpt-4.1"

,

tools=[

{

"type"

:

"code_interpreter"

,

"container"

: {

"type"

:

"auto"

,

"memory_limit"

:

"4g"

}

}

],

instructions=instructions,

input

=

"I need to solve the equation 3x + 11 = 14. Can you help me?"

,

)

print

(resp.output)

While we call this tool Code Interpreter, the model knows it as the “python tool”. Models usually understand prompts that refer to the code interpreter tool, however, the most explicit way to invoke this tool is to ask for “the python tool” in your prompts.

Containers

The Code Interpreter tool requires a

container object

. A container is a fully sandboxed virtual machine that the model can run Python code in. This container can contain files that you upload, or that it generates.

There are two ways to create containers:

Auto mode: as seen in the example above, you can do this by passing the

"container": { "type": "auto", "memory_limit": "4g", "file_ids": ["file-1", "file-2"] }

property in the tool configuration while creating a new Response object. This automatically creates a new container, or reuses an active container that was used by a previous

code_interpreter_call

item in the model’s context. Leaving out

memory_limit

keeps the default 1 GB tier for the container. Look for the

code_interpreter_call

item in the output of this API request to find the

container_id

that was generated or used.

Explicit mode: here, you explicitly

create a container

using the

v1/containers

endpoint, including the

memory_limit

you need (for example

"memory_limit": "4g"

), and assign its

id

as the

container

value in the tool configuration in the Response object. For example:

Use explicit container creation

python

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

curl https://api.openai.com/v1/containers \

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

\

-H

"Content-Type: application/json"

\

-d

'{

"name": "My Container",

"memory_limit": "4g"

}'

# Use the returned container id in the next call:

curl https://api.openai.com/v1/responses \

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

\

-H

"Content-Type: application/json"

\

-d

'{

"model": "gpt-4.1",

"tools": [{

"type": "code_interpreter",

"container": "cntr_abc123"

}],

"tool_choice": "required",

"input": "use the python tool to calculate what is 4 * 3.82. and then find its square root and then find the square root of that result"

}'

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

openai

import

OpenAI

client = OpenAI()

container = client.containers.create(name=

"test-container"

, memory_limit=

"4g"

)

response = client.responses.create(

model=

"gpt-4.1"

,

tools=[{

"type"

:

"code_interpreter"

,

"container"

: container.

id

}],

tool_choice=

"required"

,

input

=

"use the python tool to calculate what is 4 * 3.82. and then find its square root and then find the square root of that result"

)

print

(response.output_text)

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

OpenAI

from

"openai"

;

const

client =

new

OpenAI();

const

container =

await

client.containers.create({

name

:

"test-container"

,

memory_limit

:

"4g"

});

const

resp =

await

client.responses.create({

model

:

"gpt-4.1"

,

tools

: [

{

type

:

"code_interpreter"

,

container

: container.id

}

],

tool_choice

:

"required"

,

input

:

"use the python tool to calculate what is 4 * 3.82. and then find its square root and then find the square root of that result"

});

console

.log(resp.output_text);

You can choose from

1g

(default),

4g

,

16g

, or

64g

. Higher tiers offer more RAM for the session and are billed at the

built-in tools rates

for Code Interpreter. The selected

memory_limit

applies for the entire life of that container, whether it was created automatically or via the containers API.

Note that containers created with the auto mode are also accessible using the

/v1/containers

endpoint.

Expiration

We highly recommend you treat containers as ephemeral and store all data related to the use of this tool on your own systems. Expiration details:

A container expires if it is not used for 20 minutes. When this happens, using the container in

v1/responses

will fail. You’ll still be able to see a snapshot of the container’s metadata at its expiry, but all data associated with the container will be discarded from our systems and not recoverable. You should download any files you may need from the container while it is active.

You can’t move a container from an expired state to an active one. Instead, create a new container and upload files again. Note that any state in the old container’s memory (like python objects) will be lost.

Any container operation, like retrieving the container, or adding or deleting files from the container, will automatically refresh the container’s

last_active_at

time.

Work with files

When running Code Interpreter, the model can create its own files. For example, if you ask it to construct a plot, or create a CSV, it creates these images directly on your container. When it does so, it cites these files in the

annotations

of its next message. Here’s an example:

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

{

"id"

:

"msg_682d514e268c8191a89c38ea318446200f2610a7ec781a4f"

,

"content"

: [

{

"annotations"

: [

{

"file_id"

:

"cfile_682d514b2e00819184b9b07e13557f82"

,

"index"

:

null

,

"type"

:

"container_file_citation"

,

"container_id"

:

"cntr_682d513bb0c48191b10bd4f8b0b3312200e64562acc2e0af"

,

"end_index"

:

0

,

"filename"

:

"cfile_682d514b2e00819184b9b07e13557f82.png"

,

"start_index"

:

0

}

],

"text"

:

"Here is the histogram of the RGB channels for the uploaded image. Each curve represents the distribution of pixel intensities for the red, green, and blue channels. Peaks toward the high end of the intensity scale (right-hand side) suggest a lot of brightness and strong warm tones, matching the orange and light background in the image. If you want a different style of histogram (e.g., overall intensity, or quantized color groups), let me know!"

,

"type"

:

"output_text"

,

"logprobs"

: []

}

],

"role"

:

"assistant"

,

"status"

:

"completed"

,

"type"

:

"message"

}

You can download these constructed files by calling the

get container file content

method.

Any

files in the model input

get automatically uploaded to the container. You do not have to explicitly upload it to the container.

Uploading and downloading files

Add new files to your container using

Create container file

. This endpoint accepts either a multipart upload or a JSON body with a

file_id

. List existing container files with

List container files

and download bytes from

Retrieve container file content

.

Dealing with citations

Files and images generated by the model are returned as annotations on the assistant’s message.

container_file_citation

annotations point to files created in the container. They include the

container_id

,

file_id

, and

filename

. You can parse these annotations to surface download links or otherwise process the files.

Supported files

File format

MIME type

.c

text/x-c

.cs

text/x-csharp

.cpp

text/x-c++

.csv

text/csv

.doc

application/msword

.docx

application/vnd.openxmlformats-officedocument.wordprocessingml.document

.html

text/html

.java

text/x-java

.json

application/json

.md

text/markdown

.pdf

application/pdf

.php

text/x-php

.pptx

application/vnd.openxmlformats-officedocument.presentationml.presentation

.py

text/x-python

.py

text/x-script.python

.rb

text/x-ruby

.tex

text/x-tex

.txt

text/plain

.css

text/css

.js

text/javascript

.sh

application/x-sh

.ts

application/typescript

.csv

application/csv

.jpeg

image/jpeg

.jpg

image/jpeg

.gif

image/gif

.pkl

application/octet-stream

.png

image/png

.tar

application/x-tar

.xlsx

application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

.xml

application/xml or "text/xml"

.zip

application/zip

Usage notes

API Availability

Rate limits

Notes

Responses

Chat Completions

Assistants

100 RPM per org

Pricing

ZDR and data residency
