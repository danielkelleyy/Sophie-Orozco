#!/usr/bin/env python3
"""Build paste-ready copies of the VSL funnel pages for GoHighLevel.

Edit the pages in vsl-funnel/*.html (they link funnel.css and the photos in
landing-page/images/, so they're easy to edit and preview in a browser).
Then run:

    python3 vsl-funnel/build.py

Each page is written to vsl-funnel/ghl-ready/ with funnel.css and every local
image inlined, so the whole file can be pasted into a GHL Custom Code element,
the same way landing-page/landing.html is.

Page-to-page links (video.html, application.html, ...) are left as-is: swap
them for your GHL funnel step URLs, either in the source or after pasting.
"""
import base64
import mimetypes
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "ghl-ready"
PAGES = ["optin.html", "video.html", "application.html", "book-call.html", "confirmation.html"]


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def build(name: str) -> None:
    html = (HERE / name).read_text()
    css = (HERE / "funnel.css").read_text()
    # funnel.css uses only inline data: SVGs, so it can be dropped in as-is.
    html = html.replace('<link rel="stylesheet" href="funnel.css">', f"<style>\n{css}</style>")

    def inline(m: re.Match) -> str:
        src = m.group(2)
        if src.startswith(("http", "data:", "//")):
            return m.group(0)
        path = (HERE / src).resolve()
        if not path.is_file():  # e.g. LOGO_URL placeholders
            return m.group(0)
        return f'{m.group(1)}{data_uri(path)}{m.group(3)}'

    html = re.sub(r'(<img[^>]*?\ssrc=")([^"]+)(")', inline, html)
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text(html)
    print(f"ghl-ready/{name}: {len(html) // 1024} KB")


if __name__ == "__main__":
    for page in PAGES:
        build(page)
