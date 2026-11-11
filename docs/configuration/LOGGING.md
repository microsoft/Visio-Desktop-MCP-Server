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

The log level is built into the server; environment variables can't change
it. Tool-call logging omits serialized arguments and result text. An empty
argument placeholder doesn't mean the actual request had no arguments.
Individual diagnostic messages in disk logs can still contain search terms,
paths, and exception messages/stacks.

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

Disk logs retain ordinary diagnostic messages and exception details; they
aren't covered by the content-free policy for stderr and remote diagnostics.
Stderr uses controlled messages and diagnostic categories, not arbitrary free
text. Diagram content, paths, names, raw arguments/results, and exception
messages/stacks aren't included as fallback stderr text. Unrecognized
diagnostic messages are omitted from stderr. See
[Privacy and control](../PRIVACY.md#diagnostic-telemetry) for the diagnostic
information retained and the boundaries of this policy.

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
