---
title: components.json - shadcn/ui
source_url: https://ui.shadcn.com/docs/components-json
target_id: shadcn-ui
dependency: shadcn/ui
collected_at: 2026-04-16T03:29:18.014063+00:00
kind: extracted-doc
---

# components.json - shadcn/ui

Source URL:

- https://ui.shadcn.com/docs/components-json

Dependency:

- shadcn/ui

Collected at:

- 2026-04-16T03:29:18.014063+00:00

Direct links in scope:

- https://ui.shadcn.com/docs/components
- https://ui.shadcn.com/docs/installation
- https://ui.shadcn.com/docs/theming
- https://ui.shadcn.com/docs/cli
- https://ui.shadcn.com/docs/rtl
- https://ui.shadcn.com/docs/skills
- https://ui.shadcn.com/docs/mcp
- https://ui.shadcn.com/docs/registry
- https://ui.shadcn.com/docs/forms
- https://ui.shadcn.com/docs/changelog
- https://ui.shadcn.com/docs/components/radix/accordion
- https://ui.shadcn.com/docs/components/radix/alert
- https://ui.shadcn.com/docs/components/radix/alert-dialog
- https://ui.shadcn.com/docs/components/radix/aspect-ratio
- https://ui.shadcn.com/docs/components/radix/avatar
- https://ui.shadcn.com/docs/components/radix/badge
- https://ui.shadcn.com/docs/components/radix/breadcrumb
- https://ui.shadcn.com/docs/components/radix/button
- https://ui.shadcn.com/docs/components/radix/button-group
- https://ui.shadcn.com/docs/components/radix/calendar

Captured summary:

- components.json - shadcn/ui Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Theming Dark Mode CLI Monorepo Skills Open in v0 JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Registry Introduction Getting Started Namespaces Authentication Examples MCP Server Add a Registry Open in v0 registry.json registry-item.json components.json Copy Page Previous Next Configuration for your project.
- The components.json file holds configuration for your project.
- We use it to understand how your project is set up and how to generate components customized for your project.
- Note: The `components.json` file is optional It is only required if you're using the CLI to add components to your project.
- If you're using the copy and paste method, you don't need this file.

Extracted text:

components.json - shadcn/ui

Sections

Introduction

Components

Installation

Theming

CLI

RTL

Skills

MCP Server

Registry

Forms

Changelog

Components

Accordion

Alert

Alert Dialog

Aspect Ratio

Avatar

Badge

Breadcrumb

Button

Button Group

Calendar

Card

Carousel

Chart

Checkbox

Collapsible

Combobox

Command

Context Menu

Data Table

Date Picker

Dialog

Direction

Drawer

Dropdown Menu

Empty

Field

Hover Card

Input

Input Group

Input OTP

Item

Kbd

Label

Menubar

Native Select

Navigation Menu

Pagination

Popover

Progress

Radio Group

Resizable

Scroll Area

Select

Separator

Sheet

Sidebar

Skeleton

Slider

Sonner

Spinner

Switch

Table

Tabs

Textarea

Toast

Toggle

Toggle Group

Tooltip

Typography

Get Started

Installation

components.json

Theming

Dark Mode

CLI

Monorepo

Skills

Open in v0

JavaScript

Figma

llms.txt

Legacy Docs

Forms

React Hook Form

TanStack Form

Registry

Introduction

Getting Started

Namespaces

Authentication

Examples

MCP Server

Add a Registry

Open in v0

registry.json

registry-item.json

components.json

Copy Page

Previous

Next

Configuration for your project.

The

components.json

file holds configuration for your project.

We use it to understand how your project is set up and how to generate components customized for your project.

Note: The `components.json` file is optional

It is

only required if you're using the CLI

to add components to your project. If you're using the copy and paste method, you don't need this file.

You can create a

components.json

file in your project by running the following command:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init

Copy

See the

CLI section

for more information.

$schema

You can see the JSON Schema for

components.json

here

.

components.json

Copy

{

"$schema"

:

"https://ui.shadcn.com/schema.json"

}

style

The style for your components.

This cannot be changed after initialization.

components.json

Copy

{

"style"

:

"new-york"

}

The

default

style has been deprecated. Use the

new-york

style instead.

tailwind

Configuration to help the CLI understand how Tailwind CSS is set up in your project.

See the

installation section

for how to set up Tailwind CSS.

tailwind.config

Path to where your

tailwind.config.js

file is located.

For Tailwind CSS v4, leave this blank.

components.json

Copy

{

"tailwind"

: {

"config"

:

"tailwind.config.js"

|

"tailwind.config.ts"

}

}

tailwind.css

Path to the CSS file that imports Tailwind CSS into your project.

components.json

Copy

{

"tailwind"

: {

"css"

:

"styles/global.css"

}

}

tailwind.baseColor

This is used to generate the default theme tokens for your components.

This cannot be changed after initialization.

components.json

Copy

{

"tailwind"

: {

"baseColor"

:

"neutral"

|

"stone"

|

"zinc"

|

"mauve"

|

"olive"

|

"mist"

|

"taupe"

}

}

