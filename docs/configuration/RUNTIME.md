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
| `VISIO_APP_VISIBLE` | Visible | `1`, `true`, `yes`, `on` enable visibility/repainting, case-insensitive and without trimming. Any other explicit value, including empty or surrounding whitespace, hides it |
{: .settings-table }

Hidden doesn't mean headless: an interactive Windows session, installed
Visio, and an open application are still required for desktop operations.
Use [manage_visio open](../tools/MANAGE_VISIO.md) before creating a new
drawing, or let [manage_document open](../tools/MANAGE_DOCUMENT.md) start
Visio when opening an intended existing drawing. Other tools don't start
it implicitly. No environment setting saves a drawing automatically.

## Session mode

| Variable | Default | Accepted values and effect |
| --- | --- | --- |
| `VISIO_MCP_SESSION_TYPE` | `interactive` | Trimmed, case-insensitive `interactive` or `eval` labels the session in operational diagnostics. Unset/blank uses `interactive`; other values become `unknown`. `eval` also requires a newly launched, verified Visio instance |
{: .settings-table }

Leave this unset for normal client use. `eval` is for controlled evaluation, not a startup troubleshooting switch: it rejects a shared or unverifiable Visio instance with `VISIO_NOT_AVAILABLE` before changing its display, add-on, or document state. It doesn't terminate other Visio sessions or guarantee that no other Visio processes are running. Changing session type doesn't override Office diagnostic-data permissions.

## Index freshness

The first eligible tool call in a session refreshes the stencil index in the
background if the saved index is more than 15 minutes old. This built-in
interval is **not a periodic timer** and can't be changed with an environment
variable.

For changes now, use [manage_visio update_index](../tools/MANAGE_VISIO.md).
It waits for refresh/publication and bypasses freshness without opening Visio
or requiring a restart.

Configure custom content through [registered Visio locations](../CUSTOM_CONTENT.md).
Built-in content follows the Windows display language, falling back to English
or another installed Visio language; there's no setting to choose it.

**Related:** [Configuration](../CONFIGURATION.md) | [Logging](LOGGING.md) |
[Custom shapes](../CUSTOM_CONTENT.md).
