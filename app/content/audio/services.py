from sqlalchemy.orm import Session
from app.content.audio.models import AudioContent
from app.content.models import ContentType

class AudioService:
    @staticmethod
    def get_all_audios(db: Session):
        if db is not None:
            try:
                return db.query(AudioContent).all()
            except Exception:
                pass
        return []

    @staticmethod
    def create_audio(db: Session, title: str, file_path: str, duration_seconds: int = 0):
        if db is None:
            return None
        slug = title.lower().replace(" ", "-")
        audio = AudioContent(
            title=title,
            slug=slug,
            type=ContentType.AUDIO,
            file_path=file_path,
            duration_seconds=duration_seconds
        )
        db.add(audio)
        db.commit()
        db.refresh(audio)
        return audio
