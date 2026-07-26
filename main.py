from fastapi import FastAPI
from api.routes import data, web

app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)

app.include_router(web.router)
app.include_router(data.router, prefix="/api", tags=["Data API"])
