from sqlalchemy.orm import Session
from app.data.models import ItemModel

class DataService:
    @staticmethod
    def get_all_items(db: Session):
        if db is not None:
            try:
                return db.query(ItemModel).all()
            except Exception:
                pass
        return None

    @staticmethod
    def get_item_by_id(db: Session, item_id: int):
        if db is not None:
            try:
                return db.query(ItemModel).filter(ItemModel.id == item_id).first()
            except Exception:
                pass
        return None

    @staticmethod
    def create_item(db: Session, name: str, value: int):
        if db is None:
            return None
        new_item = ItemModel(name=name, value=value)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
