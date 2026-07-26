# Generic FastAPI + PostgreSQL Boilerplate Seed Data

_AUTH = [
    ("POST", "/api/v1/auth/register", "S'inscrire (Nouveau compte)"),
    ("POST", "/api/v1/auth/login", "Se connecter (Obtenir JWT)"),
    ("GET",  "/api/v1/auth/me", "Profil utilisateur courant"),
    ("POST", "/api/v1/auth/refresh", "Rafraîchir le token JWT"),
]

_DATABASE_ENDPOINTS = [
    ("GET",  "/api/data", "Obtenir les données exemple depuis PostgreSQL"),
    ("GET",  "/api/items/{item_id}", "Obtenir un élément spécifique par ID"),
    ("POST", "/api/items", "Créer un nouvel élément dans PostgreSQL"),
    ("GET",  "/api/status", "Vérifier la connexion à la base de données"),
]

_SYSTEM_ENDPOINTS = [
    ("GET",  "/", "Page d'accueil de l'application (SSR)"),
    ("GET",  "/modules", "Catalogue des modules fonctionnels"),
    ("GET",  "/apps", "Référence des points de terminaison API"),
    ("GET",  "/design-system", "Tokens et composants du Design System"),
    ("GET",  "/documentation", "Documentation et guide d'architecture"),
    ("GET",  "/changelog", "Historique des versions du boilerplate"),
    ("GET",  "/docs", "Documentation interactive Swagger UI"),
    ("GET",  "/redoc", "Documentation alternative ReDoc"),
]

_CLIENT_PORTAL = []
_MANAGER_PORTAL = []

_COLORS_BRAND = [
    ("Primary", "#0070f3", "--primary-color · #0070f3 (Vercel Blue)"),
    ("Primary Light", "#e6f0fe", "--primary-light · #e6f0fe"),
    ("Secondary", "#7928ca", "--secondary-color · #7928ca (Purple)"),
    ("Secondary Light", "#f3e8ff", "--secondary-light · #f3e8ff"),
    ("Accent Vert", "#10b981", "--accent-color · #10b981 (Emerald)"),
    ("Black", "#000000", "--black · #000000"),
]

_COLORS_FUNCTIONAL = [
    ("Success", "#10b981", "--success-color · #10b981"),
    ("Danger", "#ef4444", "--danger-color · #ef4444"),
    ("Warning", "#f59e0b", "--warning-color · #f59e0b"),
    ("Info", "#3b82f6", "--info-color · #3b82f6"),
]

_COLORS_SURFACE = [
    ("Body BG", "#f8fafc", "--body-bg · #f8fafc"),
    ("Body Color", "#0f172a", "--body-color · #0f172a"),
    ("Text Muted", "#64748b", "--text-muted · #64748b"),
    ("Border", "#e2e8f0", "--border-color · #e2e8f0"),
    ("Card BG", "#ffffff", "--card-bg · #ffffff"),
    ("Footer BG", "#0f172a", "--footer-bg · #0f172a"),
]

_SHADOWS = [
    ("--shadow-sm", "0 1px 2px 0 rgba(0, 0, 0, 0.05)"),
    ("--shadow-md", "0 4px 6px -1px rgba(0, 0, 0, 0.1)"),
    ("--shadow-lg", "0 10px 15px -3px rgba(0, 0, 0, 0.1)"),
    ("--shadow-glow", "0 0 20px rgba(0, 112, 243, 0.25)"),
]

_SPACINGS = [
    ("--spacing-xs", "0.25rem", "4px"),
    ("--spacing-sm", "0.5rem", "8px"),
    ("--spacing-md", "1rem", "16px"),
    ("--spacing-lg", "1.5rem", "24px"),
    ("--spacing-xl", "2rem", "32px"),
    ("--spacing-xxl", "3rem", "48px"),
]

_TECH_TAGS = [
    "FastAPI",
    "PostgreSQL",
    "Neon Serverless",
    "SQLAlchemy 2.0",
    "Pydantic v2",
    "Jinja2 SSR",
    "Vercel",
    "JWT Auth",
    "Docker Ready",
    "OpenAPI 3.0",
]

_INFRA_ESSENTIALS = [
    {
        "name": "Point d'entrée modulaire",
        "tag": "Architecture",
        "description": "Découpage propre en routers (`api/routes/`), couche de données (`db/`) et services (`services/`).",
    },
    {
        "name": "Neon PostgreSQL Serverless",
        "tag": "Database",
        "description": "Connexion sécurisée avec pooling PGBouncer, SSL et auto-création des tables SQLAlchemy.",
    },
    {
        "name": "Déploiement Vercel Zero-Config",
        "tag": "DevOps",
        "description": "Déploiement serverless optimisé via `requirements.txt` et injection automatique des variables d'environnement.",
    },
    {
        "name": "Rendu hybride SSR + API",
        "tag": "Frontend",
        "description": "Vues HTML dynamiques servies par Jinja2 et points de terminaison REST retournant du JSON.",
    },
]

_TECH_STACK = [
    {
        "name": "FastAPI",
        "version": "0.140+",
        "description": "Framework web Python asynchrone haute performance basé sur Starlette et Pydantic.",
    },
    {
        "name": "PostgreSQL (Neon)",
        "version": "17 Serverless",
        "description": "Base relationnelle Cloud haute disponibilité avec autoscaling et pooling d'instance.",
    },
    {
        "name": "SQLAlchemy",
        "version": "2.0+",
        "description": "ORM moderne orienté type-safety pour l'accès et les requêtes en base de données.",
    },
    {
        "name": "Jinja2",
        "version": "3.1+",
        "description": "Moteur de templates rapide et expressif pour le rendu HTML Server-Side.",
    },
]

