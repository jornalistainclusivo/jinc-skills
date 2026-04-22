# JINC Apps — Conventions & Standards Reference

This file guides the SDD Architect skill when making JINC-specific recommendations. Always apply these when generating stack alternatives, ADRs, or code patterns for JINC Apps repositories.

---

## 🏗️ Stack Preferences by Project Type

### Web (Next.js — JINC Standard)

| Layer | Preferred | Acceptable | Avoid |
|-------|-----------|------------|-------|
| Framework | Next.js 15 (App Router) | Astro (content sites) | Pages Router (legacy), CRA |
| Styling | Vanilla CSS + CSS Variables | Tailwind CSS | Inline styles, CSS-in-JS |
| State | Zustand | React Context (local) | Redux (unless existing) |
| Auth | Supabase Auth (PKCE) | Clerk | NextAuth (unless existing) |
| Database | Supabase (Postgres) | PlanetScale, Neon | SQLite (prod), MongoDB |
| ORM | Prisma | Drizzle ORM | Raw SQL (unless optimization needed) |
| API Style | REST (Next.js API Routes) | tRPC (fullstack TS) | GraphQL (unless needed) |
| Cache | Upstash Redis | Vercel KV | In-memory (stateful servers) |
| Deployment | Vercel | Railway, Fly.io | Self-hosted (unless required) |
| Testing | Vitest + Playwright | Jest + Cypress | — |

### Mobile (React Native — JINC Standard)

| Layer | Preferred | Acceptable | Avoid |
|-------|-----------|------------|-------|
| Framework | Expo (managed workflow) | Expo (bare) | RN CLI alone |
| Navigation | Expo Router | React Navigation | Custom routing |
| State | Zustand | Jotai | Redux |
| API Client | TanStack Query + Axios | SWR + Fetch | Raw fetch without error handling |
| Auth | Supabase Auth | Clerk | Custom JWT |
| Storage | Expo SecureStore | AsyncStorage (non-sensitive) | LocalStorage |
| Testing | Jest + Detox | — | Manual only |

### Backend / API (Node.js — JINC Standard)

| Layer | Preferred | Acceptable | Avoid |
|-------|-----------|------------|-------|
| Runtime | Node.js 20 LTS | Bun | Deno (unless WASM target) |
| Framework | Fastify | Express, Hono | NestJS (over-engineered for most cases) |
| Validation | Zod | Yup | Joi |
| Queue | BullMQ (Redis) | Inngest | Home-grown polling |
| Observability | OpenTelemetry + Sentry | Datadog | console.log only |
| Config | `dotenv` + `env-schema` | `t3-env` | Hardcoded values |

### CMS (JINC Standard — Strapi 5)

| Aspect | Convention |
|--------|-----------|
| Version | Strapi 5.x (current) |
| DB | Postgres 16 (never SQLite in prod) |
| Media | Cloudinary provider |
| Auth | JWT + API tokens per service |
| Deployment | Railway (CMS) + Vercel (Frontend) |
| Content Types | Use `type: collectionType` for editorial content |
| Webhooks | Use for content pipeline triggers |

---

## 🎨 Design System Rules (Non-Negotiable)

### Color System — Neutral-First Palette
JINC uses a **semantic neutral** color system. No category colors on UI elements.

```css
/* JINC Color Tokens */
--color-neutral-50: #FAFAFA;
--color-neutral-100: #F5F5F5;
--color-neutral-200: #E5E5E5;
--color-neutral-300: #D4D4D4;
--color-neutral-400: #A3A3A3;
--color-neutral-500: #737373;
--color-neutral-600: #525252;
--color-neutral-700: #404040;
--color-neutral-800: #262626;
--color-neutral-900: #171717;

/* Semantic mapping */
--color-bg-primary: var(--color-neutral-50);
--color-text-primary: var(--color-neutral-900);
--color-border: var(--color-neutral-200);
--color-interactive: var(--color-neutral-900); /* hover: neutral-700 */
```

**🚫 Purple/Violet Ban:** Never use violet or purple (`#6B21A8`, `purple`, `violet`, `hsl(270-300, *)`) in any UI element.

**Typography:**
- Serif font: Body content (articles, long-form text)
- Sans-serif font: UI elements (buttons, labels, navigation)
- Maximum content width: `70ch` (readability lock)
- Minimum text contrast: 7:1 ratio (WCAG AAA)

### Accessibility Requirements (WCAG 2.2 AAA)
- Keyboard navigation: Full `Tab` / `Shift+Tab` with logical order
- Focus indicator: `focus-visible:ring-2` on all interactive elements
- Screen readers: `aria-label` on icon-only buttons, `aria-hidden` on decorative elements
- Images: Alt text required. Use `<AutoAltImage>` component with AI-generated fallback
- Motion: Respect `prefers-reduced-motion` — wrap all CSS animations

---

## 📝 ADR Format (Architecture Decision Records)

Use this format for all ADRs in the Tech Stack section:

```markdown
### ADR-[N]: [Decision Title]

**Date:** [YYYY-MM-DD]
**Status:** 🟢 Accepted | 🟡 Proposed | 🔴 Deprecated

**Context:**
[What problem or need prompted this decision? What constraints existed?]

**Decision:**
[What was decided? Be specific and unambiguous.]

**Rationale:**
[Why was this option chosen over alternatives? Reference alternatives considered.]

**Alternatives Considered:**
| Option | Rejected Because |
|--------|-----------------|
| [Alt 1] | [Reason] |
| [Alt 2] | [Reason] |

**Consequences:**
- **Positive:** [Benefits of this decision]
- **Negative:** [Trade-offs or risks accepted]
- **Technical debt:** [Any shortcuts taken that must be revisited]

**Review At:** [Milestone or date to revisit this decision]
```