tailwind.cssVariables

We use and recommend CSS variables for theming.

Set

tailwind.cssVariables

to

true

to generate semantic theme tokens like

background

,

foreground

, and

primary

. Set it to

false

to generate inline Tailwind color utilities instead.

components.json

Copy

{

"tailwind"

: {

"cssVariables"

:

`

true

`

|

`

false

`

}

}

For more information, see the

theming docs

.

This cannot be changed after initialization.

To switch between CSS variables and utility classes, you'll have to delete and re-install your components.

tailwind.prefix

The prefix to use for your Tailwind CSS utility classes. Components will be added with this prefix.

components.json

Copy

{

"tailwind"

: {

"prefix"

:

"tw-"

}

}

rsc

Whether or not to enable support for React Server Components.

The CLI automatically adds a

use client

directive to client components when set to

true

.

components.json

Copy

{

"rsc"

:

`

true

`

|

`

false

`

}

tsx

Choose between TypeScript or JavaScript components.

Setting this option to

false

allows components to be added as JavaScript with the

.jsx

file extension.

components.json

Copy

{

"tsx"

:

`

true

`

|

`

false

`

}

aliases

The CLI uses these values and the

paths

config from your

tsconfig.json

or

jsconfig.json

file to place generated components in the correct location.

Path aliases have to be set up in your

tsconfig.json

or

jsconfig.json

file.

Important:

If you're using the

src

directory, make sure it is included under

paths

in your

tsconfig.json

or

jsconfig.json

file.

aliases.utils

Import alias for your utility functions.

components.json

Copy

{

"aliases"

: {

"utils"

:

"@/lib/utils"

}

}

aliases.components

Import alias for your components.

components.json

Copy

{

"aliases"

: {

"components"

:

"@/components"

}

}

aliases.ui

Import alias for

ui

components.

The CLI will use the

aliases.ui

value to determine where to place your

ui

components. Use this config if you want to customize the installation directory for your

ui

components.

components.json

Copy

{

"aliases"

: {

"ui"

:

"@/app/ui"

}

}

aliases.lib

Import alias for

lib

functions such as

format-date

or

generate-id

.

components.json

Copy

{

"aliases"

: {

"lib"

:

"@/lib"

}

}

aliases.hooks

Import alias for

hooks

such as

use-media-query

or

use-toast

.

components.json

Copy

{

"aliases"

: {

"hooks"

:

"@/hooks"

}

}

registries

Configure multiple resource registries for your project. This allows you to install components, libraries, utilities, and other resources from various sources including private registries.

See the

Namespaced Registries

documentation for detailed information.

Basic Configuration

Configure registries with URL templates:

components.json

Copy

{

"registries"

: {

"@v0"

:

"https://v0.dev/chat/b/{name}"

,

"@acme"

:

"https://registry.acme.com/{name}.json"

,

"@internal"

:

"https://internal.company.com/{name}.json"

}

}

The

{name}

placeholder is replaced with the resource name when installing.

Advanced Configuration with Authentication

For private registries that require authentication:

components.json

Copy

{

"registries"

: {

"@private"

: {

"url"

:

"https://api.company.com/registry/{name}.json"

,

"headers"

: {

"Authorization"

:

"Bearer ${REGISTRY_TOKEN}"

,

"X-API-Key"

:

"${API_KEY}"

},

"params"

: {

"version"

:

"latest"

}

}

}

}

Environment variables in the format

${VAR_NAME}

are automatically expanded from your environment.

Using Namespaced Registries

Once configured, install resources using the namespace syntax:

Copy

# Install from a configured registry

npx

shadcn@latest

add

@v0/dashboard

# Install from private registry

npx

shadcn@latest

add

@private/button

# Install multiple resources

npx

shadcn@latest

add

@acme/header

@internal/auth-utils

Example: Multiple Registry Setup

components.json

Copy

{

"registries"

: {

"@shadcn"

:

"https://ui.shadcn.com/r/{name}.json"

,

"@company-ui"

: {

"url"

:

"https://registry.company.com/ui/{name}.json"

,

"headers"

: {

"Authorization"

:

"Bearer ${COMPANY_TOKEN}"

}

},

"@team"

: {

"url"

:

"https://team.company.com/{name}.json"

,

"params"

: {

"team"

:

"frontend"

,

"version"

:

"${REGISTRY_VERSION}"

}

}

}

}

This configuration allows you to:

Install public components from shadcn/ui

Access private company UI components with authentication

Use team-specific resources with versioning

For more information about authentication, see the

Authentication

documentation.

Installation

Theming

On This Page

$schema

style

tailwind

tailwind.config

tailwind.css

tailwind.baseColor

tailwind.cssVariables

tailwind.prefix

rsc

tsx

aliases

aliases.utils

aliases.components

aliases.ui

aliases.lib

aliases.hooks

registries

Basic Configuration

Advanced Configuration with Authentication

Using Namespaced Registries

Example: Multiple Registry Setup

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Adobe, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now

Deploy to Vercel

Create Project
