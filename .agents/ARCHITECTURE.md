# Antigravity Kit Architecture

> Comprehensive AI Agent Capability Expansion Toolkit — JINC Edition

---

## 📋 Overview

Antigravity Kit is a modular system consisting of:

- **20 Specialist Agents** - Role-based AI personas
- **47 Skills** - Domain-specific knowledge modules
- **11 Workflows** - Slash command procedures

---

## 🏗️ Directory Structure

```plaintext
.agents/
├── ARCHITECTURE.md          # This file
├── agents/                  # 20 Specialist Agents
├── skills/                  # 47 Skills
├── workflows/               # 11 Slash Commands
├── rules/                   # Global Rules
└── scripts/                 # Master Validation Scripts
```

---

## 🤖 Agents (20)

Specialist AI personas for different domains.

| Agent                    | Focus                      | Skills Used                                              |
| ------------------------ | -------------------------- | -------------------------------------------------------- |
| `orchestrator`           | Multi-agent coordination   | parallel-agents, behavioral-modes                        |
| `project-planner`        | Discovery, task planning   | brainstorming, plan-writing, architecture                |
| `frontend-specialist`    | Web UI/UX                  | frontend-design, react-best-practices, tailwind-patterns |
| `backend-specialist`     | API, business logic        | api-patterns, nodejs-best-practices, database-design     |
| `database-architect`     | Schema, SQL                | database-design                                          |
| `mobile-developer`       | iOS, Android, RN           | mobile-design                                            |
| `game-developer`         | Game logic, mechanics      | game-development                                         |
| `devops-engineer`        | CI/CD, Docker              | deployment-procedures, docker-containers                 |
| `security-auditor`       | Security compliance        | vulnerability-scanner, red-team-tactics                  |
| `penetration-tester`     | Offensive security         | red-team-tactics                                         |
| `test-engineer`          | Testing strategies         | testing-patterns, tdd-workflow, webapp-testing           |
| `debugger`               | Root cause analysis        | systematic-debugging                                     |
| `performance-optimizer`  | Speed, Web Vitals          | performance-profiling                                    |
| `seo-specialist`         | Ranking, visibility        | seo-fundamentals, geo-fundamentals                       |
| `documentation-writer`   | Manuals, docs              | documentation-templates                                  |
| `product-manager`        | Requirements, user stories | plan-writing, brainstorming                              |
| `product-owner`          | Strategy, backlog, MVP     | plan-writing, brainstorming                              |
| `qa-automation-engineer` | E2E testing, CI pipelines  | webapp-testing, testing-patterns                         |
| `code-archaeologist`     | Legacy code, refactoring   | clean-code, code-review-checklist                        |
| `explorer-agent`         | Codebase analysis          | -                                                        |

---

## 🧩 Skills (47)

Modular knowledge domains that agents can load on-demand, based on task context.

### Frontend & UI (4)

| Skill                   | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| `react-best-practices`  | React & Next.js performance optimization (Vercel — 57 rules)          |
| `web-design-guidelines` | Web UI audit — 100+ rules for accessibility, UX, performance (Vercel) |
| `tailwind-patterns`     | Tailwind CSS v4 utilities                                             |
| `frontend-design`       | UI/UX patterns, design systems                                        |

### Backend & API (3)

| Skill                   | Description                    |
| ----------------------- | ------------------------------ |
| `api-patterns`          | REST, GraphQL, tRPC            |
| `nodejs-best-practices` | Node.js async, modules         |
| `python-patterns`       | Python standards, FastAPI      |

### CMS & Editorial (1)

| Skill                            | Description                                                    |
| -------------------------------- | -------------------------------------------------------------- |
| `strapi-editorial-orchestrator`  | Strapi 5 editorial AI pipeline — A11y, SEO, AST Blocks, WCAG  |

### Database (1)

| Skill             | Description                 |
| ----------------- | --------------------------- |
| `database-design` | Schema design, optimization |

### TypeScript/JavaScript (1)

| Skill               | Description                                       |
| ------------------- | ------------------------------------------------- |
| `typescript-expert`  | Type-level programming, strict typing, Zod, perf  |

