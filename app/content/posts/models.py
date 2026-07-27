from sqlalchemy import Column, Integer, Text, ForeignKey
from app.content.models import Content, ContentType

class PostContent(Content):
    __tablename__ = "content_posts"

    id = Column(Integer, ForeignKey("contents.id", ondelete="CASCADE"), primary_key=True)
    body_markdown = Column(Text, nullable=True)
    author = Column(Text, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": ContentType.POST,
    }