---

## 🔌 API Naming Conventions

### REST API Standards

```
Base URL: /api/v{major-version}/

# Collections
GET    /api/v1/articles              → List (with pagination)
POST   /api/v1/articles              → Create

# Resources
GET    /api/v1/articles/:id          → Read single
PATCH  /api/v1/articles/:id          → Partial update (prefer over PUT)
DELETE /api/v1/articles/:id          → Soft delete (add ?force=true for hard)

# Nested resources
GET    /api/v1/articles/:id/comments → List article comments
POST   /api/v1/articles/:id/comments → Add comment

# Actions (when REST verbs don't fit)
POST   /api/v1/articles/:id/publish  → Publish action
POST   /api/v1/articles/:id/archive  → Archive action
```

**Response envelope standard:**
```json
{
  "data": { ... },           // or array for collections
  "meta": {                  // collections only
    "total": 100,
    "page": 1,
    "per_page": 20
  },
  "error": null              // or { "code": "E_...", "message": "..." }
}
```

**Error codes:** Always prefix with `E_` followed by domain and issue:
- `E_AUTH_REQUIRED` — unauthenticated
- `E_AUTH_FORBIDDEN` — authenticated but unauthorized
- `E_VALIDATION_FAILED` — input validation error (include `fields` array)
- `E_NOT_FOUND` — resource doesn't exist
- `E_CONFLICT` — state conflict (e.g., duplicate slug)
- `E_ACCESSIBILITY_REQUIRED` — JINC-specific: content fails a11y requirements

---

## 🗄️ Database Conventions

### Postgres / Supabase Schema Standards

```sql
-- Table naming: plural snake_case
CREATE TABLE articles (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug        TEXT NOT NULL UNIQUE,
  title       TEXT NOT NULL,
  status      TEXT NOT NULL DEFAULT 'draft'
              CHECK (status IN ('draft', 'review', 'published', 'archived')),
  author_id   UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
  content     TEXT,
  alt_texts   JSONB DEFAULT '{}',  -- { image_url: alt_text }
  metadata    JSONB DEFAULT '{}',  -- extensible without migrations
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  deleted_at  TIMESTAMPTZ          -- soft delete (NULL = active)
);

-- Always add updated_at trigger
CREATE TRIGGER set_updated_at
  BEFORE UPDATE ON articles
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- RLS enabled by default in Supabase
ALTER TABLE articles ENABLE ROW LEVEL SECURITY;
```

**Naming rules:**
- Tables: `plural_snake_case` (e.g., `user_profiles`, `article_revisions`)
- Columns: `snake_case`
- PKs: Always `id UUID` with `gen_random_uuid()`
- FKs: `{referenced_table_singular}_id` (e.g., `author_id`, `category_id`)
- Booleans: `is_` or `has_` prefix (e.g., `is_published`, `has_alt_text`)
- Timestamps: `*_at` suffix (e.g., `created_at`, `published_at`, `deleted_at`)
- Soft delete: Always `deleted_at TIMESTAMPTZ` — never hard delete unless legally required

---

## 📦 Repository & Branch Conventions

### Branch Strategy (JINC DevOps)

```
main          ← Production. Protected. No direct pushes.
  └── feat/[feature-name]    ← Feature branches
  └── fix/[bug-name]         ← Bug fixes
  └── docs/sdd-[feature]     ← SDD and documentation
  └── infra/[change]         ← Infrastructure changes
  └── chore/[task]           ← Dependencies, tooling
```

### Commit Message Convention (Conventional Commits + JINC)

```
<type>(<scope>): <description>

[body — optional, for complex changes]

[footer — issue refs, breaking changes]
```

Types:
- `feat` — new feature
- `fix` — bug fix
- `docs` — documentation (including SDD)
- `refactor` — code restructure without behavior change
- `perf` — performance improvement
- `test` — test additions/changes
- `chore` — dependency updates, tooling
- `a11y` — accessibility improvement (JINC-specific)
- `infra` — infrastructure/deployment changes
- `ethics` — content safety, LGPD compliance changes (JINC-specific)

### Git Tag — State Saving (JINC Versionamento Perpétuo)

When a milestone is reached:
```bash
git tag -a v{Major}.{Minor}.{Patch}-{branch-name} -m "feat: [what was completed and validated]"
git push origin v{Major}.{Minor}.{Patch}-{branch-name}
```

---

## 🔐 Security Standards

- **Secrets:** Never in code. Always in `.env`. Never in `git add`. Use `dotenv-vault` or Vercel env for CI.
- **Dependencies:** Run `npm audit` before every deploy. Alert on HIGH/CRITICAL.
- **Auth:** Always PKCE flow for public clients. Never implicit flow.
- **API:** Rate limit all public endpoints. Default: 100 req/min per IP.
- **Headers:** `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options` required in prod.
- **Input:** Never trust client input. Always validate with Zod/schema before processing.
- **Logging:** Never log PII, tokens, or passwords. Redact before logging.

---

## 🧪 Testing Pyramid (JINC Standard)

```
         E2E (Playwright)        ← Critical user journeys only (5-10% of tests)
      ──────────────────────
    Integration Tests (Vitest)   ← API, DB, service integrations (20-30%)
  ────────────────────────────
Unit Tests (Vitest / Jest)        ← Business rules, utils, components (60-70%)
```

**Test file placement:**
- Unit: Colocated with source — `feature.ts` → `feature.test.ts`
- Integration: `tests/integration/`
- E2E: `tests/e2e/` (Playwright)

**Coverage minimum:** 80% on business rule files. Not required on UI-only components.
