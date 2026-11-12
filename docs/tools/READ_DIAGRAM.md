---
title: read_diagram
parent: Tool reference
nav_order: 4
permalink: /tools/read-diagram/
---
# read_diagram

Read diagram **content**, not visual defects. Source reads require the intended
drawing to be retained through `manage_document` `open` or `create`.
Reading never opens or reopens a drawing or starts Visio.
Issued-artifact retrieval doesn't require an open drawing or Visio.
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

If `outputPath` names an existing JSON file, that file is replaced. This tool has no overwrite flag. Use a new `.json` filename to preserve existing files, or omit `outputPath` to let the server choose a destination when an artifact is needed.

Before reading an existing file, open it with
[manage_document](MANAGE_DOCUMENT.md) `action="open"` and reuse its returned
`diagramId`. Use `action="create"` only when a new drawing is intended, not
to recover an existing-document task. `filePath` is an alternative selector
for an already-retained saved drawing, not an open request.

At least one document selector is required. Omit unused arguments rather than sending null read selectors or flags. Reads include unsaved edits; don't save the drawing solely to read it.

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

## Stable shape IDs

Use the exact shape and connector IDs returned by `read_diagram` for follow-up reads and edits. Don't reconstruct IDs or substitute labels, names, or native numeric IDs.

A read limited to selected pages or shapes doesn't establish document-wide ID uniqueness. Ambiguous IDs can return `DUPLICATE_ID`; don't guess which shape they identify.

## Examples

```json
{"diagramId": "<diagramId>", "target": {"kind": "document"}, "scope": "semantic"}
```

```json
{"diagramId": "<diagramId>", "target": {"kind": "shape", "page": "1", "shapeId": "<shapeId>", "relation": "contained"}, "scope": "allDepth", "includeHyperlinks": true}
```

## Large results and artifacts

Consume the source read's initial `output.chunks`. If `output.nextChunkOffset` is present, call this tool with **only** the exact issued artifact path and returned offset:

```json
{"artifactPath": "<returned artifactPath>", "chunkOffset": 4}
```

Artifact-retrieval responses return the batch fields **at the top level**, not inside `output`:

| Field | Initial source-read response | Artifact-retrieval response |
| --- | --- | --- |
| Chunk text | `output.chunks` | `chunks` |
| Next batch offset | `output.nextChunkOffset` | `nextChunkOffset` |
| Issued path | `output.artifactPath` | `artifactPath` |

For example, a retrieval response can contain this excerpt; chunk text is illustrative:

```json
{
  "artifactPath": "<returned artifactPath>",
  "chunkOffset": 4,
  "chunks": ["<fragment 5>", "<fragment 6>", "<fragment 7>", "<fragment 8>"],
  "nextChunkOffset": 8
}
```

Append these `chunks` to the earlier batch, then use the top-level `nextChunkOffset` for the next call. Stop when that field is absent or null.

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

If `availabilityComplete:false` is returned, the full `availability` list isn't inline. Retrieve the exact issued `availabilityArtifactPath` using the [artifact protocol](#large-results-and-artifacts), starting at `chunkOffset:0` unless that artifact already has a returned batch. The path can be the same as `output.artifactPath`; in that case, finish consuming its existing chunks rather than starting a separate retrieval. Missing inline diagnostics don't mean every field was available.

Partial/unavailable features expose `features.<name>.missingValues:"NA"`.
Available values remain intact; missing typed values remain null, not the
string `"NA"`. Invalid selectors, unresolved identity collisions, and detected
document changes still produce errors.

Deterministic output includes `output.breakdown.text`; JSON graph output
also embeds `textCounts`:

| Count | Meaning |
| --- | --- |
| `rawTextShapes` | Non-whitespace raw text records, including inherited master text and field placeholders |
| `resolvedTextShapes` | Nonempty resolved display text or literal text without fields; empty evaluated fields don't count |
| `fieldTextShapes` | Shapes with text-field evidence or field placeholders |
| `unresolvedFieldShapes` | Field-bearing shapes without complete field resolution |

If `output.breakdownComplete:false` is returned, the shape-kind, master-usage, and Shape Data field breakdown maps are omitted from the response. Empty maps then mean omitted detail, not zero occurrences. Fixed totals, including text counts, remain available, and the persisted diagram artifact isn't truncated by this omission.

`labels`/`labelCount` use raw text records, not visible-label counts or counts
of shapes with their own instance XML text. When unresolved fields remain,
the resolved count is a lower bound. Counts don't infer whether text was
instance-authored or inherited. Preserve raw text evidence and update backing
Shape Data rather than replacing field-bearing labels.

## Coverage and restrictions

The initial source-read response's `output` describes the complete result, not just its first chunk batch. Artifact retrieval returns the same coverage fields at the top level:

| Field under `output` | Meaning |
| --- | --- |
| `expectedCounts` | Records expected for the requested output and scope |
| `emittedCounts` | Records emitted across the complete output, not just the current batch |
| `scopeCounts` | Source record counts within the requested scope |
| `excludedCounts` | All-depth source records excluded by that scope |
| `scopeComplete` | Every expected record within the requested scope was emitted |
| `complete` | The output is scope-complete and excludes no all-depth source records |

These counts cover categories such as shapes, connectors, containments, labels, and group ancestries. A `topLevel` read can have `output.scopeComplete:true` and `output.complete:false` because nested records were intentionally excluded. Use `scope:"allDepth"` when nested content is required. Neither coverage flag means you have already retrieved every chunk.

Check completeness, scope coverage, and warnings before inferring absence.
Retrieving every chunk doesn't prove the original scope included every shape.
The public tool has no `options`, `projection`, `outputFormat`, shape `offset`/
`limit`, `unbounded`, `textContains`, `master`, `useSelection`, or `includeShapeData` argument.
Don't send legacy internal-model fields.

**Related:** [Update](UPDATE_DIAGRAM.md) | [Visual validation](VALIDATE_DIAGRAM.md) |
[Tool overview](../TOOLS.md).
