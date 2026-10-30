---
title: Configuration
nav_order: 10
permalink: /configuration/
has_toc: false
---
# Configure the server

Most users can leave server settings unset. Configure environment variables
on the **MCP server process**, not just Visio or an unrelated terminal.
Save intended work before restarting the server to apply changed settings:
retained drawing IDs belong to the previous session.

| Reference | Contents |
| --- | --- |
| [Runtime and discovery](configuration/RUNTIME.md) | Output root, visibility, locale, caches, usage ranking, index freshness, master resolution, response format |
| [Logging and diagnostics](configuration/LOGGING.md) | Levels, file logging, retention, argument limits, locations, telemetry distinction |

Tool arguments such as `options.autoLayout`, export `dpi`, and `overwrite`
are per-request settings, **not environment variables**. Find them in the
[tool reference](TOOLS.md).

## Complete VS Code example

Put this in `.vscode\mcp.json`, preserving any other configured servers.
Environment values are strings. Replace the sample folder with your approved
writable destination; don't assume `%VARIABLE%` placeholders are expanded
inside every client's JSON environment values.

```json
{
  "servers": {
    "visio-local": {
      "type": "stdio",
      "command": "dnx",
      "args": ["Microsoft.Visio.Mcp", "--prerelease"],
      "env": {
        "VISIO_MCP_ROOT": "C:\\VisioOutput",
        "VISIO_MCP_VISIBLE": "true",
        "VISIO_MCP_LOG_LEVEL": "Information",
        "VISIO_MCP_LOG_FILE": "true",
        "VISIO_MCP_LOG_RETENTION_DAYS": "14"
      }
    }
  }
}
```

For another client, put the same `env` object inside that client's server entry;
don't replace its surrounding schema with VS Code's `servers` wrapper.

## Output location

The default is `%USERPROFILE%\Documents\VisioMcp`. An explicit save without a
destination generates a path there for an unsaved drawing; use the actual
returned path. `VISIO_MCP_ROOT` changes that default, not Windows permissions,
client approvals, app-data paths, or a trusted-folder boundary.
See [runtime settings](configuration/RUNTIME.md#output-and-application).

## Local diagnostic files

Logs, stencil snapshots, and the search database live under the fixed
`%LOCALAPPDATA%\VisioMcp` app-data root, separately from diagrams.
See [exact paths and logging controls](configuration/LOGGING.md).
Changing output folders doesn't relocate these files.

Boolean parsing isn't uniform. For example, `VISIO_MCP_CACHE_DISABLED=1`
doesn't disable caching; use `true`. Read accepted values before changing a
setting, and remove an override to restore its default.

**Related:** [Setup](SETUP.md) | [Privacy and control](PRIVACY.md) |
[Troubleshooting](TROUBLESHOOTING.md).
