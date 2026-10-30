---
title: Client configuration
parent: Set up
nav_order: 2
permalink: /setup/clients/
---
# Client-specific paths and schemas

Configuration locations and formats vary by client version and installation.
Use the active configuration opened by your client. Not every client/version
has been tested with Visio.

Run the client and server locally on the Windows desktop with Visio.
Open the client's active configuration, back it up, and merge only the
`visio-local` entry without replacing other servers or exposing credentials.
All examples use your configured NuGet sources, without a feed override.

## Configuration locations

These are Windows/PowerShell path expressions, not literal strings to paste
into JSON. Resolve them for your user and installation.

| Client | Windows configuration path | Format |
| --- | --- | --- |
| VS Code | `$env:APPDATA\Code\User\mcp.json`; workspace `.vscode\mcp.json` | JSON: `servers` |
| Claude Desktop | `$env:LOCALAPPDATA\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json` | JSON: `mcpServers` |
| Copilot Desktop | `$env:USERPROFILE\.copilot\mcp-config.json` | JSON: `mcpServers` |
| AnythingLLM Desktop | `$env:USERPROFILE\AppData\anythingllm-desktop\storage\plugins\anythingllm_mcp_servers.json` | JSON: `mcpServers` |
| Antigravity | `$env:USERPROFILE\.gemini\config\mcp_config.json` | JSON: `mcpServers` |
| ChatGPT Desktop | `$env:USERPROFILE\.codex\config.toml` | TOML: `mcp_servers` |
| Codex | `$env:USERPROFILE\.codex\config.toml` | TOML: `mcp_servers` |
| Hermes | `$env:LOCALAPPDATA\Local\Hermes\config.yaml` | YAML: `mcp_servers` |

### Client-specific notes

- **VS Code:** use **MCP: Open User Configuration** for the active profile;
  the table gives the default profile location. Use the complete
  [VS Code example](../SETUP.md), not the `mcpServers` example below.
- **Claude Desktop:** the packaged-installation path can differ from the
  standard `%APPDATA%\Claude\claude_desktop_config.json` location.
  Use **Settings > Developer > Edit Config** to open the active file.
  See [Claude Desktop MCP setup](https://modelcontextprotocol.io/docs/develop/connect-local-servers).
- **Copilot Desktop:** don't assume that all Copilot-branded clients read
  the same configuration file. Confirm the active configuration location
  in the installed app before editing.
- **AnythingLLM and Antigravity:** the listed Windows paths haven't been
  verified for all versions. Check the installed app's configuration:
  [AnythingLLM MCP](https://docs.anythingllm.com/mcp-compatibility/overview) |
  [Antigravity MCP](https://antigravity.google/docs/mcp).
- **ChatGPT Desktop / Codex:** clients using the same Codex host share
  `~/.codex/config.toml`. This doesn't make a browser-only ChatGPT session
  a local Windows stdio client.
  See [MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).
- **Hermes:** configuration depends on the specific product/version.
  [Nous Research's Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/)
  uses `~/.hermes/config.yaml` with the YAML schema below.
  Don't assume the table's Hermes path applies to that product.

## Shared JSON configuration

For clients using an `mcpServers` JSON wrapper, merge this minimal entry
into the concerned client's file. Include any additional fields required
by that client/version.

```json
{
  "mcpServers": {
    "visio-local": {
      "command": "dnx",
      "args": ["Microsoft.Visio.Mcp", "--prerelease"]
    }
  }
}
```

## ChatGPT Desktop / Codex TOML

```toml
[mcp_servers.visio-local]
command = "dnx"
args = ["Microsoft.Visio.Mcp", "--prerelease"]
```

## Hermes YAML

```yaml
mcp_servers:
  visio-local:
    command: dnx
    args:
      - Microsoft.Visio.Mcp
      - --prerelease
```

Apply the change using the client's documented reload/restart action, review
trust and tool approvals, and confirm the eight tools appear. Discovery
alone doesn't verify desktop automation; complete the
[first-diagram walkthrough](../FIRST_DIAGRAM.md).

For server environment variables, use [Configuration](../CONFIGURATION.md).
