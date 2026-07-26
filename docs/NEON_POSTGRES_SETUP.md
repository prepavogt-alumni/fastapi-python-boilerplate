# Guide d'Intégration Neon PostgreSQL & Architecture FastAPI

Ce document détaille la restructuration de l'application FastAPI selon le principe de **Séparation des Responsabilités (Separation of Concerns)** ainsi que la procédure complète d'intégration de la base de données **Neon PostgreSQL** sur Vercel.

---

## 📂 1. Architecture du Projet

Le projet a été organisé pour séparer clairement les vues (HTML), la logique métier/routes API, la couche de données (ORM SQLAlchemy) et les scripts d'administration.

```text
fastapi-python-boilerplate/
├── main.py                     # Point d'entrée principal (Configuration FastAPI & Routers)
├── .env                        # Variables d'environnement locales (Neon PostgreSQL)
├── pyproject.toml              # Dépendances Python du projet
├── requirements.txt            # Dépendances pour le runtime Vercel
├── api/
│   ├── __init__.py
│   └── routes/
│       ├── __init__.py
│       ├── data.py             # Endpoints API (/api/data, /api/items, /api/status)
│       └── web.py              # Endpoint Web servant la page HTML racine (/)
├── db/
│   ├── __init__.py
│   ├── database.py             # Configuration de la connexion SQLAlchemy & Session (get_db)
│   └── models.py               # Modèles de données ORM (Table `items`)
├── templates/
│   └── index.html              # Template HTML / CSS séparé du code Python
├── docs/
│   └── NEON_POSTGRES_SETUP.md  # La présente documentation
└── scripts/
    ├── create_db.py            # Script de création d'une nouvelle base de données Neon
    ├── test_db.py              # Script de test de connexion et d'opérations en BDD
    └── test_api.py             # Script de test d'intégration des endpoints FastAPI
```

---

## 🗄️ 2. Configuration & Connexion Neon PostgreSQL

### Variables d'environnement (`.env`)

Lorsque vous intégrez Neon sur Vercel, les variables d'environnement suivantes sont automatiquement fournies :

```env
# Connexion principale (PGBouncer Pooler - Serverless)
DATABASE_URL=postgresql://neondb_owner:YOUR_PASSWORD@ep-billowing-art-awajjp3s-pooler.c-12.us-east-1.aws.neon.tech/fastapi_db?channel_binding=require&sslmode=require

# Connexion Directe / Unpooled (Nécessaire pour les DDL comme CREATE DATABASE)
DATABASE_URL_UNPOOLED=postgresql://neondb_owner:YOUR_PASSWORD@ep-billowing-art-awajjp3s.c-12.us-east-1.aws.neon.tech/fastapi_db?sslmode=require

# Variables Vercel Postgres
POSTGRES_URL=postgresql://...
POSTGRES_URL_NON_POOLING=postgresql://...
POSTGRES_USER=neondb_owner
POSTGRES_HOST=ep-billowing-art-awajjp3s-pooler.c-12.us-east-1.aws.neon.tech
POSTGRES_PASSWORD=YOUR_PASSWORD
POSTGRES_DATABASE=fastapi_db
```

### Couche de connexion (`db/database.py`)

- Utilise `pool_pre_ping=True` pour gérer automatiquement la déconnexion inhérente aux environnements Serverless.
- Fournit la fonction génératrice `get_db()` utilisée avec la dépendance `Depends(get_db)` dans FastAPI.

---

## 🆕 3. Créer une nouvelle base de données personnalisée

Par défaut, Neon fournit une base nommée `neondb`. Pour créer et utiliser une base personnalisée (ex: `fastapi_db`) :

### Option A : Via le script Python automatisé
Exécutez la commande suivante :
```bash
python scripts/create_db.py fastapi_db
```
*Remarque : Ce script se connecte en mode `AUTOCOMMIT` sur le port direct (`DATABASE_URL_UNPOOLED`) pour exécuter l'instruction `CREATE DATABASE`.*

### Option B : Via la Console Neon (Dashboard Web)
1. Allez sur [Neon.tech](https://console.neon.tech/).
2. Sélectionnez votre projet > Onglet **Databases**.
3. Cliquez sur **New Database**, nommez-la `fastapi_db` et validez.
4. Mettez à jour le nom de la base dans le fichier `.env` ou dans le dashboard Vercel (**Settings > Environment Variables**).

---

## 🛠️ 4. Scripts d'administration et de test

Des scripts prêts à l'emploi sont mis à disposition dans le dossier `scripts/` :

### 1. Script de création de base (`scripts/create_db.py`)
Crée une nouvelle base PostgreSQL sur votre cluster Neon.
```bash
python scripts/create_db.py <nom_de_la_base>
```

### 2. Script de test de connexion BDD (`scripts/test_db.py`)
Teste la connexion au serveur Neon, vérifie la création des tables et effectue un test d'écriture/lecture.
```bash
python scripts/test_db.py
```

### 3. Script de test d'intégration API (`scripts/test_api.py`)
Valide l'ensemble des points de terminaison de l'application (`GET /api/status`, `GET /api/data`, `POST /api/items`, `GET /`).
```bash
python scripts/test_api.py
```

---

## 🚀 5. Exécution Locale et Déploiement

### Exécution locale
```bash
# 1. Créer l'environnement virtuel et installer les dépendances
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Tester l'API et la base de données
python scripts/test_db.py
python scripts/test_api.py

# 3. Lancer le serveur uvicorn
uvicorn main:app --reload
```

### Déploiement Vercel
1. Commitez et poussez votre code sur GitHub (`git push`).
2. Sur Vercel, l'intégration Neon injecte automatiquement vos variables `DATABASE_URL` / `POSTGRES_URL`.
3. Le fichier `requirements.txt` sera lu par Vercel pour installer `fastapi`, `sqlalchemy` et `psycopg2-binary`.
