<br /><br /><br /><br />

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" />
  <img src="https://img.shields.io/badge/python-3.11-blue.svg" />
  <a href="https://github.com/nanaelie">
    <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20by%20nanaelie-ff69b4.svg" />
  </a>
</p>

# threads-dlp

**threads-dlp** est un outil en ligne de commande qui permet de télécharger des vidéos publiques depuis Threads à partir de leur URL.

Développé en Python 3.11.2, il utilise Selenium pour l'extraction du lien vidéo et `tqdm` pour afficher une barre de progression lors du téléchargement.

N’hésite pas à laisser une ⭐ sur [GitHub](https://github.com/nanaelie/threads-dlp), ça aide énormément !

## Sommaire
- [threads-dlp](#)
    - [Sommaire](#sommaire)
    - [Fonctionnalités](#fonctionnalités)
    - [Installation](#installation)
        - [1. Cloner le dépôt](#1._loner_le_dépôt)
        - [2. Créer un environnement virtuel_(recommandé)](#2._créer_un_environnement_virtuel_(recommandé))
        - [3. Installation des dépendances](#3._installation_des_dépendances)
        - [4. Installation de l’outil](#4._installation_de_l’outil)
        - [5. Utilisation](#5._utilisation)
        - [6. Paramètres](#6._paramètres)

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

### 2. Créer un environnement virtuel (recommandé)

Développement testé avec **Python 3.11.2**.  
Il est fortement conseillé d’utiliser un **environnement virtuel**.

```bash
# Création
python3.11 -m venv .venv

# Activation (Linux/macOS)
source .venv/bin/activate

# Activation (Windows)
.venv\Scripts\activate
```

### 3. Installation des dépendances

```bash
pip install -r requirements.txt
```

> Le module `tqdm` est utilisé pour la barre de progression.

### 4. Installation de l’outil

```bash
pip install .
```

> Cela installe toutes les dépendances et rend la commande `threads-dlp` disponible globalement (dans l’environnement virtuel).

### 5. Utilisation

Une fois installé, exécute simplement :

```bash
threads-dlp --url <lien_threads> -to <chemin_de_sortie>
```

### 6. Paramètres

| Option                | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| `--url` (obligatoire) | URL de la vidéo Threads                                           |
| `-to` / `--output`    | Dossier de sortie pour enregistrer la vidéo (défaut : `./videos`) |
| `-v` / `--version`    | Affiche la version de l’outil                                     |

#### Exemple

```bash
threads-dlp --url https://www.threads.net/t/Cq8kz123Xy -to ./mes_videos
```

## Structure du projet

```
threads-dlp/
├── LICENSE             # Licence Apache 2.0 pour l’utilisation et la distribution du projet
├── README.md           # Documentation principale du projet
├── requirements.txt    # Liste des dépendances Python à installer
├── setup.py            # Script d'installation du paquet (`pip install .`)
├── CONTRIBUTING.md     # Guide pour contribuer au projet 
└── threads-dlp         # Dossier principal contenant le code source
    ├── downloader.py   # Télécharge une vidéo à partir de son lien direct avec barre de progression
    ├── extractor.py    # Extrait le lien source de la vidéo Threads à partir d’une URL
    ├── make_out_path.py# Génère un nom de fichier unique basé sur l’URL Threads
    ├── threads_dlp.py  # Script principal de la CLI (point d’entrée)
    ├── __version__.py  # Contient la version actuelle de l’outil
    ├── __init__.py     # Fichier d’initialisation du module Python
    └── __pycache__/    # Dossier généré automatiquement par Python (à ignorer dans Git)
```

## Contribution

Les contributions sont les bienvenues !  
Si tu souhaites corriger un bug, améliorer une fonctionnalité ou proposer une idée, merci de consulter le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour connaître les bonnes pratiques à suivre.

Même les petites améliorations comptent.

