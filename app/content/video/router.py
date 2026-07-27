from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.content.video.services import VideoService

router = APIRouter()

@router.get("/")
def list_videos(db: Session = Depends(get_db)):
    videos = VideoService.get_all_videos(db)
    return {"status": "ok", "count": len(videos), "videos": videos}

@router.post("/")
def create_video(title: str, video_url: str, thumbnail_url: str = None, db: Session = Depends(get_db)):
    video = VideoService.create_video(db, title, video_url, thumbnail_url)
    if not video:
        return {"error": "Database not configured"}
    return {"status": "created", "video_id": video.id, "title": video.title}
