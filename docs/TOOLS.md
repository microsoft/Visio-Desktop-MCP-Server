---
title: Tool reference
nav_order: 6
permalink: /tools/
has_toc: false
---
# Tool reference

Each tool has its own parameter, default, example, result, and restriction
reference below. Examples show **tool arguments**, not terminal commands.
Replace angle-bracket placeholders with actual returned IDs, paths, or bindings.

| Tool | Purpose | Needs Visio open? |
| --- | --- | --- |
| [manage_visio](tools/MANAGE_VISIO.md) | Open/close the managed application; refresh the content index | `open` launches it; refresh doesn't |
| [manage_document](tools/MANAGE_DOCUMENT.md) | Drawings, pages, themes, explicit saves, exports | Yes |
| [create_diagram](tools/CREATE_DIAGRAM.md) | Add content to one existing page | Yes |
| [read_diagram](tools/READ_DIAGRAM.md) | Read content or retrieve issued JSON artifacts | Source reads: yes; artifacts: no |
| [update_diagram](tools/UPDATE_DIAGRAM.md) | Apply ordered, focused page edits | Yes |
| [validate_diagram](tools/VALIDATE_DIAGRAM.md) | Check supported visual defects | Yes |
| [get_visual_model_schema](tools/GET_VISUAL_MODEL_SCHEMA.md) | Retrieve the canonical nested authoring schema | No |
| [content_search](tools/CONTENT_SEARCH.md) | Query masters, stencils, and templates | No |

For top-level arguments, use the connected server's `tools/list` schemas.
For nested shapes, relationships, and update operations, use
`get_visual_model_schema` and the [Visual Model payload reference](tools/VISUAL_MODEL.md).
Server-injected C# services, logging, cancellation, progress, and request
context parameters are **not client arguments**.

## Calling sequence and units

Search for real masters, explicitly open Visio, then create/open a drawing.
Reuse its server-issued, session-scoped `diagramId`. Create/update requires
one **existing** page; file paths aren't substitutes for retained IDs there.
Read before editing and save explicitly when intended.

Page selectors are names/NameU values or **1-based index strings** (`"1"`).
Page/list order positions are **zero-based integers**. Geometry uses inches,
rotation radians, and font size/line weight points.

## Errors and completion

Tool errors use MCP `isError` with JSON text containing `error.code`,
`message`, and optional `subCode`, `path`, or `details`.
Create/update can also deliver operation failures and warnings in a successful
transport response. Inspect them before claiming completion or retrying.
Correct bad input rather than replaying it unchanged.

## Read results

Large reads can return issued artifacts instead of a complete inline payload.
Follow the [read chunk protocol](tools/READ_DIAGRAM.md#large-results-and-artifacts);
source completeness and retrieval completion are different.

**Related:** [Work with diagrams](WORK_WITH_DIAGRAMS.md) |
[Configuration](CONFIGURATION.md) | [Troubleshooting](TROUBLESHOOTING.md).
