# Troubleshooting

| Problem | What to try |
| --- | --- |
| `dnx` is not found | Install the .NET 10 SDK, then restart your terminal and AI client. Check that `dnx --help` works. |
| The package cannot be found | Include `--prerelease` and check that your NuGet configuration allows nuget.org. |
| Visio tools do not appear | Check that the server is enabled in your client and inspect its MCP output. Organizational policy may restrict MCP servers. |
| Visio is unavailable | Open Visio Desktop manually to complete licensing or first-run prompts, then retry. Ask your assistant to open Visio before working with drawings. |
| A document or shape is not found | Reopen the drawing through the assistant. Use its exact path, page name, and returned shape identifiers rather than reusing an old session's IDs. |
| A custom shape is missing | Ask the assistant to import the local stencil, or refresh the index after saving changes to an indexed stencil. |

## Find logs

Check your client's MCP output first. Local server logs are in:

```text
%LOCALAPPDATA%\VisioMcpServer\logs
```

Save any work before restarting the server. Review and redact logs before
sharing them. If the problem persists, see [Help and feedback](SUPPORT.md).
