# HeroUI To shadcn Migration Example

This note turns the current HeroUI and shadcn knowledgebase material into a repo-specific migration example for `cloudravenlabs`.

It is not a recommendation to rewrite the whole UI at once. The better path here is a staged migration:

1. install shadcn alongside HeroUI
2. migrate one small surface at a time
3. keep the visual language stable while the component ownership model changes
4. remove HeroUI provider and theme wiring only after the last dependent surfaces are gone

## Why Migrate In This Repo

Based on the local knowledgebase:

- HeroUI is good for fast packaged UI assembly
- shadcn is better when the team wants open-code components that live in the repo and can be edited directly

That makes the migration question less about appearance and more about ownership:

- HeroUI means package-managed components plus a provider/theme integration
- shadcn means copied-in components, CSS variables, and direct repo ownership

For CloudRaven, the strongest reason to migrate is design-system control across a growing app surface, not a need to radically restyle the product.

## Current HeroUI Footprint

Right now the repo still depends on HeroUI in a few important ways:

- `app/providers.tsx` wraps the app in `HeroUIProvider`
- `tailwind.config.js` includes the HeroUI theme plugin and content path
- multiple app surfaces import `Button`, `Input`, `Textarea`, `Chip`, `Card`, `Tabs`, `Avatar`, and `Tooltip` from `@heroui/react`

That means the clean migration shape is:

- first migrate leaf components and isolated forms
- then migrate higher-level layout components
- finally remove provider and plugin wiring

## Recommended First Migration Target

Use `app/components/lead-inquiry/lead-inquiry-form.tsx` as the first example.

Why this file is a good starter:

- it uses a small HeroUI surface: `Button`, `Input`, `Textarea`
- it is public-facing but operationally low-risk
- it already uses plain Tailwind for the surrounding layout
- it shows the real shift from HeroUI field props to shadcn's explicit label, field, and error composition model

## Suggested shadcn Setup For This Repo

The local shadcn docs point to:

- Next.js installation
- `components.json`
- CLI-driven component generation
- CSS variable theming

A reasonable setup for this repo would look like:

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "utils": "@/lib/utils",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}
```

The practical install path would be:

```bash
npx shadcn@latest init
npx shadcn@latest add button input textarea label select card badge tabs tooltip avatar separator
```

## Theme Strategy

Do not restyle the app during the first migration pass.

Instead:

- keep the existing CloudRaven palette in `app/globals.css`
- map shadcn semantic tokens onto the existing `--cr-*` variables
- preserve the same neutral, editorial look while the component source changes

That keeps the migration focused on implementation ownership rather than visual churn.

## Component Mapping

These are the most common replacements you will hit first in this repo:

| HeroUI | shadcn / local alternative | Migration note |
| --- | --- | --- |
| `Button` | `@/components/ui/button` | straightforward replacement for most cases |
| `Input` | `Label` + `Input` + explicit error text | HeroUI field props become explicit layout |
| `Textarea` | `Label` + `Textarea` + explicit error text | same pattern as `Input` |
| `Chip` | `Badge` | variants usually need a small custom mapping |
| `Card`, `CardBody` | `Card`, `CardContent` | simple structural migration |
| `Tabs`, `Tab` | `Tabs`, `TabsList`, `TabsTrigger`, `TabsContent` | more explicit structure in shadcn |
| `Tooltip` | `TooltipProvider`, `Tooltip`, `TooltipTrigger`, `TooltipContent` | slightly more verbose |
| `Avatar` | `Avatar`, `AvatarImage`, `AvatarFallback` | mostly mechanical |
| `Image` | plain `next/image` or existing local image usage | often simpler to drop package coupling |
| `HeroUIProvider` | no equivalent for basic shadcn components | remove only after HeroUI components are gone |

## Example: Lead Inquiry Form

### Current HeroUI shape

The current file uses:

- `Input` with `label`, `labelPlacement`, `isInvalid`, `errorMessage`, and `onValueChange`
- `Textarea` with the same field-prop pattern
- `Button` with `isLoading`

That is convenient, but it couples field structure to the component API.

### shadcn migration shape

In shadcn, the same form becomes more explicit:

- field labels are rendered with `Label`
- errors are rendered as normal text below fields
- value changes use standard React `onChange`
- loading state is handled with `disabled` plus your own loading text or spinner

### Example migrated version

This example assumes you have added:

- `@/components/ui/button`
- `@/components/ui/input`
- `@/components/ui/textarea`
- `@/components/ui/label`
- `@/lib/utils` with a `cn()` helper

```tsx
"use client";

import React from "react";
import { Icon } from "@iconify/react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";

type FieldProps = {
  id: string;
  label: string;
  error?: string;
  children: React.ReactNode;
};

function FormField({ id, label, error, children }: FieldProps) {
  return (
    <div className="space-y-2">
      <Label htmlFor={id} className="text-sm font-medium text-zinc-900">
        {label}
      </Label>
      {children}
      {error ? <p className="text-xs leading-6 text-red-700">{error}</p> : null}
    </div>
  );
}

