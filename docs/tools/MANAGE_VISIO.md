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
in [known Visio locations](../CUSTOM_SHAPES.md).

## Actions and results

| Action | Behavior | Result |
| --- | --- | --- |
| `open` | Explicitly start Visio before desktop operations; reuse the live instance on repeated opens | `instanceId`, `open` |
| `close` | Close the managed application only when no retained drawings remain; never quit unrelated/user-owned processes | `instanceId`, `open`, `alreadyClosed` where applicable |
| `update_index` | Rescan known locations and publish the refreshed snapshot before returning | `action`, `stencilCount`, `masterCount`, `failedStencilCount`, `persisted`, `finishedUtc` |

A new launch receives a new instance ID. Repeated open preserves its ID and
retained drawings. Closing an already externally closed application is
idempotent. Other tools don't silently restart Visio after external closure.

Refresh is package-only: it neither launches Visio nor requires a restart.
It bypasses the [automatic refresh freshness gate](../configuration/RUNTIME.md#index-freshness).
It doesn't import/copy files or update shapes already placed in drawings.
Check `failedStencilCount`: completion doesn't mean every source was readable.
`persisted=false` means the refreshed snapshot is in memory but wasn't written
to the persistent cache, for example when another writer owns the cache lock.

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
Close only after explicitly saving any work to retain and closing retained
drawings through [manage_document](MANAGE_DOCUMENT.md):

```json
{"action": "close"}
```

## Failure handling

Application close rejects while retained drawings remain. Closing a drawing
discards unsaved edits, so don't close drawings merely to make application
shutdown succeed. Close/reopen isn't a generic retry strategy.

After external closure or server restart, open the application and saved
drawings explicitly; old retained IDs aren't reusable and unsaved content
isn't automatically recovered.

**Related:** [Tool overview](../TOOLS.md) | [Troubleshooting](../TROUBLESHOOTING.md).
