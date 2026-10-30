"""Check built Pages links, assets, and fragments without external requests."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


def check_site(root, baseurl):
    pages = {}
    for path in root.rglob("*.html"):
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parser
    if not pages:
        return ["No built HTML pages found."]

    errors = []
    prefix = baseurl.rstrip("/")
    for source, parser in pages.items():
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            if path.startswith("/"):
                if prefix and path != prefix and not path.startswith(prefix + "/"):
                    errors.append(f"{source.relative_to(root)}: outside baseurl: {link}")
                    continue
                target = root / path[len(prefix):].lstrip("/")
            else:
                target = source.parent / path if path else source
            target = target.resolve()
            if not target.is_relative_to(root):
                errors.append(f"{source.relative_to(root)}: outside site: {link}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{source.relative_to(root)}: missing target: {link}")
            elif url.fragment and target in pages:
                fragment = unquote(url.fragment)
                if fragment not in pages[target].ids:
                    errors.append(f"{source.relative_to(root)}: missing anchor: {link}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    errors = check_site(args.site.resolve(), args.baseurl)
    if errors:
        print("\n".join(errors))
        return 1
    print("All internal links, assets, and anchors resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
