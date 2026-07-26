import os
import sys
from pathlib import Path

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

from fastapi.testclient import TestClient
from main import app

def run_api_test():
    client = TestClient(app)

    print("--- Test des Endpoints FastAPI (API & HTML Pages) ---")
    
    # Test API
    res_status = client.get("/api/status")
    print("GET /api/status -> Status Code:", res_status.status_code)
    print("  Réponse:", res_status.json())

    res_data = client.get("/api/data")
    print("\nGET /api/data -> Status Code:", res_data.status_code)

    # Test HTML Pages
    routes_to_test = [
        ("/", "Accueil"),
        ("/modules", "Modules"),
        ("/modules/authentication", "Détail Module (authentication)"),
        ("/apps", "APIs Reference"),
        ("/design-system", "Design System"),
        ("/documentation", "Documentation"),
        ("/changelog", "Changelog"),
        ("/demo", "Démo HTML initiale"),
    ]

    print("\n--- Validation des pages HTML ---")
    for path, label in routes_to_test:
        res = client.get(path)
        status = "✅ 200 OK" if res.status_code == 200 else f"❌ {res.status_code}"
        content_type = res.headers.get("content-type", "")
        print(f"{status} | {label:<30} -> Path: {path:<25} ({content_type})")

if __name__ == "__main__":
    run_api_test()
