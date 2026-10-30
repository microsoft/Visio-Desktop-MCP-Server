---
title: Overview
nav_order: 1
permalink: /
---
# Visio Desktop MCP Server

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

The server works only with the Visio desktop app installed on Windows. It
doesn't work with Visio for the web or provide headless cloud automation. The
AI client reads your source files; the server doesn't import CSV, JSON, or
Excel files itself. Only the capabilities exposed by its tools are available;
some tasks may still need to be done directly in Visio.

Results depend on your model, installed content, and drawing complexity.
Review source fidelity and appearance in Visio before relying on a drawing.
Local automation also doesn't mean model processing stays on your device:
read [Privacy and control](PRIVACY.md) before using sensitive content.

Also expect these preview limitations:

- **Output varies:** results can differ between models and between runs of
  the same prompt.
- **Layout needs review:** spacing, alignment, connector routing, and text
  placement may need manual adjustment.
- **Large drawings:** large or highly connected diagrams may need several
  scoped operations and extra review. A partial answer about a large drawing
  doesn't mean the rest of it is empty.
- **Existing diagrams:** scope changes narrowly and verify that unrelated
  content was preserved.
- **Layout check:** it finds visual problems only. It doesn't fix them or
  confirm that the content is correct, and skipped items haven't been
  checked. See [Validate and export](VALIDATE_AND_EXPORT.md).
- **Custom and smart shapes:** shapes that rely on macros, add-ins, protected
  cells, or other shape logic may not behave as in manual use. See
  [Test before standardizing](CUSTOM_SHAPES.md#test-before-standardizing).
- **Add-ins and macros:** the server turns off Visio events while it works,
  so add-ins, macros, and some built-in features might not run. Events stay
  off for that Visio instance until you turn them back on. See
  [Add-ins and macros don't run](TROUBLESHOOTING.md#add-ins-and-macros-dont-run).
- **Legacy stencils:** `.vss` and `.vst` files don't expose indexed masters;
  use a modern-format copy. See [Discover and bind masters](CUSTOM_SHAPES.md#discover-and-bind-masters).
- **Saving:** changes are saved only when the agent saves the drawing, so ask
  it to save and check the reported path before closing. You don't need to
  save it yourself in Visio. Exporting doesn't save the drawing, closing discards
  unsaved changes, and an export can replace an earlier export with the same
  name. Don't edit the same diagram yourself,
  open another copy of it, or let more than one agent work on it at the same
  time. See [Manage pages and save](WORK_WITH_DIAGRAMS.md#manage-pages-and-save).
- **Interactive session:** run the AI client, the server, and Visio in the
  same signed-in Windows session, even when Visio runs hidden. There's no
  hosted version, and the server isn't designed to run as an unattended
  Windows service. Don't start it in WSL, a development container, an SSH
  session, or a cloud workspace.
  See [Prerequisites](SETUP.md#prerequisites).
- **Client compatibility:** not every AI client or version has been tested
  with this preview. A local MCP configuration doesn't override your
  organization's restrictions on AI clients, MCP servers, or tools.
