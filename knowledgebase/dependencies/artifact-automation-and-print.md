# Artifact Automation And Print

This brief covers the repo's artifact-as-code workflows for slides, print assets, and presentation helpers.

## Where It Shows Up

- `docs/slides/Laplink/work/`
- `docs/slides/TOPSprint/work/`
- `docs/slides/TOPSprint/work/build_top_sprint_print_assets.mjs`

## Key Dependencies

- `pptxgenjs` for editable slide generation
- `sharp` for deterministic image composition and export
- `qrcode` for tracked print and campaign assets
- `skia-canvas`, `linebreak`, `fontkit`, `prismjs`, and `mathjax-full` inside the custom PPTX helper stack

## Why It Belongs In The Knowledgebase

- These workflows are not incidental scripts; they are a real delivery lane for client-facing artifacts.
- Layout, typography, code rendering, and export behavior all depend on a specialized toolchain that is easy to break through transitive dependency drift.
- Several helper dependencies are imported directly in repo scripts and should be treated as intentional parts of the workflow surface.

## CloudRaven Guidance

- Treat generated decks and print assets as reproducible build outputs, not one-off exports.
- Keep the helper toolchain documented whenever text measurement, syntax rendering, image composition, or QR generation behavior changes.
- If a script imports a package directly, prefer declaring it directly in `package.json` instead of relying on transitive installs.
- When updating the workflow, verify:
  - text still fits the intended layout
  - image export sizes and aspect ratios remain stable
  - QR codes remain readable in final output
  - helper dependencies still resolve in a clean install

## Review Questions

- Is the dependency part of the durable artifact pipeline or just an experiment?
- Does the script still work in a fresh install without undeclared transitive packages?
- Are we preserving editable output where that matters more than flattened media?
