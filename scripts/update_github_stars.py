#!/usr/bin/env python3
import datetime
import http.client
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


GITHUB_USER = "sjtuyinjie"
FEATURED_REPOS = [
    "SJTU-ViSYS/M2DGR",
    "SJTU-ViSYS/Ground-Fusion",
    "SJTU-ViSYS/M2DGR-plus",
    "SJTU-ViSYS/Sky-GVINS",
]
OUTPUT_PATH = pathlib.Path("_data/github_stars.yml")
HEADERS = {
    "User-Agent": "sjtuyinjie-github-io-metrics-updater",
    "Accept": "application/vnd.github+json",
}


def fetch_json(url: str) -> object:
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8", errors="ignore"))


def fetch_json_with_retries(url: str, retries: int = 2) -> object:
    last_error: Exception | None = None
    for _ in range(retries + 1):
        try:
            return fetch_json(url)
        except (
            urllib.error.URLError,
            TimeoutError,
            json.JSONDecodeError,
            http.client.RemoteDisconnected,
        ) as exc:
            last_error = exc
    raise last_error or RuntimeError(f"Failed to fetch JSON: {url}")


def fetch_user_repo_stars_from_repos_api(repo_type: str, page: int = 1, total: int = 0) -> int:
    url = (
        f"https://api.github.com/users/{GITHUB_USER}/repos"
        f"?type={repo_type}&per_page=100&page={page}"
    )
    repos = fetch_json_with_retries(url)
    if not isinstance(repos, list):
        raise ValueError("Unexpected repos API response")

    page_total = total + sum(int(repo.get("stargazers_count") or 0) for repo in repos)
    if len(repos) == 100:
        return fetch_user_repo_stars_from_repos_api(repo_type, page + 1, page_total)
    return page_total


def fetch_user_repo_stars_from_search_api(page: int = 1, total: int = 0) -> int:
    query = urllib.parse.quote(f"user:{GITHUB_USER} fork:true")
    url = f"https://api.github.com/search/repositories?q={query}&per_page=100&page={page}"
    result = fetch_json_with_retries(url)
    repos = result.get("items") or []
    page_total = total + sum(int(repo.get("stargazers_count") or 0) for repo in repos)
    if len(repos) == 100 and page < 10:
        return fetch_user_repo_stars_from_search_api(page + 1, page_total)
    return page_total


def fetch_user_repo_stars() -> int:
    methods = [
        lambda: fetch_user_repo_stars_from_repos_api("owner"),
        lambda: fetch_user_repo_stars_from_repos_api("all"),
        lambda: fetch_user_repo_stars_from_search_api(),
    ]
    errors = []
    for method in methods:
        try:
            return method()
        except (
            urllib.error.URLError,
            TimeoutError,
            ValueError,
            json.JSONDecodeError,
            http.client.RemoteDisconnected,
        ) as exc:
            errors.append(str(exc))
    raise RuntimeError("; ".join(errors))


def fetch_repo_stars(full_name: str) -> int:
    url = f"https://api.github.com/repos/{full_name}"
    try:
        repo = fetch_json_with_retries(url)
        return int(repo.get("stargazers_count") or 0)
    except (
        urllib.error.URLError,
        TimeoutError,
        ValueError,
        json.JSONDecodeError,
        http.client.RemoteDisconnected,
    ):
        page_url = f"https://r.jina.ai/http://github.com/{full_name}"
        text = fetch_text_with_retries(page_url)
        match = re.search(r"([\d,.]+[kK]?)\s+stars", text, flags=re.IGNORECASE)
        if not match:
            raise ValueError(f"Failed to parse stars for {full_name}")
        raw = match.group(1).replace(",", "")
        multiplier = 1000 if raw.lower().endswith("k") else 1
        numeric = float(raw[:-1] if raw.lower().endswith("k") else raw) * multiplier
        return int(round(numeric))


def fetch_text_with_retries(url: str, retries: int = 2) -> str:
    last_error: Exception | None = None
    for _ in range(retries + 1):
        try:
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
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
    raise last_error or RuntimeError(f"Failed to fetch text: {url}")


def fetch_total_stars() -> int:
    user_stars = fetch_user_repo_stars()
    featured_stars = sum(fetch_repo_stars(name) for name in FEATURED_REPOS)
    return user_stars + featured_stars


def write_yaml(stars: int) -> None:
    today = datetime.date.today().isoformat()
    content = f"stars: {stars}\nupdated_at: \"{today}\"\n"
    OUTPUT_PATH.write_text(content, encoding="utf-8")


def main() -> int:
    try:
        stars = fetch_total_stars()
        write_yaml(stars)
    except (
        urllib.error.URLError,
        TimeoutError,
        ValueError,
        RuntimeError,
        http.client.RemoteDisconnected,
    ) as exc:
        print(f"[github-stars-update] {exc}", file=sys.stderr)
        return 0

    print(f"[github-stars-update] Updated stars to {stars}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
