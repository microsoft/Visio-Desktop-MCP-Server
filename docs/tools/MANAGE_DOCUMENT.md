---
title: manage_document
parent: Tool reference
nav_order: 2
permalink: /tools/manage-document/
---
# manage_document

Manage writable documents, pages, themes, explicit saves, and exports.
Opening an existing drawing starts Visio if needed; creating a new drawing
requires [opening Visio](MANAGE_VISIO.md) first. Other actions don't start
it implicitly. Creation/opening returns a retained `diagramId`; save
preserves that ID.

## Arguments by action

Every call requires string `action`. All actions except `create` and `open`
require string `diagramId`. Supply only the additional fields listed:

| Action | Additional arguments | Allowed `options` fields |
| --- | --- | --- |
| `create` | None; **no outputPath** | `template` |
| `open` | Required `filePath` | None |
| `close` | None | `discardUnsavedChanges` |
| `save` | Optional `outputPath` | `overwrite` |
| `getActivePage` | None | None |
| `addPage` | Required `pageName` | Page settings below |
| `renamePage` | Required `oldPageName`, `pageName` | None |
| `updatePage` | Required `pages` with exactly one selector | At least one page setting |
| `deletePage` | Required `pages` with exactly one selector | None |
| `clearPage` | Required `pages` with exactly one selector | None |
| `activatePage` | Required `pages` with exactly one selector | None |
| `listThemes` | None | None |
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
| `discardUnsavedChanges` | Boolean, default `false`; `close` only. Set to `true` only after user approval to close and discard unsaved changes |
| `widthIn`, `heightIn` | Positive finite numbers, inches |
| `autoSize` | Boolean or null; `addPage` and `updatePage` only. `true` enables native AutoSize; `false` disables it |
| `orientation` | `Portrait` or `Landscape`; not export `intent` |
| `background` | Boolean: background/foreground page |
| `assignBackground` | Background-page name/selector |
| `position` | Integer at least zero: destination page order |
| `theme` | Exact `themes[].name` from `listThemes` for the same drawing, not a numeric index; applies to all foreground pages |
| `themeSource` | Set to `user` only for an explicitly requested `NoTheme` |
| `intent`, `dpi` | [Export-specific options](../VALIDATE_AND_EXPORT.md#export-a-separate-artifact) |

For `addPage` and `updatePage`, omitted/null `autoSize` preserves the page's
AutoSize mode unless `widthIn` or `heightIn` is supplied. Explicit dimensions
disable AutoSize by default; with `autoSize:true`, the dimensions apply first,
then AutoSize is enabled. An orientation-only change preserves AutoSize.

## Lifecycle examples

These are separate calls. Replace `<diagramId>` with the create/open result:

For a new drawing, first call `manage_visio` with `{"action":"open"}`, then:

```json
{"action": "create"}
```

For an existing drawing, this call opens Visio if needed:

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

Enable AutoSize on an existing page:

```json
{"action": "updatePage", "diagramId": "<diagramId>", "pages": ["1"], "options": {"autoSize": true}}
```

Set explicit dimensions, disabling AutoSize by default:

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

## Discover and apply themes

List the native full-theme catalog of the retained drawing:

```json
{"action": "listThemes", "diagramId": "<diagramId>"}
```

The result includes `diagramId` and `themes`, whose entries have `name`,
localized `displayName`, and boolean `requiresUserIntent`. Document-specific
choices come first; the catalog also includes unused host built-ins.
Discovery doesn't create another drawing, modify the drawing, or save it.
External theme files not exposed by Visio's catalog aren't enumerated.

Copy an exact returned `name`, not its display name or a guessed color:

```json
{"action": "setTheme", "diagramId": "<diagramId>", "options": {"theme": "<returned theme name>"}}
```

The server resolves that universal name to the native localized name.
Application affects all foreground pages and remains unsaved. Choose
`NoTheme` only when the user explicitly requests theme removal, and include
`"themeSource":"user"` in `options`; don't infer consent from discovery.

## Side effects

`clearPage` deletes all shapes/connectors but preserves page settings.
`deletePage` deletes the page/content subject to native restrictions.
`getActivePage` returns `pageName` without saving or changing activation.
Page/theme/content changes remain unsaved; exporting doesn't save the source.

`close` closes already-saved documents normally. If the document has unsaved
changes, it does not close or save it. It returns `closed:false`,
`requiresConfirmation:true`, and warnings, not a tool error. Save first to
keep the changes, or set `options.discardUnsavedChanges:true` to explicitly
authorize closing the document and discarding its unsaved changes. Only
supply this option after user approval.

**Related:** [Create](CREATE_DIAGRAM.md) | [Update](UPDATE_DIAGRAM.md) |
[Work with diagrams](../WORK_WITH_DIAGRAMS.md).
