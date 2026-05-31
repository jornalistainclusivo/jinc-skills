---
name: devops-jinc-protocol
version: 2.0
status: Core-Governance
location: .agents/rules/devops-jinc-protocol.md
description: Framework de governança de elite para Vibe-Coding, DevOps e Full-Stack Engineering.
principles:
  - Accessibility-First (WCAG 2.2 AAA + Cognitive A11y)
  - Zero-Trust Security (Shift-Left, SBOM, No exposed secrets)
  - Atomic Commits (Conventional Commits, Clean history)
  - Documentation-as-Code (ADRs, Telemetry, and Logs)
  - Agentic Predictability (Zero-Hallucination, Explicit reasoning)
---

# 🛡️ DevOps JINC Protocol: AI-Native Hybrid Governance

## 1. O Motor Agêntico (Rules of Engagement)

O agente de IA operando neste repositório **deve** internalizar este comportamento antes de qualquer modificação:

- **Zero-Hallucination Policy:** Se uma biblioteca, dependência ou versão do Next.js/React não possuir uma funcionalidade nativa, o agente DEVE alertar o humano. Proibido inventar APIs ou _polyfills_ inseguros.
- **Security by Default:** Arquivos de ambiente (`.env*`), chaves de API, tokens e senhas NUNCA devem ser adicionados ao _stage_ do Git. O agente deve sugerir a inclusão em `.gitignore` pró-ativamente.
- **Agnosticismo de Estado Lógico:** Questione ambiguidades de arquitetura antes de escrever a primeira linha de código. Use o comando `/plan` compulsoriamente para _features_ complexas.

## 2. Padrões de Engenharia Full-Stack & DevOps

### 2.1 Arquitetura Next.js / React

- **Server-First:** Priorizar React Server Components (RSC) para redução de bundle JavaScript. Usar a diretiva `"use client"` estritamente nas bordas da árvore de componentes (onde há interatividade ou estado).
- **Data Fetching:** Implementar ISR (Incremental Static Regeneration) ou cache revalidado por _tags_ para otimização de performance no Edge.
- **Observabilidade:** Todo bloco `try/catch` de funções críticas deve gerar logs estruturados, não apenas `console.error`.

### 2.2 Segurança de Infraestrutura (Zero-Trust)

- **Sanitização de Inputs:** Nunca confiar no input do cliente ou do servidor. Validar dados com esquemas robustos (ex: Zod) no nível da API e de _Server Actions_.
- **Docker Multi-Stage:** Imagens de contêineres devem ser _multi-stage_, utilizando imagens distroless ou Alpine mínimas para produção, reduzindo a superfície de ataque.
- **Supply Chain:** Sugerir rodar `npm audit` ou ferramentas de escaneamento de vulnerabilidade (SAST/DAST) após adições significativas de dependências.

---

## 3. Fluxo de Trabalho Híbrido (The JINC SDLC)

1.  **Intenção (Humano):** Define o "quê" e o "porquê" (ex: "Criar o componente de busca universal com filtros").
2.  **Mapeamento & Segurança (IA):** O agente avalia dependências e riscos de segurança da solicitação.
3.  **Prototipagem de Acessibilidade (IA):** O agente constrói o esqueleto HTML semântico e as marcações WAI-ARIA **antes** do CSS e da lógica JS.
4.  **Execução (H+IA):** Implementação lógica focada no Design System Neutro e performance (Core Web Vitals).
5.  **Validação de Saída (IA):** Rodar scripts de validação (`checklist.py` / linters / test suites) e gerar o **PR Template**.

---

## 🏗️ 4. Pull Request Contract (Saída Mandatória)

_Ao finalizar uma branch, o agente DEVE compilar o resultado neste template exato:_

```markdown
# 🤖 [TIPO]: Descrição Concisa (Ex: feat: implementa camada de cache ISR)

## 📝 Resumo do Contexto

[Explicação técnica do que foi resolvido e por que esta abordagem foi escolhida. Links para ADRs se aplicável].

## 🔗 Issue / Ticket

Ref: #000

## 🏷️ Escopo de Mudança (Selecione)

- [ ] `a11y`: Acessibilidade (Sensorial ou Cognitiva).
- [ ] `sec`: Correção/Aprimoramento de Segurança.
- [ ] `infra`: Docker, CI/CD, ISR, Deploy.
- [ ] `feat`: Nova funcionalidade.
- [ ] `fix`: Correção de bug.
- [ ] `refactor`: Limpeza de código/Design System.

---

## ♿ Auditoria de Inclusão (WCAG 2.2 AAA & Cognitive)

- [ ] **Navegação:** Teclado (Tab/Shift+Tab) mapeado, sem _keyboard traps_.
- [ ] **Foco:** Visível (`focus-visible:ring-2` ou superior) em elementos interativos.
- [ ] **Semântica ARIA:** `aria-labels`, `aria-expanded`, e `aria-hidden` aplicados conforme W3C.
- [ ] **Contraste & Cor:** Proporção mínima de 7:1 (AAA) respeitada. Nenhuma informação transmitida _apenas_ por cor.
- [ ] **Imagens & Fallbacks:** Componente `<AutoAltImage>` implementado com descrições semânticas.
- [ ] **Acessibilidade Cognitiva:** Animações respeitam `prefers-reduced-motion`.

## 🏛️ Design System Neutro & CWV

- [ ] **Paleta:** Uso exclusivo do espectro `neutral-50` a `neutral-900`.
- [ ] **Métricas CWV:** LCP otimizado (imagens em WebP/AVIF com `priority`), sem CLS (tamanhos de mídia definidos).
- [ ] **Tipografia:** `font-serif` restrito a conteúdo longo; `font-sans` para microcópia e UI. Leitura travada em `max-w-[70ch]`.

## 🛠️ DevOps & Zero-Trust

- [ ] **Secrets:** Ausência absoluta de credenciais hardcoded. `.env.example` atualizado se necessário.
- [ ] **Docker:** Build testado no ambiente local.
- [ ] **Logs:** Decisões arquiteturais registradas no `DECISION_LOG.md`.

## 🧪 Plano de Teste e Rollback

1. Comandos para teste local: `git fetch && git checkout <branch> && npm run dev`
2. URL esperada: `http://localhost:3000/...`
3. **Plano de Rollback:** Reverter o commit `XXXXX` se as métricas de latência aumentarem >20%.
```

---

## 5. Comandos de Operação Especiais (Agent Slash Commands)

O agente reconhece as seguintes diretivas no chat:

- `/plan <objetivo>`: Interrompe a execução. O agente deve listar as etapas técnicas detalhadas, dependências e riscos antes de gerar código.
- `/audit`: Dispara uma revisão silenciosa no arquivo atual em busca de vulnerabilidades OWASP, vazamento de memória e quebras no WCAG.
- `/refactor`: Reescreve o bloco de código focado em modularização, extração de componentes de servidor (Next.js) e simplificação ciclomática.
- `/status`: Avalia o git diff atual contra a intenção original, identificando o que falta para completar a sprint.
