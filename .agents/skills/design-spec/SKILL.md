---
name: design-spec
description: How to author a DESIGN.md file — the machine-readable design-token + human-rationale format that must exist before any UI is built. YAML front-matter token schema (colors, typography, spacing, rounded, components), type system, token references, and canonical section order.
when_to_use: "BEFORE writing any UI code (web or mobile). Read when creating or updating a project's DESIGN.md, defining design tokens, or when a UI task needs a design source-of-truth. Pair with frontend-design (web aesthetics) or mobile-design (mobile)."
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
---

# DESIGN.md Specification

> **🛡️ JINC GOVERNANCE:**
> JINC governance and approved requirements
> ↓
> PRD / approved product requirements
> ↓
> SDD / approved engineering constraints
> ↓
> DESIGN.md — visual and interaction design source of truth
> ↓
> implementation
>
> Accessibility must be part of the DESIGN.md definition itself, not an afterthought.
>
> A DESIGN.md establishes evidence and constraints for UI execution. **Design approval and technical validation establish evidence and constraints, not authorization for consequential actions.** (Human Gate applies).
>
> Two layers: machine-readable **design tokens** (YAML front matter) + human-readable **rationale** (markdown body).
> Tokens are normative; prose gives context. Prose may use descriptive names ("Midnight Forest Green") that map to systematic token names (`primary`).
>
> _Format adapted from the [DESIGN.md spec](https://github.com/google-labs-code/design.md) (Google Labs, Apache-2.0). A linter/exporter exists: `npx @google/design.md`._
>
> 📚 **Reference library:** [collection.md](collection.md) — 70+ real-world DESIGN.md files (Airbnb, Stripe, Linear, Vercel, Apple…) to study or adapt as a starting point.

---

## When to produce a DESIGN.md

This is a **hard gate** for UI work: before writing components, pages, or styles, a `DESIGN.md` must exist at the project root. If absent, create it first from the brief; if present, read it and conform.

**Hierarchy Rule:** DESIGN.md is subordinate to authoritative JINC governance and approved product/engineering requirements. Within those constraints, DESIGN.md is the source of truth for visual and interaction design. If authoritative upstream requirements conflict: STOP / surface the conflict for resolution.

The token block converts cleanly to/from `tokens.json`, Figma variables, and Tailwind theme config — so it is the bridge between design intent and code.

---

## 1. File structure

```
---
<YAML token front matter>
---

# Project Name (optional title)

## Overview
## Colors
## Typography
## Layout
## Elevation & Depth
## Shapes
## Accessibility
## Components
## Do's and Don'ts
```

Front matter MUST begin and end with a line containing exactly `---`. Sections use `##` headings, appear in the order above, and may be omitted if irrelevant. Domain-specific sections may be added.

---

## 2. Token schema (YAML front matter)

```yaml
version: alpha # optional
name: Daylight Prestige
description: ... # optional
colors:
  <token-name>: "#RRGGBB"
typography:
  <token-name>:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
rounded:
  <scale>: 8px
spacing:
  <scale>: 16px # Dimension or unitless number
components:
  <component-name>:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 12px
```

`<scale>` is a named level: `xs sm md lg xl full` (any descriptive key is valid).

---

## 3. Type system

| Type            | Format                          | Example            |
| --------------- | ------------------------------- | ------------------ |
| Color           | `#` + hex (sRGB)                | `"#1A1C1E"`        |
| Dimension       | number + unit (`px`/`em`/`rem`) | `48px`, `-0.02em`  |
| Token Reference | `{path.to.token}`               | `{colors.primary}` |
| Typography      | composite object                | see §4             |

**Typography properties:** `fontFamily` (string), `fontSize` (Dimension), `fontWeight` (number — bare or quoted are equivalent in YAML), `lineHeight` (Dimension or unitless multiplier — unitless recommended), `letterSpacing` (Dimension), `fontFeature` (string), `fontVariation` (string).

**Token references:** wrapped in `{}` pointing to another value in the tree. Most groups must reference a **primitive** (`{colors.primary-60}`), not a group. Inside `components`, references to **composite** values are allowed (`{typography.label-md}`).

**Component property tokens:** `backgroundColor`, `textColor` (Color); `typography` (Typography); `rounded`, `padding`, `size`, `height`, `width` (Dimension).

**Variants:** define UI states as separate entries with a related key — `button-primary`, `button-primary-hover`.

---

## 4. Sections (canonical order)

| #   | Section           | Aliases          | Purpose                                                                                                                                                                                                                                                                                                                                                                                                          |
| --- | ----------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Overview          | Brand & Style    | Brand personality, audience, emotional tone. Fallback context when a token isn't defined.                                                                                                                                                                                                                                                                                                                        |
| 2   | Colors            |                  | Palettes; at least `primary`. **JINC targets WCAG 2.2 AAA where applicable. Contrast requirements must be evaluated according to content and component type, including: normal text (≥ 7:1), large text (≥ 4.5:1), and non-text UI elements (≥ 3:1). Never validate a palette by isolated color values alone; validate the actual foreground/background relationships in which tokens are intended to be used.** |
| 3   | Typography        |                  | 9–15 levels, each a semantic role (headline/body/label) × size.                                                                                                                                                                                                                                                                                                                                                  |
| 4   | Layout            | Layout & Spacing | Grid model, spacing scale, containment.                                                                                                                                                                                                                                                                                                                                                                          |
| 5   | Elevation & Depth | Elevation        | Shadows, OR for flat designs the alternative (borders, tonal layers, contrast).                                                                                                                                                                                                                                                                                                                                  |
| 6   | Shapes            |                  | Corner radii, edge treatment, shape language.                                                                                                                                                                                                                                                                                                                                                                    |
| 7   | Accessibility     |                  | **Mandatory section.** Prefer native semantic HTML. Document interaction semantics, keyboard behavior, accessible names/states, and assistive-technology intent. Use ARIA only where native semantics are insufficient. Valid design tokens and a valid DESIGN.md are design evidence, not accessibility verification. Actual implementation must still be tested.                                               |
| 8   | Components        |                  | Per-atom guidance: Buttons, Inputs, Cards, Chips, Lists, etc.                                                                                                                                                                                                                                                                                                                                                    |
| 9   | Do's and Don'ts   |                  | Guardrails during generation.                                                                                                                                                                                                                                                                                                                                                                                    |

---

## 5. Recommended token names (guidance, not required)

- **Colors:** `primary secondary tertiary neutral surface on-surface error`
- **Typography:** `headline-display headline-lg headline-md body-lg body-md body-sm label-lg label-md label-sm`
- **Rounded:** `none sm md lg xl full`

---

## 6. Consumer behavior for unknown content

The spec is extensible. When encountering content it doesn't define:

| Scenario                                        | Behavior                                         |
| ----------------------------------------------- | ------------------------------------------------ |
| Unknown section heading (`## Iconography`)      | Preserve; do not error                           |
| Unknown color token name                        | Accept if value is valid                         |
| Unknown typography token name                   | Accept as valid typography                       |
| Unknown spacing value                           | Accept; store as string if not a valid dimension |
| Unknown component property                      | Accept with warning                              |
| **Duplicate section heading** (two `## Colors`) | **Error; reject the file**                       |

---

## 7. Minimal example

```markdown
---
name: Calm Scheduler
colors:
  primary: "#1A1C1E"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
typography:
  h1:
    {
      fontFamily: Public Sans,
      fontSize: 48px,
      fontWeight: 600,
      lineHeight: 1.1,
    }
  body-md:
    {
      fontFamily: Public Sans,
      fontSize: 16px,
      fontWeight: 400,
      lineHeight: 1.6,
    }
rounded: { sm: 4px, md: 8px }
spacing: { sm: 8px, md: 16px, lg: 32px }
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    rounded: "{rounded.md}"
    padding: 12px
---

# Calm Scheduler

## Overview

A calm, professional interface for a healthcare scheduling platform.

## Colors

- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Tertiary (#B8422E):** The sole driver for interaction.
- **Neutral (#F7F5F2):** Warm limestone foundation.

## Accessibility

Accessibility-first: intended text/background pairs meet the applicable JINC WCAG 2.2 targets — including 7:1 for normal text and 4.5:1 for large text at AAA — and non-text interactive indicators meet their applicable contrast requirements.

## Do's and Don'ts

- Do use the tertiary color only for the single most important action per screen.
- Don't mix rounded and sharp corners in the same view.
- Do validate every semantic foreground/background pair against the applicable JINC accessibility target.
```

---

## Workflow

1. Read the brief and infer the design direction. MUST use `a11y-master` to evaluate inclusion requirements, and `frontend-design` / `mobile-design` for UI direction.
2. **ALWAYS read [collection.md](collection.md) first** — 70+ real-world DESIGN.md files. Find the 1–2 closest in vibe/industry to the brief, open their `DESIGN.md` on GitHub, and study how they structure tokens. Adapt, never blindly copy. **Anti-fabrication applies: Never fabricate or imply execution that did not occur.**
3. **Write `DESIGN.md` at the project root** — tokens first, then rationale prose. Ensure accessibility is baked into the foundation.
4. **DESIGN.md creation and validation establish design evidence and constraints, not authorization.**
   Continue normal design/specification work as appropriate.
   Before a consequential action that independently requires authorization — such as merge, deployment, publication, release, protected-branch push, or implementation that the user has explicitly reserved for approval — STOP and obtain the required Human Gate approval.
5. Build UI strictly against the tokens and PRD. Descriptive names in prose must map to token names.
6. Keep DESIGN.md synchronized when the visual or interaction language changes. It remains the design source of truth within the boundaries established by JINC governance and approved product/engineering requirements.
