from sqlalchemy.orm import Session
from app.content.video.models import VideoContent
from app.content.models import ContentType

class VideoService:
    @staticmethod
    def get_all_videos(db: Session):
        if db is not None:
            try:
                return db.query(VideoContent).all()
            except Exception:
                pass
        return []

    @staticmethod
    def create_video(db: Session, title: str, video_url: str, thumbnail_url: str = None, resolution: str = "1080p"):
        if db is None:
            return None
        slug = title.lower().replace(" ", "-")
        video = VideoContent(
            title=title,
            slug=slug,
            type=ContentType.VIDEO,
            video_url=video_url,
            thumbnail_url=thumbnail_url,
            resolution=resolution
        )
        db.add(video)
        db.commit()
        db.refresh(video)
        return video
