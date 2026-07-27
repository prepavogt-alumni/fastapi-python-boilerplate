import os
import json
import httpx
from typing import Optional, Any
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
        if not self.url or not self.token:
            return None
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
        if not self.url or not self.token:
            return False
        val_str = json.dumps(value) if not isinstance(value, str) else value
        command = ["SET", key, val_str]
        if ttl_seconds:
            command.extend(["EX", str(ttl_seconds)])

        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, json=command, headers=self.headers)
            return res.status_code == 200 and res.json().get("result") == "OK"

    async def delete(self, key: str) -> bool:
        if not self.url or not self.token:
            return False
        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, json=["DEL", key], headers=self.headers)
            return res.status_code == 200 and res.json().get("result", 0) > 0

    async def exists(self, key: str) -> bool:
        if not self.url or not self.token:
            return False
        async with httpx.AsyncClient() as client:
            res = await client.post(self.url, json=["EXISTS", key], headers=self.headers)
            return res.status_code == 200 and res.json().get("result", 0) == 1
