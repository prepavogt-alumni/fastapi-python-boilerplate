# Data structures ported from COOP-CA AMIFOND Pages

_AUTH = [
    ("POST", "/api/v1/auth/login/", "Connexion"),
    ("POST", "/api/v1/auth/logout/", "Déconnexion"),
    ("POST", "/api/v1/auth/register/", "Inscription"),
    ("GET",  "/api/v1/auth/users/me/", "Profil courant"),
    ("POST", "/api/v1/token/", "Obtenir JWT"),
    ("POST", "/api/v1/token/refresh/", "Rafraîchir JWT"),
]

_ENTERPRISE = [
    ("GET",  "/api/v1/enterprise/enterprises/", "Liste des entreprises"),
    ("POST", "/api/v1/enterprise/enterprises/", "Créer"),
    ("GET",  "/api/v1/enterprise/enterprises/{id}/", "Détail"),
    ("PATCH", "/api/v1/enterprise/enterprises/{id}/", "Modifier"),
    ("GET",  "/api/v1/enterprise/branches/", "Agences / Branches"),
    ("POST", "/api/v1/enterprise/branches/", "Créer agence"),
    ("GET",  "/api/v1/enterprise/exercices/", "Exercices comptables"),
    ("POST", "/api/v1/enterprise/exercices/", "Créer exercice"),
    ("GET",  "/api/v1/enterprise/governance/", "Organes de gouvernance"),
    ("GET",  "/api/v1/enterprise/configuration/", "Configuration générale"),
]

_ACCOUNTS = [
    ("GET",  "/api/v1/accounts/plans/", "Plans comptables"),
    ("POST", "/api/v1/accounts/plans/", "Créer plan"),
    ("GET",  "/api/v1/accounts/records/", "Enregistrements (~1532 comptes)"),
    ("GET",  "/api/v1/accounts/charts/", "Plans comptables"),
    ("GET",  "/api/v1/accounts/charts/{id}/entries/", "Écritures du plan"),
]

_TIERS = [
    ("GET",  "/api/v1/tiers/tiers/", "Liste des tiers"),
    ("POST", "/api/v1/tiers/tiers/", "Créer un tiers"),
    ("GET",  "/api/v1/tiers/tiers/{id}/", "Détail tiers"),
    ("GET",  "/api/v1/tiers/roles/", "Rôles des tiers"),
    ("POST", "/api/v1/tiers/roles/", "Attribuer un rôle"),
    ("GET",  "/api/v1/tiers/societaires/", "Sociétaires (KYC)"),
    ("GET",  "/api/v1/tiers/contacts/", "Contacts"),
    ("GET",  "/api/v1/tiers/adresses/", "Adresses"),
    ("GET",  "/api/v1/tiers/attachments/", "Pièces jointes"),
]

_ACCOUNTING = [
    ("GET",  "/api/v1/accounting/journals/", "Journaux (7 types : CA,BQ,PS,CR,VR,OD,AN)"),
    ("POST", "/api/v1/accounting/journals/", "Créer journal"),
    ("GET",  "/api/v1/accounting/entries/", "Écritures comptables"),
    ("POST", "/api/v1/accounting/entries/", "Nouvelle écriture"),
    ("GET",  "/api/v1/accounting/entries/{id}/", "Détail écriture"),
]

_TREASURY = [
    ("GET",  "/api/v1/treasury/sessions/", "Sessions de caisse"),
    ("POST", "/api/v1/treasury/sessions/", "Ouvrir une session"),
    ("GET",  "/api/v1/treasury/operations/", "Opérations de caisse"),
    ("POST", "/api/v1/treasury/operations/", "Enregistrer opération"),
    ("GET",  "/api/v1/treasury/balance/", "Balance de caisse"),
]

_LOANS = [
    ("GET",  "/api/v1/loans/products/", "Produits de crédit"),
    ("POST", "/api/v1/loans/products/", "Créer produit"),
    ("GET",  "/api/v1/loans/applications/", "Demandes de crédit"),
    ("POST", "/api/v1/loans/applications/", "Soumettre demande"),
    ("GET",  "/api/v1/loans/loans/", "Crédits actifs"),
    ("GET",  "/api/v1/loans/repayments/", "Remboursements"),
    ("POST", "/api/v1/loans/repayments/", "Enregistrer remboursement"),
    ("GET",  "/api/v1/loans/provisions/", "Provisions COBAC"),
]

