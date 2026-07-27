from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.database import engine, Base

# Importation des routers des apps
from app.pages.router import router as pages_router
from app.data.router import router as data_router
from app.content.router import content_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Production Serverless Boilerplate avec Neon PostgreSQL, Vercel et Apps Modulaires",
    version=settings.VERSION,
)

# Montage des fichiers statiques
app.mount("/static", StaticFiles(directory="static"), name="static")

# Auto-création des tables DB au démarrage
if engine:
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        pass

# 1. Routes Web Jinja2 (SSR sur /)
app.include_router(pages_router)

# 2. Routes API JSON (/api & /api/v1)
app.include_router(data_router, prefix="/api", tags=["Data API"])
app.include_router(content_router, prefix="/api/v1")
