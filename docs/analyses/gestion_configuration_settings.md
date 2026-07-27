# Document d'Analyse : Gestion de la Configuration & Settings dans FastAPI

## 1. Contexte et Enjeux

Dans la conception d'applications web modernes en Python / FastAPI, la gestion de la configuration (variables d'environnement, secrets, paramètres de base de données, paramètres de stockage) est un composant stratégique.

Cette étude analyse la meilleure localisation et les meilleures pratiques de conception pour le système de configuration du projet **`playground/fastapi-python-boilerplate`**.

---

## 2. Comparatif des Approches de Placement du Module Config

### Option A : Configuration à la Racine (`/config/settings.py`)
Inspirée de la structure par défaut de Django (`myproject/settings.py` au même niveau que les apps).

* **Avantages :** Séparation visuelle entre le code source applicatif (`app/`) et les paramètres globaux.
* **Inconvénients majeurs :**
  1. **Rupture d'encapsulation :** Le package Python `app/` n'est plus autonome. Il dépend d'un dossier situé hors de sa portée d'importation standard.
  2. **Problèmes d'importation :** Nécessite l'ajout explicite du répertoire racine dans le `PYTHONPATH` (`from config.settings import settings`).
  3. **Complexité de conteneurisation :** Dans un Dockerfile ou une fonction serverless (Vercel / AWS Lambda), le déploiement doit embarquer deux répertoires racine au lieu d'un package applicatif unique.

### Option B : Configuration dans le Socle Core (`app/core/config.py`) [RECOMMANDÉE]
Convention standard de l'écosystème FastAPI (recommandée par Sebastián Ramírez / Tiangolo et utilisée dans les templates officiels FastAPI).

* **Avantages :**
  1. **Autonomie complète du package :** Le dossier `app/` constitue une unité d'exécution autonome.
  2. **Imports propres et explicites :** `from app.core.config import settings` (ou `from app.config.settings import settings`).
  3. **Respect de la Clean Architecture :** Le module `core` se situe au niveau le plus bas du graphe de dépendances (infrastructure), pouvant être consommé par toutes les apps métier (`pages`, `data`, `content`).
  4. **Facilité de test :** Possibilité d'injecter des configurations de test isolées sans polluer l'environnement global.

---

## 3. Conformité aux Meilleures Pratiques de Génie Logiciel

### 3.1. Manifeste 12-Factor App (Factor III : Config)
Le principe III de la méthodologie *12-Factor App* stipule que la configuration doit être strictement séparée du code et injectée via des variables d'environnement.

En combinant `app/core/config.py` avec la bibliothèque **`pydantic-settings`**, l'application garantit :
* La lecture automatique des fichiers `.env` et des variables d'environnement système.
* Le typage strict et la validation des configurations (ex: conversion automatique des types de chaînes en objets `PostgresDsn`, `HttpUrl`, `int` ou `bool`).
* L'échec immédiat au démarrage (*Fail-Fast*) si une variable obligatoire (ex: `DATABASE_URL`) est absente ou mal formatée.

---

## 4. Spécification Technique de l'Implémentation

```python
# app/core/config.py
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Infos Projet
    PROJECT_NAME: str = "FastAPI + Postgres Boilerplate"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "Production"
    DEBUG: bool = False
    
    # Sécurité
    SECRET_KEY: str = "default-dev-secret-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Base de données
    DATABASE_URL: Optional[str] = None
    POSTGRES_URL: Optional[str] = None
    
    # Stockage Médias
    STORAGE_PROVIDER: str = "local" # "local" ou "s3"
    S3_BUCKET_NAME: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def sqlalchemy_database_url(self) -> Optional[str]:
        url = self.DATABASE_URL or self.POSTGRES_URL
        if url and url.startswith("postgres://"):
            return url.replace("postgres://", "postgresql://", 1)
        return url

settings = Settings()
```

---

## 5. Refactorisation Prévue des Composants

1. **`app/core/database.py`** :
   Consommera `settings.sqlalchemy_database_url` au lieu d'appeler manuellement `os.getenv()`.
2. **`app/main.py`** :
   Utilisera `settings.PROJECT_NAME` et `settings.VERSION` pour instancier l'application FastAPI.
3. **`app/pages/services.py`** :
   Affichera dynamiquement `settings.ENVIRONMENT` et les métadonnées globales.

---

## 6. Conclusion

L'adoption de **`app/core/config.py`** combinée à **Pydantic Settings** garantit une architecture conforme aux plus hauts standards du dev logiciel : haute cohésion, typage strict, sécurité, et portabilité parfaite du package `app/`.
