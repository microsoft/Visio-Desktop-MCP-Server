---
title: validate_diagram
parent: Tool reference
nav_order: 6
permalink: /tools/validate-diagram/
---
# validate_diagram

Read-only visual-quality checks after authoring or on an explicit validation
request. This doesn't repair content or prove source/business correctness.
For ordinary reading and inventory, use [read_diagram](READ_DIAGRAM.md).

## Arguments

| Argument | Type/default | Meaning |
| --- | --- | --- |
| `diagramId` | Optional string | Retained live drawing, including unsaved edits; takes precedence over file path |
| `filePath` | Optional string | Absolute drawing path when no retained ID is supplied |
| `options` | Optional object | Scope settings below |
| `codes` | Optional string | Comma-separated finding codes; filters detail, not global counts |
| `offset` | Nonnegative integer; `0` | Position in matched detail sequence; follow returned `nextOffset` |

At least one document selector is required; Visio must be explicitly open.

| `options` field | Default | Behavior |
| --- | --- | --- |
| `pages` | All pages | String-array page names/1-based index strings |
| `shapeIds` | No filter | Retain findings involving at least one selected stable logical shape ID; other shapes still participate in interactions |
| `includeOcclusion` | `true` | `false` skips `CONNECTOR_OCCLUSION` |

See the canonical [eight finding-code definitions](../VALIDATE_AND_EXPORT.md#validate-the-layout).

## Example

```json
{
  "diagramId": "<diagramId>",
  "options": {"pages": ["1"], "includeOcclusion": true},
  "codes": "TEXT_OVERFLOW,UNGLUED_CONNECTOR",
  "offset": 0
}
```

To page, repeat the same selectors/options/code filter with the returned
`nextOffset` as `offset`. Keep the drawing unchanged while comparing pages.

## Results

| Field | Interpretation |
| --- | --- |
| `counts.byCode`, `counts.bySeverity`, `findingsTotal` | Complete findings totals for the evaluated scope, before code filtering/pagination |
| `findingsMatched` | Number matching the requested code filter |
| `findings` | At most 30 records per response, distributed across finding classes |
| `findingsOmitted`, `nextOffset` | More detail remains; narrow by codes or follow the offset |
| `checks.LOW_CONTRAST_TEXT` | Candidate, evaluated, skipped counts and skip reasons |
| Finding fields | `code`, `severity` (`info`/`warning`), `message`, `shapeIds`, `pageId`, diagnostic `data` |

Take totals from counts, **not the capped findings array**. Attribute defects
to the validator and cite its returned IDs. For edits, prefer read-returned
stable IDs: validation can fall back to native IDs for unindexed shapes.

A blank or entirely unmatched code filter currently falls back to unfiltered
findings rather than an empty success result. Use the exact supported codes.

## Scope limits

Disabled checks, unselected pages, and skipped contrast candidates are
**unevaluated**, not clean. Zero findings means none detected only for the
pages/candidates actually evaluated. An absent code count isn't proof of a
clean check if relevant candidates were skipped.

Read back labels, identifiers, relationships, memberships, and data separately
to establish source fidelity. Formal validation doesn't save the drawing.

**Related:** [Validate and export guide](../VALIDATE_AND_EXPORT.md) |
[Update](UPDATE_DIAGRAM.md) | [Tool overview](../TOOLS.md).
