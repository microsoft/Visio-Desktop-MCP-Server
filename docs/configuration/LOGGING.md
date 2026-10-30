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
| `VISIO_MCP_LOG_FILE` | Enabled | Trimmed `0`, `false`, or `off`, case-insensitive, disables disk logging; other values keep it enabled |

The log level and the size limit for logged tool arguments are built into the
server; environment variables can't change them. Tool arguments in logs
remain redacted.

Logs roll over to a new file each day. The server doesn't delete old log
files, so review and remove them when you no longer need them.

## Fixed locations

| Files | Location |
| --- | --- |
| Daily logs | `%LOCALAPPDATA%\VisioMcp\logs\visio-mcp-YYYY-MM-DD.log` |
| Stencil snapshot/usage | `%LOCALAPPDATA%\VisioMcp\stencil-cache\index.json` and `usage.json` |
| Master-search SQLite database | `%LOCALAPPDATA%\VisioMcp\sqlite_index\masters_corpus_v3.db` |

`VISIO_MCP_ROOT` doesn't move these files. Published CLI launch settings don't
expose their paths as directory/database overrides.

The server also logs to **stderr**, keeping stdout for MCP protocol messages.
Disabling file logging doesn't disable stderr; inspect the client's server
output for startup errors.

## Local output versus remote telemetry

Disk logging, stderr, local usage ranking, and remote operational diagnostics
are separate. Use supported Office diagnostic-data controls and your
organization's policy.

Required-tier diagnostic eligibility isn't proof of emission: Office
permission, build/configured routing, and successful sink initialization also
matter. See [Privacy and control](../PRIVACY.md#diagnostic-telemetry).

Review/redact logs before sharing. Don't post drawings, private paths, raw
arguments, or confidential content publicly. Use the
[safe issue-report checklist](../SUPPORT.md).

**Related:** [Troubleshooting](../TROUBLESHOOTING.md) |
[Runtime settings](RUNTIME.md).
