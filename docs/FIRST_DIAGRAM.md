---
title: First diagram
nav_order: 3
permalink: /first-diagram/
---
# Create your first diagram

Complete [setup](SETUP.md), then try a small drawing with built-in shapes.
The following are requests to your AI agent, not terminal commands.

## Create and save

> Open Visio and create a new drawing with a landscape page named Onboarding.
> Use standard flowchart process shapes for these five steps, in order:
> Offer accepted; Complete paperwork; Provision account and device;
> Complete orientation; Ready to start. Join consecutive steps with attached,
> directed connectors. Save as a new onboarding.vsdx without replacing an
> existing file. Read the result and report the full saved path, the five
> process-step labels, and the step and connector counts.

Approve intended tool actions, then inspect the drawing in Visio. Expect
**five process steps and four connectors**, excluding any decorative title.
Select a shape and inspect its label; move it to check that connectors remain
attached. The result should be editable shapes, not a flattened picture.

The agent must explicitly open Visio and save the drawing. Connecting the
server, creating content, or editing it doesn't automatically save a file.
Use the successful save's reported path; see [output locations](CONFIGURATION.md#output-location)
if you need a different default.

## Make one focused change

> Read the current onboarding drawing. Insert a Manager check-in step between
> Complete orientation and Ready to start, matching its neighboring shapes.
> Replace only the connection between those steps with connections through the
> new step. Preserve everything else. Save to the same file, read it again,
> and report the process-step and connector counts.

Expect **six steps and five connectors**. Check the actual drawing if the
reported counts differ. You can keep it open between requests; avoid manual
edits while the agent is working.

## Check the result

Continue with [Validate and export](VALIDATE_AND_EXPORT.md) to check supported
layout defects and create a separate PNG or PDF.

**Related:** [Work with diagrams](WORK_WITH_DIAGRAMS.md) for other workflows |
[Examples and best practices](EXAMPLES.md) for clearer requests |
[Troubleshooting](TROUBLESHOOTING.md) if a step fails.
