---
title: Help and feedback
nav_order: 13
permalink: /support/
---
# Help and feedback

Your feedback helps shape Visio Desktop MCP Server. To ask a question, report a bug,
or suggest a feature, open an issue in
[GitHub Issues](https://github.com/microsoft/Visio-Desktop-MCP-Server/issues).
Before you open a new issue, search the existing issues to see whether someone
has already reported the same problem or made the same request.

If something isn't working, check [Troubleshooting](TROUBLESHOOTING.md) first,
because it may already describe a fix. If file logging is enabled, the server
writes its logs to `%LOCALAPPDATA%\VisioMcp\logs`. You can include relevant log
excerpts in your report, but review them first and remove any credentials,
personal information, or confidential content. For log filenames and settings,
see [Configuration](CONFIGURATION.md#local-diagnostic-files).

When you report a bug, include the following information so that we can
reproduce it:

- The server package version, your Windows and Visio versions, and the AI
  client you're using.
- What you asked the agent to do, what happened, and what you expected to
  happen instead.
- The minimal steps that reproduce the problem. If they help explain it, add
  sanitized log excerpts or a screenshot.

Don't post confidential drawings, personal data, credentials, or unreviewed
logs in a public issue. Where possible, reproduce the problem with a small,
non-sensitive example drawing.

If you find a security vulnerability, don't report it in a public issue.
Instead, follow the private reporting process described in
[Security](SECURITY.md).
