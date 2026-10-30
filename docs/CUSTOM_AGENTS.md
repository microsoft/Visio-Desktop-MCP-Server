---
title: Custom agents
nav_order: 8
permalink: /custom-agents/
has_toc: false
---
# Reuse standards with a custom agent

Visio Desktop MCP Server provides the tools. A custom agent defines how to use
them: approved shapes, source data, workflow, verification, and when to stop.
Complete [setup](SETUP.md) and [approve your shape mappings](CUSTOM_SHAPES.md)
first, then use the [sample agent](custom_agents/SAMPLE_AGENT.md).

## Why use one

- **Consistency:** the same masters, connectors, containers, and checks apply
  to every request.
- **Shorter prompts:** state stable standards once; prompts carry only the
  task-specific source, destination, and intent.
- **Safer edits:** the agent reads before it changes, preserves unrelated
  content, and stops instead of guessing.
- **Focused tools:** a `tools` list limits the agent to what the task needs.
- **Shareable:** a workspace agent file is versioned and reviewed with your
  team's other standards.

Use a custom agent for recurring diagrams, organization-specific stencils,
consistent metadata, multi-stage workflows, or careful updates to existing
drawings. For one-off tasks or exploration, start with an ordinary prompt.

## Parts of an agent

| Part | What to define | Where it lives |
| :--- | :--- | :--- |
| Identity | Name and a description of when to select the agent | `name` and `description` front matter |
| Instructions | Role, goals, behavior rules, and constraints | Markdown body |
| Tools | Server tools and client tool sets the agent may use | `tools` front matter |
| Knowledge | Authoritative source data, approved stencils, naming conventions, and required Shape Data | Body; reference files in your workspace |
| Model | An optional preferred model | `model` front matter; other settings come from the client |
| Workflow | Steps such as understand, inspect, resolve masters, author, read back, verify, and report | Body |
| Inputs and output | Expected source, destination, and the response format | Body |
| Security | Permitted tools and file locations | `tools` front matter; client approvals still apply |
| Error handling | Retry limits, stopping conditions, and when to ask a person | Body |

Keep task-specific intent in the prompt and stable standards in the agent.
Persist standards in the file, not in conversation history: drawing IDs and
chat context belong to one session.

## Build one

1. Choose one recurring diagram type and its authoritative source.
2. List the component types and resolve an approved master for each one.
3. Create an `.agent.md` file with `name`, `description`, and `tools` front
   matter. See [where to save it](custom_agents/SAMPLE_AGENT.md#save-the-file).
4. In the body, write the role, source rules, shape mappings, workflow,
   stopping conditions, and response format.
5. Select the agent and test both creation and a focused edit. Review the
   results in Visio.
6. Update the file as your standards evolve.

A custom agent makes results more consistent; it doesn't guarantee identical
or correct output. It doesn't install stencils, add server capabilities, grant
filesystem access, or bypass approvals. For client controls and all
supported fields, see
[VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents).

**Related:** [Sample agent](custom_agents/SAMPLE_AGENT.md) |
[Examples and best practices](EXAMPLES.md) | [Tool reference](TOOLS.md).