### Systems Programming (1)

| Skill       | Description                                               |
| ----------- | --------------------------------------------------------- |
| `rust-pro`  | Rust 1.75+, async, ownership, systems programming         |

### Cloud & Infrastructure (3)

| Skill                   | Description                                        |
| ----------------------- | -------------------------------------------------- |
| `docker-containers`     | Dockerfile, Compose, multi-stage builds, debugging |
| `deployment-procedures` | CI/CD, deploy workflows                            |
| `server-management`     | Infrastructure management                          |

### Testing & Quality (5)

| Skill                   | Description              |
| ----------------------- | ------------------------ |
| `testing-patterns`      | Jest, Vitest, strategies |
| `webapp-testing`        | E2E, Playwright          |
| `tdd-workflow`          | Test-driven development  |
| `code-review-checklist` | Code review standards    |
| `lint-and-validate`     | Linting, validation      |

### Security (2)

| Skill                   | Description              |
| ----------------------- | ------------------------ |
| `vulnerability-scanner` | Security auditing, OWASP |
| `red-team-tactics`      | Offensive security       |

### Architecture & Planning (4)

| Skill           | Description                |
| --------------- | -------------------------- |
| `app-builder`   | Full-stack app scaffolding |
| `architecture`  | System design patterns     |
| `plan-writing`  | Task planning, breakdown   |
| `brainstorming` | Socratic questioning       |

### Spec-Driven Documentation Pipeline (3)

| Skill           | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| `prd-creator`   | Product Requirements Documents — WHAT to build and WHY       |
| `sdd-creator`   | Software Design Documents — architecture, C4, tech decisions |
| `spec-creator`  | Technical Specifications — types, contracts, state machines   |

### JINC Governance & DevOps (2)

| Skill                        | Description                                                   |
| ---------------------------- | ------------------------------------------------------------- |
| `jinc-governance-standards`  | Accessibility (WCAG 2.2 AAA), ethics, inclusive engineering    |
| `devops-jinc-protocol`       | Vibe-Coding governance, PR templates, quality gates           |

### Mobile (1)

| Skill           | Description           |
| --------------- | --------------------- |
| `mobile-design` | Mobile UI/UX patterns |

### Game Development (1)

| Skill              | Description           |
| ------------------ | --------------------- |
| `game-development` | Game logic, mechanics |

### SEO & Growth (2)

| Skill              | Description                    |
| ------------------ | ------------------------------ |
| `seo-fundamentals` | SEO, E-E-A-T, Core Web Vitals |
| `geo-fundamentals` | GenAI optimization             |

### Shell/CLI (2)

| Skill                | Description                              |
| -------------------- | ---------------------------------------- |
| `bash-linux`         | Linux commands, scripting                |
| `powershell-windows` | Windows PowerShell patterns and pitfalls |

### AI/Agent Tooling (4)

| Skill                | Description                                          |
| -------------------- | ---------------------------------------------------- |
| `prompt-engineer`    | Advanced prompt engineering, Vibe-Coding workflows   |
| `skill-creator`      | Create, evaluate, and iterate on agent skills        |
| `intelligent-routing`| Auto-select agents based on request domain analysis  |
| `mcp-builder`        | Model Context Protocol server development            |

### Cross-Cutting Utilities (7)

| Skill                     | Description                 |
| ------------------------- | --------------------------- |
| `clean-code`              | Coding standards (Global)   |
| `behavioral-modes`        | Agent personas              |
| `parallel-agents`         | Multi-agent patterns        |
| `documentation-templates` | Doc formats                 |
| `i18n-localization`       | Internationalization        |
| `performance-profiling`   | Web Vitals, optimization    |
| `systematic-debugging`    | Troubleshooting             |

---

## 🔄 Workflows (11)

Slash command procedures. Invoke with `/command`.

| Command          | Description              |
| ---------------- | ------------------------ |
| `/brainstorm`    | Socratic discovery       |
| `/create`        | Create new features      |
| `/debug`         | Debug issues             |
| `/deploy`        | Deploy application       |
| `/enhance`       | Improve existing code    |
| `/orchestrate`   | Multi-agent coordination |
| `/plan`          | Task breakdown           |
| `/preview`       | Preview changes          |
| `/status`        | Check project status     |
| `/test`          | Run tests                |
| `/ui-ux-pro-max` | Design with 50 styles    |

