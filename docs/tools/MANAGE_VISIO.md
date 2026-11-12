---
title: manage_visio
parent: Tool reference
nav_order: 1
permalink: /tools/manage-visio/
---
# manage_visio

Manage the server-owned application session or refresh content discovery.
This tool doesn't open drawings; use [manage_document](MANAGE_DOCUMENT.md).

## Arguments

| Argument | Type | Required | Values |
| --- | --- | --- | --- |
| `action` | string | Yes | `open`, `close`, `update_index` |

There is **no** client `options` or `filePath` argument. Place approved content
in [known Visio locations](../CUSTOM_CONTENT.md).

## Actions and results

| Action | Behavior | Result |
| --- | --- | --- |
| `open` | Explicitly start Visio before desktop operations; reuse the live instance on repeated opens | `instanceId`, `open` |
| `close` | Check all live documents before closing saved retained drawings and quitting only the server-owned application; unsaved work blocks shutdown with a confirmation warning, not a tool error | `instanceId`, `open`, `alreadyClosed` where applicable; `open:true`, `requiresConfirmation:true`, and warnings when unsaved work blocks close |
| `update_index` | Rescan known locations; updated content is available to search when the call finishes | `action`, `stencilCount`, `masterCount`, `failedStencilCount`, `persisted`, `finishedUtc` |

A new launch receives a new instance ID. Repeated open preserves its ID and
retained drawings. Closing an already externally closed application is
idempotent. [manage_document](MANAGE_DOCUMENT.md) `action="open"` or `action="create"` starts Visio
if needed, including after external closure. Other document actions and
source reads don't implicitly restart it.

Refresh neither launches Visio nor requires a restart.
It runs even when the index is newer than the [automatic refresh threshold](../configuration/RUNTIME.md#index-freshness).
It doesn't import/copy files or update shapes already placed in drawings.
Check `failedStencilCount`: completion doesn't mean every source was readable.
`persisted=false` doesn't mean refresh failed: the refreshed content is usable in the current session, but this refresh wasn't saved for reuse after a restart.

## Examples

Open the application:

```json
{"action": "open"}
```

Refresh after installing or changing approved stencil/template files:

```json
{"action": "update_index"}
```

Then search the refreshed content with [content_search](CONTENT_SEARCH.md).
Close only after explicitly saving any work to retain. Saved retained
drawings are closed as part of application shutdown:

```json
{"action": "close"}
```

## Failure handling

Application close checks all live documents before closing any retained
drawings. If that check finds unsaved work, no drawings are closed and Visio
remains open with `open:true`, `requiresConfirmation:true`, and warnings,
not a tool error. It does not save or discard those changes.
Save first to keep them, or explicitly close each retained
unsaved drawing through [manage_document](MANAGE_DOCUMENT.md#side-effects)
with `options.discardUnsavedChanges:true` only after user approval to discard
its edits, then retry application close. Don't discard work merely to make
shutdown succeed. Close/reopen isn't a generic retry strategy.

The server refuses to quit a shared or user-owned application. Ownership
violations and operational failures remain tool errors. Native state changes
or failures after the initial check can interrupt an already-started shutdown;
inspect actual state before retrying.

After external closure or server restart, reopen the intended saved drawing through `manage_document action="open"`; it starts Visio if needed. Old retained IDs aren't reusable and unsaved content
isn't automatically recovered.

**Related:** [Tool overview](../TOOLS.md) | [Troubleshooting](../TROUBLESHOOTING.md).