export function LeadInquiryFormShadcnExample() {
  const [values, setValues] = React.useState({
    fullName: "",
    email: "",
    organization: "",
    website: "",
    goals: "",
  });
  const [errors, setErrors] = React.useState<Record<string, string | undefined>>({});
  const [isSubmitting, setIsSubmitting] = React.useState(false);
  const [successMessage, setSuccessMessage] = React.useState<string | null>(null);

  const setField = (key: keyof typeof values, value: string) => {
    setValues((current) => ({ ...current, [key]: value }));
    setErrors((current) => ({ ...current, [key]: undefined }));
    setSuccessMessage(null);
  };

  return (
    <div className="border border-zinc-300/80 bg-[#fbfaf7] p-5 sm:p-6">
      <div className="mb-5 border-b border-zinc-300/80 pb-5">
        <p className="text-[11px] font-semibold uppercase tracking-[0.16em] text-zinc-500">
          Public inquiry
        </p>
        <h3 className="mt-1 text-lg font-semibold text-zinc-950">
          Tell CloudRaven what you are trying to launch or improve
        </h3>
        <p className="mt-2 text-sm leading-7 text-zinc-700">
          No account creation required. A short note about the workflow, market, or product is enough to start.
        </p>
      </div>

      <form className="space-y-5">
        <div className="grid gap-4 sm:grid-cols-2">
          <FormField id="fullName" label="Name" error={errors.fullName}>
            <Input
              id="fullName"
              placeholder="Your name"
              value={values.fullName}
              onChange={(event) => setField("fullName", event.target.value)}
              className={cn(errors.fullName && "border-red-500 focus-visible:ring-red-500")}
            />
          </FormField>

          <FormField id="email" label="Work email" error={errors.email}>
            <Input
              id="email"
              type="email"
              placeholder="you@company.com"
              value={values.email}
              onChange={(event) => setField("email", event.target.value)}
              className={cn(errors.email && "border-red-500 focus-visible:ring-red-500")}
            />
          </FormField>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          <FormField id="organization" label="Organization">
            <Input
              id="organization"
              placeholder="Company or team"
              value={values.organization}
              onChange={(event) => setField("organization", event.target.value)}
            />
          </FormField>

          <FormField id="website" label="Website">
            <Input
              id="website"
              placeholder="https://example.com"
              value={values.website}
              onChange={(event) => setField("website", event.target.value)}
            />
          </FormField>
        </div>

        <FormField id="goals" label="What are you trying to improve?" error={errors.goals}>
          <Textarea
            id="goals"
            rows={6}
            placeholder="Describe the workflow, friction, or opportunity you want CloudRaven to help with."
            value={values.goals}
            onChange={(event) => setField("goals", event.target.value)}
            className={cn(errors.goals && "border-red-500 focus-visible:ring-red-500")}
          />
        </FormField>

        {successMessage ? (
          <div className="border border-emerald-300/80 bg-emerald-50 px-4 py-3 text-sm leading-7 text-emerald-900">
            <div className="flex items-start gap-2">
              <Icon icon="lucide:check-circle-2" className="mt-1 h-4 w-4 shrink-0" />
              <p>{successMessage}</p>
            </div>
          </div>
        ) : null}

        <div className="flex flex-wrap items-center gap-3">
          <Button
            type="submit"
            disabled={isSubmitting}
            className="h-11 border border-zinc-300/80 bg-zinc-950 px-5 text-sm font-medium text-white hover:bg-zinc-800"
          >
            {isSubmitting ? "Submitting..." : "Start the conversation"}
          </Button>
          <p className="text-sm leading-7 text-zinc-600">
            CloudRaven will review the note and follow up directly.
          </p>
        </div>
      </form>
    </div>
  );
}
```

## What Changes In Practice

The code gets slightly more verbose, but the tradeoff is intentional:

- the field structure is now owned by the repo
- validation rendering is now explicit and easy to standardize
- styling is plain Tailwind plus local component classes
- the migration path is incremental because this form can coexist with HeroUI elsewhere

## Recommended Migration Sequence

Use this order for the real repo:

1. Initialize shadcn and add the smallest common primitives:
   - `button`
   - `input`
   - `textarea`
   - `label`
   - `badge`
   - `card`
2. Migrate isolated public forms first:
   - `app/components/lead-inquiry/lead-inquiry-form.tsx`
   - `app/components/join/login-form.tsx`
3. Migrate shared workspace leaf elements:
   - buttons
   - chips/badges
   - simple cards
4. Migrate structured navigation pieces:
   - tabs
   - tooltips
   - avatars
5. Remove HeroUI infrastructure only after usage reaches zero:
   - remove `HeroUIProvider` from `app/providers.tsx`
   - remove `@heroui/theme` plugin wiring from `tailwind.config.js`
   - remove HeroUI packages from `package.json`

## Repo-Specific Caveats

- Keep HeroUI and shadcn side by side during the transition. A big-bang rewrite is unnecessary here.
- Preserve the current CloudRaven visual language while migrating. Do not combine a design refresh with a component-system swap.
- The biggest implementation shift is not the button API. It is the move from provider/package ownership to repo-local component ownership.
- Use the dependency manifest and the UI-system briefs after each phase so design-system drift stays visible.

## When This Migration Is Worth It

This is worth doing if you want:

- more direct control over component code
- fewer design-system decisions hidden behind package updates
- easier long-term customization of the workspace and public site

It is probably not worth doing if your real goal is only to restyle a few screens. In that case, staying on HeroUI and tightening local Tailwind patterns may be the lower-cost move.
