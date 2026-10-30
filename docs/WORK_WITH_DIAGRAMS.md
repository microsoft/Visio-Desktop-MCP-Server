---
title: Work with diagrams
nav_order: 4
permalink: /work-with-diagrams/
---
# Create, read, and update diagrams

For the basic walkthrough, start with [Your first diagram](FIRST_DIAGRAM.md).
These patterns apply to larger drawings and existing files.

## Create from source material

Give your AI client process notes, an inventory, or a file it can read. The
client interprets that source; the Visio server doesn't directly import
arbitrary CSV, JSON, or spreadsheets.

> Use the complete travel-approval.csv attached to this chat. Open Visio and
> create a cross-functional flowchart. Create one step per distinct StepID,
> with a native swimlane per department and actual lane membership. Label
> decision branches from the source. Report missing information instead of
> inventing it. Compare steps, branches, and memberships with the input, then
> save as a new travel-approval.vsdx.

Repeated source IDs describing branches shouldn't become duplicate steps.
For shape-sensitive drawings, [resolve approved masters](CUSTOM_SHAPES.md)
before authoring.

## Read without editing

> Inspect infrastructure.vsdx without changing or saving it. On the Architecture
> page, list the servers, their Shape Data, network zones, and connections.
> Report missing fields as unknown.

Read results can include shapes, text, relationships, and native container or
swimlane membership. Request nested content when needed; the default read scope
is top-level shapes. For large results, the agent must
[retrieve all returned chunks](TOOLS.md#read-results) before drawing conclusions.

Reading supports explanation and source comparison, not visual-defect detection.
For that, use [validation](VALIDATE_AND_EXPORT.md#validate-the-layout).

## Make focused updates

> Read the Architecture page of infrastructure.vsdx. Change the owner of Order
> Service to Order Platform in Shape Data. Preserve all unrelated content,
> connections, formatting, and page settings. Leave the changes unsaved for review.

The agent should use exact shape identities returned by a read, not guessed
names or native numeric IDs. Creation and updates target **one existing page**
in a document retained by the server.

## Manage pages and save

Page creation, renaming, resizing, ordering, activation, clearing, and deletion
use separate document-management actions. Document themes apply to all
foreground pages, not only the edited page.

| Save instruction | Effect |
| --- | --- |
| Save the current drawing | Updates its current file, or generates a destination for a new drawing. |
| Save a new copy | Uses another destination; replacing an existing destination requires explicit overwrite. |
| Leave unsaved | Keeps live edits available for review in the current session. |

Keep backups and avoid concurrent edits. Closing a drawing through the server
**discards unsaved changes**; restarting loses session-scoped document identities.
An error can follow partial changes, so inspect the drawing before retrying.

**Related:** [Validate and export](VALIDATE_AND_EXPORT.md) |
[Tool reference](TOOLS.md) | [Troubleshooting](TROUBLESHOOTING.md).
