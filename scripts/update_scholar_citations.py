#!/usr/bin/env python3
import datetime
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


SCHOLAR_URL = "https://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en&cstart=0&pagesize=100"
OUTPUT_PATH = pathlib.Path("_data/scholar_stats.yml")
SCHOLAR_SOURCES = [
    SCHOLAR_URL,
    "https://api.allorigins.win/raw?url="
    + urllib.parse.quote(SCHOLAR_URL, safe=""),
    "https://r.jina.ai/http://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en&cstart=0&pagesize=100",
]
PAPER_ALIASES = [
    (re.compile(r"Innovation-based Kalman filter", re.I), "Innovation-KF"),
    (re.compile(r"Towards Robust Sensor-Fusion Ground SLAM", re.I), "M3DGR & GF2"),
    (re.compile(r"Implicit Event-RGBD Neural SLAM", re.I), "EN-SLAM"),
    (re.compile(r"Disentangled Acoustic Fields", re.I), "DAF"),
    (re.compile(r"Ground-[Cc]hallenge", re.I), "Ground-Challenge"),
    (re.compile(r"Ground-Fusion", re.I), "Ground-Fusion"),
    (re.compile(r"M2C-GVIO", re.I), "M2C-GVIO"),
    (re.compile(r"Sky-GVINS", re.I), "Sky-GVINS"),
    (re.compile(r"Ultra-Fusion", re.I), "Ultra-Fusion"),
    (re.compile(r"In-P3 VIO", re.I), "In-P3 VIO"),
    (re.compile(r"\bLIGO\b", re.I), "LIGO"),
    (re.compile(r"\bM2DGR\b", re.I), "M2DGR"),
]
CITATION_THRESHOLD = 25


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


def strip_html(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", value)).strip()


def short_paper_name(title: str) -> str:
    clean = strip_html(title)
    for pattern, alias in PAPER_ALIASES:
        if pattern.search(clean):
            return alias
    before_colon = re.split(r"[:：]", clean, maxsplit=1)[0].strip()
    return before_colon[:26] + "…" if len(before_colon) > 28 else before_colon


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


def extract_papers(text: str) -> list[tuple[str, int]]:
    papers: list[tuple[str, int]] = []
    seen: set[str] = set()

    for match in re.finditer(
        r'class="gsc_a_at"[^>]*>([\s\S]*?)</a>[\s\S]*?class="gsc_a_ac[^"]*"[^>]*>\s*([\d,]*)',
        text,
        flags=re.I,
    ):
        title = strip_html(match.group(1))
        cites = int((match.group(2) or "0").replace(",", "") or "0")
        if title and title not in seen:
            seen.add(title)
            papers.append((title, cites))

    if papers:
        return papers

    for match in re.finditer(
        r"^\|\s*(?!Title)(.+?)\s*\|\s*(\d+)\s*\|\s*\d{4}\s*\|",
        text,
        flags=re.M,
    ):
        title = strip_html(match.group(1))
        cites = int(match.group(2))
        if title and title not in seen:
            seen.add(title)
            papers.append((title, cites))

    return papers


def build_breakdown(papers: list[tuple[str, int]]) -> list[tuple[str, int]]:
    major: list[tuple[str, int]] = []
    others = 0
    for title, cites in sorted(papers, key=lambda item: item[1], reverse=True):
        if cites >= CITATION_THRESHOLD:
            major.append((short_paper_name(title), cites))
        else:
            others += cites
    if others > 0:
        major.append(("Others", others))
    return major


def fetch_scholar_data() -> tuple[int, list[tuple[str, int]]]:
    errors = []
    for source in SCHOLAR_SOURCES:
        try:
            text = fetch_text_with_retries(source)
            citations = extract_citations(text)
            papers = extract_papers(text)
            return citations, build_breakdown(papers)
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            errors.append(f"{source}: {exc}")

    raise RuntimeError("; ".join(errors))


def write_yaml(citations: int, papers: list[tuple[str, int]]) -> None:
    today = datetime.date.today().isoformat()
    lines = [f"citations: {citations}", f'updated_at: "{today}"', "papers:"]
    if papers:
        for name, count in papers:
            safe_name = name.replace('"', '\\"')
            lines.append(f'  - name: "{safe_name}"')
            lines.append(f"    citations: {count}")
    else:
        lines.append("  []")
    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    try:
        citations, papers = fetch_scholar_data()
        write_yaml(citations, papers)
    except RuntimeError as exc:
        print(f"[scholar-update] {exc}", file=sys.stderr)
        return 0

    print(f"[scholar-update] Updated citations to {citations} with {len(papers)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
