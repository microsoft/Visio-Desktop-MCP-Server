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
| `VISIO_MCP_LOG_LEVEL` | `Information` | Named levels, case-insensitive: `Trace`, `Debug`, `Information`, `Warning`, `Error`, `Critical`, `None`. Invalid values fall back |
| `VISIO_MCP_LOG_FILE` | Enabled | Trimmed `0`, `false`, or `off`, case-insensitive, disables disk logging; other values keep it enabled |
| `VISIO_MCP_LOG_RETENTION_DAYS` | `14` | Nonnegative integer days; `0` retains indefinitely. Invalid/negative values use default; old rolling logs are cleaned at startup |
| `VISIO_MCP_LOG_ARG_MAX` | `2048` | Nonnegative serialized argument-log size budget in bytes per call; invalid/negative values use default |

The argument-log budget limits diagnostics, not accepted tool input or
response size. It doesn't request unredacted input.
Tool-argument logging remains redacted.

For a temporary investigation, set `VISIO_MCP_LOG_LEVEL` to `Debug`,
reproduce the issue, then return to `Information`. `None` suppresses local
log levels; it isn't a remote diagnostic-data control.

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
organization's policy. Environment settings don't override an Office policy
that disables diagnostics.

Required-tier diagnostic eligibility isn't proof of emission: Office
permission, build/configured routing, and successful sink initialization also
matter. See [Privacy and control](../PRIVACY.md#diagnostic-telemetry).

## Advanced telemetry diagnostics

These advanced controls configure remote telemetry routing and diagnostics.
They are **not required or recommended for normal client setup** and
don't control diagramming features.

| Variable | Default | Effect and limits |
| --- | --- | --- |
| `VISIO_MCP_UTEL_TOKEN` | Build-embedded routing token, if present | Nonblank, trimmed runtime override of ingestion routing. Blank falls back to build metadata; no resolved token means no remote emission. No token value is reproduced here |
| `VISIO_MCP_UTEL_NAMESPACE` | `Office.Visio.Mcp` | Trimmed event namespace; blank uses the default. Must contain at least one period; otherwise telemetry initialization is disabled for that run |
| `VISIO_MCP_BUILD_AUDIENCE` | Assembly-stamped audience; otherwise `Dogfood` | Nonblank, trimmed override of the reported audience. Doesn't change the binary's stamped audience, install features, select a release, or bypass Production scanner restrictions |
| `VISIO_MCP_UTEL_PRIVACY_GUARD_ENABLED` | Enabled for eligible non-Production audiences | Trimmed, case-insensitive `true`/`false`; unset or unrecognized values use the default. Scanner remains off if either the stamped or resolved audience is `Production` |

The scanner setting concerns telemetry scanning, not document sensitivity
labels, sharing, or client approvals. Remote emission still requires Office
diagnostic-data permission, resolved routing, and successful sink
initialization; these controls don't override organizational policy.

Review/redact logs before sharing. Don't post drawings, private paths, raw
arguments, or confidential content publicly. Use the
[safe issue-report checklist](../SUPPORT.md).

**Related:** [Troubleshooting](../TROUBLESHOOTING.md) |
[Runtime settings](RUNTIME.md).
