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
from db.database import engine, Base
from db import models
from api.routes import pages_data as pd

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
        config = models.ProjectConfig(
            title="FastAPI + PostgreSQL",
            subtitle="Production Boilerplate · Neon Serverless · Vercel",
            description="Boilerplate moderne et modulaire avec FastAPI, Neon PostgreSQL et Jinja2 SSR",
            environment="Production",
            tech_tags=pd._TECH_TAGS
        )
        db.add(config)
        print("✅ Configuration du projet insérée.")

        # 2. Design Tokens
        for name, val, lbl in pd._COLORS_BRAND:
            db.add(models.DesignToken(category="brand", name=name, value=val, label=lbl))
        for name, val, lbl in pd._COLORS_FUNCTIONAL:
            db.add(models.DesignToken(category="functional", name=name, value=val, label=lbl))
        for name, val, lbl in pd._COLORS_SURFACE:
            db.add(models.DesignToken(category="surface", name=name, value=val, label=lbl))
        for name, val in pd._SHADOWS:
            db.add(models.DesignToken(category="shadow", name=name, value=val, label=""))
        for name, val, lbl in pd._SPACINGS:
            db.add(models.DesignToken(category="spacing", name=name, value=val, label=lbl))
        print("✅ Tokens du Design System insérés (Couleurs, Ombres, Espacements).")

        # 3. Tech Stack & Infra
        for t in pd._TECH_STACK:
            db.add(models.TechStackItem(name=t["name"], version=t["version"], description=t["description"]))
        print("✅ Pile technique (Tech Stack) insérée.")

        for inf in pd._INFRA_ESSENTIALS:
            db.add(models.InfraItem(name=inf["name"], tag=inf["tag"], description=inf["description"]))
        print("✅ Éléments d'infrastructure insérés.")

        # 4. Modules & Endpoints
        for m in pd._MODULES:
            mod_obj = models.Module(
                slug=m["slug"],
                name=m["name"],
                tagline=m["tagline"],
                description=m["description"],
                category=m["category"],
                badge=m["badge"],
                badge_class=m["badge_class"],
                version=m["version"],
                status=m["status"],
                maintainer=m["maintainer"],
                compatibility=m["compatibility"],
                doc_intro=m["doc_intro"],
                install_snippet=m["install_snippet"],
                config_snippet=m["config_snippet"],
                note=m["note"],
            )
            db.add(mod_obj)
            db.flush()

            for method, path, summary in m.get("endpoints", []):
                db.add(models.Endpoint(module_id=mod_obj.id, method=method, path=path, summary=summary))
        print(f"✅ {len(pd._MODULES)} Modules fonctionnels et leurs endpoints insérés.")

        # 5. Changelog Releases
        for rel in pd._CHANGELOG:
            db.add(models.ChangelogRelease(
                version=rel["version"],
                date_str=rel["date"],
                tag=rel["tag"],
                tag_class=rel["tag_class"],
                changes=rel["changes"]
            ))
        print(f"✅ {len(pd._CHANGELOG)} Versions du Changelog insérées.")

        db.commit()
        print("\n🎉 BASE DE DONNÉES RÉINITIALISÉE ET REPEUPLÉE AVEC SUCCÈS !")

    except Exception as e:
        db.rollback()
        print("❌ Erreur lors du seeding:", e)
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
