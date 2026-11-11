---
title: read_diagram
parent: Tool reference
nav_order: 4
permalink: /tools/read-diagram/
---
# read_diagram

Read diagram **content**, not visual defects. Source reads require the intended
drawing to be retained through `manage_document` `open` or `create`.
Reading never opens or reopens a drawing or starts Visio, even for package-first
reads. Issued-artifact retrieval doesn't require an open drawing or Visio.
Reads don't save the drawing.

## Source-read arguments

| Argument | Type/default | Meaning |
| --- | --- | --- |
| `diagramId` | Nonblank string | Retained live drawing, including unsaved edits; takes precedence over `filePath` |
| `filePath` | Nonblank string | Absolute path selecting an already-retained saved drawing when no retained ID is supplied; doesn't open it |
| `target` | Required object | One target variant below |
| `scope` | String: `topLevel` | `semantic` keeps data-bearing master instances atomic; `allDepth` includes reachable subshapes |
| `includeFormatting` | Boolean: `false` | Full shape formatting |
| `includeGeometry` | Boolean: `false` | Shape/connector geometry and transforms |
| `includeHyperlinks` | Boolean: `false` | Hyperlink evidence |
| `includeLayers` | Boolean: `false` | Page layer definitions and memberships |
| `outputPath` | Optional string | Exact `.json` filename, not a directory; requests an artifact destination |

Before reading an existing file, open it with
[manage_document](MANAGE_DOCUMENT.md) `action="open"` and reuse its returned
`diagramId`. Use `action="create"` only when a new drawing is intended, not
to recover an existing-document task. `filePath` is an alternative selector
for an already-retained saved drawing, not an open request.

At least one document selector is required. Omit unused arguments rather
than sending null read selectors/flags. Presentation/spatial opt-ins may
require live reads. Clean saved package formats can use package-first reading;
dirty/never-saved drawings use live state. Don't save only to optimize reads.

## Targets

| `target` | Required fields | Behavior |
| --- | --- | --- |
| `{"kind":"document"}` | `kind` | All pages |
| `{"kind":"pages","pages":["1","Architecture"]}` | `kind`, nonempty `pages` | Each requested page once, in document order; `"all"` isn't a selector |
| `{"kind":"shape","page":"1","shapeId":"<shapeId>"}` | `kind`, `page`, `shapeId` | Exact returned shape ID; optional `relation` defaults `both` |
| `{"kind":"selection"}` | `kind` | User-directed current selection on the active page; `relation` defaults `selected` |

For shape/selection targets, `relation` can be `selected`, `contained`,
`overlapping`, or `both`. Containment expands native/group descendants;
spatial overlap is association evidence, **not a visual-defect finding**.
Only returned `containerMemberships` establishes native container membership;
group ancestry is separate. Don't autonomously use the user's selection.

## Examples

```json
{"diagramId": "<diagramId>", "target": {"kind": "document"}, "scope": "semantic"}
```

```json
{"diagramId": "<diagramId>", "target": {"kind": "shape", "page": "1", "shapeId": "<shapeId>", "relation": "contained"}, "scope": "allDepth", "includeHyperlinks": true}
```

## Large results and artifacts

Consume initial `output.chunks`. While `output.nextChunkOffset` is present,
call this tool with **only** the exact issued artifact path and returned offset:

```json
{"artifactPath": "<returned artifactPath>", "chunkOffset": 4}
```

The `4` is illustrative: use the returned offset, not a guessed byte/shape
offset. Each batch contains up to four UTF-8 chunks, each at most 8,000 bytes.
Concatenate chunks verbatim before parsing; stop when no next offset remains.
Don't restart at zero unless intentionally retrying the initial batch.

Only the latest 64 issued artifact paths are retained for this server session.
Unknown, evicted, deleted, or byte/hash-modified artifacts fail; reread the
document rather than mixing snapshots. This isn't an arbitrary-file reader.
Retrieval neither rereads Visio nor saves it and remains available after
the drawing or application closes, while the issued artifact remains valid
in the same server session.

## Partial evidence and text counts

Missing overlap bounds don't fail the entire read. Available selected,
contained, and proven overlap matches are returned with `complete:false`
and warnings. `availability` identifies affected `pageId`, `shapeId`, and
`field` (`bounds` or `overlap`) with `status:"NA"`. Unknown overlap candidates
aren't proven nonmatches, so don't treat the result as exhaustive.
This evidence survives detail materialization and artifact/chunk retrieval.

Partial/unavailable features expose `features.<name>.missingValues:"NA"`.
Available values remain intact; missing typed values remain null, not the
string `"NA"`. Invalid selectors, duplicate logical IDs, and detected
document changes still produce errors.

Deterministic output includes `output.breakdown.text`; JSON graph output
also embeds `textCounts`:

| Count | Meaning |
| --- | --- |
| `rawTextShapes` | Non-whitespace raw text records, including inherited master text and field placeholders |
| `resolvedTextShapes` | Nonempty resolved display text or literal text without fields; empty evaluated fields don't count |
| `fieldTextShapes` | Shapes with text-field evidence or field placeholders |
| `unresolvedFieldShapes` | Field-bearing shapes without complete field resolution |

`labels`/`labelCount` use raw text records, not visible-label counts or counts
of shapes with their own instance XML text. When unresolved fields remain,
the resolved count is a lower bound. Counts don't infer whether text was
instance-authored or inherited. Preserve raw text evidence and update backing
Shape Data rather than replacing field-bearing labels.

## Coverage and restrictions

Check completeness, scope coverage, and warnings before inferring absence.
Retrieving every chunk doesn't prove the original scope included every shape.
The public tool has no `options`, `projection`, `outputFormat`, shape `offset`/
`limit`, `unbounded`, `textContains`, `master`, `useSelection`, or `includeShapeData` argument.
Don't send legacy internal-model fields.

**Related:** [Update](UPDATE_DIAGRAM.md) | [Visual validation](VALIDATE_DIAGRAM.md) |
[Tool overview](../TOOLS.md).
