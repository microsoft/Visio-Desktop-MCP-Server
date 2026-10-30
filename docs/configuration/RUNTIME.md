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
{: .settings-table }

Hidden doesn't mean headless: an interactive Windows session, installed
Visio, and explicit [manage_visio open](../tools/MANAGE_VISIO.md) are still
required. No environment setting saves a drawing automatically.

### Index freshness

The first eligible tool call in a session refreshes the stencil index in the
background if the saved index is more than 15 minutes old. This built-in
interval is **not a periodic timer** and can't be changed with an environment
variable.

For changes now, use [manage_visio update_index](../tools/MANAGE_VISIO.md).
It waits for refresh/publication and bypasses freshness without opening Visio
or requiring a restart.

Configure custom content through [registered Visio locations](../CUSTOM_SHAPES.md).
Built-in content follows the Windows display language, falling back to English
or another installed Visio language; there's no setting to choose it.

**Related:** [Configuration](../CONFIGURATION.md) | [Logging](LOGGING.md) |
[Custom shapes](../CUSTOM_SHAPES.md).
