# threads-dlp

`threads-dlp` is a command-line tool for downloading videos from publicly viewable Threads posts. It runs on Linux, macOS, Windows, and Android through Termux. It uses Python and HTTP requests; Chrome, Selenium, and a Threads account are not required.

## Features

- Accepts Threads post links on `threads.com` and `threads.net`, including `/t/` and `/share/` links
- Finds the video attached to the requested post and selects its highest-resolution progressive MP4
- Streams downloads to disk and displays progress in an interactive terminal
- Creates the output folder when needed and avoids overwriting existing files
- Removes incomplete downloads when a network or disk error occurs

Only public posts are supported. Private, deleted, age-restricted, or otherwise unavailable posts cannot be downloaded. The tool does not log in or accept account credentials.

## Requirements

- Python 3.9 or newer
- An internet connection

## Install

Install from a repository checkout:

```bash
git clone https://github.com/nanaelie/threads-dlp.git
cd threads-dlp
python -m pip install .
```

## Termux on Android

Install Python in Termux, create an isolated environment, and install the package:

```bash
pkg update
pkg install python git
git clone https://github.com/nanaelie/threads-dlp.git
cd threads-dlp
python -m venv .venv
. .venv/bin/activate
python -m pip install .
```

To save into Android shared storage, grant Termux storage access once and choose the Downloads folder:

```bash
termux-setup-storage
threads-dlp --url "https://www.threads.com/@username/post/POST_ID" --output ~/storage/downloads/Threads
```

Termux storage access is optional. You can also save to a folder inside Termux's private files.

## Usage

```bash
threads-dlp --url "https://www.threads.net/@username/post/POST_ID"
```

Choose an output folder with `--output` or `-o`:

```bash
threads-dlp --url "https://www.threads.com/t/POST_ID" --output "./videos"
```

The saved filename uses the post ID, for example `POST_ID.mp4`. If that file already exists, the tool uses the next available name, such as `POST_ID-1.mp4`.

Show the available options or installed version:

```bash
threads-dlp --help
threads-dlp --version
```

## Troubleshooting

- **No public video was found:** check that the link points to a post containing a video and that it opens without signing in.
- **The video source returned an error:** video links can expire. Run the command again to extract a fresh link.
- **Permission denied:** choose a folder Termux can write to. For Android shared storage, run `termux-setup-storage` and use `~/storage/downloads`.
- **Threads changed its page:** extraction relies on data embedded in Threads' public web pages. A change to that page format can require an update to this tool.

## Project layout

```text
threads-dlp/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
└── threads_dlp/
    ├── __init__.py
    ├── __version__.py
    ├── cli.py
    ├── downloader.py
    ├── errors.py
    ├── extractor.py
    ├── http_client.py
    ├── make_out_path.py
    └── models.py
```

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
