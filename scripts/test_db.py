import os
import sys
from pathlib import Path
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

# Ajouter le répertoire racine au PYTHONPATH
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

# Charger le fichier .env
env_file = root_dir / ".env"
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k, v)

from app.core.database import engine, Base
from app.data.models import ItemModel

def run_db_test():
    print("--- Test de connexion Neon PostgreSQL ---")
    if not engine:
        print("❌ Engine non initialisé (DATABASE_URL manquante).")
        sys.exit(1)
        
    try:
        with engine.connect() as conn:
            version = conn.execute(text("SELECT version();")).scalar()
            print("1. ✅ Connexion réussie ! Version PostgreSQL :")
            print("   ", version)
        
        print("\n2. ✅ Vérification / Création des tables...")
        Base.metadata.create_all(bind=engine)
        print("   Table 'items' prête.")

        print("\n3. ✅ Test d'insertion et de lecture...")
        SessionLocal = sessionmaker(bind=engine)
        db = SessionLocal()
        
        test_item = ItemModel(name="Item de test script", value=999)
        db.add(test_item)
        db.commit()
        db.refresh(test_item)
        print(f"   Item inséré - ID: {test_item.id}, Name: '{test_item.name}', Value: {test_item.value}")
        
        total = db.query(ItemModel).count()
        print(f"   Nombre total d'éléments en base : {total}")
        db.close()
        
        print("\n🎉 TOUS LES TESTS DE BASE DE DONNÉES SONT RÉUSSIS !")

    except Exception as e:
        print("\n❌ ERREUR DE BASE DE DONNÉES :", e)

if __name__ == "__main__":
    run_db_test()
