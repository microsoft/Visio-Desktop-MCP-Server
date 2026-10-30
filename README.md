# Visio MCP Server

Create, understand, and update native, editable Visio diagrams with your AI
agent. This repository provides documentation and feedback channels for the
[Microsoft.Visio.Mcp package](https://www.nuget.org/packages/Microsoft.Visio.Mcp).

**Preview:** for evaluation, not production or critical workloads. Review the
license terms included with the package.

## Documentation

**[Documentation site](https://microsoft.github.io/Visio-Desktop-MCP-Server)**

Read here on GitHub:
[Overview](docs/INDEX.md) | [Set up](docs/SETUP.md) |
[First diagram](docs/FIRST_DIAGRAM.md) | [Tool reference](docs/TOOLS.md) |
[Examples](docs/EXAMPLES.md).

[Troubleshooting](docs/TROUBLESHOOTING.md) | [Privacy](docs/PRIVACY.md) |
[Help and feedback](docs/SUPPORT.md) | [Security](docs/SECURITY.md).

## Maintain the site

Every published page lives in `docs`. Name Markdown files, including issue
templates, in uppercase with underscores (for example, `VALIDATE_AND_EXPORT.md`),
matching GitHub's `SUPPORT.md` and `CODE_OF_CONDUCT.md`. Folders, images,
scripts, and Jekyll or Sass files keep the lowercase names their tools expect.
Each subject has one canonical page; link to it instead of copying instructions. Each page sets a `permalink`, so
published URLs don't change when files move. The relative-links
plugin maps those links to each page's published permalink. Put images in
`assets/images` and link them relatively from the page (for example,
`../assets/images/name.png` from `docs`). Sanitize screenshots so they contain
no personal paths, names, or confidential content.

Site styling lives in `_sass`: the color scheme in `_sass/color_schemes/visio.scss`,
overrides in `_sass/custom/custom.scss`, and the navigation breakpoint in
`_sass/custom/setup.scss` (below 960px, navigation collapses into a menu).
Before opening a pull request, run
`python scripts/check_site.py _site --baseurl /Visio-Desktop-MCP-Server` on a
built site to check internal links, assets, and anchors.

The Pages configuration targets
`https://microsoft.github.io/Visio-Desktop-MCP-Server`. The Documentation workflow
builds the site and checks internal links/anchors on pull requests; only `main`
deploys. Before the first deployment, a repository administrator must select
**Settings > Pages > Source > GitHub Actions**. Adding these files doesn't
publish the site or change repository settings.
