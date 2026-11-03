"""Check generated Pages output without fetching third-party services."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import urlopen
from urllib.error import HTTPError
import xml.etree.ElementTree as ET

BASE = "https://b1011205.github.io/vecord-support/"
STORE = "https://apps.apple.com/jp/app/vecord/id6793060453"
NAV = [("整備記録のコツ", BASE + "articles/"),
       ("プライバシー", BASE + "privacy-policy/"),
       ("サポート", BASE + "support/"),
       ("OSSライセンス", BASE + "licenses/")]
PUBLIC = {"", "support/", "privacy-policy/", "licenses/", "contact/",
          "articles/", "articles/oil-change-record/", "articles/car-maintenance-record/"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.refs, self.images = [], [], [], []
        self.meta, self.ids, self.headings = {}, set(), []
        self.canonical, self.title, self.lang, self.script_count = None, "", None, 0
        self.nav_links, self.nav_list_depth = [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "ul" and "nav-list" in a.get("class", "").split():
            self.nav_list_depth = len(self.stack)
        if tag == "a" and self.nav_list_depth:
            self.nav_links.append({"href": a.get("href", ""), "text": ""})
        if tag == "html":
            self.lang = a.get("lang")
        if "id" in a:
            if a["id"] in self.ids:
                self.errors.append("duplicate id: " + a["id"])
            self.ids.add(a["id"])
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(int(tag[1]))
        if tag == "meta":
            self.meta[a.get("name", a.get("property"))] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag == "script":
            self.script_count += 1
        if tag == "img":
            if "alt" not in a:
                self.errors.append("img without alt")
            self.images.append(a)
        if tag in {"a", "link"} and "href" in a:
            self.refs.append(a["href"])
        if tag in {"img", "script"} and "src" in a:
            self.refs.append(a["src"])

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if tag == "ul" and len(self.stack) == self.nav_list_depth:
            self.nav_list_depth = 0
        if not self.stack or self.stack[-1] != tag:
            self.errors.append("unmatched closing tag: " + tag)
        else:
            self.stack.pop()

    def handle_data(self, data):
        if self.stack and self.stack[-1] == "title":
            self.title += data
        if self.nav_list_depth and self.stack[-1] == "a":
            self.nav_links[-1]["text"] += data


def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("directory", type=Path)
    cli.add_argument("--http", help="local origin, e.g. http://127.0.0.1:8027")
    args = cli.parse_args()
    root = args.directory.resolve()
    assert not (root / "docs").exists(), "marketing drafts leaked to build"
    assert not (root / "scripts").exists(), "scripts leaked to build"
    assert not (root / "README.md").exists(), "README leaked to build"
    pages = {}
    for file in root.rglob("*.html"):
        parser = Page()
        parser.feed(file.read_text())
        assert not parser.stack and not parser.errors, (file, parser.stack, parser.errors)
        assert parser.lang == "ja" and parser.headings.count(1) == 1, file
        pages[file.resolve()] = parser
    seen_titles, seen_desc = set(), set()
    for path in sorted(PUBLIC):
        file = (root / path / "index.html").resolve()
        page = pages[file]
        assert page.canonical == BASE + path, (path, "canonical")
        assert page.meta.get("description"), (path, "description")
        assert "noindex" not in page.meta.get("robots", ""), path
        assert page.title not in seen_titles, "duplicate title"
        assert page.meta["description"] not in seen_desc, "duplicate description"
        seen_titles.add(page.title)
        seen_desc.add(page.meta["description"])
        if not path or path.startswith("articles/"):
            assert STORE in page.refs, (path, "missing Store CTA")
            assert page.script_count == 0, (path, "unexpected JavaScript")
            for key in ["og:title", "og:description", "og:image", "og:image:alt", "twitter:card", "twitter:title", "twitter:description", "twitter:image"]:
                assert page.meta.get(key), (path, key)
            assert page.meta["og:url"] == BASE + path, path
        print("PASS page", BASE + path)
    assert "noindex" in pages[(root / "404.html").resolve()].meta.get("robots", "")
    links = 0
    for file, page in pages.items():
        document_url = BASE + file.relative_to(root).as_posix()
        nav = [(link["text"].strip(), urljoin(document_url, link["href"]))
               for link in page.nav_links]
        assert nav == NAV, (file, "inconsistent header navigation", nav)
        for ref in page.refs + [page.meta[k] for k in ["og:image", "twitter:image"] if k in page.meta]:
            parsed = urlsplit(urljoin(document_url, ref))
            if parsed.netloc != urlsplit(BASE).netloc:
                continue
            assert parsed.path.startswith("/vecord-support/"), (file, "subpath escape", ref)
            local = root / unquote(parsed.path.removeprefix("/vecord-support/"))
            if local.is_dir():
                local = local / "index.html"
            assert local.is_file(), (file, "broken link", ref)
            if parsed.fragment and local.suffix == ".html":
                assert unquote(parsed.fragment) in pages[local.resolve()].ids, (file, "missing anchor", ref)
            links += 1
    sitemap = ET.parse(root / "sitemap.xml")
    locations = [e.text for e in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    assert set(locations) == {BASE + p for p in PUBLIC} and len(locations) == len(PUBLIC)
    if args.http:
        for path in PUBLIC:
            with urlopen(args.http + "/vecord-support/" + path) as response:
                assert response.status == 200
        for path in ["docs/marketing/social-posts.md", "docs/marketing/kpi-tracking.csv", "scripts/check-site.py", "not-a-real-page/"]:
            try:
                urlopen(args.http + "/vecord-support/" + path)
                raise AssertionError("non-public path returned 200: " + path)
            except HTTPError as error:
                assert error.code == 404
                assert "ページが見つかりません" in error.read().decode()
    print(f"PASS {len(pages)} HTML documents, {links} internal references, {len(locations)} sitemap URLs; drafts excluded")


if __name__ == "__main__":
    main()
