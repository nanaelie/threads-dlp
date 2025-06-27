<br /><br /><br /><br />

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" />
  <img src="https://img.shields.io/badge/python-3.11-blue.svg" />
  <a href="https://github.com/nanaelie">
    <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20by%20nanaelie-ff69b4.svg" />
  </a>
</p>

<p align="center">
    <h1>threads-dlp</h1><br />
    <p><h2>threads-dlp</h2> est un outil en ligne de commande qui permet de télécharger des vidéos publiques depuis Threads à partir de leur URL.</p><br />
    <p>Développé en Python 3.11.2, il utilise Selenium pour l'extraction du lien vidéo, dottify pour simplifier l'accès aux données extraites, et tqdm pour afficher une barre de progression lors du téléchargement.</p><br />
    <p>N’hésite pas à laisser une ⭐ sur <a href="https://github.com/nanaelie/threads-dlp">GitHub</a>, ça aide énormément !</p>
</p>
<br />
## Sommaire
- [threads-dlp](#threads-dlp)
    - [Sommaire](#sommaire)
    - [Fonctionnalités](#fonctionnalités)
    - [Installation](#installation)
        - [1. Cloner le dépôt](#1._cloner_le_dépôt)
        - [2. Installation des dépendances](#2._installation_des_dépendances)
        - [3. Installation de l’outil](#3._installation_de_l’outil)
        - [4. Utilisation](#4._utilisation)
        - [5. Paramètres](#5._paramètres)

## Fonctionnalités

- Extraction automatique du lien source de la vidéo
- Téléchargement propre avec suivi en temps réel
- Interface en ligne de commande simple
- Téléchargement dans un dossier personnalisé
- Compatible avec Linux, macOS et Windows

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/nanaelie/threads-dlp.git
cd threads-dlp
```

### 2. Installation des dépendances

```bash
pip install -r requirements.txt
```

> Le module `tqdm` est utilisé pour la barre de progression.

### 3. Installation de l’outil

```bash
pip install .
```

> Cela installe toutes les dépendances et rend la commande `threads-dlp` disponible globalement (dans l’environnement virtuel).

### 4. Utilisation

Une fois installé, exécute simplement :

```bash
threads-dlp --url <lien_threads> -to <chemin_de_sortie>
```

### 5. Paramètres

| Option                | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| `--url` (obligatoire) | URL de la vidéo Threads                                           |
| `-to` / `--output`    | Dossier de sortie pour enregistrer la vidéo (défaut : `./`) |
| `-v` / `--version`    | Affiche la version de l’outil                                     |

#### Exemple

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