_SHARES = [
    ("GET",  "/api/v1/shares/types/", "Types de parts sociales"),
    ("POST", "/api/v1/shares/types/", "Créer type"),
    ("GET",  "/api/v1/shares/subscriptions/", "Souscriptions"),
    ("POST", "/api/v1/shares/subscriptions/", "Souscrire"),
    ("GET",  "/api/v1/shares/payments/", "Libérations de parts"),
    ("POST", "/api/v1/shares/payments/", "Enregistrer libération"),
    ("GET",  "/api/v1/shares/withdrawals/", "Retraits de parts"),
]

_EVENTS = [
    ("GET",  "/api/v1/events/", "Journaux d'événements"),
    ("GET",  "/api/v1/events/rule-configs/", "Règles comptables (15 règles PC-EMF)"),
    ("POST", "/api/v1/events/rule-configs/", "Configurer une règle"),
]

_CLIENT_PORTAL = [
    ("GET",  "/api/v1/client/me/", "Mon profil"),
    ("GET",  "/api/v1/client/comptes/", "Mes comptes"),
    ("GET",  "/api/v1/client/credits/", "Mes crédits"),
    ("GET",  "/api/v1/client/parts/", "Mes parts sociales"),
    ("GET",  "/api/v1/client/operations/", "Mes opérations"),
    ("GET",  "/api/v1/client/documents/", "Mes documents"),
    ("POST", "/api/v1/client/demandes/", "Soumettre une demande"),
    ("GET",  "/api/v1/client/notifications/", "Notifications"),
    ("GET",  "/api/v1/client/solde/", "Solde récapitulatif"),
]

_MANAGER_PORTAL = [
    ("GET",    "/manager/", "Tableau de bord"),
    ("GET",    "/manager/customers/", "Gestion clients"),
    ("GET",    "/manager/loans/", "Gestion crédits"),
    ("GET",    "/manager/shares/", "Gestion parts sociales"),
    ("GET",    "/manager/treasury/", "Gestion trésorerie"),
    ("GET",    "/manager/accounting/", "Gestion comptabilité"),
    ("GET",    "/manager/reports/", "Rapports & états"),
    ("GET",    "/manager/settings/", "Paramètres"),
]

_COLORS_BRAND = [
    ("Primary", "#1a5276", "--primary-color · #1a5276"),
    ("Primary Light", "var(--primary-light)", "--primary-light · #eef3f7"),
    ("Secondary", "var(--secondary-color)", "--secondary-color · #d4ac0d"),
    ("Secondary Light", "var(--secondary-light)", "--secondary-light · #fcf6d6"),
    ("Accent Vert", "var(--accent-color)", "--accent-color · #117a65"),
    ("Black", "var(--black)", "--black · #000000"),
]

_COLORS_FUNCTIONAL = [
    ("Success", "var(--success-color)", "--success-color · #27ae60"),
    ("Danger", "var(--danger-color)", "--danger-color · #c0392b"),
    ("Warning", "var(--warning-color)", "--warning-color · #f39c12"),
    ("Info", "var(--info-color)", "--info-color · #2980b9"),
]

_COLORS_SURFACE = [
    ("Body BG", "var(--body-bg)", "--body-bg · #f8f9fa"),
    ("Body Color", "var(--body-color)", "--body-color · #333333"),
    ("Text Muted", "var(--text-muted)", "--text-muted · #6e7191"),
    ("Border", "var(--border-color)", "--border-color · #e0e0e0"),
    ("Card BG", "var(--card-bg)", "--card-bg · #ffffff"),
    ("Footer BG", "var(--footer-bg)", "--footer-bg · #0d2c40"),
]

_SHADOWS = [
    ("--shadow-sm", "0 2px 4px rgba(26, 82, 118, 0.08)"),
    ("--shadow-md", "0 6px 16px rgba(26, 82, 118, 0.12)"),
    ("--shadow-lg", "0 12px 28px rgba(26, 82, 118, 0.16)"),
    ("--shadow-glow", "0 0 20px rgba(26, 82, 118, 0.25)"),
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
    "COBAC",
    "PC-EMF 2010",
    "OHADA",
    "JWT",
    "RBAC",
    "FastAPI",
    "PostgreSQL (Neon)",
    "Docker",
    "OpenAPI 3.0",
]

