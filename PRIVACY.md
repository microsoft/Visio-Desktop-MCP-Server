# Privacy and control

The server runs locally and can read and modify files accessible to your Windows
account. Your AI client may send diagram content, prompts, and tool results to
its model provider. Local execution does not mean your conversation stays on
your PC; review your client's data policies and your organization's requirements.

Only connect trusted clients and approve access to drawings you intend to use.
Do not share confidential drawings or logs in public issues.

## Diagnostic telemetry

The server can send diagnostic telemetry to Microsoft, subject to Office's
diagnostic-data settings. To disable server telemetry, add this environment
setting to its MCP client configuration and restart the server:

```json
{
  "env": {
    "VISIO_MCP_UTEL_LOGGING_ENABLED": "false"
  }
}
```

This does not disable your AI client's telemetry or local server logs.
See the [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement).
