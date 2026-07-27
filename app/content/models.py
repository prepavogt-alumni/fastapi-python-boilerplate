import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from app.core.database import Base

class ContentType(str, enum.Enum):
    POST = "post"
    AUDIO = "audio"
    VIDEO = "video"

class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True)
    type = Column(Enum(ContentType), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "content",
    }
