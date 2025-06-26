import requests
from typing import Any
from os.path import basename
from make_out_path import out_path

def downloader(url: str, src: str) -> Any:
    path = src.split('https://instagram.foua4-1.fna.fbcdn.net')[1]
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "identity;q=1, *;q=0",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "i",
        "Range": "bytes=0-",
        "Referer": f"{src}",
        "Sec-Ch-UA": "'Google Chrome';v='137', 'Chromium';v='137', 'Not/A)Brand';v='24",
        "Sec-Ch-UA-Mobile": "?0",
        "Sec-Ch-ua-Platform": "Linux",
        "Sec-Fetch-Dest": "video",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "user-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    }
    
    res = requests.get(src, headers=headers)
    e = res.headers.get('Content-Type').split('/')[1]
    
    if res.status_code == 206:
        outfile = out_path(url) + '.' + e
        print("Saving to ", outfile)
        output_file = open(outfile, "wb")
        output_file.write(res.content)
        output_file.close()
        print('done!')
    else:
        print(res.status_code)
    
