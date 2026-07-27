from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.content.audio.services import AudioService

router = APIRouter()

@router.get("/")
def list_audios(db: Session = Depends(get_db)):
    audios = AudioService.get_all_audios(db)
    return {"status": "ok", "count": len(audios), "audios": audios}

@router.post("/")
def create_audio(title: str, file_path: str, duration: int = 0, db: Session = Depends(get_db)):
    audio = AudioService.create_audio(db, title, file_path, duration)
    if not audio:
        return {"error": "Database not configured"}
    return {"status": "created", "audio_id": audio.id, "title": audio.title}
