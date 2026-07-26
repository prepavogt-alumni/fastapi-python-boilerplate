# Runbook Opérationnel — FastAPI + Neon PostgreSQL sur Vercel

Ce **Runbook** fournit toutes les instructions opérationnelles indispensables pour démarrer, administrer, tester, dépanner et déployer l'application `fastapi-python-boilerplate`.

---

## 🎯 1. Prérequis & Environnement

- **Python** : `>= 3.10`
- **Gestionnaire de dépendances** : `pip` ou `uv`
- **Base de données** : Neon PostgreSQL (Instance Cloud Serverless)
- **Hébergeur Web** : Vercel (Serverless Functions)

---

## 🚀 2. Initialisation Rapide (Environnement Local)

### Étape 2.1 : Cloner et préparer l'environnement virtuel

```bash
# Se placer dans le dossier du projet
cd playground/fastapi-python-boilerplate

# Créer et activer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
pip install httpx  # Nécessaire pour l'exécution des scripts de test API
```

### Étape 2.2 : Configuration des variables d'environnement (`.env`)

Assurez-vous qu'un fichier `.env` existe à la racine du projet avec les variables fournies par Neon :

```env
DATABASE_URL=postgresql://neondb_owner:YOUR_PASSWORD@ep-billowing-art-awajjp3s-pooler.c-12.us-east-1.aws.neon.tech/fastapi_db?channel_binding=require&sslmode=require
DATABASE_URL_UNPOOLED=postgresql://neondb_owner:YOUR_PASSWORD@ep-billowing-art-awajjp3s.c-12.us-east-1.aws.neon.tech/fastapi_db?sslmode=require
```

---

## ⚙️ 3. Procédures Opérationnelles Courantes

### 🔹 Tâche 3.1 : Créer une nouvelle base de données Neon

Pour provisionner une nouvelle base (ex: `dev_db` ou `prod_db`) :

```bash
python scripts/create_db.py <nom_de_la_base>
```
*Note : Le script bascule automatiquement sur l'URL `DATABASE_URL_UNPOOLED` en mode `AUTOCOMMIT`.*

### 🔹 Tâche 3.2 : Vérifier la connexion et la santé de la Base de Données

Pour vérifier la connectivité et la création automatique de la table `items` :

```bash
python scripts/test_db.py
```
**Résultat attendu :**
```text
1. ✅ Connexion réussie ! Version PostgreSQL : PostgreSQL 17.10...
2. ✅ Vérification / Création des tables...
3. ✅ Test d'insertion et de lecture...
🎉 TOUS LES TESTS DE BASE DE DONNÉES SONT RÉUSSIS !
```

### 🔹 Tâche 3.3 : Lancer les tests d'intégration API

Pour simuler les requêtes HTTP locales vers les endpoints FastAPI :

```bash
python scripts/test_api.py
```

### 🔹 Tâche 3.4 : Démarrer le serveur de développement local

```bash
uvicorn main:app --reload --port 8000
```
- **Documentation interactive Swagger UI** : [http://localhost:8000/docs](http://localhost:8000/docs)
- **Interface Web HTML** : [http://localhost:8000/](http://localhost:8000/)
- **Status API** : [http://localhost:8000/api/status](http://localhost:8000/api/status)

---

## 🚢 4. Procédure de Déploiement Production (Vercel)

### Déploiement automatique via Git

```bash
git add .
git commit -m "feat: infrastructure & database configuration"
git push origin main
```
1. Vercel détecte automatiquement le push et lance le build.
2. Vercel installe les paquets listés dans `requirements.txt`.
3. L'intégration Neon sur Vercel injecte automatiquement les clés d'accès `DATABASE_URL` et `POSTGRES_URL`.

### Tester en local avec le CLI Vercel

```bash
# Installer le CLI Vercel si besoin
npm install -g vercel

# Lancer l'émulateur d'environnement Vercel
vercel dev
```

---

## 🔍 5. Guide de Dépannage (Troubleshooting)

| Symptôme / Erreur | Cause probable | Solution opérationnelle |
|---|---|---|
| `ModuleNotFoundError: No module named 'sqlalchemy'` | L'environnement virtuel n'est pas activé ou les paquets ne sont pas installés. | Exécuter `source .venv/bin/activate` puis `pip install -r requirements.txt`. |
| `psycopg2.OperationalError: SSL error` | Mode SSL manquant dans la chaîne de connexion Neon. | Ajouter `?sslmode=require` à la fin de la variable `DATABASE_URL`. |
| `OperationalError: cannot insert inside a transaction` lors de `CREATE DATABASE` | tentative d'exécution de `CREATE DATABASE` au travers d'un pooler de connexion ou d'un bloc transactionnel. | Utiliser `DATABASE_URL_UNPOOLED` avec `isolation_level="AUTOCOMMIT"`. |
| `database: not configured` dans `/api/status` | Les variables d'environnement `DATABASE_URL` ou `POSTGRES_URL` ne sont pas chargées. | Vérifier la présence du fichier `.env` en local ou les clés dans le dashboard Vercel. |
| `Connection timed out` sur Vercel Serverless | Connexion fermée par Neon après inactivité. | S'assurer que `pool_pre_ping=True` est présent dans `create_engine()` (`db/database.py`). |
