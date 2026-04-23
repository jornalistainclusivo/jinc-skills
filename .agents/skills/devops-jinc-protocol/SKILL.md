---
name: devops-jinc-protocol
version: 1.2
status: Core-Governance
location: .agents/rules/devops-jinc-protocol.md
description: Framework de governança para Vibe-Coding e Engenharia Híbrida.
principles:
  - Accessibility-First (WCAG 2.2 AAA)
  - Zero-Trust Security (No exposed secrets)
  - Atomic Commits (Clean history)
  - Documentation-as-Code (ADRs and Logs)
---

# 🛡️ DevOps JINC Protocol: Hybrid Governance

## 1. Fluxo de Trabalho (The JINC Way)

### 1.1 O Ciclo Vibe-Coding

1. **Intenção (Humano):** Define o "quê" e o "porquê" (ex: "Criar o ContextualLayer para acessibilidade cognitiva").
2. **Prototipagem & Crítica (IA):** Sugere a implementação, mas **deve** questionar ambiguidades antes de escrever o código.
3. **Refinamento (H+IA):** Iteração focada em performance e refinamento do Design System Neutro.
4. **Validação de Saída (IA):** Antes de entregar, o agente deve rodar os scripts de validação (`checklist.py`) e gerar o PR Template preenchido.

### 1.2 Regras de Ouro para o Agente

- **Proibição de Alucinação:** Se uma biblioteca não existir ou uma versão do Next.js não suportar uma feature, o agente deve avisar, nunca inventar.
- **Limpeza de Rastro:** Arquivos `.env` nunca devem ser sugeridos para `git add`.
- **Higiene de Branch:** Todo trabalho novo deve nascer em uma branch `feat/` ou `fix/`.

---

## 🏗️ 2. Template de Pull Request (Saída Mandatória)

_Sempre que o Agente finalizar uma tarefa, ele deve gerar o conteúdo abaixo preenchido com base no que foi realmente feito._

```markdown
# 🤖 [TIPO]: Descrição Concisa (Ex: feat: infra-docker-isr)

## 📝 Descrição

## 🔗 Issue / Sprint

## 🏷️ Tipo de Mudança

- [ ] `ethics` / `a11y`: Acessibilidade e Inclusão.
- [ ] `infra`: Docker, CI/CD, ISR, Deploy.
- [ ] `feat`: Nova funcionalidade.
- [ ] `fix`: Correção de bug.
- [ ] `refactor`: Limpeza de código/Design System.

---

## ♿ Checklist de Acessibilidade (WCAG 2.2 AAA)

- [ ] **Navegação:** Teclado (Tab/Shift+Tab) funcional e lógico.
- [ ] **Foco:** Visível (`focus-visible:ring-2`) em todos os elementos.
- [ ] **Semântica:** Uso de tags nativas (HTML5) em vez de divs clicáveis.
- [ ] **Leitores de Tela:** `aria-labels` e `aria-hidden` aplicados onde necessário.
- [ ] **Contraste:** Proporção 7:1 (AAA) validada.
- [ ] **Imagens:** Componente `<AutoAltImage>` com IA-fallback implementado.

## 🏛️ Design System & Arquitetura

- [ ] **Paleta:** Uso exclusivo de `neutral-50` a `neutral-900`. Zero cores de categoria.
- [ ] **Grid:** Leitura travada em `max-w-[70ch]`.
- [ ] **Tipografia:** `font-serif` para conteúdo, `font-sans` para interface.

## 🛠️ Qualidade e GitOps

- [ ] **Secrets:** `.env` validado e seguro.
- [ ] **Scripts:** `checklist.py` executado com sucesso.
- [ ] **Docker:** Build multi-stage testado (se aplicável).
- [ ] **Logs:** Registro de decisão adicionado ao `DECISION_LOG.md`.

## 🧪 Como Testar (Passo a Passo)

1. `git checkout <branch>`
2. `npm install` (ou `docker-compose up`)
3. Testar comportamento em: `http://localhost:3000/...`

---
```

---

## 3. Comandos de Operação (Slash Commands)

- `/plan`: O agente deve decompor a intenção humana em tarefas atômicas antes de codar.
- `/audit`: O agente revisa o próprio código buscando falhas de segurança e A11y.
- `/status`: Resumo do que foi feito vs. o que falta no Roadmap atual.
