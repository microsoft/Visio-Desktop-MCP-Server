---
title: Visual Model payloads
parent: Tool reference
nav_order: 9
permalink: /tools/visual-model/
---
# Visual Model payloads

Shared nested fields for [create](CREATE_DIAGRAM.md) and
[update](UPDATE_DIAGRAM.md). Retrieve the complete machine-readable contract
with [get_visual_model_schema](GET_VISUAL_MODEL_SCHEMA.md).
Use canonical casing below, not read-output field names or old aliases.

## Root and shape fields

| Field | Meaning |
| --- | --- |
| `SchemaVersion` | Required string `"1.0"` |
| `Shapes` | Required array of shapes |
| `Relationships` | Required object with optional `Connects`/`Contains` arrays |
| `Layers` | Optional array: required `name`, optional boolean `visible`/`print`/`locked`, string `color` |
| `Metadata` | Optional `Title`, `Author`, `Description`, `VisioVersion`, `CreatedUtc`, `ModifiedUtc`, `Extensions`; timestamps are date-time strings, not proof every field changes a native property |
| `Extensions` | Preserved JSON passthrough; not an executable capability |
{: .field-table }

Shapes require unique nonempty `ID` and real `NameU` from
[content_search](CONTENT_SEARCH.md). Optional fields:

| Group | Writable fields |
| --- | --- |
| Source | `StencilPath` paired with the discovered master |
| Label | `Text`; metadata titles aren't visible page titles |
| Geometry | `PinX`, `PinY`, positive `Width`/`Height`, `Angle`; shape-dependent `BeginX`, `BeginY`, `EndX`, `EndY`, `Geometry` |
| Style/data | `Formatting`, `ShapeData`, `Hyperlinks` |
| Layers | `Layers`: unique nonempty names; undefined names are created with native defaults |

Inches are used for geometry, radians for `Angle`. `LocPinX`/`LocPinY`,
`VisioShapeId`, `Kind`, `Is1D`, `MasterId`, and `ParentId` are read observations,
not ordinary mutation controls or identity/membership substitutes.

`updateNode.patch` accepts the writable label/geometry/style/data fields above,
**not** identity/source fields or `Layers`. Change memberships with
`addToLayer`/`removeFromLayer`. Some older descriptive strings mention patch
`Layers`; the canonical patch schema doesn't define it.

## Connections and containment

Create connections require `source`/`target`; `ID` is optional and generated
when omitted. Update `addEdge` requires a new `ID` too. Optional writable fields:
`Text`, `Formatting`, `ShapeData`, `Hyperlinks`.
`updateEdge.patch` accepts those plus `source`/`target`.
Connector `NameU`, `Layers`, `glueStatus`, and native identity evidence aren't
connection-write fields.

Each create containment needs `ID`, `parent` (native container ID), and `child`
(member ID). `position` requests a zero-based native-list slot.
Placement/group ancestry alone isn't native membership.

## Formatting

Keep all fields under `Formatting`. Omitted/null typed values leave defaults
unchanged; preserving arbitrary JSON keys doesn't guarantee applying arbitrary
ShapeSheet cells.

| Fields | Type / units |
| --- | --- |
| `FillForegnd`, `FillBkgnd`, `LineColor`, `CharColor` | Color strings such as `#RRGGBB` or `RGB(r,g,b)` |
| `LineWeight`, `CharSize` | Numbers in points |
| `LinePattern`, `FillPattern` | Native integer patterns; 0 none, 1 solid |
| `FillForegndTrans`, `FillBkgndTrans` | Numbers, transparency fraction 0-1 |
| `FillGradientEnabled` | Integer 0/1 |
| `CharStyle`, `TextBkgnd` | Native integer style bitmask/background code |
| `BeginArrow`, `EndArrow` | Integer styles 0-43 |
| `BeginArrowSize`, `EndArrowSize` | Integer sizes 0-6 |
| `TxtPinX`, `TxtPinY` | Text-block position in inches |
| `VerticalAlign` | Integer: 0 top, 1 middle, 2 bottom |
| `ZOrder` | `BringToFront` or `SendToBack` |

Layer `color` additionally accepts `#RGB`, palette indices `"0"`-`"23"`,
or `"255"` for no color.

## Shape Data and hyperlinks

Shape Data is an array, not a key/value object:

```json
{
  "ShapeData": [{"name": "Owner", "label": "Service owner", "value": "Platform"}],
  "Hyperlinks": [{"name": "detail", "description": "Detailed design", "subAddress": "Detail"}]
}
```

Data row `name` is required. Optional `label`, `value`, and raw `formula`
(Visio FormulaU) are writable; the label defaults to the row name.
An unambiguous existing label can address a row, but prefer its exact identity.
`type`, `format`, `prompt`, `invisible`, and
`isEmpty` describe read-side evidence, not data-definition editing commands.

Links use optional `name`, `description`, `address`, `subAddress`, `delete`.
New links require an address/sub-address. Updates merge rows; reuse the
returned name to edit/delete one without dropping other links.
For same-document page navigation, omit/leave `address` empty and supply the
page name in `subAddress`; `delete=true` removes the addressed link.

## Low-level geometry

`Geometry` contains `{"type":"lineTo","lineTo":[{"X":1,"Y":2}]}` or
`{"type":"nurbsTo","nurbsTo":{...}}` entries. NURBS parameters include
`x`, `y`, `a`, `b`, `c`, `d`, `e` and raw extras; consult the schema.
These are geometry payloads, not an arbitrary-drawing or ShapeSheet-evaluation tool.

**Related:** [Tool overview](../TOOLS.md) | [Read evidence](READ_DIAGRAM.md).
