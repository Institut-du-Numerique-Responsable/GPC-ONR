"""Ajoute au sitemap les pages HTML autonomes de docs/, que MkDocs n'y inscrit pas."""
import gzip
from datetime import date
from pathlib import Path

PAGES = ["presentation.html"]


def on_post_build(config, **kwargs):
    site = Path(config["site_dir"])
    sitemap = site / "sitemap.xml"
    if not sitemap.exists():
        return
    base = config["site_url"].rstrip("/") + "/"
    xml = sitemap.read_text(encoding="utf-8")
    entries = "".join(
        f"\n    <url>\n         <loc>{base}{page}</loc>\n         <lastmod>{date.today().isoformat()}</lastmod>\n    </url>"
        for page in PAGES
        if f"<loc>{base}{page}</loc>" not in xml
    )
    xml = xml.replace("</urlset>", entries + "\n</urlset>", 1)
    sitemap.write_text(xml, encoding="utf-8")
    (site / "sitemap.xml.gz").write_bytes(gzip.compress(xml.encode("utf-8")))
