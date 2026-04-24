# Antigravity JINC Skills 🪐

Uma infraestrutura soberana e orientada a IA (_AI-native_) para orquestração de múltiplos agentes e desenvolvimento contínuo de _skills_. Construída sob o paradigma do **Vibe-Coding**, esta arquitetura utiliza um motor agnóstico de modelos (otimizado para Gemini 2.5/3.1 Pro via Antigravity IDE) para automatizar, gerar e auditar fluxos de trabalho de engenharia de software e jornalismo inclusivo.

Este repositório é fundamentado e baseado no framework [Antigravity Kit](https://github.com/vudovn/antigravit-kit).

## 🏗️ Arquitetura e Governança (SDD)

Este repositório é estritamente governado pelo paradigma **Specification-Driven Development (SDD)**. Nenhuma habilidade, agente ou documento arquitetural existe fora de um contrato de dados rigidamente tipado.

A integridade estrutural é mantida por um motor **Pydantic** (`.agents/scripts/checklist.py`), que atua como o juiz final sobre a validade de qualquer _skill_ injetada no ecossistema.

### A "Catraca" de Integração Contínua (CI/CD)

Para evitar alucinações de LLMs e a degradação do contexto, o repositório conta com uma blindagem em duas camadas:

1. **Local (Husky + lint-staged):** Intercepta operações de `git commit`, aplicando formatação forçada via Prettier e rodando o validador Pydantic. Arquivos fora do padrão estrutural são sumariamente rejeitados antes de tocarem a _staging area_.
2. **Remota (GitHub Actions):** Pipeline cirúrgico e otimizado que executa a validação Python em instâncias efêmeras para garantir a imutabilidade do contrato SDD na _branch_ principal.

## 🤖 Ecossistema de Agentes

A comunicação entre modelos não é feita por inferência aleatória, mas por um "Handshake" algorítmico baseado em regras de domínio.

- **`orchestrator` (O Maestro):** Atua como o _API Gateway_ do ecossistema. Analisa o `PLAN.md`, aplica checkpoints de roteamento rigorosos e invoca os agentes de domínio corretos (ex: `frontend-specialist`, `database-architect`, `test-engineer`) de forma sequencial e isolada.
- **`skill-creator` (A Fábrica):** Agente recursivo especializado em construir, auditar e realizar testes A/B (_evals_) quantitativos em novas _skills_, retroalimentando a capacidade da própria infraestrutura.

## 📂 Topologia do Repositório

```text
antigravity-jinc-skills/
├── .agents/
│   ├── agents/          # Manifestos de personas autônomas e especialistas de domínio
│   ├── rules/           # Governança global e protocolos do ecossistema JINC
│   ├── scripts/         # Ferramentas determinísticas Python (Validador Pydantic, etc)
│   ├── skills/          # Diretório modular de habilidades acionáveis
│   └── workflows/       # Cadeias de execução multi-agente
├── .github/workflows/   # Pipeline de Integração Contínua (SDD Validation)
├── package.json         # Roteamento de automação local (Husky, Prettier)
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

---

### Sincronização Final

```bash
git add README.md
git commit -m "docs: atualizacao do readme com referencia ao framework base antigravit-kit"
git push origin main
```
