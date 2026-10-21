import html
import json
import re
from html.parser import HTMLParser
from typing import Any, Dict, Iterator, List, Optional, Tuple
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests

from threads_dlp.errors import ThreadsDlpError
from threads_dlp.http_client import create_session
from threads_dlp.models import Media

_THREADS_HOSTS = {"threads.com", "threads.net"}
_MEDIA_HOST_SUFFIXES = ("fbcdn.net", "cdninstagram.com", "threads.com", "threads.net")
_CRAWLER_USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
_POST_PATHS = (
    re.compile(r"/@[^/]+/post/([A-Za-z0-9_-]+)(?:/|$)"),
    re.compile(r"/t/([A-Za-z0-9_-]+)(?:/|$)"),
)
_SHARE_PATH = re.compile(r"/share/([A-Za-z0-9_-]+)(?:/|$)")


class _PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.json_scripts: List[str] = []
        self.meta: Dict[str, str] = {}
        self._script_parts: List[str] = []
        self._capture_script = False

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        if tag == "meta":
            key = values.get("property") or values.get("name")
            content = values.get("content")
            if key and content:
                self.meta[key.lower()] = content
        if tag == "script":
            self._capture_script = (
                values.get("type", "").lower() == "application/json"
                or "data-sjs" in values
            )
            self._script_parts = []

    def handle_data(self, data: str) -> None:
        if self._capture_script:
            self._script_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._capture_script:
            self.json_scripts.append("".join(self._script_parts))
            self._script_parts = []
            self._capture_script = False


def _normalise_page_url(value: str) -> Tuple[str, str, str]:
    raw = value.strip()
    try:
        parsed = urlsplit(raw)
    except ValueError as exc:
        raise ThreadsDlpError("Enter a valid Threads post URL from threads.com or threads.net.") from exc
    host = (parsed.hostname or "").lower()
    allowed_hosts = _THREADS_HOSTS | {f"www.{item}" for item in _THREADS_HOSTS}
    if parsed.scheme.lower() not in {"http", "https"} or host not in allowed_hosts:
        raise ThreadsDlpError("Enter a valid Threads post URL from threads.com or threads.net.")
    try:
        port = parsed.port
    except ValueError as exc:
        raise ThreadsDlpError("The Threads URL contains an invalid port.") from exc
    if parsed.username or parsed.password or (port not in {None, 80, 443}):
        raise ThreadsDlpError("The Threads URL contains an unsupported host or port.")
    path = parsed.path or "/"
    match = None
    for pattern in _POST_PATHS:
        match = pattern.search(path)
        if match:
            break
    if match:
        post_id = match.group(1)
    elif _SHARE_PATH.search(path):
        post_id = ""
    else:
        raise ThreadsDlpError("The URL must point to a Threads post or share link.")
    canonical_host = host.removeprefix("www.")
    page_url = urlunsplit(("https", canonical_host, path, parsed.query, ""))
    referer = f"https://{canonical_host}/"
    return page_url, post_id, referer


def _post_id_from_url(value: str) -> str:
    parsed = urlsplit(value)
    for pattern in _POST_PATHS:
        match = pattern.search(parsed.path)
        if match:
            return match.group(1)
    return ""


def _walk(value: Any) -> Iterator[Dict[str, Any]]:
    pending = [value]
    while pending:
        current = pending.pop()
        if isinstance(current, dict):
            yield current
            pending.extend(current.values())
        elif isinstance(current, list):
            pending.extend(current)
        elif isinstance(current, str) and current.lstrip().startswith(("{", "[")):
            try:
                pending.append(json.loads(current))
            except (json.JSONDecodeError, RecursionError):
                continue


def _media_url(value: Any, base_url: str) -> Optional[str]:
    if not isinstance(value, str) or not value.strip():
        return None
    cleaned = html.unescape(value.strip())
    cleaned = cleaned.replace("\\/", "/")
    try:
        absolute = urljoin(base_url, cleaned)
        parsed = urlsplit(absolute)
    except ValueError:
        return None
    host = (parsed.hostname or "").lower()
    if (
        parsed.scheme.lower() != "https"
        or parsed.username
        or parsed.password
        or not any(host == suffix or host.endswith(f".{suffix}") for suffix in _MEDIA_HOST_SUFFIXES)
    ):
        return None
    return absolute


