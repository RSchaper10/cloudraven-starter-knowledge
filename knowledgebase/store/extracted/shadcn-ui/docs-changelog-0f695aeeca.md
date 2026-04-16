---
title: Changelog - shadcn/ui
source_url: https://ui.shadcn.com/docs/changelog
target_id: shadcn-ui
dependency: shadcn/ui
collected_at: 2026-04-16T03:29:18.817513+00:00
kind: extracted-doc
---

# Changelog - shadcn/ui

Source URL:

- https://ui.shadcn.com/docs/changelog

Dependency:

- shadcn/ui

Collected at:

- 2026-04-16T03:29:18.817513+00:00

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

- Changelog - shadcn/ui Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Theming Dark Mode CLI Monorepo Skills Open in v0 JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Registry Introduction Getting Started Namespaces Authentication Examples MCP Server Add a Registry Open in v0 registry.json registry-item.json Changelog RSS Latest updates and announcements.
- April 2026 - shadcn apply We added shadcn apply so you can switch presets in an existing project without starting over.
- When you run npx shadcn@latest apply in an existing project, we apply a new preset, reinstall your existing components, and update your theme, colors, CSS variables, fonts, and icons.
- pnpm npm yarn bun pnpm dlx shadcn@latest apply --preset b2D0vQ7G4 Copy The CLI keeps the current base and RTL settings from your existing project, even when the preset URL was generated with different values.
- Try a Preset April 2026 - Component Composition We've added Composition sections across the component docs so you can see the correct structure at a glance: what wraps what, which subcomponents belong together, and how to avoid invalid nesting.

Extracted text:

Changelog - shadcn/ui

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

Changelog

RSS

Latest updates and announcements.

April 2026 - shadcn apply

We added

shadcn apply

so you can switch presets in an existing project without starting over.

When you run

npx shadcn@latest apply

in an existing project, we apply a new preset, reinstall your existing components, and update your theme, colors, CSS variables, fonts, and icons.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest apply --preset b2D0vQ7G4

Copy

The CLI keeps the current base and RTL settings from your existing project, even when the preset URL was generated with different values.

Try a Preset

April 2026 - Component Composition

We've added

Composition

sections across the component docs so you can see the correct structure at a glance: what wraps what, which subcomponents belong together, and how to avoid invalid nesting.

Copy

Card

├── CardHeader

│ ├── CardTitle

│ ├── CardDescription

│ └── CardAction

├── CardContent

└── CardFooter

Why we added this

We've found that

LLMs and coding agents compose elements more reliably

when they can see the full structure: fewer missing wrappers, fewer wrong hierarchies, better matches to the examples.

Bring docs into your agent

You or your LLM can pull the same component documentation, including composition, usage, and examples, into context from the CLI:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest docs card

Copy

If you're using the

shadcn/skills

, this is done automatically for you.

More Updates

March 2026

Introducing Luma

March 2026

shadcn/cli v4

February 2026

Blocks for Radix and Base UI

February 2026

Unified Radix UI Package

January 2026

RTL Support

January 2026

Inline Start and End Styles

January 2026

Base UI Documentation

December 2025

npx shadcn create

October 2025

Registry Directory

October 2025

New Components

September 2025

Registry Index

August 2025

shadcn CLI 3.0 and MCP Server

July 2025

Universal Registry Items

July 2025

Local File Support

June 2025

radix-ui Migration

June 2025

Calendar Component

May 2025

New Site

April 2025

MCP

April 2025

shadcn 2.5.0

April 2025

Cross-framework Route Support

February 2025

Tailwind v4

February 2025

Updated Registry Schema

January 2025

Blocks Community

December 2024

Monorepo Support

November 2024

Icons

October 2024

React 19

October 2024

Sidebar

August 2024

npx shadcn init

April 2024

Lift Mode

March 2024

Introducing Blocks

March 2024

Breadcrumb and Input OTP

December 2023

New Components

July 2023

JavaScript

June 2023

New CLI, Styles and more

On This Page

April 2026 - shadcn apply

April 2026 - Component Composition

More Updates

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Adobe, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now

Deploy to Vercel

Create Project
