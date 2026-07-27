# Document d'Analyse Architecturelle : Modularisation par Apps ("Django-like") dans FastAPI

## 1. Contexte et Objectifs

L'objectif de cette étude et réorganisation est de faire évoluer le projet **`playground/fastapi-python-boilerplate`** d'une structure horizontale par couches (Package by Layer) vers une **architecture modulaire par domaines / "apps" (Package by Feature / Domain-Driven Design)**, en s'inspirant de la logique des applications Django et de la structure validée sur le projet de référence `learning/datascientest/projects/_fastapi-react-cryptobot/backend/app`.

### Problématique de la structure initiale
Initialement, le projet présentait un découpage par responsabilité technique :
* `api/routes/` pour la couche contrôleur/routing
* `services/` pour la logique métier
* `db/` pour la couche d'accès aux données (modèles ORM et session DB)

**Inconvénients majeurs :**
1. **Dispersion du code métier :** Les composants d'une même fonctionnalité (ex: les pages web ou les données de démonstration) sont répartis dans des dossiers distants.
2. **Couplage fort et faible lisibilité :** Modifier ou supprimer un module nécessite d'intervenir simultanément dans plusieurs sous-dossiers isolés.
3. **Difficulté de scalabilité :** L'ajout de nouvelles fonctionnalités complexes (comme la gestion de contenus multi-médias : posts, audio, vidéo) alourdit indéfiniment les dossiers racine `db/models.py`, `services/`, etc.

---

## 2. Comparatif des Architectures