def _candidate_urls(media: Dict[str, Any], base_url: str) -> List[Tuple[int, int, str]]:
    candidates: List[Tuple[int, int, str]] = []
    versions = media.get("video_versions")
    if isinstance(versions, list):
        for version in versions:
            if not isinstance(version, dict):
                continue
            value = _media_url(version.get("url"), base_url)
            if value:
                width = version.get("width")
                height = version.get("height")
                resolution = (width if isinstance(width, int) else 0) * (height if isinstance(height, int) else 0)
                candidates.append((resolution, len(candidates), value))
    direct = _media_url(media.get("video_url"), base_url)
    if direct:
        candidates.append((0, len(candidates), direct))
    return candidates


def _select_video(data_blocks: List[str], target_id: str, page_url: str) -> Optional[str]:
    matches: List[Tuple[int, int, str]] = []
    for block in data_blocks:
        try:
            root = json.loads(block)
        except (json.JSONDecodeError, TypeError, RecursionError):
            continue
        for item in _walk(root):
            item_id = item.get("code") or item.get("shortcode")
            if item_id != target_id:
                continue
            carousel = item.get("carousel_media")
            media_items = carousel if isinstance(carousel, list) else [item]
            for media_item in media_items:
                if isinstance(media_item, dict):
                    candidates = _candidate_urls(media_item, page_url)
                    if candidates:
                        matches.extend(candidates)
                        break
    if not matches:
        return None
    return max(matches, key=lambda candidate: (candidate[0], -candidate[1]))[2]


def extractor(url: str) -> Media:
    page_url, target_id, referer = _normalise_page_url(url)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.8",
        "User-Agent": _CRAWLER_USER_AGENT,
    }
    with create_session() as session:
        try:
            response = session.get(page_url, headers=headers, timeout=(15, 30), allow_redirects=True)
        except requests.Timeout as exc:
            raise ThreadsDlpError("The request to Threads timed out. Check the connection and try again.") from exc
        except requests.RequestException as exc:
            raise ThreadsDlpError("Could not connect to Threads. Check the connection and try again.") from exc

        with response:
            final_host = (urlsplit(response.url).hostname or "").lower().removeprefix("www.")
            if final_host not in _THREADS_HOSTS:
                raise ThreadsDlpError("The Threads link redirected to an unsupported website.")
            if response.status_code == 404:
                raise ThreadsDlpError("Threads could not find that post. Check the link and try again.")
            if response.status_code in {401, 403}:
                raise ThreadsDlpError("Threads did not allow access to this page. Only publicly viewable posts are supported.")
            if response.status_code >= 400:
                raise ThreadsDlpError(f"Threads returned HTTP {response.status_code} while loading the post.")
            parser = _PageParser()
            try:
                parser.feed(response.text)
                parser.close()
            except Exception as exc:
                raise ThreadsDlpError("Threads returned a page that could not be read.") from exc

            page_id = _post_id_from_url(response.url)
            canonical_url = parser.meta.get("og:url", "")
            canonical_id = _post_id_from_url(canonical_url)
            if not target_id:
                target_id = canonical_id or page_id
            if not target_id:
                raise ThreadsDlpError("The share link did not resolve to a public Threads post.")

            video_url = _select_video(parser.json_scripts, target_id, response.url)
            if not video_url and canonical_id == target_id:
                video_url = _media_url(
                    parser.meta.get("og:video")
                    or parser.meta.get("og:video:url")
                    or parser.meta.get("twitter:player:stream"),
                    response.url,
                )
            if not video_url:
                raise ThreadsDlpError(
                    "No public video was found for this post. It may be private, deleted, restricted, or contain no video."
                )
            return Media(post_id=target_id, url=video_url, referer=referer)
