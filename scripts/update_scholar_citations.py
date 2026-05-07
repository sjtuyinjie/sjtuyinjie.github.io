#!/usr/bin/env python3
import datetime
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


SCHOLAR_URL = "https://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en"
OUTPUT_PATH = pathlib.Path("_data/scholar_stats.yml")
SCHOLAR_SOURCES = [
    SCHOLAR_URL,
    "https://api.allorigins.win/raw?url="
    + urllib.parse.quote(SCHOLAR_URL, safe=""),
    "https://r.jina.ai/http://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en",
]


def fetch_text(url: str) -> str:
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


def fetch_text_with_retries(url: str, retries: int = 2) -> str:
    last_error: Exception | None = None
    for _ in range(retries + 1):
        try:
            return fetch_text(url)
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
    raise last_error or RuntimeError("Failed to fetch Scholar source")


def extract_citations(text: str) -> int:
    patterns = [
        r'class="gsc_rsb_std">([\d,]+)</td>',
        r"<td[^>]*>\s*Citations\s*</td>\s*<td[^>]*>\s*([\d,]+)\s*</td>",
        r"Citations[\s\S]*?\n\s*([\d,]+)",
        r"Citations\s+([\d,]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return int(match.group(1).replace(",", ""))

    raise ValueError("Failed to locate citation count in Scholar page")


def fetch_citations() -> int:
    errors = []
    for source in SCHOLAR_SOURCES:
        try:
            return extract_citations(fetch_text_with_retries(source))
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            errors.append(f"{source}: {exc}")

    raise RuntimeError("; ".join(errors))


def write_yaml(citations: int) -> None:
    today = datetime.date.today().isoformat()
    content = f'citations: {citations}\nupdated_at: "{today}"\n'
    OUTPUT_PATH.write_text(content, encoding="utf-8")


def main() -> int:
    try:
        citations = fetch_citations()
        write_yaml(citations)
    except RuntimeError as exc:
        print(f"[scholar-update] {exc}", file=sys.stderr)
        # Keep workflow green when Scholar blocks requests temporarily.
        return 0

    print(f"[scholar-update] Updated citations to {citations}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
