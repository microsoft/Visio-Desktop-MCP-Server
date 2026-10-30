---
title: Custom agents
nav_order: 8
permalink: /custom-agents/
---
# Reuse instructions with a custom agent

A custom agent combines reusable instructions and tool selection. Use one
for recurring diagram types or team standards; use an ordinary prompt for a
one-off task. Complete [setup](SETUP.md) and
[approve your shape mappings](CUSTOM_SHAPES.md) first.

## Create an agent in VS Code

Create a workspace agent at
`.github\agents\visio-architecture.agent.md`.

Use this starter, replacing the illustrative stencil and master names with
your actual approved content:

```markdown
---
name: Visio Architecture
description: Creates and revises architecture drawings using approved masters.
tools: ['read', 'search', 'visio-local/*']
---

Represent only the user's agreed source. Preserve identifiers, labels,
relationships, and Shape Data. Report missing information rather than inventing it.

Before authoring:
- Open Visio explicitly, then create/open the target drawing and select its page.
- Search for approved masters and keep each masterId paired with its source path.
- Use ApprovedArchitecture.vssx: Application for applications, Service for services.
- Reuse the same binding for equivalent types. Stop if an approved master is missing.

For existing drawings:
- Read first and use returned stable shape IDs.
- Make only the requested changes on the chosen page; preserve unrelated content.
- Use attached directed connectors and native containers with actual members.

Before finishing:
- Read back and compare content, connections, membership, and metadata with the source.
- Validate supported visual defects; if repairs are requested, repair and check again.
- Save only as instructed. Treat exports as separate artifacts, not source saves.
- Report changes, unresolved issues, and the full path after a successful save.

Stop for missing source data, conflicting requirements, or repeated failures.
```

`visio-local/*` selects the tools from the server with that configured name.
Change it if your server ID differs. `read` and `search` are client tool sets,
not Visio server tools. Confirm availability in the chosen session.

## Try and maintain it

Select the custom agent and give it a task-specific source and destination:

> Use inventory.csv to create an architecture drawing with the approved shape
> mappings. Save as a new inventory-architecture.vsdx without replacing another
> file. Report missing information and unresolved findings.

Test both creation and a focused edit. Review the result in Visio, and maintain
instructions alongside your team's standards.

Custom agents don't install stencils, add server capabilities, grant filesystem
access, or bypass approvals. For current client controls and other scopes, see
[VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents).

**Related:** [Examples and best practices](EXAMPLES.md) | [Tool reference](TOOLS.md).
