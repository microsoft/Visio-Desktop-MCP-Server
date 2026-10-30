---
title: Validate and export
nav_order: 5
permalink: /validate-and-export/
---
# Validate and export

Use this after [creating or updating a drawing](WORK_WITH_DIAGRAMS.md).
Compare content with your source separately: visual validation doesn't prove
business correctness.

## Validate the layout

> Validate the current drawing for supported visual defects. Report the returned
> shape IDs and findings. Make focused repairs without changing the process,
> validate again, and describe anything unresolved. Save after review.

`validate_diagram` reports these eight finding categories:

| Code | Checks for |
| --- | --- |
| `OVERLAP` | Shapes covering each other |
| `TEXT_OVERFLOW` | Text larger than its shape |
| `CONNECTOR_LABEL_COLLISION` | Connector labels colliding with other content |
| `CONNECTOR_OCCLUSION` | Connectors hidden behind shapes |
| `UNGLUED_CONNECTOR` | Unattached connector endpoints |
| `OUT_OF_BOUNDS` | Content outside the page |
| `INVISIBLE_IN_RASTER` | Shapes invisible in raster output |
| `LOW_CONTRAST_TEXT` | Text contrast against the resolved background |

Validation reports findings; it doesn't repair the drawing itself. Findings
are scoped to evaluated pages and candidates. Disabled checks and skipped
contrast candidates are **unevaluated**, not clean.

The response's totals and `counts` describe the complete findings set; the
detail array is capped at 30 records. Use `codes` or follow `nextOffset` for
more detail rather than counting only the first array.

## Export a separate artifact

> Export page 1 of onboarding.vsdx to onboarding.png at 300 DPI. Export the
> entire document to onboarding-review.pdf in the same folder. Use distinct
> filenames if those exports already exist and report the full output paths.

| Output | Page selection |
| --- | --- |
| PNG, JPG/JPEG, GIF, BMP, TIF/TIFF, EMF, SVG | One page, selected pages, or all pages as separate images |
| PDF, XPS | Whole document only; a page subset isn't accepted |

For one image, supply one page selector and a complete output filename.
For multiple/all image pages, supply a destination **directory** and an
explicit format; the server generates page-based filenames.

Only PNG accepts a custom positive integer DPI. Omitting it preserves Visio's
current raster settings; temporary DPI changes are restored after export.
PDF/XPS support `print` (default) or `screen` intent, not PNG DPI.

Exports use the current drawing, including unsaved edits, but **don't save
the source drawing**. Export defaults allow replacing existing export files;
choose new filenames or set `options.overwrite=false` when preserving them.

**Related:** [Validation parameters](tools/VALIDATE_DIAGRAM.md) |
[Export requests](tools/MANAGE_DOCUMENT.md#page-and-export-examples) |
[Examples](EXAMPLES.md) for source checks | [Troubleshooting](TROUBLESHOOTING.md).
