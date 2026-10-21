import re
from pathlib import Path
from typing import Optional, Union

from threads_dlp.errors import ThreadsDlpError


def out_path(post_id: str, output: Optional[Union[str, Path]] = None, index: int = 0) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9_-]+", post_id):
        raise ThreadsDlpError("The Threads post link contains an invalid post ID.")
    directory = Path(output if output is not None else ".").expanduser()
    directory.mkdir(parents=True, exist_ok=True)
    suffix = f"-{index}" if index else ""
    return directory / f"{post_id}{suffix}.mp4"