---

## 🎯 Skill Loading Protocol

```plaintext
User Request → Skill Description Match → Load SKILL.md
                                            ↓
                                    Read references/
                                            ↓
                                    Read scripts/
```

### Skill Structure

```plaintext
skill-name/
├── SKILL.md           # (Required) Metadata & instructions
├── scripts/           # (Optional) Python/Bash scripts
├── references/        # (Optional) Templates, docs
└── assets/            # (Optional) Images, logos
```

### Enhanced Skills (with scripts/references)

| Skill               | Files | Coverage                            |
| ------------------- | ----- | ----------------------------------- |
| `app-builder`       | 20    | Full-stack scaffolding              |

---

## 🔧 Scripts (2)

Master validation scripts that orchestrate skill-level scripts.

### Master Scripts

| Script          | Purpose                                 | When to Use              |
| --------------- | --------------------------------------- | ------------------------ |
| `checklist.py`  | Priority-based validation (Core checks) | Development, pre-commit  |
| `verify_all.py` | Comprehensive verification (All checks) | Pre-deployment, releases |

### Usage

```bash
# Quick validation during development
python .agents/scripts/checklist.py .

# Full verification before deployment
python .agents/scripts/verify_all.py . --url http://localhost:3000
```

### What They Check

**checklist.py** (Core checks):

- Security (vulnerabilities, secrets)
- Code Quality (lint, types)
- Schema Validation
- Test Suite
- UX Audit
- SEO Check

**verify_all.py** (Full suite):

- Everything in checklist.py PLUS:
- Lighthouse (Core Web Vitals)
- Playwright E2E
- Bundle Analysis
- Mobile Audit
- i18n Check

For details, see [scripts/README.md](scripts/README.md)

---

## 📊 Statistics

| Metric              | Value                         |
| ------------------- | ----------------------------- |
| **Total Agents**    | 20                            |
| **Total Skills**    | 47                            |
| **Total Workflows** | 11                            |
| **Total Scripts**   | 2 (master) + 18 (skill-level) |
| **Skill Categories**| 18                            |
| **Coverage**        | ~90% web/mobile development   |

### Skill Distribution by Category

| Category                           | Count |
| ---------------------------------- | ----- |
| Frontend & UI                      | 4     |
| Cross-Cutting Utilities            | 7     |
| Testing & Quality                  | 5     |
| Architecture & Planning            | 4     |
| AI/Agent Tooling                   | 4     |
| Backend & API                      | 3     |
| Cloud & Infrastructure             | 3     |
| Spec-Driven Documentation Pipeline | 3     |
| SEO & Growth                       | 2     |
| Shell/CLI                          | 2     |
| Security                           | 2     |
| JINC Governance & DevOps           | 2     |
| Database                           | 1     |
| TypeScript/JavaScript              | 1     |
| Systems Programming                | 1     |
| Mobile                             | 1     |
| Game Development                   | 1     |
| CMS & Editorial                    | 1     |

---

## 🔗 Quick Reference

| Need     | Agent                 | Skills                                |
| -------- | --------------------- | ------------------------------------- |
| Web App  | `frontend-specialist` | react-best-practices, frontend-design |
| API      | `backend-specialist`  | api-patterns, nodejs-best-practices   |
| Mobile   | `mobile-developer`    | mobile-design                         |
| Database | `database-architect`  | database-design                       |
| Security | `security-auditor`    | vulnerability-scanner                 |
| Testing  | `test-engineer`       | testing-patterns, webapp-testing      |
| Debug    | `debugger`            | systematic-debugging                  |
| Plan     | `project-planner`     | brainstorming, plan-writing           |
| PRD      | `product-manager`     | prd-creator                           |
| SDD      | `project-planner`     | sdd-creator                           |
| Spec     | `backend-specialist`  | spec-creator                          |
| Docker   | `devops-engineer`     | docker-containers                     |
