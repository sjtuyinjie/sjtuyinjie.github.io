#!/usr/bin/env python3
import datetime
import pathlib
import re
import sys
import urllib.error
import urllib.request


SCHOLAR_URL = "https://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en"
OUTPUT_PATH = pathlib.Path("_data/scholar_stats.yml")


def fetch_html(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


def extract_citations(html: str) -> int:
    # Google Scholar profile sidebar usually renders total citations
    # as the first "gsc_rsb_std" value.
    matches = re.findall(r'class="gsc_rsb_std">([\d,]+)</td>', html)
    if not matches:
        raise ValueError("Failed to locate citation count in Scholar page")
    return int(matches[0].replace(",", ""))


def write_yaml(citations: int) -> None:
    today = datetime.date.today().isoformat()
    content = f'citations: {citations}\nupdated_at: "{today}"\n'
    OUTPUT_PATH.write_text(content, encoding="utf-8")


def main() -> int:
    try:
        html = fetch_html(SCHOLAR_URL)
        citations = extract_citations(html)
        write_yaml(citations)
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        print(f"[scholar-update] {exc}", file=sys.stderr)
        # Keep workflow green when Scholar blocks requests temporarily.
        return 0

    print(f"[scholar-update] Updated citations to {citations}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
