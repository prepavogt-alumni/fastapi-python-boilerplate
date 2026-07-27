# Document d'Analyse : Intégration d'Upstash Redis (Vercel KV)

## 1. Contexte et Enjeux

Dans un environnement Serverless comme **Vercel**, l'utilisation d'une base de données In-Memory / Clé-Valeur traditionnelle via des connexions TCP persistantes pose des défis de gestion de pool de connexions lors du passage à l'échelle (scale-down / scale-up des lambdas).

L'intégration d'**Upstash Redis (Vercel KV)** via son **API REST HTTP native** résout élégamment ce problème :
* Aucune connexion TCP persistante à maintenir.
* Temps de réponse extrêmement bas (< 10ms).
* Compatibilité native avec l'architecture Serverless FastAPI sur Vercel.

---

## 2. Cas d'Usage Clés dans l'Architecture

### 2.1. Response Caching (Cache API & Vues SSR)
Mise en cache des réponses HTTP des endpoints lourds ou fréquents (ex: liste des modules, tokens de design system, articles du blog).

### 2.2. Rate Limiting & Protection contre les Abus
Limitation du nombre de requêtes par IP sur les routes sensibles (`/api/v1/auth/login`, endpoints d'upload de contenu `/content/upload`).

### 2.3. Gestion de Sessions & Révocation de Tokens JWT (Blacklist)
Stockage des jetons révoqués lors de la déconnexion d'un utilisateur (`/logout`) avec durée d'expiration (TTL) automatique.

### 2.4. File d'Attente de Tâches Asynchrones (Task Queues)
Découplage des traitements lourds (transcodage vidéo, encodage audio, génération de thumbnails) initiés par l'app `content`.

---

## 3. Configuration & Variables d'Environnement

Les identifiants Upstash Redis / Vercel KV configurés dans `.env` et déclarés dans `app/core/config.py` :

```ini
CACHE_PROVIDER=upstash_redis
KV_REST_API_URL="https://infinite-shark-180736.upstash.io"
KV_REST_API_TOKEN="gQAAAAAAAsIAAAIgcDI4OWI5ZmIzYzk2MDY0MDJkYjFmMjNmMGMzYTU0ZmIwZA"
KV_REST_API_READ_ONLY_TOKEN="ggAAAAAAAsIAAAIgcDIY2Lxz60tRTlGNR0jknA_HCqi2twIPukJ9j4fp9WLIkA"
REDIS_URL="rediss://default:gQAAAAAAAsIAAAIgcDI4OWI5ZmIzYzk2MDY0MDJkYjFmMjNmMGMzYTU0ZmIwZA@infinite-shark-180736.upstash.io:6379"
```

---

## 4. Spécification du Pattern Cache Adapter (`app/shared/cache/`)

De la même manière que pour le stockage des fichiers médias (`StorageProvider`), la gestion du cache s'appuie sur le pattern **Adapter** :

```text
app/shared/cache/
├── __init__.py                # Factory get_cache_provider()
├── base.py                    # Interface abstraite CacheProvider (get, set, delete, exists)
├── memory.py                  # Implémentation InMemoryCacheProvider (dev sans Redis)
└── upstash_redis.py           # Implémentation UpstashRedisCacheProvider (Serverless REST API)
```

---

## 5. Spécification de l'Implémentation `UpstashRedisCacheProvider`

```python
# app/shared/cache/upstash_redis.py
import os
import httpx
from typing import Optional, Any
import json
from app.shared.cache.base import CacheProvider

class UpstashRedisCacheProvider(CacheProvider):
    """
    Implémentation de CacheProvider pour Upstash Redis via REST API (Vercel KV Serverless-native).
    """
    def __init__(self, url: Optional[str] = None, token: Optional[str] = None):
        self.url = url or os.getenv("KV_REST_API_URL")
        self.token = token or os.getenv("KV_REST_API_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    async def get(self, key: str) -> Optional[Any]:
        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, json=["GET", key], headers=self.headers)
            if res.status_code == 200:
                val = res.json().get("result")
                if val is not None:
                    try:
                        return json.loads(val)
                    except Exception:
                        return val
        return None

    async def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> bool:
        val_str = json.dumps(value) if not isinstance(value, str) else value
        command = ["SET", key, val_str]
        if ttl_seconds:
            command.extend(["EX", str(ttl_seconds)])

        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, json=command, headers=self.headers)
            return res.status_code == 200 and res.json().get("result") == "OK"

    async def delete(self, key: str) -> bool:
        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, json=["DEL", key], headers=self.headers)
            return res.status_code == 200

    async def exists(self, key: str) -> bool:
        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, json=["EXISTS", key], headers=self.headers)
            return res.status_code == 200 and res.json().get("result") == 1
```

---

## 6. Validation de la Connexion

Le test d'exécution HTTP vers Upstash confirme la réactivité :
```text
SET status: 200 Response: {'result': 'OK'}
GET status: 200 Response: {'result': 'Hello Upstash Redis!'}
```
