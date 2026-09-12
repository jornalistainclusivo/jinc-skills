---
name: mcp-builder
description: "Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks."
when_to_use: "When building or reviewing MCP servers or clients, designing MCP tools/resources/prompts, migrating protocol versions, or validating MCP security and interoperability."
risk: unknown
source: community
date_added: "2026-02-27"
version: 1.0.0
---

# MCP Server Development Guide

## Overview

Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.
Build interoperable MCP implementations against the stable **2026-07-28** specification. Treat extensions as negotiated, opt-in capabilities rather than core protocol guarantees.

> **JINC Governance Principle:** Verification establishes technical evidence, not authorization.
> For consequential MCP tool execution: Successful schema validation, capability negotiation, or tool discovery NEVER constitutes user authorization for a consequential action. Explicit user approval requirements remain separate from protocol-level technical readiness.

---

# Process

## 🚀 High-Level Workflow

Creating a high-quality MCP server involves four main phases:

### Phase 1: Deep Research and Planning

#### 1.1 Understand Modern MCP Design and Protocol Baseline

- **Stable Baseline**: The authoritative stable baseline is MCP **2026-07-28**.
- **Stateless Request Model**: Core requests are stateless and self-contained. Do not infer protocol version, client capabilities, identity, conversation, or task state from a transport connection or process lifetime. Put cross-request state behind explicit identifiers supplied on every relevant request.
- **API Coverage vs. Workflow Tools**: Balance comprehensive API endpoint coverage with specialized workflow tools. Prioritize comprehensive API coverage when uncertain.
- **Tool Naming and Discoverability**: Clear, descriptive tool names help agents find tools quickly (e.g., `github_create_issue`).

#### 1.2 Core versus Extensions

Negotiate the protocol version and capabilities; do not assume a peer implements every optional feature.

- **Stable core**: Base protocol, versioning, message patterns.
- **Optional core features**: Resources, prompts, tools, elicitation (advertise and check capabilities before use).
- **Extensions**: Tasks, Skills over MCP, MCP Apps (opt-in, require explicit support).
- **Experimental/vendor**: Draft or vendor extensions (isolate behind adapters).

_Never label an extension as stable merely because one SDK or host supports it._

#### 1.3 Study Protocol and Framework Documentation

- **MCP Protocol Documentation**: Start at `https://modelcontextprotocol.io/sitemap.xml`, fetch specific pages with `.md` suffix.
- **Recommended stack**: TypeScript (recommended) or Python.
- **Transports**:
  - `stdio`: Local process integration. Constrain process and filesystem access.
  - Streamable HTTP: Remote/shared service. Use MCP HTTP authorization, enforce network boundaries.

Load framework documentation as needed:

- [📋 View Best Practices](./reference/mcp_best_practices.md)
- [⚡ TypeScript Guide](./reference/node_mcp_server.md)
- [🐍 Python Guide](./reference/python_mcp_server.md)

---

### Phase 2: Implementation

#### 2.1 Set Up Project Structure

See language-specific guides for project setup ([⚡ TypeScript Guide](./reference/node_mcp_server.md) / [🐍 Python Guide](./reference/python_mcp_server.md)).

#### 2.2 Implement Core Infrastructure

- **Server Discovery**: Servers must implement `server/discover` for protocol-version and capability discovery.
- Create shared utilities (API client, error handling, formatting, pagination).
- Tolerate interleaved requests from unrelated tasks and validate every request independently.

#### 2.3 Implement Tools, Resources, and Prompts

For each tool:

- **Input Schema (JSON Schema 2020-12)**: Use Zod (TypeScript) or Pydantic (Python). Declare required fields explicitly. Prefer narrow enums, bounds, and `additionalProperties: false`.
- **Output Schema**: Use `structuredContent` and `outputSchema` for predictable, typed results.
- **Annotations**: Mark read-only, destructive, idempotent, or open-world behavior. _Note: Treat annotations as untrusted hints unless the server itself is trusted._
- **Actionable Error Messages**: Return stable machine-readable errors without internal stack traces or secrets.

**$ref and Validator Safety**:

