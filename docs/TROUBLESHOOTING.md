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

## Collect diagnostics

Use [Configuration](CONFIGURATION.md#local-diagnostic-files) for log
locations and settings. In VS Code, use **MCP: List Servers**, select the
server, and choose **Show Output**, including when no log file was created.

Review and sanitize excerpts before sharing. See [Help and feedback](SUPPORT.md)
for what to include and private security-reporting guidance.
