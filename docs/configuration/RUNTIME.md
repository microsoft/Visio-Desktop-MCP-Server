---
title: Runtime and discovery
parent: Configuration
nav_order: 1
permalink: /configuration/runtime/
---
# Runtime and discovery

Set these in the [server entry's environment](../CONFIGURATION.md#complete-vs-code-example),
then restart the server after safely saving intended work. Defaults below
mean **unset**, not necessarily your current machine's values.

## Output and application

| Variable | Default | Accepted values and effect |
| --- | --- | --- |
| `VISIO_MCP_ROOT` | `%USERPROFILE%\Documents\VisioMcp` | Nonblank directory path; created at startup. Blank/whitespace uses default. Generated drawings/read artifacts, not authorization or app-data relocation |
| `VISIO_MCP_VISIBLE` | Visible | `1`, `true`, `yes`, `on` enable visibility/repainting, case-insensitive. Any other explicit value, including empty, hides it |

Hidden doesn't mean headless: an interactive Windows session, installed
Visio, and explicit [manage_visio open](../tools/MANAGE_VISIO.md) are still
required. No environment setting saves a drawing automatically.

## Discovery and caching

| Variable | Default | Accepted values and effect |
| --- | --- | --- |
| `VISIO_MCP_STENCIL_LCID` | Automatic | Integer locale, e.g. `1033`. Requested locale is tried before UI locale, English, and other installed numeric folders; invalid/unavailable values fall back |
| `VISIO_MCP_CACHE_DISABLED` | Cache enabled | Only `true`, case-insensitive, disables persistent stencil caching; `1` does **not** |
| `VISIO_MCP_USAGE_TRACKING` | Enabled | Only `false`, case-insensitive, disables successful-master usage tracking and usage-driven ranking boost |
| `VISIO_MCP_INDEX_REFRESH_SECONDS` | `900` | Nonnegative integer seconds; invalid/negative values use default. See freshness below |
| `VISIO_MCP_STRICT_MASTER` | Disabled | Exact `1`, `true`, or `TRUE` makes unresolved source ties fail instead of deterministic tie-breaking with a warning |

Prefer explicit discovered `masterId`/source pairs to any ambiguity setting.
See [master binding](../tools/CONTENT_SEARCH.md#results-and-master-bindings).

Disabling the persistent stencil cache also prevents persistent usage tracking;
it isn't a global off-switch for every in-memory index or SQLite database.
Usage tracking here is local master-ranking behavior, not a remote telemetry
opt-out. See [logging and diagnostics](LOGGING.md).

### Index freshness

The refresh interval is a cross-process freshness test for the first eligible
tool-call warm-up, **not a periodic timer**. `0` forces that first-call refresh
in the next session; it doesn't reindex on every call.

For changes now, use [manage_visio update_index](../tools/MANAGE_VISIO.md).
It waits for refresh/publication and bypasses freshness without opening Visio
or requiring a restart.

Configure custom content through [known/registered Visio locations](../CUSTOM_SHAPES.md).
Locale changes affect
built-in discovery, not display language or arbitrary custom-root selection.

## MCP response format

| Variable | Default | Accepted values and effect |
| --- | --- | --- |
| `VISIO_MCP_STRUCTURED_CONTENT` | Disabled | Exact `1` or `true` adds MCP `structuredContent` alongside JSON text; other values leave it disabled |

Enable only when the client requires that extra slot. It duplicates payload
size, doesn't change the tool's JSON contract, and isn't a chunk-size control.
For large reads, use the [artifact protocol](../tools/READ_DIAGRAM.md#large-results-and-artifacts).

**Related:** [Configuration](../CONFIGURATION.md) | [Logging](LOGGING.md) |
[Custom shapes](../CUSTOM_SHAPES.md).
