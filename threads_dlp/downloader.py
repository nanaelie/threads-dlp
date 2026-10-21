import os
import sys
import tempfile
from pathlib import Path
from typing import Optional, Union

import requests

from threads_dlp.errors import ThreadsDlpError
from threads_dlp.http_client import create_session
from threads_dlp.make_out_path import out_path
from threads_dlp.models import Media

_USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


def _format_size(value: int) -> str:
    size = float(value)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def _show_progress(downloaded: int, total_size: Optional[int]) -> None:
    if not sys.stderr.isatty():
        return
    if total_size:
        percent = min(downloaded / total_size * 100, 100)
        message = f"Downloaded {_format_size(downloaded)} / {_format_size(total_size)} ({percent:5.1f}%)"
    else:
        message = f"Downloaded {_format_size(downloaded)}"
    print(f"\r{message}", end="", file=sys.stderr, flush=True)


def downloader(media: Media, output: Optional[Union[str, Path]] = None) -> Path:
    try:
        target = out_path(media.post_id, output)
    except OSError as exc:
        raise ThreadsDlpError(f"Could not create the output folder: {exc}") from exc

    reserved = False
    temporary_path = None
    progress_shown = False
    session = create_session()
    try:
        index = 0
        while True:
            target = out_path(media.post_id, output, index=index)
            try:
                descriptor = os.open(target, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
                os.close(descriptor)
                reserved = True
                break
            except FileExistsError:
                index += 1
            except OSError as exc:
                raise ThreadsDlpError(f"Could not create the output file: {exc}") from exc

        headers = {
            "Accept": "video/mp4,application/octet-stream;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "identity",
            "Referer": media.referer,
            "User-Agent": _USER_AGENT,
        }
        try:
            response = session.get(media.url, headers=headers, stream=True, timeout=(15, 60))
        except requests.Timeout as exc:
            raise ThreadsDlpError("The video download timed out. Check the connection and try again.") from exc
        except requests.RequestException as exc:
            raise ThreadsDlpError("Could not connect to the video source. Check the connection and try again.") from exc

        with response:
            if response.status_code >= 400:
                raise ThreadsDlpError(f"The video source returned HTTP {response.status_code}. The video link may have expired; try again.")
            content_type = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
            if content_type and not content_type.startswith("video/") and content_type not in {"application/octet-stream", "binary/octet-stream"}:
                raise ThreadsDlpError("The video source returned a web page instead of a video. The post may be unavailable; try again.")
            length_value = response.headers.get("Content-Length", "")
            total_size = int(length_value) if length_value.isdigit() else None
            descriptor, temporary_name = tempfile.mkstemp(prefix=f".{media.post_id}.", suffix=".part", dir=str(target.parent))
            temporary_path = Path(temporary_name)
            downloaded = 0
            last_progress = 0
            with os.fdopen(descriptor, "wb") as output_file:
                try:
                    for chunk in response.iter_content(chunk_size=64 * 1024):
                        if not chunk:
                            continue
                        output_file.write(chunk)
                        downloaded += len(chunk)
                        if downloaded - last_progress >= 512 * 1024 or (total_size and downloaded >= total_size):
                            _show_progress(downloaded, total_size)
                            progress_shown = True
                            last_progress = downloaded
                except requests.RequestException as exc:
                    raise ThreadsDlpError("The download was interrupted. Check the connection and try again.") from exc
            _show_progress(downloaded, total_size)
            progress_shown = True
            if downloaded == 0:
                raise ThreadsDlpError("The video source returned an empty file.")
            if total_size is not None and downloaded != total_size:
                raise ThreadsDlpError("The download ended before all video data arrived. Check the connection and try again.")
        os.replace(temporary_path, target)
        temporary_path = None
        reserved = False
        return target
    except OSError as exc:
        raise ThreadsDlpError(f"Could not save the video: {exc}") from exc
    finally:
        session.close()
        if progress_shown and sys.stderr.isatty():
            print(file=sys.stderr)
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass
        if reserved:
            try:
                target.unlink(missing_ok=True)
            except OSError:
                pass
