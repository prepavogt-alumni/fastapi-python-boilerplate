# Document d'Analyse : Intégration de Vercel Blob Storage

## 1. Contexte et Objectif

L'objectif de cette étude est d'intégrer le service de stockage d'objets **Vercel Blob Storage** dans l'architecture modulaire du projet **`playground/fastapi-python-boilerplate`**.

Grâce au pattern **Storage Adapter** mis en place dans `app/shared/storage/`, l'application peut utiliser Vercel Blob en production sans modifier la moindre ligne de code dans les sous-modules métier (`app/content/audio`, `app/content/video`, etc.).

---

## 2. Configuration & Clés d'Accès

Les variables d'environnement suivantes ont été configurées dans `.env` et déclarées dans `app/core/config.py` :

```ini
STORAGE_PROVIDER=vercel_blob
VERCEL_BLOB_STORE_ID="store_UpipzFtMHvTlTCVb"
VERCEL_BLOB_READ_WRITE_TOKEN="vercel_blob_rw_UpipzFtMHvTlTCVb_rjZ4WbiKPSOuL1CWkUr1CjpSvIDBNe"
```

---

## 3. Spécification Technique du VercelBlobStorageProvider

L'API REST v7 officielle de Vercel Blob requiert le header `x-vercel-blob-access` (avec `private` ou `public` selon la configuration du store) :

```python
# app/shared/storage/vercel_blob.py
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
```

---

## 4. Factory & Bascule Dynamique

La fonction `get_storage_provider()` dans `app/shared/storage/__init__.py` injecte automatiquement le bon provider selon la variable d'environnement `STORAGE_PROVIDER` :

* `STORAGE_PROVIDER=local` ➔ `LocalStorageProvider` (dev local sur disque)
* `STORAGE_PROVIDER=s3` ➔ `S3StorageProvider` (AWS S3)
* `STORAGE_PROVIDER=vercel_blob` ➔ `VercelBlobStorageProvider` (Vercel Store Private/Public)

---

## 5. Validation & Test d'Upload

Le test d'envoi synchrone/asynchrone valide que le fichier est bien déposé sur Vercel Blob :

```text
Using storage provider: VercelBlobStorageProvider
Uploaded URL: https://upipzftmhvtltcvb.private.blob.vercel-storage.com/demo/test_file-C2fFsY3yGybLdT7tSJiKFjo4xq2uo0.txt
```
