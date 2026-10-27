# Visio MCP Server

Create, understand, and edit Visio diagrams with your AI assistant.

The [Visio MCP Server](https://www.nuget.org/packages/Microsoft.Visio.Mcp) connects
MCP-compatible AI clients to Microsoft Visio Desktop on your Windows PC. This
repository provides setup guidance, examples, and a place to share feedback.

**Preview:** for evaluation only, not production or critical workloads. Review
the license terms included with the NuGet package before use.

## What can you do?

- Create flowcharts, org charts, network diagrams, and other drawings.
- Read an existing diagram and ask questions about its contents.
- Update shapes, text, connections, formatting, and Shape Data.
- Check for common visual issues and export to PNG, SVG, or PDF.
- Find shapes in installed or custom stencils.

## Get started

You need Windows 10 or 11, licensed Visio Desktop, the
[.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0), and an MCP-compatible
AI client.

### 1. Connect your AI client

`dnx` downloads and runs the server from NuGet. No separate installation is needed.

For VS Code, add this to `.vscode\mcp.json`, then start the server from the MCP
server list:

```json
{
  "servers": {
    "visio": {
      "type": "stdio",
      "command": "dnx",
      "args": ["Microsoft.Visio.Mcp", "--prerelease"]
    }
  }
}
```

For other clients, use `dnx Microsoft.Visio.Mcp --prerelease` as the local stdio
server command. The surrounding configuration format depends on the client.

### 2. Try a prompt

> Open Visio and create a simple approval flowchart with a decision and two
> outcomes. Save it in the default output folder and tell me the file path.

Generated files default to `%USERPROFILE%\Documents\VisioModelMcp`.
See [more examples](docs/EXAMPLES.md).

## Available tools

Your AI assistant chooses the tools needed for your request.

| Tool | Purpose |
| --- | --- |
| `manage_visio` | Open or close Visio; import stencils and refresh the shape index. |
| `manage_document` | Create, open, save, close, or export drawings; manage pages. |
| `create_diagram` | Add a diagram to an existing page. |
| `read_diagram` | Read a drawing, page, or specific shapes. |
| `update_diagram` | Edit shapes, connections, containers, and layers. |
| `validate_diagram` | Check for common visual issues. |
| `content_search` | Find available stencils, templates, and shapes. |
| `get_visual_model_schema` | Get the structured diagram format used by the tools. |

## Before you use it

Work on a copy of important drawings, review the result, and explicitly ask to
save changes. AI-generated layouts and answers can be incomplete or inaccurate.

This server requires desktop Visio on Windows. It does not run in Visio for the
web, on macOS, or as a headless cloud service. Available shapes depend on your
installed Visio content.

[Troubleshooting](TROUBLESHOOTING.md) |
[Privacy](PRIVACY.md) |
[Help and feedback](SUPPORT.md) |
[Security](SECURITY.md)
