---
title: update_diagram
parent: Tool reference
nav_order: 5
permalink: /tools/update-diagram/
---
# update_diagram

Apply a nonempty, ordered edit batch to one existing page. Read first and use
[returned stable shape/connector IDs](READ_DIAGRAM.md#stable-shape-ids). Never substitute labels, guesses,
`visioShapeId`, or page-local strings such as `1:48`.

## Arguments and options

| Argument | Type | Required |
| --- | --- | --- |
| `diagramId` | Retained document ID string; not a file path | Yes |
| `page` | Existing page name/NameU or 1-based index string | Yes |
| `operations` | JSON-encoded **array string**, not an array argument | Yes |
| `options` | Object | No |

Schema discovery includes `toolInputs.update_diagram` with the complete outer
contract and encoded-call examples. Unknown top-level arguments reject;
unknown option and nested payload properties are ignored. They can't
bypass page/lifecycle/theme prohibitions or turn an empty patch into a
change. See [input validation](GET_VISUAL_MODEL_SCHEMA.md#input-validation).

| Option | Default | Meaning |
| --- | --- | --- |
| `atomic` | `false` | Abort on failure and attempt batch rollback; inspect errors/state |
| `autoOpenStencils` | `true` | Master-resolution assistance for additions |
| `validate` | `false` | Validate affected successful-operation shapes on this page |
| `returnFields` | Omitted | String array selecting `actions`, `ok_ids`, or `all` |

Updates remain unsaved even with validation. Use
[manage_document](MANAGE_DOCUMENT.md) for page management, saving, and export.
Don't put page overrides inside operations.

## All 17 operations

Every object needs `op`; other required fields are below.

| `op` | Required fields | Optional fields / effect |
| --- | --- | --- |
| `addNode` | `shape` with `ID`, `NameU` | `styleFrom`: same-page peer's unset size/style; explicit shape values win |
| `addCallout` | `shape`, `target` | `preferredSide`, `clearance`; genuine native callout master only |
| `updateNode` | `id`, `patch` | Change supported non-null shape fields in place |
| `deleteNode` | `id` | `cascadeEdges` defaults `true` |
| `addEdge` | `connection` with new `ID`, `source`, `target` | Glued directed connection |
| `updateEdge` | `id`, `patch` | Endpoints, label, style, data, hyperlinks |
| `deleteEdge` | `id` | Delete connector |
| `addToContainer` | `container`, `member` | Actual native membership |
| `removeFromContainer` | `container`, `member` | Remove membership, not the shape |
| `reorderContainerMember` | `container`, `member`, `position` | Nonnegative zero-based native-list position |
| `replaceContainerMembers` | `container`, `members` | Complete ordered unique ID array; failure restores original order |
| `fitContainer` | `container` | `padding`, `heading`; non-list native containers only |
| `createLayer` | `layer` | `visible`, `print`, `locked`, `color` |
| `updateLayer` | `layer` | At least one non-null `newName`, `visible`, `print`, `locked`, `color` |
| `deleteLayer` | `layer` | Preserve shapes |
| `addToLayer` | `layer`, `member` | Add shape/connector membership |
| `removeFromLayer` | `layer`, `member` | Remove shape/connector membership |

Callout `preferredSide`: `auto`, `left`, `right`, `above`, `below`.
`clearance`: 0-2 inches, default 0.2.
Container `padding`: 0-2 inches, default 0.25.
`heading` requires a master with a visible heading, including visible text on
native group children in page coordinates. Hidden or transparent text doesn't
satisfy verification; otherwise omit `heading` and set `Text`.
Layer fields and all supported patches are in the [payload reference](VISUAL_MODEL.md).

To clear a connector label, use an `updateEdge` patch with `"Text":""`.
Omitted/null text leaves the label unchanged. Every edge patch needs at
least one non-null change; empty/all-null patches reject. Null fields may
accompany another non-null change. For example, JSON-encode this operation
array into `operations`:

```json
[{"op":"updateEdge","id":"<connectorId>","patch":{"Text":""}}]
```

## Example: targeted label and data edit

Replace placeholders with values from a current [read](READ_DIAGRAM.md):

```json
{
  "diagramId": "<diagramId>",
  "page": "1",
  "operations": "[{\"op\":\"updateNode\",\"id\":\"<shapeId>\",\"patch\":{\"Text\":\"Order Service\",\"ShapeData\":[{\"name\":\"Owner\",\"value\":\"Order Platform\"}]}}]",
  "options": {"atomic": true, "validate": true, "returnFields": ["actions", "ok_ids"]}
}
```

## Ordering and preservation

A new ID can be referenced only after an earlier operation creates it.
`addEdge` requires an ID distinct from existing shapes/connectors; use
`updateEdge` for an existing connector, or delete it before recreating it.

For native-list additions, put `addToContainer` immediately after `addNode`,
then an exact-slot `reorderContainerMember` if needed for an eligible ordered
list item. Ordinary contained shapes don't acquire an ordered slot merely
by joining a native list container. Moving a native CFF Swimlane List or
Phase List uses a native container move to translate nested members while
retaining membership and order. Direct lane/phase geometry edits remain
guarded and can return warnings. Don't use `fitContainer` to size
swimlane/phase lists.

Use `addCallout`, not a node plus a separate connector, for an intrinsic callout
leader. Discover `kind="callout"` and identify the exact target; nearby intent
isn't inferred. A native container is likewise not a decorative rectangle.

Without atomic mode, successful edits may remain after a failure. Inspect
`ok`, summaries, failures, warnings, and rollback outcomes before retrying.
Don't promise a successful save or perfect rollback from transport success.

## Results

See the shared [authoring result fields](../TOOLS.md#authoring-results) for `ok`, outcome counts, failures, structured warnings, and free-text notes. Request `actions` and/or `ok_ids` through `options.returnFields` when those details are needed; they are omitted by default.

Use a failure's zero-based `operationIndex`, when present, to locate the affected input operation. Inspect the verdict and actual drawing state even if successful IDs are returned: they don't guarantee that the rest of the batch succeeded or that changes survived a rollback. A successful update still leaves edits unsaved.

**Related:** [Save explicitly](MANAGE_DOCUMENT.md) | [Create](CREATE_DIAGRAM.md) |
[Schema](GET_VISUAL_MODEL_SCHEMA.md).
