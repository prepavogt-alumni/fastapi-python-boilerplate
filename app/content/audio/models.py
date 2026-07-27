from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.content.models import Content, ContentType

class AudioContent(Content):
    __tablename__ = "content_audios"

    id = Column(Integer, ForeignKey("contents.id", ondelete="CASCADE"), primary_key=True)
    file_path = Column(String(512), nullable=True)
    duration_seconds = Column(Integer, nullable=True)
    bitrate = Column(Integer, nullable=True)
    transcript = Column(Text, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": ContentType.AUDIO,
    }
