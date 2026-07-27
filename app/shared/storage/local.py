import os
import shutil
from typing import BinaryIO
from app.shared.storage.base import StorageProvider

class LocalStorageProvider(StorageProvider):
    def __init__(self, base_dir: str = "static/uploads"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    async def upload(self, file_obj: BinaryIO, filename: str, folder: str) -> str:
        target_dir = os.path.join(self.base_dir, folder)
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(target_dir, filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file_obj, buffer)
            
        return f"/{file_path}"

    async def delete(self, file_path: str) -> bool:
        clean_path = file_path.lstrip("/")
        if os.path.exists(clean_path):
            os.remove(clean_path)
            return True
        return False
