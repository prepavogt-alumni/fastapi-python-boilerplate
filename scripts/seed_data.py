import os
import sys
from pathlib import Path

# Ajouter le répertoire racine au PYTHONPATH
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

# Charger .env
env_file = root_dir / ".env"
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k, v)

from sqlalchemy.orm import sessionmaker
from app.core.database import engine, Base
from app.pages import models as page_models
from app.pages import data as pd
from app.data.models import ItemModel

def seed_database():
    if not engine:
        print("Erreur: Impossible de se connecter à la base de données (engine non configuré).")
        sys.exit(1)

    print("--- Réinitialisation & Seeding BDD Neon PostgreSQL ---")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    try:
        # 1. Project Config
        config = page_models.ProjectConfig(
            title="FastAPI + PostgreSQL",
            subtitle="Production Boilerplate · Neon Serverless · Vercel",
            description="Boilerplate moderne et modulaire avec FastAPI, Neon PostgreSQL et Jinja2 SSR",
            environment="Production",
            tech_tags=pd._TECH_TAGS
        )
        db.add(config)

        # 2. Design Tokens
        for name, val, label in pd._COLORS_BRAND:
            db.add(page_models.DesignToken(category="brand", name=name, value=val, label=label))
        for name, val, label in pd._COLORS_FUNCTIONAL:
            db.add(page_models.DesignToken(category="functional", name=name, value=val, label=label))
        for name, val, label in pd._COLORS_SURFACE:
            db.add(page_models.DesignToken(category="surface", name=name, value=val, label=label))
        for name, val in pd._SHADOWS:
            db.add(page_models.DesignToken(category="shadow", name=name, value=val))
        for name, val, label in pd._SPACINGS:
            db.add(page_models.DesignToken(category="spacing", name=name, value=val, label=label))

        # 3. Modules & Endpoints
        for mdata in pd._MODULES:
            mod = page_models.Module(
                slug=mdata["slug"],
                name=mdata["name"],
                tagline=mdata["tagline"],
                description=mdata["description"],
                category=mdata["category"],
                badge=mdata["badge"],
                badge_class=mdata["badge_class"],
                version=mdata["version"],
                status=mdata["status"],
                maintainer=mdata["maintainer"],
                compatibility=mdata["compatibility"],
                doc_intro=mdata["doc_intro"],
                install_snippet=mdata["install_snippet"],
                config_snippet=mdata["config_snippet"],
                note=mdata["note"]
            )
            db.add(mod)
            db.flush()

            for method, path, summary in mdata["endpoints"]:
                db.add(page_models.Endpoint(
                    module_id=mod.id,
                    category=mod.category,
                    method=method,
                    path=path,
                    summary=summary
                ))

        # 4. Changelog
        for cdata in pd._CHANGELOG:
            db.add(page_models.ChangelogRelease(
                version=cdata["version"],
                date_str=cdata["date"],
                tag=cdata["tag"],
                tag_class=cdata["tag_class"],
                changes=cdata["changes"]
            ))

        # 5. Tech Stack & Infra
        for ts in pd._TECH_STACK:
            db.add(page_models.TechStackItem(name=ts["name"], version=ts["version"], description=ts["description"]))
        for infra in pd._INFRA_ESSENTIALS:
            db.add(page_models.InfraItem(name=infra["name"], tag=infra["tag"], description=infra["description"]))

        # 6. Sample Items
        db.add(ItemModel(name="Sample Item 1 (Database)", value=100))
        db.add(ItemModel(name="Sample Item 2 (Database)", value=200))
        db.add(ItemModel(name="Sample Item 3 (Database)", value=300))

        db.commit()
        print("✅ Base de données initialisée et alimentée avec succès !")

    except Exception as e:
        db.rollback()
        print("❌ Erreur durant le seeding :", e)
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
