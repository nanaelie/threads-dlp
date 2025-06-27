<br /><br /><br /><br />

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.1-blue.svg" />
  <img src="https://img.shields.io/badge/python-3.11-blue.svg" />
  <a href="https://github.com/nanaelie">
    <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20by%20nanaelie-ff69b4.svg" />
  </a>
</p>

<h1 align="center"><a href="#">threads-dlp</a></h1>

<p align="center"><i>threads-dlp</i> est un outil en ligne de commande qui permet de télécharger des vidéos<br />publiques depuis Threads à partir de leur URL.</p>
<p align="center">Développé en Python 3.11.2, il utilise <code>Selenium</code> pour l'extraction du lien vidéo, <code>dottify</code> pour simplifier<br />l'accès aux données extraites, et <code>tqdm</code> pour afficher une barre de progression lors du téléchargement.</p>
<p align="center">N’hésite pas à laisser une ⭐ sur <a href="https://github.com/nanaelie/threads-dlp">GitHub</a>, ça aide énormément !</p>

## Sommaire
- [threads-dlp](#threads-dlp)
  - [Sommaire](#sommaire)
  - [Fonctionnalités](#fonctionnalités)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
    - [1. Paramètres](#1-paramètres)
    - [2. Exemple](#2-exemple)
  - [Structure du projet](#structure-du-projet)
  - [Contribution](#contribution)

## Fonctionnalités

- Extraction automatique du lien source de la vidéo
- Téléchargement propre avec suivi en temps réel
- Interface en ligne de commande simple
- Téléchargement dans un dossier personnalisé
- Compatible avec Linux, macOS et Windows

## Installation

```bash
pip install threads-dlp
```

## Utilisation

Une fois installé, exécute simplement :

```bash
threads-dlp --url <lien_threads> -to <chemin_de_sortie>
```

### 1. Paramètres

| Option                | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| `--url` (obligatoire) | URL de la vidéo Threads                                           |
| `-to` / `--output`    | Dossier de sortie pour enregistrer la vidéo (défaut : `./`) |
| `-v` / `--version`    | Affiche la version de l’outil                                     |

### 2. Exemple

```bash
threads-dlp --url https://www.threads.net/t/Cq8kz123Xy -to ./mes_videos
```

## Structure du projet

```
threads-dlp/
├── CONTRIBUTING.md     # Guide pour contribuer au projet
├── LICENSE             # Licence Apache 2.0 pour l’utilisation et la distribution
├── pyproject.toml      # Configuration du projet (PEP 621) avec dépendances, version, etc.
├── README.md           # Documentation principale du projet
├── requirements.txt    # Dépendances du projet (optionnel si pyproject.toml suffit)
├── setup.py            # Ancien script d’installation (remplacé par pyproject.toml)
└── threads_dlp/        # Dossier principal contenant le code source
    ├── __init__.py         # Initialise le package Python
    ├── __version__.py      # Contient la version actuelle du projet
    ├── cli.py              # Point d’entrée de la CLI (command-line interface)
    ├── downloader.py       # Télécharge la vidéo depuis une URL Threads, avec `tqdm`
    ├── extractor.py        # Extrait les données Threads avec Selenium
    ├── make_out_path.py    # Génère un nom de fichier local à partir du lien Threads
    └── __pycache__/        # Dossier auto-généré par Python (à ignorer dans Git)
```

## Contribution

Les contributions sont les bienvenues !  
Si tu souhaites corriger un bug, améliorer une fonctionnalité ou proposer une idée, merci de consulter le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour connaître les bonnes pratiques à suivre.

Même les petites améliorations comptent.
