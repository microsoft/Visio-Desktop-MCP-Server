---
title: Privacy and control
nav_order: 11
permalink: /privacy/
---
# Privacy and control

The server runs locally and can read and modify files accessible to your Windows
account. Your AI client may send diagram content, prompts, and tool results to
its model provider. Local execution does not mean your conversation stays on
your PC; review your client's data policies and your organization's requirements.

Only connect trusted clients and approve access to drawings you intend to use.
Do not share confidential drawings or logs in public issues.

## Diagnostic telemetry

The server can send operational diagnostics to Microsoft when Office
diagnostic-data permissions and its telemetry configuration allow it.
Required-tier diagnostics are permitted unless Office diagnostic data is
fully disabled. Organizational policy can take precedence over user settings.
Use your organization's supported Office privacy controls.

Office diagnostic settings don't control your AI client's handling of diagram
content. Conversely, disabling local file logging doesn't disable remote
diagnostics or stderr output.

## Files and approvals

The default output folder isn't an access boundary. The server runs with your
Windows account's filesystem permissions and doesn't maintain a trusted-folder
allowlist. Client approvals are separate controls, not a guarantee that every
file operation is restricted to that folder.

Keep backups of important drawings, approve intended operations, and review
results before saving or sharing. For log paths and local logging settings,
see [Configuration](CONFIGURATION.md); for safe issue reports, see
[Help and feedback](SUPPORT.md).

See the [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement).
