from app.core.config import settings
from app.shared.cache.base import CacheProvider
from app.shared.cache.memory import InMemoryCacheProvider
from app.shared.cache.upstash_redis import UpstashRedisCacheProvider

def get_cache_provider() -> CacheProvider:
    """
    Factory renvoyant le CacheProvider configuré selon settings.CACHE_PROVIDER
    """
    provider = (settings.CACHE_PROVIDER or "upstash_redis").lower()

    if provider in ("upstash_redis", "redis", "vercel_kv"):
        return UpstashRedisCacheProvider()
    else:
        return InMemoryCacheProvider()
