---
title: shadcn - shadcn/ui | CloudRaven Enrichment
source_url: https://ui.shadcn.com/docs/cli
target_id: shadcn-ui
dependency: shadcn/ui
collected_at: 2026-04-16T03:29:16.890569+00:00
kind: enriched-doc
tags: ui-system, react, tailwind, design-system, open-code
---

# shadcn - shadcn/ui | CloudRaven Enrichment

Source URL:

- https://ui.shadcn.com/docs/cli

Dependency:

- shadcn/ui

Collection scope:

- Collect the core shadcn/ui docs for installation, CLI usage, configuration, theming, and the LLM-readable index.

What this page is useful for:

- shadcn - shadcn/ui Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Theming Dark Mode CLI Monorepo Skills Open in v0 JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Registry Introduction Getting Started Namespaces Authentication Examples MCP Server Add a Registry Open in v0 registry.json registry-item.json shadcn Copy Page Previous Next Use the shadcn CLI to add components to your project.
- init Use the init command to initialize configuration and dependencies for an existing project, or create a new project with --name .
- The init command installs dependencies, adds the cn util and configures CSS variables for the project.
- pnpm npm yarn bun pnpm dlx shadcn@latest init Copy Options Copy Usage: shadcn init [options] [components...] initialize your project and install dependencies Arguments: components names, url or local path to component Options: -t, --template < templat e > the template to use.

CloudRaven applicability:

- Use this material when the app wants an open-code component system that can be installed, owned, and customized directly inside the repo.

Prototype-to-production review:

- High fit when the team wants design-system control without depending on a closed component package abstraction.
- Review component ownership, update strategy, and styling conventions early so copied-in code does not drift inconsistently.

CloudRaven example paths:

- Replace package-based UI dependencies with copied-in components the team can edit freely.
- Build dashboards, forms, and admin surfaces with Tailwind-aligned components that stay close to the app code.

Suggested retrieval tags:

- `ui-system`
- `react`
- `tailwind`
- `design-system`
- `open-code`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/shadcn-ui/docs-cli-7e8314087c.md`
- Raw source: `knowledgebase/store/raw_html/shadcn-ui/docs-cli-7e8314087c.html`
