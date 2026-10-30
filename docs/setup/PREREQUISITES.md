---
title: Prerequisite checks
parent: Set up
nav_order: 1
permalink: /setup/prerequisites/
---
# Check prerequisites before connecting

Use these checks before [configuring the client](../SETUP.md#connect-from-vs-code).
They diagnose readiness; none launches the MCP server or saves a drawing.

## Desktop and Visio

Use an interactive Windows desktop session.
Use installed, licensed Visio Desktop under the same Windows user as the
client/server, not Visio for the web or a remote Linux/container session.

Open Visio manually once and complete sign-in, activation, licensing, and
other first-run prompts. Check release compatibility for your specific
Visio edition/build rather than assuming every perpetual or subscription
edition is validated.

## SDK and launcher

Install the [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
(10.0.100 or later in the .NET 10 family). The SDK includes runtimes; a
runtime-only installation doesn't supply the required SDK tooling.
Check from a Windows terminal:

```powershell
dotnet --info
dotnet --list-sdks
dotnet --list-runtimes
dnx --help
```

Confirm a .NET 10 SDK is listed and `dnx` is available. If commands aren't
found after installing, reopen the terminal/client and inspect its PATH.
An SDK selected by a workspace `global.json` can differ from another terminal;
check the environment actually launching the server.

## Client, access, and assets

| Check | Ready when... |
| --- | --- |
| Local MCP support | The chosen client/profile can launch a command over stdio on this Windows desktop |
| Model/session | Agent/tool-calling mode is selected, not text-only chat |
| Entitlement | Your account has the needed client/model access, quota, and organizational permission; the server supplies none |
| Package source | Approved NuGet sources, source mapping, proxy, and endpoint policies allow obtaining `Microsoft.Visio.Mcp` |
| Files | Required drawings/templates/stencils are local, approved, and licensed for use |
| Destination | An organization-approved folder is writable by the server's Windows user |

Don't disable security controls or substitute private package-feed URLs from
old guides to make setup work. Follow your organization's approved package
configuration.

After connecting, tool discovery verifies the MCP link only. Complete the
[first-diagram exercise](../FIRST_DIAGRAM.md) to check desktop automation,
native editability, reading, and explicit saving.

**Related:** [Setup troubleshooting](../TROUBLESHOOTING.md#connection-and-startup) |
[Configuration](../CONFIGURATION.md).
