from abc import ABC, abstractmethod
from typing import Optional, Any

class CacheProvider(ABC):
    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        """Récupère une valeur du cache par sa clé."""
        pass

    @abstractmethod
    async def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> bool:
        """Enregistre une valeur dans le cache avec un TTL optionnel."""
        pass

    @abstractmethod
    async def delete(self, key: str) -> bool:
        """Supprime une clé du cache."""
        pass

    @abstractmethod
    async def exists(self, key: str) -> bool:
        """Vérifie si une clé existe dans le cache."""
        pass
