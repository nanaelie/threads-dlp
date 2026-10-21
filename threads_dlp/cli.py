import argparse
import sys

from threads_dlp.__version__ import __version__
from threads_dlp.downloader import downloader
from threads_dlp.errors import ThreadsDlpError
from threads_dlp.extractor import extractor


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="threads-dlp",
        description="Download a video from a public Threads post.",
    )
    parser.add_argument("--url", required=True, help="URL of a Threads post or share link")
    parser.add_argument("-o", "--output", default=".", help="Folder where the video is saved (default: current folder)")
    parser.add_argument("-v", "--version", action="version", version=f"threads-dlp {__version__}")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        media = extractor(args.url)
        output_path = downloader(media, args.output)
    except ThreadsDlpError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Downloaded: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
