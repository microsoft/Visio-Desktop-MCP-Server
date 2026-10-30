---
title: create_diagram
parent: Tool reference
nav_order: 3
permalink: /tools/create-diagram/
---
# create_diagram

Add native shapes, connectors, memberships, layers, data, and formatting to
**one existing page** of a retained document. It doesn't create the drawing
or page, save edits, or export. Use [manage_document](MANAGE_DOCUMENT.md) for those.

## Arguments

| Argument | Type | Required | Meaning |
| --- | --- | --- | --- |
| `visualModelJson` | JSON-encoded string | Yes | Complete Visual Model object; don't flatten its nested fields |
| `diagramId` | Nonblank string | Yes | Actual retained ID from document create/open |
| `page` | Nonblank string | Yes | Existing page name/NameU or 1-based index string |
| `options` | Object | No | Page-authoring settings below |

## Options

| Field | Default | Behavior |
| --- | --- | --- |
| `diagramKind` | Omitted | `swimlane` enables cross-functional authoring behavior; doesn't choose a document template |
| `autoOpenStencils` | `true` | Try discovered exact-source recovery for unknown masters; explicit bindings are preferred |
| `autoLayout` | Omitted/off | `off`, `auto`, `hierarchy`, `flowchart`, `tree`, `network`, `compact` |
| `finish` | `true` | Cosmetic finishing can enlarge small labels and fit content; use `false` to preserve authored presentation |
| `validate` | `false` | Post-authoring quality check on the selected page |
| `validationDetail` | `summary` | `full` also returns findings and implies validation; `all` is an alias for full |
| `returnFields` | Omitted | String array selecting heavy `actions`, `shapeIdMap`, `ok_ids`, or `all` fields |

Boolean fields require booleans. Layout/detail/kind fields are strings.
Use canonical layout values: layout overrides supplied coordinates and
reroutes connectors. Leave it off for deliberately positioned containers/
swimlanes. A no-coordinates fallback can still place multiple unpositioned nodes.

### Layout aliases

The parser trims surrounding whitespace and ignores case:

| Canonical value | Other accepted strings |
| --- | --- |
| `off` | `none`, `false`, `no`; omitted/blank also means off |
| `auto` | `on`, `true`, `yes`, `default` |
| `hierarchy` | `orgchart`, `org`, `org-chart`, `organization` |
| `flowchart` | `flow`, `process` |
| `tree` | No aliases |
| `network` | `radial`, `circular` |
| `compact` | `compacttree`, `compact-tree` |

These are string aliases, not JSON booleans. An unrecognized nonblank
string falls back to `auto`; it doesn't disable layout or return a
validation error. Prefer canonical strings to avoid accidental layout.

## Example

First use [content_search](CONTENT_SEARCH.md) to choose a real master; replace
`<masterId>` and `<diagramId>`. This example authors a two-node connected
drawing without layout or cosmetic overrides:

```json
{
  "diagramId": "<diagramId>",
  "page": "1",
  "visualModelJson": "{\"SchemaVersion\":\"1.0\",\"Shapes\":[{\"ID\":\"step-a\",\"NameU\":\"<masterId>\",\"Text\":\"Start\",\"PinX\":2,\"PinY\":3,\"Width\":1.5,\"Height\":0.75},{\"ID\":\"step-b\",\"NameU\":\"<masterId>\",\"Text\":\"Review\",\"PinX\":5,\"PinY\":3,\"Width\":1.5,\"Height\":0.75}],\"Relationships\":{\"Connects\":[{\"source\":\"step-a\",\"target\":\"step-b\",\"Text\":\"Next\"}]}}",
  "options": {"autoLayout": "off", "finish": false, "validate": true}
}
```

Connector `ID` can be omitted on create; it is generated deterministically.
New node/connector IDs must not collide with existing document IDs.

## Structure and completion

Use the [payload reference](VISUAL_MODEL.md) for exact shape/data/style fields.
Use real `Relationships.Connects`, not proximity, for connections.
Use a native container master and `Relationships.Contains` for actual membership.
Native list slots use zero-based `position`.

For swimlanes, supply lane/member geometry in the initial create, size lanes
to their content, and use `diagramKind="swimlane"`. Don't simulate membership
with rectangles or use auto-layout to pull members out of their lanes.

`Metadata.Title` isn't a visible title: create visible title content separately.
Don't send request-level stencil lists, page-size/target-page overrides,
document themes, exports, or automatic-save options.

Inspect returned warnings/failures and requested heavy fields, read back to
reconcile with the source, then explicitly save. A transport success alone
isn't proof that every requested operation succeeded.

**Related:** [Read](READ_DIAGRAM.md) | [Update](UPDATE_DIAGRAM.md) |
[Schema](GET_VISUAL_MODEL_SCHEMA.md).
