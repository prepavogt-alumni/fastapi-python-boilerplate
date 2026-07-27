from abc import ABC, abstractmethod
from typing import BinaryIO

class StorageProvider(ABC):
    @abstractmethod
    async def upload(self, file_obj: BinaryIO, filename: str, folder: str) -> str:
        """Upload un fichier et retourne son URL ou son chemin relatif d'accès."""
        pass

    @abstractmethod
    async def delete(self, file_path: str) -> bool:
        """Supprime un fichier du stockage."""
        pass
