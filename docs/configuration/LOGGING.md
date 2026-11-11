---
title: Logging and diagnostics
parent: Configuration
nav_order: 2
permalink: /configuration/logging/
---
# Logging and diagnostics

These control local diagnostic output, not tool permissions or drawing saves.
Configure them in the [server launch environment](../CONFIGURATION.md),
then restart safely.

## Supported settings

| Variable | Default | Accepted values and effect |
| --- | --- | --- |
| `VISIO_MCP_LOCAL_LOG_ENABLED` | Enabled | Trimmed `0`, `false`, or `off`, case-insensitive, disables disk logging; other values keep it enabled |

The log level isn't configurable. Tool-call logs omit request arguments and result text, but individual diagnostic messages can still contain search terms, paths, and exception messages/stacks.

Logs roll over to a new file each day. The server doesn't delete old log
files, so review and remove them when you no longer need them.

## Fixed locations

| Purpose | Directory |
| --- | --- |
| Logs | `%LOCALAPPDATA%\VisioMcp\logs` |
| Stencil discovery data | `%LOCALAPPDATA%\VisioMcp\stencil-cache` |
| Search data | `%LOCALAPPDATA%\VisioMcp\sqlite_index` |

`VISIO_MCP_ROOT` doesn't move these directories. Their locations aren't configurable.

The server also logs to **stderr**, keeping stdout for MCP protocol messages.
Disabling file logging doesn't disable stderr; inspect the client's server
output for startup errors.

Disk logs retain ordinary diagnostic messages and exception details; they
aren't covered by the content-free policy for stderr and remote diagnostics.
Stderr omits diagram content, paths, names, raw arguments/results, and exception messages/stacks. See
[Privacy and control](../PRIVACY.md#diagnostic-telemetry) for the diagnostic
information retained and the boundaries of this policy.

## Local output versus remote telemetry

Local file logging and remote diagnostics have separate controls. Disabling file logging doesn't disable remote diagnostics. Use supported Office diagnostic-data controls and your organization's policy. See [Privacy and control](../PRIVACY.md#diagnostic-telemetry).

Review/redact logs before sharing. Don't post drawings, private paths, raw
arguments, or confidential content publicly. Use the
[safe issue-report checklist](../SUPPORT.md).

**Related:** [Troubleshooting](../TROUBLESHOOTING.md) |
[Runtime settings](RUNTIME.md).
