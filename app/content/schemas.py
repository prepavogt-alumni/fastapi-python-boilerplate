from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.content.models import ContentType

class ContentBase(BaseModel):
    title: str
    type: ContentType

class ContentCreate(ContentBase):
    pass

class ContentResponse(ContentBase):
    id: int
    slug: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