- Never dereference network `$ref` values automatically.
- Reject schemas with unresolved external references.
- Bound schema depth, total subschemas, and validation time to prevent denial-of-service.

#### 2.4 Security Requirements

Apply these strict trust boundaries and security requirements:

1. **Consent and least privilege**: Expose only required data and obtain explicit approval before tool execution or data sharing.
2. **Untrusted metadata**: Do not use tool descriptions, annotations, client info, server info, or model-produced arguments as authorization evidence.
3. **Input and output validation**: Validate schemas, arguments, structured results, URIs, and content types at trust boundaries.
4. **Secret handling**: Load credentials from environment/secret manager; never place real keys in configuration, logs, traces, prompts, or error payloads.
5. **Execution isolation**: Sandbox subprocesses and filesystem access; use explicit path grants.
6. **Auditability**: Record security-relevant decisions, approvals, tool identity, and result status without storing sensitive payloads unnecessarily.

---

### Phase 3: Review and Test

#### 3.1 Code Quality and Security Review

Review for:

- DRY principle, consistent error handling, full type coverage.
- Deprecated features: The 2026-07-28 spec deprecates legacy roots, sampling, and logging shapes. Ensure compatibility window for older clients but design for the modern spec.
- Check that JINC Governance rules for authorization are strictly enforced.

#### 3.2 Build and Test

**TypeScript:**

- Run `npm run build`
- Test with MCP Inspector: `npx @modelcontextprotocol/inspector`

**Python:**

- Verify syntax: `python -m py_compile your_server.py`
- Test with MCP Inspector

**Testing Matrix:**
Ensure your implementation passes these test scenarios:

- **Contract**: Invalid JSON-RPC, missing metadata, unsupported version/capability.
- **Statelessness**: Interleaved requests, reconnects, process reuse.
- **Schema security**: External `$ref`, recursive/composed schemas limits.
- **Authorization**: Denied access, approval gates, credential isolation.
- **Failure handling**: Timeouts, cancellation, structured errors, no secret leakage.

---

### Phase 4: Create Evaluations

After implementing your MCP server, create comprehensive evaluations to test its effectiveness.

**Load [✅ Evaluation Guide](./reference/evaluation.md) for complete evaluation guidelines.**

#### 4.1 Understand Evaluation Purpose

Use evaluations to test whether LLMs can effectively use your MCP server to answer realistic, complex questions.

#### 4.2 Create 10 Evaluation Questions

1. **Tool Inspection**: List available tools and understand their capabilities
2. **Content Exploration**: Use READ-ONLY operations to explore available data
3. **Question Generation**: Create 10 complex, realistic questions
4. **Answer Verification**: Solve each question yourself to verify answers

#### 4.3 Evaluation Requirements

Ensure each question is: Independent, Read-only, Complex, Realistic, Verifiable, and Stable.

#### 4.4 Output Format

Create an XML file with this structure:

```xml
<evaluation>
  <qa_pair>
    <question>Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?</question>
    <answer>3</answer>
  </qa_pair>
<!-- More qa_pairs... -->
</evaluation>
```

---

# Reference Files

## 📚 Documentation Library

Load these resources as needed during development:

### Core MCP Documentation (Load First)

- **MCP Protocol**: Start with sitemap at `https://modelcontextprotocol.io/sitemap.xml`
- [📋 MCP Best Practices](./reference/mcp_best_practices.md) - Universal MCP guidelines including naming conventions, response formats, transport selection, and security.

### SDK Documentation (Load During Phase 1/2)

- **Python SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

### Language-Specific Implementation Guides (Load During Phase 2)

- [🐍 Python Implementation Guide](./reference/python_mcp_server.md)
- [⚡ TypeScript Implementation Guide](./reference/node_mcp_server.md)

### Evaluation Guide (Load During Phase 4)

- [✅ Evaluation Guide](./reference/evaluation.md)

## When to Use

This skill is applicable to execute the workflow or actions described in the overview, and when building or reviewing MCP servers or clients, designing MCP tools/resources/prompts, migrating protocol versions, or validating MCP security and interoperability.

## Limitations

- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
