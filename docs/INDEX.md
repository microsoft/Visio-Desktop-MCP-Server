---
title: Overview
nav_order: 1
permalink: /
---
# Visio Desktop MCP

Create, inspect, and update **native, editable Visio diagrams** from an
MCP-compatible AI client. The client interprets your request and supplies the
model; the local server provides tools that automate Visio Desktop on Windows
over standard input/output (`stdio`), not HTTP.

**Preview:** for evaluation, not production or critical workloads. Review the
license terms included with the package.
{: .preview-notice }

## Start here

[Set up your client](SETUP.md) > [Create your first diagram](FIRST_DIAGRAM.md) >
[Work with diagrams](WORK_WITH_DIAGRAMS.md).

## Find the right guide

| I want to... | Read |
| --- | --- |
| Create, analyze, or make focused edits | [Work with diagrams](WORK_WITH_DIAGRAMS.md) |
| Check layout and share an image or PDF | [Validate and export](VALIDATE_AND_EXPORT.md) |
| Understand the eight tools and their contracts | [Tool reference](TOOLS.md) |
| Use approved stencils and templates | [Custom shapes](CUSTOM_SHAPES.md) |
| Reuse team-specific instructions | [Custom agents](CUSTOM_AGENTS.md) |
| Write a clear request from source data | [Examples and best practices](EXAMPLES.md) |
| Change output, discovery, caching, or diagnostics | [Configuration](CONFIGURATION.md) |
| Understand data handling and permissions | [Privacy and control](PRIVACY.md) |
| Resolve a failure or report a problem | [Troubleshooting](TROUBLESHOOTING.md) and [Help](SUPPORT.md) |

## Know the boundaries

The server requires the installed Windows desktop app; it doesn't operate
Visio for the web or provide headless cloud automation. The AI client reads
your source files; the server isn't a general-purpose spreadsheet or CSV
importer. Only the capabilities exposed by its tools are available.

Results depend on your model, installed content, and drawing complexity.
Review source fidelity and appearance in Visio before relying on a drawing.
Local automation also doesn't mean model processing stays on your device:
read [Privacy and control](PRIVACY.md) before using sensitive content.

### Add-ins and Automation events

During automation, the server turns off Visio's
`Application.EventsEnabled` setting so add-ins can't change a drawing
unexpectedly. Add-ins, macros, and some built-in drawing features depend on
these events. The setting applies to the whole Visio instance, not one
document: it stays off after an MCP call, and closing a drawing doesn't reset
it.

To restore normal behavior after you finish MCP work:

1. Stop the MCP server.
2. In Visio, go to **File > Options > Advanced**.
3. Under **General**, select **Enable Automation Events**, and then select **OK**.

Using MCP again can turn events off again. You don't need to disable your
add-ins.
