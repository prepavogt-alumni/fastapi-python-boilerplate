import os
from typing import Optional
from pathlib import Path
from pydantic import BaseModel

# Chargement manuel de .env s'il existe à la racine
root_dir = Path(__file__).resolve().parent.parent.parent
env_file = root_dir / ".env"

if env_file.exists():
    with open(env_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

class Settings(BaseModel):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "FastAPI + Postgres Boilerplate")
    VERSION: str = os.getenv("VERSION", "1.0.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "Production")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Database
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    POSTGRES_URL: Optional[str] = os.getenv("POSTGRES_URL")

    # Storage
    STORAGE_PROVIDER: str = os.getenv("STORAGE_PROVIDER", "vercel_blob")
    S3_BUCKET_NAME: Optional[str] = os.getenv("S3_BUCKET_NAME")
    
    # Vercel Blob Storage
    VERCEL_BLOB_STORE_ID: Optional[str] = os.getenv("VERCEL_BLOB_STORE_ID")
    VERCEL_BLOB_READ_WRITE_TOKEN: Optional[str] = os.getenv("VERCEL_BLOB_READ_WRITE_TOKEN")

    # Cache / Upstash Redis (Vercel KV)
    CACHE_PROVIDER: str = os.getenv("CACHE_PROVIDER", "upstash_redis")
    KV_REST_API_URL: Optional[str] = os.getenv("KV_REST_API_URL")
    KV_REST_API_TOKEN: Optional[str] = os.getenv("KV_REST_API_TOKEN")
    KV_REST_API_READ_ONLY_TOKEN: Optional[str] = os.getenv("KV_REST_API_READ_ONLY_TOKEN")
    REDIS_URL: Optional[str] = os.getenv("REDIS_URL")

    @property
    def sqlalchemy_database_url(self) -> Optional[str]:
        url = self.DATABASE_URL or self.POSTGRES_URL
        if url and url.startswith("postgres://"):
            return url.replace("postgres://", "postgresql://", 1)
        return url

settings = Settings()
