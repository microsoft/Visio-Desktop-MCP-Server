---
title: get_visual_model_schema
parent: Tool reference
nav_order: 7
permalink: /tools/get-visual-model-schema/
---
# get_visual_model_schema

Return the canonical JSON Schema for the nested Visual Model, ordered
update-operation array, and outer create/update arguments.
No Visio connection or document is needed.

## Arguments and example

There are **no client arguments or options**:

```json
{}
```

## What it returns

The schema has the Visual Model at its root, an `updateOperations` array
contract, and `$defs` for:

- Shapes, shape patches, connectors, connector patches, and native containment.
- Layers and all supported update operations.
- Formatting, Shape Data, hyperlinks, geometry, and metadata.

The root requires `SchemaVersion`, `Shapes`, and `Relationships`.
`SchemaVersion` is exactly `"1.0"`. Shape identity requires `ID` and `NameU`.
The [payload reference](VISUAL_MODEL.md) explains writable fields versus
read-side observations and units.

`toolInputs.create_diagram` and `toolInputs.update_diagram` contain complete
outer argument and option schemas, plus full-call `examples` with the nested
payloads already encoded as strings. These supplement the nested contracts;
they don't replace them.

## Input validation

Create/update reject unknown top-level arguments. Unknown properties inside
their `options`, Visual Model objects, and operation objects are ignored;
they don't become authored changes. Use canonical fields rather than relying
on ignored properties, and read back to verify the result.
Freeform extension maps remain passthrough data.

Explicit document/page management, lifecycle, export, and document-wide theme
overrides remain prohibited in authoring payloads/options. Unsupported
operation names still reject; a patch with only ignored fields is empty and
rejects. Each `updateEdge.patch` needs at least one non-null change, although
null fields may accompany a real change.

Invalid enum values identify the property, rejected value, and allowed
values. Type errors identify the property path and expected/actual JSON
types. This tolerance applies only to create/update; `read_diagram` retains
its strict argument contract and has no `options` object.

## Use it correctly

For [create_diagram](CREATE_DIAGRAM.md), construct a conforming object and
JSON-encode it into `visualModelJson`. For [update_diagram](UPDATE_DIAGRAM.md),
construct a nonempty conforming operation array and JSON-encode it into
`operations`. Both tool arguments are strings; nested JSON isn't flattened
into top-level tool parameters.

Use the connected server's `tools/list` schemas for lifecycle/read/search
arguments. This tool isn't a replacement for those schemas and doesn't
return a drawing or a list of installed masters. Discover actual master
bindings with [content_search](CONTENT_SEARCH.md).

Schema fields used for read round trips aren't necessarily writable native
properties. For example, `VisioShapeId` is an observation, not an update ID,
and `ParentId` isn't a create-time native-membership instruction.

**Related:** [Tool overview](../TOOLS.md) | [Visual Model payloads](VISUAL_MODEL.md).
