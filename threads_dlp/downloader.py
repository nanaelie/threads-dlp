import requests
from tqdm import tqdm
from typing import Any
from os.path import basename
from threads_dlp.make_out_path import out_path

def downloader(url: str, src: str, output: str = None) -> Any:
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
    
    print(f"Envoi de la requête GET vers la source avec headers personnalisés")
    res = requests.get(src, headers=headers, stream=True)
    print(f"Statut HTTP reçu : {res.status_code}")

    e = res.headers.get('Content-Type').split('/')[1]
    print(f"Type de contenu détecté : {res.headers.get('Content-Type')} - Extension choisie : .{e}")

    if res.status_code == 206:
        outfile = out_path(url) + '.' + e
        if output is None:
            outfile_path = './' + outfile
        else:
            if output.endswith('/'):
                outfile_path = output + outfile
            else:
                outfile_path = output + '/' + outfile

        print(f"Enregistrement dans : {outfile_path}")

        total_size = int(res.headers.get('Content-Length', 0))
        chunk_size = 1024
        with open(outfile_path, "wb") as output_file, tqdm(
            total=total_size, unit='B', unit_scale=True, desc='Téléchargement', ncols=80
        ) as progress_bar:
            for chunk in res.iter_content(chunk_size=chunk_size):
                if chunk:
                    output_file.write(chunk)
                    progress_bar.update(len(chunk))

        print("Écriture du fichier terminée")
    else:
        print(f"Échec du téléchargement, code HTTP : {res.status_code}")


