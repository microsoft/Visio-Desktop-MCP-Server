---
title: Set up
nav_order: 2
permalink: /setup/
---
# Set up your AI client

## Prerequisites

Use an interactive Windows desktop session with:

- Installed, activated, licensed **Visio Desktop**, not browser-only Visio.
- The [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) for the
  `dnx` launcher, plus network access to the package source.
- An approved AI client that supports **local stdio MCP servers**, with a
  tool-capable model and an agent/tool-calling session.

Run the client, server, and Visio as the same Windows user. Use a local Windows
client window, not a server running in WSL, a container, SSH, or a cloud workspace.
The server doesn't include an AI model or a subscription to one.

Complete the [prerequisite checks](setup/PREREQUISITES.md), including Visio's
first-run prompts and the SDK commands, before editing your client settings.

## Connect from VS Code

In a local project, create `.vscode\mcp.json`, or merge the server entry into
that file without replacing other settings. For user-profile scope, run
**MCP: Open User Configuration** instead of guessing the active profile's path.
Back up an existing configuration before editing; preserve unrelated servers
and never expose stored credentials.

```json
{
  "servers": {
    "visio-local": {
      "type": "stdio",
      "command": "dnx",
      "args": ["Microsoft.Visio.Mcp", "--prerelease"]
    }
  }
}
```

`visio-local` is an example server ID; `Microsoft.Visio.Mcp` is the package ID.
The command downloads and runs the [NuGet package](https://www.nuget.org/packages/Microsoft.Visio.Mcp)
without a separate global-tool installation. Review the package license before
use. `--prerelease` allows preview versions from your configured NuGet sources.

In VS Code, run **MCP: List Servers**, select the server, and start it. Review
trust and tool-approval prompts; approve only the actions you intend. Select an
agent-capable chat session and enable the server's tools.

See the client-maintained [VS Code MCP guide](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
for configuration scopes and controls. Other local clients use the same
`dnx Microsoft.Visio.Mcp --prerelease` command but their own configuration format.
Don't copy VS Code's `servers` wrapper into a client expecting another schema.
A client's stdio support isn't a claim that every client/version has been
validated with this preview. See [client-specific paths and schemas](setup/CLIENTS.md)
for client-specific locations, JSON/TOML/YAML examples, and
version-specific notes.

## Verify the connection

Confirm that the [eight tools](TOOLS.md) appear. Tool discovery doesn't launch
Visio or prove desktop automation works. Complete the
[first-diagram walkthrough](FIRST_DIAGRAM.md) for an end-to-end check.

If launch fails, check [setup troubleshooting](TROUBLESHOOTING.md#connection-and-startup)
before retrying. Don't substitute a private feed from an old draft.

## Update or remove

Save work before restarting the server. An unpinned `dnx` configuration
resolves package versions from your configured sources; confirm the version
in the client's server output when updating.
To remove the integration, stop the server and remove only its client entry.
Saved drawings remain where you saved them.

**Related:** [Prerequisite checks](setup/PREREQUISITES.md) |
[Client configuration](setup/CLIENTS.md) |
[Configuration](CONFIGURATION.md) | [Privacy](PRIVACY.md).
