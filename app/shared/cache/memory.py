import time
from typing import Optional, Any, Dict, Tuple
from app.shared.cache.base import CacheProvider

class InMemoryCacheProvider(CacheProvider):
    """
    Implémentation basique en mémoire du cache (pour dev local sans Redis).
    """
    def __init__(self):
        self._store: Dict[str, Tuple[Any, Optional[float]]] = {}

    async def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None
        val, expiry = self._store[key]
        if expiry and time.time() > expiry:
            del self._store[key]
            return None
        return val

    async def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> bool:
        expiry = time.time() + ttl_seconds if ttl_seconds else None
        self._store[key] = (value, expiry)
        return True

    async def delete(self, key: str) -> bool:
        if key in self._store:
            del self._store[key]
            return True
        return False

    async def exists(self, key: str) -> bool:
        return await self.get(key) is not None
