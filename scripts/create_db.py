import os
import sys
from pathlib import Path
from sqlalchemy import create_engine, text

# Charger le fichier .env si présent
root_dir = Path(__file__).resolve().parent.parent
env_file = root_dir / ".env"

if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k, v)

def create_database(db_name: str = "fastapi_db"):
    url_unpooled = os.getenv("DATABASE_URL_UNPOOLED") or os.getenv("POSTGRES_URL_NON_POOLING")
    
    if not url_unpooled:
        print("Erreur: DATABASE_URL_UNPOOLED ou POSTGRES_URL_NON_POOLING introuvable dans l'environnement.")
        sys.exit(1)

    print(f"Tentative de création de la base de données '{db_name}'...")
    # L'instruction CREATE DATABASE nécessite le mode AUTOCOMMIT sous PostgreSQL
    engine = create_engine(url_unpooled, isolation_level="AUTOCOMMIT")

    with engine.connect() as conn:
        exists = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :dbname"),
            {"dbname": db_name}
        ).scalar()
        
        if not exists:
            conn.execute(text(f'CREATE DATABASE "{db_name}";'))
            print(f"✅ Base de données '{db_name}' créée avec succès !")
        else:
            print(f"ℹ️ La base de données '{db_name}' existe déjà.")

if __name__ == "__main__":
    target_db = sys.argv[1] if len(sys.argv) > 1 else "fastapi_db"
    create_database(target_db)