_CORE_TEAM = "FastAPI Core Team"
_COMPAT = "FastAPI / Python 3.10+"
_PROD_READY = "Production Ready"
_STABLE = "Stable"
_BADGE_ADV = "Avancé"
_BADGE_MID = "Intermédiaire"
_BADGE_ESS = "Essentiel"

_MODULES = [
    {
        "slug": "authentication",
        "name": "Authentification & Sécurité",
        "tagline": "JWT · Password Hashing · OAuth2 · RBAC",
        "description": "Gestion des utilisateurs, hachage de mots de passe (passlib / bcrypt) et sécurisation des endpoints par tokens JWT.",
        "category": "Core",
        "badge": _BADGE_ESS,
        "badge_class": "badge-primary",
        "version": "v1.0",
        "endpoint_count": len(_AUTH),
        "endpoints": _AUTH,
        "models": ["User", "UserRole", "RefreshToken"],
        "status": _PROD_READY,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Module d'authentification prêt pour la production incluant la validation des données d'entrée via Pydantic et la sécurisation des endpoints.",
        "install_snippet": '# Prêt à l\'emploi dans api/routes/data.py et services/',
        "config_snippet": '# .env\nJWT_SECRET_KEY="your-secret-key"\nJWT_ALGORITHM="HS256"',
        "note": "Utilise l'en-tête Authorization: Bearer <token> pour sécuriser les appels API.",
    },
    {
        "slug": "database",
        "name": "PostgreSQL & ORM",
        "tagline": "SQLAlchemy 2.0 · Neon Serverless · Session Injection",
        "description": "Couche d'accès aux données PostgreSQL avec sessions gérées via la dépendance FastAPI `Depends(get_db)`.",
        "category": "Data",
        "badge": _BADGE_ESS,
        "badge_class": "badge-primary",
        "version": "v1.0",
        "endpoint_count": len(_DATABASE_ENDPOINTS),
        "endpoints": _DATABASE_ENDPOINTS,
        "models": ["ItemModel", "ProjectConfig", "DesignToken", "Module", "Endpoint"],
        "status": _PROD_READY,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Gère la connexion à Neon PostgreSQL, le pool PGBouncer et la création automatique du schéma via SQLAlchemy.",
        "install_snippet": 'from db.database import get_db\nfrom db import models',
        "config_snippet": '# db/database.py\nengine = create_engine(DATABASE_URL, pool_pre_ping=True)',
        "note": "Pre-ping configuré pour gérer l'inactivité serverless sans déconnexion brute.",
    },
    {
        "slug": "web-templates",
        "name": "Rendu Web & Design System",
        "tagline": "Jinja2 · HTML5 / CSS3 · Tokens Dynamiques · Dark Mode",
        "description": "Système de rendu de pages Web côté serveur avec thèmes adaptatifs, composants UI réutilisables et Design System configurable en base de données.",
        "category": "Frontend",
        "badge": _BADGE_MID,
        "badge_class": "badge-neutral",
        "version": "v1.0",
        "endpoint_count": len(_SYSTEM_ENDPOINTS),
        "endpoints": _SYSTEM_ENDPOINTS,
        "models": ["DesignToken", "ProjectConfig"],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Templates Jinja2 organisés de manière modulaire dans `templates/pages/` avec styles partagés dans `static/`.",
        "install_snippet": 'templates = Jinja2Templates(directory="templates")',
        "config_snippet": 'app.mount("/static", StaticFiles(directory="static"), name="static")',
        "note": "Supporte la personnalisation dynamique des couleurs et des composants par projet.",
    },
    {
        "slug": "monitoring",
        "name": "Healthcheck & Monitoring",
        "tagline": "Status API · DB Ping · OpenAPI Docs",
        "description": "Supervision de la santé de l'application, statut de la connexion base de données et documentation Swagger / ReDoc intégrée.",
        "category": "Ops",
        "badge": _BADGE_ESS,
        "badge_class": "badge-primary",
        "version": "v1.0",
        "endpoint_count": 2,
        "endpoints": [
            ("GET", "/api/status", "Vérifier le statut de l'API et de la BDD"),
            ("GET", "/docs", "Interface Swagger UI"),
        ],
        "models": [],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Fournit un endpoint `/api/status` consommable par des sondes Kubernetes, UptimeRobot ou Vercel Health Checks.",
        "install_snippet": 'from api.routes import data\napp.include_router(data.router, prefix="/api")',
        "config_snippet": '@router.get("/status")\ndef get_status(db: Session = Depends(get_db)):\n    ...',
        "note": "Génère automatiquement les spécifications OpenAPI 3.0.",
    },
]

_MODULES_BY_SLUG = {m["slug"]: m for m in _MODULES}

_CHANGELOG = [
    {
        "version": "v1.0.0",
        "date": "Juillet 2026",
        "tag": "Release",
        "tag_class": "badge-primary",
        "changes": [
            "Lancement initial du boilerplate FastAPI + Neon PostgreSQL",
            "Architecture modulaire complète avec séparation des responsabilités",
            "Intégration d'un Design System dynamique configurable via ORM",
            "Support du déploiement serverless sur Vercel avec pré-ping BDD",
            "Suite de scripts CLI de test et d'administration (seed, test_db, test_api)",
        ],
    },
]
