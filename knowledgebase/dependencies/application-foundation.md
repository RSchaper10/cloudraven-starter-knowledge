# Application Foundation

This brief covers the starter application layer: AWS Amplify Gen 2 for Next.js, HeroUI, shadcn/ui, and Tailwind CSS.

## AWS Amplify Gen 2 for Next.js

Role:

- Fullstack TypeScript foundation for auth, data, storage, and deployment-adjacent backend resources in a Next.js app.

Why it fits CloudRaven:

- It supports rapid prototyping with a direct path to managed AWS resources.
- It keeps backend intent close to the application project instead of splitting early across many services.

Priority docs:

- https://docs.amplify.aws/nextjs/
- https://docs.amplify.aws/nextjs/build-a-backend/auth/grant-access-to-auth-resources/
- https://docs.amplify.aws/nextjs/build-a-backend/storage/set-up-storage/

Key concepts:

- backend resources are defined in TypeScript
- auth, data, storage, and functions are composable resources
- access control is explicit and should be modeled early
- Next.js usage should be aligned with App Router boundaries and server/client rendering behavior

Production cautions:

- auth and storage access rules should be designed before content workflows expand
- prototype-friendly defaults can become risky if roles and resource boundaries stay implicit
- docs are extensive, so tasks should route to the exact resource area before implementation

Suggested tags:

- `aws`
- `amplify`
- `nextjs`
- `auth`
- `data`
- `storage`

## HeroUI

Role:

- React component and design-system layer for fast interface assembly.

Priority docs:

- https://heroui.com/docs/guide/introduction
- https://heroui.com/docs/guide/installation

Why it fits CloudRaven:

- Useful for moving quickly on admin surfaces, onboarding flows, dashboards, and internal tooling.

Production cautions:

- use a clear design token strategy early if custom branding matters
- avoid mixing too many visual systems once the app grows

Suggested tags:

- `ui-system`
- `react`
- `design-system`

Migration example:

- `knowledgebase/dependencies/heroui-to-shadcn-migration-example.md`

## shadcn/ui

Role:

- Open-code component system for building and owning the UI layer directly in the application repo.

Priority docs:

- https://ui.shadcn.com/llms.txt
- https://ui.shadcn.com/docs/installation
- https://ui.shadcn.com/docs/cli
- https://ui.shadcn.com/docs/components-json
- https://ui.shadcn.com/docs/theming

Why it fits CloudRaven:

- Useful when the team wants to customize component code directly instead of depending on a package-managed design system.
- Pairs well with Tailwind when the app needs a component starter layer without giving up implementation ownership.

Production cautions:

- copied-in component code needs clear ownership and conventions or it will drift across the app
- define how the team will evaluate upstream changes before the component surface grows large

Suggested tags:

- `ui-system`
- `react`
- `tailwind`
- `design-system`
- `open-code`

Migration example:

- `knowledgebase/dependencies/heroui-to-shadcn-migration-example.md`

## Tailwind CSS

Role:

- Styling utility layer that pairs well with component systems and custom interfaces.

Priority docs:

- https://tailwindcss.com/docs/installation/framework-guides/nextjs
- https://tailwindcss.com/docs/styling-with-utility-classes

Why it fits CloudRaven:

- Excellent for fast iteration across portals, content tools, dashboards, and presentation-like web artifacts.

Production cautions:

- utility sprawl becomes a maintenance issue without conventions
- define layout, spacing, and theme patterns early to reduce drift

Suggested tags:

- `tailwind`
- `styling`
- `frontend`
