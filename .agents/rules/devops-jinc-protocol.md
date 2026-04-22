---
trigger: always_on
---

# 🛡️ DevOps JINC Protocol: Hybrid Governance

Este protocolo estabelece as diretrizes mandatórias para a colaboração entre o Arquiteto Humano e os Agentes de IA na organização **Jornalista Inclusivo (JINC Apps)**. Seu objetivo é garantir que toda automação resulte em código acessível, seguro e arquiteturalmente coerente.

---
name: devops-jinc-protocol
version: 1.3
status: Core-Governance
location: .agents\rules\devops-jinc-protocol.md
description: Framework de governança para Vibe-Coding, Engenharia Híbrida e Versionamento Perpétuo.
Principles:
- Accessibility-First (WCAG 2.2 AAA)
- Zero-Trust Security (No exposed secrets)
- Atomic Commits (Clean history)
- Documentation-as-Code (ADRs and Logs)
- Immutable Versioning (Git Tags State Saving)
- Environment Hygiene (No local contamination)
---

## 1. Fluxo de Trabalho (The JINC Way)

### 1.1 O Ciclo Vibe-Coding

1. **Intenção (Humano):** Define o "quê" e o "porquê" (ex: "Criar o ContextualLayer para acessibilidade cognitiva").
2. **Prototipagem & Crítica (IA):** Sugere a implementação, mas **deve** questionar ambiguidades antes de escrever o código.
3. **Refinamento (H+IA):** Iteração focada em performance e refinamento do Design System Neutro.
4. **Validação de Saída (IA):** Antes de entregar, o agente deve rodar os scripts de validação `checklist.py`) e gerar o PR Template preenchido.
5. **Preservação de Estado (H+IA):** Congelamento da versão validada utilizando Git Tags antes de mesclar ou encerrar o ciclo.

### 1.2 Regras de Ouro para o Agente

- **Proibição de Alucinação:** Se uma biblioteca não existir ou uma versão do Next.js não suportar uma feature, o agente deve avisar, nunca inventar.
- **Limpeza de Rastro:** Arquivos `.env` nunca devem ser sugeridos para `git add`.
- **Higiene de Branch:** Todo trabalho novo deve nascer em uma branch `feat/` ou `fix/`.
- **Higiene Local:** O agente deve sugerir limpeza de artefatos sensíveis/cache antes de finalizar sessões (ver seção 1.4).

### 1.3 Metodologia de Salvamento de Estado (Git Tags)

Para garantir a rastreabilidade e a recuperação perpétua de estados funcionais do código no GitHub, é **obrigatório** o uso de Etiquetas de Versão (Git Tags) a cada ciclo de desenvolvimento em uma branch.

- **Quando Taguear:** Sempre que uma branch atingir um marco funcional, passar nos testes de acessibilidade (WCAG AAA) ou antes de um PR (Pull Request) ser finalizado.
- **Nomenclatura Híbrida:** O padrão deve combinar Versionamento Semântico com o escopo da branch: `v[Major].[Minor].[Patch]-[nome-da-branch]` (Exemplo: `v1.2.4-contextual-layer`).
- **Comandos Mandatórios:** O Agente ou Desenvolvedor deve gerar e executar tags anotadas, detalhando o que foi salvo:
  1. `git tag -a vX.X.X-branch-name -m "feat: implementação concluída e validada"`
  2. `git push origin vX.X.X-branch-name` (A tag deve ser enviada explicitamente ao remote).

### 1.4 Higiene de Ambiente Local (Sanitização)

Antes de encerrar uma sessão de desenvolvimento ou alternar entre branches, o agente **deve** garantir que o ambiente local esteja higienizado segundo os princípios Zero-Trust:

- **Sanitização de Secrets:**
  - Remover arquivos `.env.local`, `.env.development` ou logs que contenham tokens, chaves de API ou credenciais de teste
  - Verificar que nenhum arquivo em `/tmp`, `/logs` ou `.cache` contenha dados PII (Personally Identifiable Information) de testes
  - Executar `git clean -fd` apenas após confirmação explícita do Humano, ou preferencialmente usar `git stash` para experimentos locais
- **Limpeza de Artefatos Temporários:**
  - Remover diretórios de build local: `.next/`, `dist/`, `build/`, `coverage/` (exceto quando explicitamente necessário para debug)
  - Limpar cache de pacotes: `npm cache clean --force` ou `rm -rf node_modules/.cache` quando houver suspeita de contaminação entre branches
  - Excluir arquivos de dump, screenshots de debug e dados de mock gerados durante o desenvolvimento
- **Isolamento de Dados de Teste:**
  - Garantir que databases SQLite, arquivos JSON de mock ou fixtures temporárias não sejam commitados acidentalmente
  - Verificar `.gitignore` antes de finalizar: deve incluir `*.local`, `*.log`, `.turbo`, `.vercel`
- **Verificação Pré-Push:**
  - Rodar `git status` e validar que apenas arquivos intencionais estão staged
  - Executar scan rápido por secrets: `git grep -i "password\|secret\|token" -- :^package.json :^README.md` ou usar ferramenta como `git-secrets`
  - Confirmar que não há alterações não salvas (uncommitted changes) críticas antes de criar tags
- **Comando de Higienização Recomendado (Checklist Local):**

  ```bash
  # Script sugerido: sanitize-local.sh
  echo "🧹 Higienizando ambiente..."
  rm -rf .next/ coverage/ *.log
  git stash push -m "wip: backup automático pre-higienização" --include-untracked
  npm cache verify
  echo "✅ Ambiente sanitizado. Lembre-se: nunca commitar arquivos .env*"
  ```

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
- [ ] **Foco:** Visível `focus-visible:ring-2`) em todos os elementos.
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
- [ ] **Higiene Local:** Cache removido, logs limpos, nenhum arquivo sensível no working tree.
- [ ] **Scripts:** `checklist.py` executado com sucesso.
- [ ] **Docker:** Build multi-stage testado (se aplicável).
- [ ] **Logs:** Registro de decisão adicionado ao `DECISION_LOG.md`.
- [ ] **Versionamento:** Git Tag Semântica gerada e subida para o GitHub `git push origin vX.X.X`).

## 🧪 Como Testar (Passo a Passo)

1. `git checkout <branch>`
2. `npm install` (ou `docker-compose up`)
3. Testar comportamento em: `http://localhost:3000/...`

---

```

