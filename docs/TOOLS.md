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
| [manage_document](tools/MANAGE_DOCUMENT.md) | Drawings, pages, themes, explicit saves, exports | `open` and `create` start it if needed; other actions require a retained drawing |
| [create_diagram](tools/CREATE_DIAGRAM.md) | Add content to one existing page | Yes |
| [read_diagram](tools/READ_DIAGRAM.md) | Read content or retrieve issued JSON artifacts | Source reads: already-retained drawing required; artifacts: no |
| [update_diagram](tools/UPDATE_DIAGRAM.md) | Apply ordered, focused page edits | Yes |
| [validate_diagram](tools/VALIDATE_DIAGRAM.md) | Check supported visual defects | Yes |
| [get_visual_model_schema](tools/GET_VISUAL_MODEL_SCHEMA.md) | Retrieve outer and nested authoring schemas | No |
| [content_search](tools/CONTENT_SEARCH.md) | Query masters, stencils, and templates | No |

For top-level arguments, use the connected server's `tools/list` schemas.
`get_visual_model_schema` also includes outer create/update contracts and
encoded-call examples under `toolInputs`, alongside the nested shape,
relationship, and operation schemas. See the
[schema reference](tools/GET_VISUAL_MODEL_SCHEMA.md) and
[Visual Model payload reference](tools/VISUAL_MODEL.md).
Send only arguments listed in the tool schema.

## Calling sequence and units

For an existing drawing, use `manage_document action="open"` with its intended
file; this starts Visio if needed. For a new drawing, search for real masters, then use `manage_document action="create"`; it also starts Visio if needed.
Reuse the returned server-issued, session-scoped `diagramId`.
Source reads require that retained drawing; `filePath` only selects an
already-retained saved drawing and never opens or reopens it.
Create/update requires one **existing** page; file paths aren't substitutes
for retained IDs there. Read before editing and save explicitly when intended.

Page selectors are names/NameU values or **1-based index strings** (`"1"`).
Page/list order positions are **zero-based integers**. Geometry uses inches,
rotation radians, and font size/line weight points.

## Errors and completion

Tool errors use MCP `isError` with JSON text containing `error.code`,
`message`, and optional `subCode`, `path`, or `details`.
Create/update can also deliver operation failures and warnings in a successful
transport response. Inspect them before claiming completion or retrying.
Correct bad input rather than replaying it unchanged.

Create/update reject unknown top-level arguments but ignore unknown options
and nested payload properties; ignored fields aren't authored changes.
Explicit document/page/lifecycle/theme prohibitions, unsupported operations,
and nonempty-patch guards still apply. Read arguments remain strict.
See [input validation](tools/GET_VISUAL_MODEL_SCHEMA.md#input-validation).

## Read results

Large reads can return issued artifacts instead of a complete inline payload.
Follow the [read chunk protocol](tools/READ_DIAGRAM.md#large-results-and-artifacts);
source completeness and retrieval completion are different.

**Related:** [Work with diagrams](WORK_WITH_DIAGRAMS.md) |
[Configuration](CONFIGURATION.md) | [Troubleshooting](TROUBLESHOOTING.md).
