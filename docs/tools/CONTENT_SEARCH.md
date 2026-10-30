---
title: content_search
parent: Tool reference
nav_order: 8
permalink: /tools/content-search/
---
# content_search

Discover indexed masters, stencil files, and templates without opening Visio.
Search is read-only/query-only: it doesn't copy/import files or request an
index refresh. For changed content, use [update_index](MANAGE_VISIO.md).

## Arguments

| Argument | Type/default | Behavior |
| --- | --- | --- |
| `keyword` | String; empty | Case-insensitive query; ranked search supports prefix `serv*` and fuzzy `router~` |
| `type` | String: `shape` | `shape`, `stencil`, `template`, or `any` |
| `stencil` | Optional string | Scope shapes to one indexed file's name, base name, display name, or full path; not a drawing |
| `count` | Integer: `10` | Ranked limit clamped to 0-100; enumeration page size to 1-100 |
| `offset` | Integer: `0` | Nonnegative enumeration offset; ignored for ranked search |
| `synonyms` | Optional string | Caller-supplied comma/semicolon-separated alternate terms; merged by best per-master score |

There is no `options` object. Search is lexical/metadata-based, not embeddings:
arbitrary semantic synonyms aren't inferred.

## Search versus enumeration

| Request | Behavior |
| --- | --- |
| Shape keyword without a source scope | Ranked search; inspect relevance, not just rank |
| Empty keyword plus `stencil` | Enumerate that source's masters |
| Nonempty keyword plus `stencil` | Filter that source's master names/aliases; not broad ranked search |
| Empty keyword with `type="stencil"`/`"template"` | Enumerate indexed files |
| `type="any"` without source scope | Can return files and masters |

Scoped filtering uses name substrings/alias matches; trailing search markers
are stripped, not ranked prefix/fuzzy operators. `synonyms` doesn't broaden
scoped enumeration/filtering. Follow returned `nextOffset` for enumeration.

## Examples

```json
{"keyword": "application server", "type": "shape", "count": 10, "synonyms": "web server;application"}
```

```json
{"keyword": "", "type": "stencil", "count": 25, "offset": 0}
```

Use an actual indexed source returned by search, not this placeholder:

```json
{"keyword": "", "type": "shape", "stencil": "<returned source path>", "count": 25, "offset": 0}
```

## Results and master bindings

Master results include `master`, `nameU`, `masterId`, `stencil`, `path`, and
available `kind`, `isContainer`, connection/text evidence,
`score`, `rawLex`, `confidence`, `matchReason`, and `suitability`.
File results include name, display name, path, kind, and master count.

Copy **`masterId` unchanged into shape `NameU`**. If supplying `StencilPath`,
copy `path` from that same result. Preserve the pair, including full-path/
escaped IDs; don't decode/reconstruct one or select a source by filename alone.
Reuse the binding for equivalent shape types.

`score` is normalized: rank one isn't proof of suitability. Inspect absolute
relevance (`rawLex`, `confidence`), advisories, kind, and intended use.
Native callout operations require a genuine `kind="callout"` master.

Exact-name queries can include an `exact` block with all source candidates;
inspect `candidateCount`/`candidatesTruncated`. Ranked results alone aren't a
complete source inventory. Enumeration reports `totalCount`, `hasMore`,
`truncated`, and `nextOffset` where applicable.

Missing/unreadable/locked or unsupported source paths are excluded before
ranking/counts. Unindexed external files aren't imported; use
[known discovery locations](../CUSTOM_SHAPES.md). Legacy file entries may
have no extracted masters. Search doesn't restore unavailable files.
UNC/device paths aren't usable search sources. A stale local full path can
recover only a unique indexed filename; use the resolved full source binding
when identity matters.

**Related:** [Create](CREATE_DIAGRAM.md) | [Discovery settings](../configuration/RUNTIME.md).
