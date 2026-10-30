---
title: manage_document
parent: Tool reference
nav_order: 2
permalink: /tools/manage-document/
---
# manage_document

Manage writable documents, pages, themes, explicit saves, and exports.
First [open Visio](MANAGE_VISIO.md). Creation/opening returns a retained
`diagramId`; save preserves that ID.

## Arguments by action

Every call requires string `action`. All actions except `create` and `open`
require string `diagramId`. Supply only the additional fields listed:

| Action | Additional arguments | Allowed `options` fields |
| --- | --- | --- |
| `create` | None; **no outputPath** | `template` |
| `open` | Required `filePath` | None |
| `close` | None | None |
| `save` | Optional `outputPath` | `overwrite` |
| `getActivePage` | None | None |
| `addPage` | Required `pageName` | Page settings below |
| `renamePage` | Required `oldPageName`, `pageName` | None |
| `updatePage` | Required `pages` with exactly one selector | At least one page setting |
| `deletePage` | Required `pages` with exactly one selector | None |
| `clearPage` | Required `pages` with exactly one selector | None |
| `activatePage` | Required `pages` with exactly one selector | None |
| `setTheme` | None | Required `theme`; optional `themeSource` |
| `export` | Required `outputPath`; optional `pages`, `format` | `overwrite`, `intent`, `dpi` |

Paths, names, selectors, formats, and themes are strings; `pages` is a
nonempty string array. `options` is an object. Unknown top-level fields,
cross-action options, and conflicting duplicate options are rejected.

## Option types and defaults

| Option | Type and meaning |
| --- | --- |
| `template` | Drawing-template path; omit for a blank, unsaved drawing |
| `overwrite` | Boolean; save defaults `false` for a different destination, export defaults `true` |
| `widthIn`, `heightIn` | Positive finite numbers, inches |
| `orientation` | `Portrait` or `Landscape`; not export `intent` |
| `background` | Boolean: background/foreground page |
| `assignBackground` | Background-page name/selector |
| `position` | Integer at least zero: destination page order |
| `theme` | Named theme, not a numeric index; applies to all foreground pages |
| `themeSource` | Set to `user` only for an explicitly requested `NoTheme` |
| `intent`, `dpi` | [Export-specific options](../VALIDATE_AND_EXPORT.md#export-a-separate-artifact) |

## Lifecycle examples

These are separate calls. Replace `<diagramId>` with the create/open result:

```json
{"action": "create"}
```

```json
{"action": "open", "filePath": "C:\\Diagrams\\architecture.vsdx"}
```

Open takes a drawing, **not a stencil or template**. Create from a template
using `options.template`; discover source masters using [content_search](CONTENT_SEARCH.md).

```json
{"action": "save", "diagramId": "<diagramId>", "outputPath": "C:\\Diagrams\\review.vsdx", "options": {"overwrite": false}}
```

Omitting the destination saves back to the retained file, or generates a path
for an unsaved drawing. Same-path saves update that file. A different existing
destination requires overwrite; replacing another retained destination rejects.
Use the returned `filePath`, not a guessed destination.

## Page and export examples

```json
{"action": "updatePage", "diagramId": "<diagramId>", "pages": ["1"], "options": {"widthIn": 16, "heightIn": 9, "orientation": "Landscape"}}
```

```json
{"action": "export", "diagramId": "<diagramId>", "pages": ["1"], "outputPath": "C:\\Exports\\architecture.png", "options": {"dpi": 300, "overwrite": false}}
```

```json
{"action": "export", "diagramId": "<diagramId>", "format": "png", "outputPath": "C:\\Exports\\pages", "options": {"overwrite": false}}
```

```json
{"action": "export", "diagramId": "<diagramId>", "outputPath": "C:\\Exports\\review.pdf", "options": {"intent": "screen", "overwrite": false}}
```

See the canonical [format/page-selection rules](../VALIDATE_AND_EXPORT.md#export-a-separate-artifact).

## Side effects

`clearPage` deletes all shapes/connectors but preserves page settings.
`deletePage` deletes the page/content subject to native restrictions.
`getActivePage` returns `pageName` without saving or changing activation.
Page/theme/content changes remain unsaved; exporting doesn't save the source.
`close` **discards unsaved changes**.

**Related:** [Create](CREATE_DIAGRAM.md) | [Update](UPDATE_DIAGRAM.md) |
[Work with diagrams](../WORK_WITH_DIAGRAMS.md).
