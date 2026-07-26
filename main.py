from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.routes import data, web
from db.database import engine, Base
from db import models  # noqa: F401

app = FastAPI(
    title="COOP-CA AMIFOND + FastAPI",
    description="FastAPI Core Banking System on Vercel",
    version="2.5.0",
)

# Mounting static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

if engine:
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        pass

app.include_router(web.router)
app.include_router(data.router, prefix="/api", tags=["Data API"])
