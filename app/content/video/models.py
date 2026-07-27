from sqlalchemy import Column, Integer, String, ForeignKey
from app.content.models import Content, ContentType

class VideoContent(Content):
    __tablename__ = "content_videos"

    id = Column(Integer, ForeignKey("contents.id", ondelete="CASCADE"), primary_key=True)
    video_url = Column(String(512), nullable=True)
    thumbnail_url = Column(String(512), nullable=True)
    resolution = Column(String(50), nullable=True)  # ex: "1080p", "4K"
    duration_seconds = Column(Integer, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": ContentType.VIDEO,
    }