| Critère | Architecture Initiale (Package by Layer) | Architecture Cible (Django-like Apps) |
| :--- | :--- | :--- |
| **Organisation** | Par type de fichier (`routes/`, `services/`, `models/`) | Par domaine fonctionnel (`pages/`, `data/`, `content/`) |
| **Cohésion** | Faible (code d'un domaine éclaté dans tout le projet) | Forte (chaque app contient ses `models`, `schemas`, `services`, `router`) |
| **Découplage** | Difficile d'isoler ou d'extraire une fonctionnalité | Isolation complète ; suppression d'une app en supprimant son dossier |
| **Évolutivité** | Risque de fichiers "fourre-tout" (`db/models.py` géant) | Scalabilité horizontale illimitée via l'ajout de nouvelles apps |
| **Alignement Monorepo** | Hétérogène vis-à-vis des autres projets | Homogène avec `_fastapi-react-cryptobot` et les patterns entreprise |

---

## 3. Architecture Cible Détaillée

```text
playground/fastapi-python-boilerplate/
├── app/                             # Package Python principal de l'application
│   ├── __init__.py
│   │
│   ├── core/                        # SOCLE INFRASTRUCTURE & CONFIGURATION
│   │   ├── __init__.py
│   │   ├── config.py                # Pydantic BaseSettings (variables d'environnement, S3, DB)
│   │   ├── database.py              # Engine, SessionLocal, Base SQLAlchemy, get_db()
│   │   └── security.py              # Auth JWT, hashing et vérification des mots de passe
│   │
│   ├── shared/                      # UTILS & PATTERNS TRANSVERSAUX
│   │   ├── __init__.py
│   │   ├── models/                  # Modèles SQLAlchemy de base (TimestampedModel, UUIDModel)
│   │   ├── schemas/                 # Schémas Pydantic génériques (Pagination, Reponses Standard)
│   │   └── storage/                 # Adapter Pattern pour la gestion des fichiers médias
│   │       ├── base.py              # StorageProvider (Interface abstraite / Protocol)
│   │       ├── local.py             # Stockage sur système de fichier local (environnement dev)
│   │       └── s3.py                # Stockage Cloud S3 / GCS (environnement prod)
│   │
│   ├── pages/                       # APP 1 : RENDU WEB & VITRINE (Jinja2 SSR)
│   │   ├── __init__.py
│   │   ├── data.py                  # Données statiques & fallbacks (ex: pages_data.py)
│   │   ├── models.py                # Modèles DB (ProjectConfig, DesignToken, Module, ChangelogRelease)
│   │   ├── services.py              # Logique d'agrégation des données pour le rendu HTML
│   │   └── router.py                # APIRouter pour les pages HTML (GET /, GET /modules, etc.)
│   │
│   ├── data/                        # APP 2 : API DATA (Endpoints JSON)
│   │   ├── __init__.py
│   │   ├── models.py                # Modèles DB spécifiques aux données d'analyse
│   │   ├── schemas.py               # Schémas Pydantic de validation Data API
│   │   ├── services.py              # Logique métier d'analyse ou de traitement de données
│   │   └── router.py                # APIRouter JSON (/api/data)
│   │
│   ├── content/                     # APP 3 : GESTION DE CONTENUS MULTI-MÉDIAS (Domaine Extensible)
│   │   ├── __init__.py
│   │   ├── models.py                # Modèle parent polymorphe (Content, ContentType)
│   │   ├── schemas.py               # Schémas d'entrée/sortie Pydantic & Discriminators
│   │   ├── router.py                # Router principal du domaine agglomérant les sous-domaines
│   │   │
│   │   ├── posts/                   # Sous-domaine : Articles & Posts Texte
│   │   │   ├── __init__.py
│   │   │   ├── models.py            # Modèle Post (Joined Table Inheritance depuis Content)
│   │   │   ├── services.py          # Traitement du texte, parsing Markdown, SEO
│   │   │   └── router.py            # Endpoints API /api/v1/content/posts
│   │   │
│   │   ├── audio/                   # Sous-domaine : Fichiers Audio & Podcasts
│   │   │   ├── __init__.py
│   │   │   ├── models.py            # Modèle AudioContent (durée, bitrate, transcript)
│   │   │   ├── services.py          # Traitement audio, FFmpeg, Speech-To-Text
│   │   │   └── router.py            # Endpoints /api/v1/content/audio (Upload & Streaming)
│   │   │
│   │   └── video/                   # Sous-domaine : Vidéos & Transcodage
│   │       ├── __init__.py
│   │       ├── models.py            # Modèle VideoContent (résolutions, thumbnails, HLS)
│   │       ├── services.py          # Encodage HLS, génération de vignettes
│   │       └── router.py            # Endpoints /api/v1/content/video (Upload & HLS)
│   │
│   └── main.py                      # POINT D'ENTRÉE FASTAPI
│
├── public/                          # Fichiers publics statiques
├── static/                          # Assets (CSS, JS, images)
├── templates/                       # Templates HTML Jinja2 (pages/ & components/)
├── docs/                            # Documentation technique et analyses
│   └── analyses/
│       └── architecture_modulaire_apps.md
├── scripts/                         # Scripts utilitaires
├── pyproject.toml / requirements.txt
└── README.md
```

---

## 4. Analyse Approfondie des Composants Majeurs

### 4.1. L'App `pages` (Server-Side Rendering & Interface Web)
L'app `pages` encapsule l'ensemble du rendu HTML serveur (SSR) via Jinja2 :
* **[app/pages/models.py](file:///Users/awf/workspace/playground/fastapi-python-boilerplate/app/pages/models.py)** : Contient les entités de configuration du site (`ProjectConfig`), des tokens de design (`DesignToken`), des cartes de modules (`Module`), et des changelogs (`ChangelogRelease`).
* **[app/pages/services.py](file:///Users/awf/workspace/playground/fastapi-python-boilerplate/app/pages/services.py)** : Fournit des fonctions sécurisées interrogeant la base de données avec bascule automatique sur les fallbacks de `app/pages/data.py` en cas d'absence de données.
* **[app/pages/router.py](file:///Users/awf/workspace/playground/fastapi-python-boilerplate/app/pages/router.py)** : Expose les routes Web (`/`, `/modules`, `/design-system`, `/changelog`, `/documentation`).

### 4.2. Le Domaine `content` et le Polymorphisme ORM
Pour gérer de manière très flexible les différents types de contenus (texte, audio, vidéo), l'architecture s'appuie sur le pattern **Joined Table Inheritance** de SQLAlchemy :

```python
# app/content/models.py
import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from app.core.database import Base

class ContentType(str, enum.Enum):
    POST = "post"
    AUDIO = "audio"
    VIDEO = "video"

class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True)
    type = Column(Enum(ContentType), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "content",
    }
```

Chaque sous-domaine étend cette entité dans son propre fichier `models.py` (ex: `app/content/audio/models.py` avec `AudioContent`), conservant une table SQL dédiée pour ses métadonnées spécifiques sans polluer la table générique `contents`.

### 4.3. Stockage des Médias : Adapter Pattern (`app/shared/storage/`)
Afin que les sous-modules `audio` et `video` ne dépendent pas directement du système de fichier local ou d'un fournisseur cloud spécifique, le stockage s'articule autour d'une classe abstraite :

```python
# app/shared/storage/base.py
from abc import ABC, abstractmethod
from typing import BinaryIO

class StorageProvider(ABC):
    @abstractmethod
    async def upload(self, file_obj: BinaryIO, filename: str, folder: str) -> str:
        """Upload un fichier et retourne son URL ou chemin d'accès"""
        pass

    @abstractmethod
    async def delete(self, file_path: str) -> bool:
        """Supprime un fichier stocké"""
        pass
```

---

## 5. Matrice de Mapping pour la Migration

| Fichier d'origine | Emplacement cible | Rôle dans la nouvelle architecture |
| :--- | :--- | :--- |
| `db/database.py` | `app/core/database.py` | Gestion de la connexion PostgreSQL, Engine & Session |
| `db/models.py` | Réparti dans `app/pages/models.py`, `app/data/models.py`, `app/content/models.py` | Modèles ORM isolés par domaine |
| `services/pages_service.py` | `app/pages/services.py` | Service d'agrégation de données pour l'UI Jinja2 |
| `api/routes/pages_data.py` | `app/pages/data.py` | Données statiques de fallback |
| `api/routes/web.py` | `app/pages/router.py` | Router principal des pages Web Jinja2 |
| `api/routes/data.py` | `app/data/router.py` | Endpoints JSON de l'API Data |
| `main.py` | `app/main.py` | Point d'entrée FastAPI avec enregistrement des routers |

---

## 6. Conclusion et Prochaines Étapes

Cette architecture offre le meilleur compromis entre la simplicité de prise en main d'un framework web moderne (FastAPI) et la rigueur d'organisation éprouvée des frameworks d'entreprise (Django).

**Prochaines étapes recommandées :**
1. Création de la structure de dossiers `app/` avec ses sous-modules.
2. Déplacement et refactorisation des fichiers selon la matrice de migration.
3. Mise à jour des imports dans `app/main.py`.
4. Tests de non-régression sur l'application.