_INFRA_ESSENTIALS = [
    {
        "name": "Custom User Model",
        "tag": "Core",
        "description": "Email-based, prêt pour les permissions granulaires et l'extension multi-agences.",
    },
    {
        "name": "Docker Compose Prod",
        "tag": "DevOps",
        "description": "Multi-conteneurs : Web, Worker, Redis, Postgres, Nginx.",
    },
    {
        "name": "Isolation par agence",
        "tag": "Security",
        "description": "BranchScopedModel pour la séparation logique des données entre agences.",
    },
    {
        "name": "JWT + RBAC",
        "tag": "Auth",
        "description": "Tokens HttpOnly avec rotation automatique et contrôle d'accès par rôle (caissier, comptable, admin).",
    },
]

_TECH_STACK = [
    {
        "name": "FastAPI",
        "version": "0.140+",
        "description": "Framework web Python moderne, rapide (haute performance) basé sur Starlette et Pydantic.",
    },
    {
        "name": "PostgreSQL (Neon)",
        "version": "17 Serverless",
        "description": "Base relationnelle Cloud - fiabilité et autoscaling serverless pour les données financières.",
    },
    {
        "name": "SQLAlchemy",
        "version": "2.0+",
        "description": "ORM Python de référence pour une gestion fluide des données financières et des migrations.",
    },
    {
        "name": "Python",
        "version": "3.10+",
        "description": "Typage statique, performance améliorée et syntaxe moderne.",
    },
]

_CORE_TEAM = "COOP-CA AMIFOND"
_COMPAT = "FastAPI / Python 3.10+"
_PROD_READY = "Production Ready"
_STABLE = "Stable"
_BETA = "Beta"
_BADGE_ADV = "Avancé"
_BADGE_MID = "Intermédiaire"
_BADGE_ESS = "Essentiel"

