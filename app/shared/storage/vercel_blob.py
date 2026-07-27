import os
import httpx
from typing import BinaryIO, Optional
from app.shared.storage.base import StorageProvider

class VercelBlobStorageProvider(StorageProvider):
    """
    Implémentation de StorageProvider pour Vercel Blob Store.
    Utilise l'API REST v7 officielle de Vercel Blob avec jeton Read/Write.
    """
    def __init__(self, token: Optional[str] = None, access: str = "private"):
        self.token = token or os.getenv("VERCEL_BLOB_READ_WRITE_TOKEN")
        self.access = access or os.getenv("VERCEL_BLOB_ACCESS", "private")
        self.base_url = "https://blob.vercel-storage.com"

    async def upload(self, file_obj: BinaryIO, filename: str, folder: str = "uploads") -> str:
        if not self.token:
            raise ValueError("VERCEL_BLOB_READ_WRITE_TOKEN est manquant dans l'environnement")

        pathname = f"{folder}/{filename}".lstrip("/")
        url = f"{self.base_url}/{pathname}"

        headers = {
            "authorization": f"Bearer {self.token}",
            "x-api-version": "7",
            "x-vercel-blob-access": self.access,
            "x-add-random-suffix": "1"
        }

        content = file_obj.read() if hasattr(file_obj, "read") else file_obj

        async with httpx.AsyncClient() as client:
            response = await client.put(url, content=content, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data.get("url")

    async def delete(self, file_url: str) -> bool:
        if not self.token:
            return False

        headers = {
            "authorization": f"Bearer {self.token}",
            "x-api-version": "7",
            "content-type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/delete",
                json={"urls": [file_url]},
                headers=headers
            )
            return response.status_code == 200
