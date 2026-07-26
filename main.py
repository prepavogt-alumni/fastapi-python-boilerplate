from fastapi import FastAPI
from api.routes import data, web
from db.database import engine, Base
from db import models  # noqa: F401

app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)

if engine:
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        pass

app.include_router(web.router)
app.include_router(data.router, prefix="/api", tags=["Data API"])
