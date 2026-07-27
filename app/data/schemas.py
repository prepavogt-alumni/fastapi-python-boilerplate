from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    value: int = 0

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True
