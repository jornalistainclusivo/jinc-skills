# Antigravity JINC Skills 🪐

Uma infraestrutura orientada a IA (_AI-native_) para orquestração de múltiplos agentes e desenvolvimento contínuo de _skills_. Construída sob o paradigma do **Vibe-Coding**, esta arquitetura é agnóstica de modelos e integrada ao **Google Antigravity**, permitindo que os fluxos JINC operem sobre os modelos de raciocínio disponibilizados pelo runtime conforme o plano e o ambiente do usuário. O ecossistema JINC automatiza, gera e audita fluxos de trabalho de engenharia de software em jornalismo inclusivo.

Na documentação atual do Antigravity, os modelos selecionáveis incluem **Gemini 3.8 Flash, Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.1 Pro, Claude Sonnet 4.6 (thinking), Claude Opus 4.6 (thinking) e GPT-OSS-120b**. A disponibilidade pode variar por plano e evoluir independentemente deste repositório. O Antigravity também utiliza modelos adicionais não selecionáveis pelo usuário em partes específicas do runtime, como o **Nano Banana 2** para tarefas de geração de imagens.

> **Modelos disponíveis:** A lista de modelos é controlada pelo Google Antigravity e pode mudar sem alterações neste repositório. JINC é agnóstico de modelos; a disponibilidade e seleção de modelos pertencem ao ambiente de execução do Antigravity. Consulte a [documentação oficial de modelos do Antigravity](https://antigravity.google/docs/models/) para a disponibilidade atual.

Este repositório é uma infraestrutura independente derivada do [AG Kit](https://github.com/vudovn/ag-kit), fortemente adaptada para impor as diretrizes de acessibilidade (WCAG 2.2 AAA), arquitetura Zero-Trust e Governança algorítmica do Jornalista Inclusivo (JINC).

## 🏗️ Arquitetura e Governança (SDD)

Este repositório é estritamente governado pelo paradigma **Specification-Driven Development (SDD)**. Nenhuma habilidade, agente ou documento arquitetural existe fora de um contrato de dados rigidamente tipado.

A integridade estrutural e semântica é mantida por validadores rigorosos baseados em **Pydantic** (`.agents/scripts/sdd_validator.py` e `.agents/scripts/checklist.py`), que atuam como os juízes finais sobre a validade de qualquer _skill_ injetada no ecossistema e asseguram que o orquestrador mapeie a realidade arquitetural (`.agents/scripts/sync_architecture.py`).

### A "Catraca" de Integração Contínua (CI/CD)

Para evitar alucinações de LLMs e a degradação do contexto, o repositório conta com uma blindagem em duas camadas:

1. **Local (Husky + lint-staged):** Intercepta operações de `git commit`, aplicando formatação forçada via Prettier e rodando o validador Pydantic. Arquivos fora do padrão estrutural são sumariamente rejeitados antes de tocarem a _staging area_.
2. **Remota (GitHub Actions):** Pipeline cirúrgico e otimizado que executa a validação Python em instâncias efêmeras para garantir a imutabilidade do contrato SDD na _branch_ principal.

### 🛡️ Protocolo DevOps & Zero-Trust

A infraestrutura segue estritamente as diretrizes do **DevOps JINC Protocol** (`.agents/rules/devops-jinc-protocol.md`), exigindo:

- **Zero-Hallucination Policy** na geração de dependências e infraestrutura.
- **Ambiente Zero-Trust** com sanitização de _inputs_ e proteção de _secrets_.
- **Higiene de Ambiente e Versionamento Perpétuo** através de _Git Tags_ semânticas e scripts locais (ex: `sanitize-local.sh`).
- **Validação de Pull Requests e Deployments** com _templates_ mandatórios e execução da Catraca, abrangendo Core Web Vitals, conformidade WCAG 2.2 AAA e revisão algorítmica de código.
- **Human Gate:** Automações param em limites críticos de execução (ex: _merges_, alterações de infraestrutura ou deploys) exigindo aprovação humana explícita, suportada por evidências geradas pelas ferramentas de validação.

## 🤖 Ecossistema de Agentes (21 Especialistas)

A comunicação entre modelos não é feita por inferência aleatória, mas por um "Handshake" algorítmico baseado em regras de domínio.

| Agente                       | Foco              | Descrição                                                                   |
| ---------------------------- | ----------------- | --------------------------------------------------------------------------- |
| **`orchestrator`**           | Coordenação       | API Gateway do ecossistema. Analisa planos, roteia para agentes de domínio. |
| **`project-planner`**        | Planejamento      | Quebra requisitos em tarefas, planeja estrutura de arquivos e dependências. |
| **`product-owner`**          | Produto           | Ponte estratégica entre negócios e engenharia. Priorização de backlog.      |
| **`product-manager`**        | Requisitos        | User stories, acceptance criteria, specs de produto.                        |
| **`a11y-master`**            | ♿ Acessibilidade | **Pilar JINC.** WCAG 2.2 AAA, WAI-ARIA, acessibilidade cognitiva, teste AT. |
| **`frontend-specialist`**    | UI/UX Web         | React/Next.js, design system, performance-first.                            |
| **`mobile-developer`**       | Mobile            | React Native, Flutter, padrões nativos iOS/Android.                         |
| **`backend-specialist`**     | APIs/Server       | Node.js, Python, serverless, edge.                                          |
| **`database-architect`**     | Dados             | Schema design, query optimization, migrações.                               |
| **`security-auditor`**       | Segurança         | OWASP 2025, supply chain, zero trust.                                       |
| **`penetration-tester`**     | Ofensiva          | Red team, exploits, simulação de ataques.                                   |
| **`devops-engineer`**        | Deploy/CI-CD      | Produção, rollback, monitoramento, Docker.                                  |
| **`performance-optimizer`**  | Performance       | Core Web Vitals, profiling, bundle optimization.                            |
| **`test-engineer`**          | Testes            | TDD, unit/integration/E2E, cobertura.                                       |
| **`qa-automation-engineer`** | QA                | Playwright, Cypress, pipelines de regressão.                                |
| **`debugger`**               | Debug             | Root cause analysis, crash investigation.                                   |
| **`seo-specialist`**         | SEO/GEO           | SEO, E-E-A-T, Generative Engine Optimization.                               |
| **`explorer-agent`**         | Descoberta        | Análise profunda de codebase, auditorias iniciais.                          |
| **`code-archaeologist`**     | Legacy            | Reverse engineering, modernização de código legado.                         |
| **`documentation-writer`**   | Docs              | README, API docs, changelog técnico.                                        |
| **`game-developer`**         | Games             | Unity, Godot, Unreal, Phaser, Three.js.                                     |

> **Routing inteligente:** O `intelligent-routing` skill analisa automaticamente cada requisição e seleciona o(s) agente(s) mais adequado(s) sem necessidade de menção explícita.

## 📂 Topologia do Repositório

```text
antigravity-jinc-skills/
├── .agents/
│   ├── .shared/         # Recursos, templates ou metadados compartilhados entre agentes
│   ├── agents/          # 21 manifestos de personas autônomas e especialistas de domínio
│   ├── rules/           # Governança global e protocolos do ecossistema JINC
│   ├── scripts/         # Ferramentas determinísticas Python (Gatekeepers, Validadores)
│   ├── skills/          # 73+ habilidades acionáveis modulares
│   ├── workflows/       # Cadeias de execução e roteamento multi-agente
│   └── ARCHITECTURE.md  # Mapa do ecossistema de agentes (Auto-gerado)
├── .github/workflows/   # Pipeline de Integração Contínua (Validação SDD Remota)
├── .husky/              # Gatilhos locais de pré-commit (A Catraca)
├── package.json         # Roteamento de automação local (lint-staged, npm scripts)
└── README.md
```

## 📜 Regras de Contribuição (Para Agentes e Humanos)

Toda nova habilidade adicionada em `.agents/skills/` **DEVE** cumprir o seguinte contrato para ser aceita pelo sistema:

1. Conter um manifesto obrigatório chamado `SKILL.md`.
2. O arquivo deve iniciar com um bloco de metadados (_Frontmatter_) YAML demarcado por `---`.
3. O bloco YAML requer, incondicionalmente, as chaves `name` e `description`.
4. **Mandatório:** A string da chave `description` deve ser envolvida em aspas duplas (`"..."`) para sanitizar caracteres especiais (como `:`) e evitar falhas no _parser_ YAML.

## 🔌 Integração com Model Context Protocol (MCP)

Para que o orquestrador e as _skills_ deste repositório sejam consumíveis por sua IDE ou agentes externos, este diretório deve ser exposto através de um servidor **Model Context Protocol (MCP)**.

### Configuração Recomendada

Ao configurar seu cliente MCP, mapeie diretamente a raiz deste repositório para garantir a leitura do `ARCHITECTURE.md` e do diretório `.agents/`. Mantenha os objetos de configuração estritamente focados na conexão, excluindo metadados de serialização interna das IDEs.

**Exemplo de manifest (JSON) limpo:**

```json
{
  "mcpServers": {
    "jinc-skills-repo": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<SUA_CHAVE_AQUI>"
      }
    }
  }
}
```
