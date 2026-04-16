---
title: Next.js - shadcn/ui
source_url: https://ui.shadcn.com/docs/installation/next
target_id: shadcn-ui
dependency: shadcn/ui
collected_at: 2026-04-16T03:29:20.023938+00:00
kind: extracted-doc
---

# Next.js - shadcn/ui

Source URL:

- https://ui.shadcn.com/docs/installation/next

Dependency:

- shadcn/ui

Collected at:

- 2026-04-16T03:29:20.023938+00:00

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

- Next.js - shadcn/ui Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Theming Dark Mode CLI Monorepo Skills Open in v0 JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Registry Introduction Getting Started Namespaces Authentication Examples MCP Server Add a Registry Open in v0 registry.json registry-item.json Next.js Copy Page Previous Next Install and configure shadcn/ui for Next.js.
- Choose the setup that matches your starting point.
- Use shadcn/create Build your preset and generate a Next.js project command.
- Use the CLI Scaffold a new Next.js project directly from the terminal.
- Existing Project Configure shadcn/ui manually in an existing Next.js project.

Extracted text:

Next.js - shadcn/ui

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

Next.js

Copy Page

Previous

Next

Install and configure shadcn/ui for Next.js.

Choose the setup that matches your starting point.

Use shadcn/create

Build your preset and generate a Next.js project command.

Use the CLI

Scaffold a new Next.js project directly from the terminal.

Existing Project

Configure shadcn/ui manually in an existing Next.js project.

Use shadcn/create

Build Your Preset

Open

shadcn/create

and build your preset visually. Choose your style, colors, fonts, icons, and more.

Open shadcn/create

Create Project

Click

Create Project

, choose your package manager, and copy the generated command.

The generated command will look similar to this:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init --preset [CODE] --template next

Copy

The exact command will include your selected options such as

--base

,

--monorepo

, or

--rtl

.

Add Components

Add the

Card

component to your project:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add card

Copy

If you created a monorepo, run the command from

apps/web

or specify the workspace from the repo root:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add card -c apps/web

Copy

The command above will add the

Card

component to your project. You can then import it like this:

app/page.tsx

Copy

import

{

Card,

CardContent,

CardDescription,

CardHeader,

CardTitle,

}

from

"@/components/ui/card"

export

default

function

Home

()

{

return

(

<

Card

className

=

"max-w-sm"

>

<

CardHeader

>

<

CardTitle

>Project Overview</

CardTitle

>

<

CardDescription

>

Track progress and recent activity for your Next.js app.

</

CardDescription

>

</

CardHeader

>

<

CardContent

>

Your design system is ready. Start building your next component.

</

CardContent

>

</

Card

>

)

}

If you created a monorepo, update

apps/web/app/page.tsx

and import from

@workspace/ui/components/card

instead.

Use the CLI

Create Project

Run the

init

command to scaffold a new Next.js project. Follow the prompts to configure your project: base, preset, monorepo, and more.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init -t next

Copy

For a monorepo project, use

--monorepo

flag:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init -t next --monorepo

Copy

Add Components

Add the

Card

component to your project:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add card

Copy

If you created a monorepo, run the command from

apps/web

or specify the workspace from the repo root:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add card -c apps/web

Copy

The command above will add the

Card

component to your project. You can then import it like this:

app/page.tsx

Copy

import

{

Card,

CardContent,

CardDescription,

CardHeader,

CardTitle,

}

from

"@/components/ui/card"

export

default

function

Home

()

{

return

(

<

Card

className

=

"max-w-sm"

>

<

CardHeader

>

<

CardTitle

>Project Overview</

CardTitle

>

<

CardDescription

>

Track progress and recent activity for your Next.js app.

</

CardDescription

>

</

CardHeader

>

<

CardContent

>

Your design system is ready. Start building your next component.

</

CardContent

>

</

Card

>

)

}

If you created a monorepo, update

apps/web/app/page.tsx

and import from

@workspace/ui/components/card

instead.

Existing Project

Create Project

If you need a new Next.js project, create one with

create-next-app

. Otherwise, skip this step.

pnpm

npm

yarn

bun

pnpm create next-app@latest

Copy

Choose the recommended defaults so Tailwind CSS, the App Router, and the default

@/*

import alias are configured for you.

If you prefer a

src/

directory, use

--src-dir

or choose

Yes

when prompted:

pnpm

npm

yarn

bun

pnpm create next-app@latest --src-dir

Copy

With

--src-dir

, Next.js places your app in

src/app

and configures the

@/*

alias to point to

./src/*

.

Configure Tailwind CSS and Import Aliases

If you created your project with the recommended

create-next-app

defaults, you can skip this step.

If you're adding shadcn/ui to an older or custom Next.js app, make sure Tailwind CSS is installed first. You can follow the official

Next.js installation guide

.

Then make sure your

tsconfig.json

includes the

@/*

import alias:

tsconfig.json

Copy

{

"compilerOptions"

: {

"paths"

: {

"@/*"

: [

"./*"

]

}

}

}

If you used

--src-dir

, point the alias to

./src/*

instead.

Run the CLI

Run the

shadcn

init command to set up shadcn/ui in your project.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init

Copy

Add Components

You can now start adding components to your project.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add button

Copy

The command above will add the

Button

component to your project. You can then import it like this:

app/page.tsx

Copy

import

{ Button }

from

"@/components/ui/button"

export

default

function

Home

()

{

return

(

<

div

className

=

"flex min-h-svh items-center justify-center"

>

<

Button

>Click me</

Button

>

</

div

>

)

}

If you used

--src-dir

, add the component to

src/app/page.tsx

instead.

Installation

Vite

On This Page

Use shadcn/create

Build Your Preset

Create Project

Add Components

Use the CLI

Create Project

Add Components

Existing Project

Create Project

Configure Tailwind CSS and Import Aliases

Run the CLI

Add Components

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Adobe, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now

Deploy to Vercel

Create Project
