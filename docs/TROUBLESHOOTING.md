---
title: Troubleshooting
nav_order: 12
permalink: /troubleshooting/
---
# Troubleshooting

**Protect unsaved work first.** Closing a drawing through the server discards
unsaved edits. Don't close/reopen Visio or restart the server as a generic
response to a failed tool call.

## Connection and startup

| Symptom | Check |
| --- | --- |
| `dnx` not found | Install the SDK, not only the runtime, from [setup](SETUP.md). Reopen the client/terminal; check `dotnet --list-sdks` and `dnx --help`. |
| Package source unavailable | Check the configured NuGet sources, package availability, network, and approved proxy settings. Don't disable certificate/security checks or copy a private feed from an old guide. |
| Tools missing | Confirm the server is enabled in the active client/session. In VS Code, use **MCP: List Servers** and inspect its output and tool selection. |
| Visio not open | Ask the agent to use `manage_visio action="open"` before desktop operations; tool discovery alone doesn't launch it. |
| Slow first request | Package download, desktop startup, and local discovery are separate stages. Inspect output/logs to locate the delay. |

## Files and sessions

| Symptom | Check |
| --- | --- |
| Operation stalls | Inspect Visio for sign-in, recovery, or modal prompts and resolve them yourself. Check actual drawing state before retrying. |
| `COM_OPEN_CONFLICT` | Read the error's path/details; another Visio instance may hold a conflicting copy. Save work before closing anything. Reuse an already-retained drawing. |
| Access denied | Check client approval and Windows permissions; the output root isn't a filesystem sandbox. |
| `FILE_ALREADY_EXISTS` | Choose a new destination or explicitly authorize overwrite. [Save and export defaults differ](WORK_WITH_DIAGRAMS.md#manage-pages-and-save). |
| Changes absent from disk | Ask for an explicit save and confirm its returned path. An export doesn't save the source. |
| Save error names a staged recovery file | Preserve that file. Open the exact reported recovery path, inspect it, and save to an available destination; don't recreate or delete it blindly. |
| Retained ID no longer works | IDs belong to the server session. After external closure or restart, explicitly open Visio and the saved file again; unsaved state isn't automatically recovered. |

## Drawing results

| Symptom | Check |
| --- | --- |
| Custom shapes missing | Follow [Custom shapes](CUSTOM_SHAPES.md): place files in My Shapes or a folder registered under **File > Options > Advanced > File Locations** (**Stencils** or **Templates**), explicitly refresh the index, then search. |
| Stencil listed but masters absent | Legacy `.vss`/`.vst` entries don't have package-indexed masters. Use a modern-format copy. Don't open the stencil as the target drawing. |
| Missing or unexpected content | Read and compare against the complete source. [Validation](VALIDATE_AND_EXPORT.md) checks visual defects, not process completeness. |
| Partial large-diagram answer | Narrow the read or retrieve all [issued chunks](TOOLS.md#read-results). Omitted nested fields aren't proof of absence. |
| Edit fails midway | Inspect what changed before requesting a smaller correction. A successful response can still contain operation failures. |
| Add-ins or macros don't run | Visio events may be turned off. See [Add-ins and macros don't run](#add-ins-and-macros-dont-run). |

## Add-ins and macros don't run

During automation, the server turns off Visio's `Application.EventsEnabled`
setting so add-ins can't change a drawing unexpectedly. Some container and
swimlane changes turn events on briefly. Add-ins, macros, and some built-in
drawing features depend on these events and might not run or update the
diagram as they do when you edit it yourself.

The setting applies to the whole Visio instance, not one document: it stays
off after an MCP call, and closing a drawing doesn't reset it. To turn events
back on after you finish MCP work:

1. Stop the MCP server.
2. In Visio, go to **File > Options > Advanced**.
3. Under **General**, select **Enable Automation Events**, and then select **OK**.

Using MCP again can turn events off again. You don't need to disable your
add-ins.

## Collect diagnostics

Use [Configuration](CONFIGURATION.md#local-diagnostic-files) for log
locations and settings. In VS Code, use **MCP: List Servers**, select the
server, and choose **Show Output**, including when no log file was created.

Review and sanitize excerpts before sharing. See [Help and feedback](SUPPORT.md)
for what to include and private security-reporting guidance.