_MODULES = [
    {
        "slug": "authentication",
        "name": "Authentification",
        "tagline": "JWT · Custom User · RBAC · Rôles coopérative",
        "description": "Authentification complète basée sur JWT avec cookies HttpOnly. Utilisateurs personnalisés (email-based), contrôle d'accès par rôle (caissier, comptable, gestionnaire, admin) et gestion des sessions.",
        "category": "Core",
        "badge": _BADGE_ESS,
        "badge_class": "badge-primary",
        "version": "v2.0",
        "endpoint_count": len(_AUTH),
        "endpoints": _AUTH,
        "models": ["User", "ClientProfile", "CompteClient", "SavingsProduct"],
        "status": _PROD_READY,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Ce module implémente une stratégie JWT « cookie-first » : le token d'accès est posé dans un cookie HttpOnly au login, invisible au JavaScript.",
        "install_snippet": '# authentication est un module local\n"authentication",',
        "config_snippet": '# config/settings.py\nAUTH_USER_MODEL = "customers.User"',
        "note": "La stratégie « cookie HttpOnly » protège contre les attaques XSS.",
    },
    {
        "slug": "enterprise",
        "name": "Enterprise & Gouvernance",
        "tagline": "Agrégat racine · Branches · Exercices · Gouvernance OHADA",
        "description": "Gestion de la coopérative (Enterprise) comme agrégat racine. Agences/branches avec BranchScopedModel, exercices comptables, configuration générale et organes de gouvernance.",
        "category": "Core",
        "badge": _BADGE_ADV,
        "badge_class": "badge-warning",
        "version": "v1.5",
        "endpoint_count": len(_ENTERPRISE),
        "endpoints": _ENTERPRISE,
        "models": ["Enterprise", "Branch", "ExerciceComptable", "Configuration", "GovernanceOrgan"],
        "status": _PROD_READY,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le module Enterprise constitue l'agrégat racine du système. L'Enterprise représente la coopérative elle-même.",
        "install_snippet": '"apps.enterprise",',
        "config_snippet": '# routes enterprise\n/api/v1/enterprise/...',
        "note": "Le BranchScopedModel vérifie l'appartenance en base.",
    },
    {
        "slug": "accounts",
        "name": "Plan Comptable PC-EMF",
        "tagline": "AccountPlan · AccountRecord (~1532 comptes) · Plan comptable OHADA",
        "description": "Plan comptable conforme au PC-EMF (Plan Comptable des Établissements de Microfinance) avec environ 1532 comptes prédéfinis. Structure hiérarchique conforme aux normes OHADA.",
        "category": "Comptabilité",
        "badge": _BADGE_ESS,
        "badge_class": "badge-primary",
        "version": "v1.0",
        "endpoint_count": len(_ACCOUNTS),
        "endpoints": _ACCOUNTS,
        "models": ["AccountPlan", "AccountRecord", "CompanyChart"],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le module Accounts implémente le Plan Comptable des Établissements de Microfinance (PC-EMF 2010).",
        "install_snippet": '"apps.accounts",',
        "config_snippet": '# routes accounts\n/api/v1/accounts/...',
        "note": "Le plan comptable est initialisé automatiquement.",
    },
    {
        "slug": "tiers",
        "name": "Tiers & Clientèle",
        "tagline": "Tiers · SocietaireProfile · Roles · KYC · Contacts",
        "description": "Gestion des tiers (personnes physiques et morales) avec attribution de rôles multiples. Profil sociétaire avec KYC (Know Your Customer), contacts et adresses.",
        "category": "Core",
        "badge": _BADGE_MID,
        "badge_class": "badge-neutral",
        "version": "v1.0",
        "endpoint_count": len(_TIERS),
        "endpoints": _TIERS,
        "models": ["Tiers", "TiersRole", "SocietaireProfile"],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le module Tiers gère l'ensemble des acteurs de la coopérative.",
        "install_snippet": '"apps.tiers",',
        "config_snippet": '# routes tiers\n/api/v1/tiers/...',
        "note": "Les rôles de tiers sont distincts des rôles RBAC.",
    },
    {
        "slug": "accounting",
        "name": "Comptabilité Générale",
        "tagline": "Journaux · Écritures · 7 types (CA,BQ,PS,CR,VR,OD,AN) · Séquences",
        "description": "Comptabilité générale avec 7 types de journaux conformes au PC-EMF : CAisse, BanQue, Portefeuille de Souscriptions, Crédits, Virements, Ordres Divers, ANniversaire.",
        "category": "Comptabilité",
        "badge": _BADGE_ADV,
        "badge_class": "badge-warning",
        "version": "v1.0",
        "endpoint_count": len(_ACCOUNTING),
        "endpoints": _ACCOUNTING,
        "models": ["Journal", "JournalEntry", "JournalLine"],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le module Accounting implémente la comptabilité générale de la coopérative.",
        "install_snippet": '"apps.accounting",',
        "config_snippet": '# routes accounting\n/api/v1/accounting/...',
        "note": "Les journaux sont initialisés automatiquement.",
    },
    {
        "slug": "treasury",
        "name": "Trésorerie",
        "tagline": "CaisseSession · CashOperation · Balance · Séquences COBAC",
        "description": "Gestion de la trésorerie avec sessions de caisse (ouverture/fermeture), opérations de caisse et suivi des balances.",
        "category": "Opérations",
        "badge": _BADGE_ADV,
        "badge_class": "badge-warning",
        "version": "v1.0",
        "endpoint_count": len(_TREASURY),
        "endpoints": _TREASURY,
        "models": ["CaisseSession", "CashOperation"],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le module Treasury gère les opérations de caisse en temps réel.",
        "install_snippet": '"apps.treasury",',
        "config_snippet": '# routes treasury\n/api/v1/treasury/...',
        "note": "La balance de caisse doit être vérifiée à chaque fermeture.",
    },
    {
        "slug": "loans",
        "name": "Crédits",
        "tagline": "LoanProduct · LoanApplication · Amortissement · Provisions COBAC",
        "description": "Gestion complète du cycle de crédit : produits de crédit, demandes, approbation, décaissement, plan d'amortissement automatique, remboursements et provisions.",
        "category": "Crédits",
        "badge": _BADGE_ADV,
        "badge_class": "badge-warning",
        "version": "v1.0",
        "endpoint_count": len(_LOANS),
        "endpoints": _LOANS,
        "models": ["LoanProduct", "LoanApplication", "LoanRepayment"],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le module Loans couvre le cycle complet du crédit.",
        "install_snippet": '"apps.loans",',
        "config_snippet": '# routes loans\n/api/v1/loans/...',
        "note": "Le circuit d'approbation suit la gouvernance COBAC.",
    },
    {
        "slug": "shares",
        "name": "Parts Sociales",
        "tagline": "ShareType · Souscription · Libération · Retrait · Capital variable OHADA",
        "description": "Gestion des parts sociales conformément au droit OHADA : 3 catégories, souscription, libération progressive et retrait.",
        "category": "Capital",
        "badge": _BADGE_MID,
        "badge_class": "badge-neutral",
        "version": "v1.0",
        "endpoint_count": len(_SHARES),
        "endpoints": _SHARES,
        "models": ["ShareType", "ShareSubscription", "SharePayment"],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le module Shares gère le capital variable de la coopérative.",
        "install_snippet": '"apps.shares",',
        "config_snippet": '# routes shares\n/api/v1/shares/...',
        "note": "Le retrait de parts suit un préavis réglementaire.",
    },
    {
        "slug": "events",
        "name": "Moteur Comptable",
        "tagline": "BusinessEventLog · AccountingRuleConfig · 15 règles PC-EMF",
        "description": "Moteur d'événements métier qui déclenche automatiquement les écritures comptables. 15 règles prédéfinies.",
        "category": "Comptabilité",
        "badge": _BADGE_MID,
        "badge_class": "badge-neutral",
        "version": "v1.0",
        "endpoint_count": len(_EVENTS),
        "endpoints": _EVENTS,
        "models": ["BusinessEventLog", "AccountingRuleConfig"],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le module Events est le moteur central de la comptabilité automatique.",
        "install_snippet": '"apps.events",',
        "config_snippet": '# routes events\n/api/v1/events/...',
        "note": "Le replay d'événements est réservé aux administrateurs.",
    },
    {
        "slug": "portals",
        "name": "Portails Client & Gestionnaire",
        "tagline": "Portail self-service · Back-office · Tableau de bord",
        "description": "Deux portails d'accès : portail client (self-service) et portail gestionnaire (back-office) avec tableau de bord et rapports.",
        "category": "Portails",
        "badge": _BADGE_ESS,
        "badge_class": "badge-primary",
        "version": "v1.0",
        "endpoint_count": len(_CLIENT_PORTAL) + len(_MANAGER_PORTAL),
        "endpoints": _CLIENT_PORTAL + _MANAGER_PORTAL,
        "models": [],
        "status": _STABLE,
        "maintainer": _CORE_TEAM,
        "compatibility": _COMPAT,
        "doc_intro": "Le portail client permet aux sociétaires de consulter leurs informations.",
        "install_snippet": '"apps.client", "apps.manager"',
        "config_snippet": '# routes portals\n/api/v1/client/...\n/manager/...',
        "note": "Le portail client est en lecture seule.",
    },
]

