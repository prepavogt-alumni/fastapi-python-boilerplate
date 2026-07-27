from fastapi import APIRouter
from app.content.posts.router import router as posts_router
from app.content.audio.router import router as audio_router
from app.content.video.router import router as video_router

content_router = APIRouter(prefix="/content", tags=["Content Domain"])

content_router.include_router(posts_router, prefix="/posts", tags=["Posts"])
content_router.include_router(audio_router, prefix="/audio", tags=["Audio"])
content_router.include_router(video_router, prefix="/video", tags=["Video"])
