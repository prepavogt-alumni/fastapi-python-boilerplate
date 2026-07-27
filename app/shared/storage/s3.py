import os
from typing import BinaryIO
from app.shared.storage.base import StorageProvider

class S3StorageProvider(StorageProvider):
    def __init__(self, bucket_name: str = None):
        self.bucket_name = bucket_name or os.getenv("S3_BUCKET_NAME", "my-bucket")

    async def upload(self, file_obj: BinaryIO, filename: str, folder: str) -> str:
        # Implémentation indicative S3 via boto3 ou aioboto3
        key = f"{folder}/{filename}"
        return f"https://{self.bucket_name}.s3.amazonaws.com/{key}"

    async def delete(self, file_path: str) -> bool:
        return True