_MODULES_BY_SLUG = {m["slug"]: m for m in _MODULES}

_CHANGELOG = [
    {
        "version": "v2.5",
        "date": "Juillet 2026",
        "tag": "FastAPI",
        "tag_class": "badge-primary",
        "changes": [
            "Portage complet des templates AMIFOND sur FastAPI & Vercel",
            "Mise en place de Jinja2Templates et de la gestion des ressources statiques",
            "Intégration du moteur d'API FastAPI et de la base Neon PostgreSQL",
            "Support natif du rendu HTML server-side hautement performant",
        ],
    },
    {
        "version": "v2.0",
        "date": "Juillet 2026",
        "tag": "Majeure",
        "tag_class": "badge-warning",
        "changes": [
            "Migration vers ERP microfinance PC-EMF 2010",
            "Réorganisation des URLs API avec préfixe api/v1/",
            "Ajout des endpoints auth (users/me, login, logout)",
        ],
    },
    {
        "version": "v1.5",
        "date": "Mars 2026",
        "tag": "Mineure",
        "tag_class": "badge-primary",
        "changes": [
            "Ajout du moteur comptable (BusinessEventLog) avec 15 règles PC-EMF",
            "Module Parts Sociales : souscription, libération, retrait",
            "Module Crédits : produits, demandes, amortissement, provisions COBAC",
            "Module Trésorerie : sessions de caisse, opérations, balance",
        ],
    },
]
