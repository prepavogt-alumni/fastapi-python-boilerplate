from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.routes import data, web
from db.database import engine, Base
from db import models  # noqa: F401

app = FastAPI(
    title="FastAPI + Postgres Boilerplate",
    description="Production Serverless Boilerplate with Neon PostgreSQL and Vercel",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

if engine:
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        pass

app.include_router(web.router)
app.include_router(data.router, prefix="/api", tags=["Data API"])
