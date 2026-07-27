from app.core.config import settings
from app.shared.storage.base import StorageProvider
from app.shared.storage.local import LocalStorageProvider
from app.shared.storage.s3 import S3StorageProvider
from app.shared.storage.vercel_blob import VercelBlobStorageProvider

def get_storage_provider() -> StorageProvider:
    """
    Factory renvoyant le StorageProvider configuré selon settings.STORAGE_PROVIDER
    """
    provider = (settings.STORAGE_PROVIDER or "local").lower()

    if provider == "vercel_blob":
        return VercelBlobStorageProvider()
    elif provider == "s3":
        return S3StorageProvider()
    else:
        return LocalStorageProvider()
