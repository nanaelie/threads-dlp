import argparse
import os
import sys

from threads_dlp.downloader import downloader
from threads_dlp.extractor import extractor
from threads_dlp.__version__ import __version__

def main():
    parser = argparse.ArgumentParser(
        description="Télécharge une vidéo Threads à partir de son lien"
    )
    parser.add_argument(
        "--url", type=str, required=True,
        help="Lien vers la vidéo Threads"
    )
    parser.add_argument(
        "-to", "--output", type=str,
        help="Dossier où enregistrer la vidéo (par défaut : ./)"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"threads-dlp {__version__}"
    )

    args = parser.parse_args()
    url = args.url.strip()
    output_dir = args.output

    if output_dir and not os.path.exists(output_dir.strip()):
        try:
            os.makedirs(output_dir)
            print(f"Dossier de sortie créé : {output_dir}")
        except Exception as e:
            print(f"Impossible de créer le dossier '{output_dir}' : {e}")
            sys.exit(1)

    print("Extraction du lien direct de la vidéo...")
    response = extractor(url)

    if response.error:
        error(content)
        sys.exit(1)

    source_url = response.content
    print("Lien direct trouvé.")
    print("Téléchargement en cours...")
    try:
        downloader(url, source_url, output=output_dir)
        print("Téléchargement terminé avec succès.")
    except Exception as e:
        print(f"Échec du téléchargement : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
