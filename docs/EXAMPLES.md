---
title: Examples and best practices
nav_order: 9
permalink: /examples/
---
# Examples and best practices

For a complete beginner exercise, use [Your first diagram](FIRST_DIAGRAM.md).
For lifecycle and save rules, see [Work with diagrams](WORK_WITH_DIAGRAMS.md).

## Supply a verifiable source

Separate components from relationships so the agent can check exact counts:

| ID | Component | Type | Owner |
| --- | --- | --- | --- |
| APP-01 | Customer Portal | Application | Digital Commerce |
| SVC-01 | Order Service | Service | Order Platform |
| DATA-01 | Orders Database | Data store | Data Platform |

| From | To | Label |
| --- | --- | --- |
| APP-01 | SVC-01 | Submit order |
| SVC-01 | DATA-01 | Read and write orders |

> Use these tables as the complete source. Open Visio and create one application
> context diagram with three components and two directed, labeled connections.
> Store the supplied IDs and owners as Shape Data. Propose real masters before
> drawing and reuse the approved mapping. Don't invent missing information.
> Read back and compare all components, connections, labels, and metadata.
> Save as a new app-context.vsdx and report the path and any differences.

For organizational mappings, use [Custom shapes](CUSTOM_SHAPES.md) rather than
guessing stencil or master names.

## Make requests precise

| Instead of | Try |
| --- | --- |
| Improve this diagram. | Insert Fraud Review between Order Service and Payment Provider; preserve everything unrelated. |
| Fix the appearance. | Widen Order Service enough to fit its label; preserve its position and attached connectors. |
| Put these applications in a box. | Use a native Platform container and make App A, App B, and App C actual members. |

Include the **source, target file/page, scope, structure, shape policy, save
policy, and acceptance checks**. State whether to save over the original,
save a new copy, or leave changes unsaved.

## Break up large work

Understand the source, review the plan and masters, author, read back and
compare, then make focused refinements. Ask for
[visual validation](VALIDATE_AND_EXPORT.md) after authoring, not as a substitute
for source reconciliation.

Before sharing, inspect labels, identifiers, connector direction/endpoints,
native memberships, Shape Data, text fit, and preserved content in Visio.
Keep external systems outside internal boundaries and test any smart-shape
behavior your workflow depends on. Save the approved result.
Check the result of a failed operation before retrying; part of the task may
already have succeeded. Avoid simultaneous agent and manual edits.

Put stable, recurring standards in a [custom agent](CUSTOM_AGENTS.md).
Keep each individual prompt about the current task.
