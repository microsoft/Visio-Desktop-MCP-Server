import tempfile
import unittest
from pathlib import Path

from check_site import check_site


class CheckSiteTests(unittest.TestCase):
    def test_project_site_links_assets_and_fragments(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "guide").mkdir()
            (root / "style.css").write_text("", encoding="utf-8")
            (root / "index.html").write_text(
                '<a href="/project/guide/#start">Guide</a>'
                '<a href="https://example.com/elsewhere">External</a>'
                '<link href="/project/style.css" rel="stylesheet">',
                encoding="utf-8",
            )
            (root / "guide" / "index.html").write_text(
                '<h1 id="start">Guide</h1><a href="../">Home</a>'
                '<a href="#start">Start</a>',
                encoding="utf-8",
            )
            self.assertEqual(check_site(root, "/project"), [])

    def test_invalid_links_are_rejected(self):
        cases = {
            "/guide/": "outside baseurl",
            "/project/missing/": "missing target",
            "#missing": "missing anchor",
            "../outside.html": "outside site",
        }
        for link, expected in cases.items():
            with self.subTest(link=link), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                (root / "index.html").write_text(
                    f'<a href="{link}">Link</a>', encoding="utf-8"
                )
                self.assertIn(expected, check_site(root, "/project")[0])

    def test_empty_build_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(
                check_site(Path(directory).resolve(), "/project"),
                ["No built HTML pages found."],
            )


if __name__ == "__main__":
    unittest.main()
