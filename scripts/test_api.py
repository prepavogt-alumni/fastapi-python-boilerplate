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

    print("--- Test des Endpoints FastAPI ---")
    
    res_status = client.get("/api/status")
    print("GET /api/status -> Status Code:", res_status.status_code)
    print("  Réponse:", res_status.json())

    res_post = client.post("/api/items?name=Article+Script+Test&value=500")
    print("\nPOST /api/items -> Status Code:", res_post.status_code)
    print("  Réponse:", res_post.json())

    res_data = client.get("/api/data")
    print("\nGET /api/data -> Status Code:", res_data.status_code)
    print("  Réponse:", res_data.json())

    res_root = client.get("/")
    print("\nGET / (HTML Root) -> Status Code:", res_root.status_code)
    print("  Header Content-Type:", res_root.headers.get("content-type"))

if __name__ == "__main__":
    run_api_test()
