from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.data.services import DataService

router = APIRouter()

@router.get("/data")
def get_sample_data(db: Session = Depends(get_db)):
    items = DataService.get_all_items(db)
    if items:
        return {
            "source": "postgresql_neon",
            "data": [{"id": i.id, "name": i.name, "value": i.value} for i in items],
            "total": len(items)
        }

    return {
        "source": "mock",
        "data": [
            {"id": 1, "name": "Sample Item 1", "value": 100},
            {"id": 2, "name": "Sample Item 2", "value": 200},
            {"id": 3, "name": "Sample Item 3", "value": 300}
        ],
        "total": 3
    }

@router.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = DataService.get_item_by_id(db, item_id)
    if item:
        return {
            "source": "postgresql_neon",
            "item": {"id": item.id, "name": item.name, "value": item.value}
        }

    return {
        "source": "mock",
        "item": {
            "id": item_id,
            "name": "Sample Item " + str(item_id),
            "value": item_id * 100
        }
    }

@router.post("/items")
def create_item(name: str, value: int, db: Session = Depends(get_db)):
    new_item = DataService.create_item(db, name, value)
    if not new_item:
        return {"error": "Database connection not configured"}
    
    return {"message": "Item created", "item": {"id": new_item.id, "name": new_item.name, "value": new_item.value}}

@router.get("/status")
def get_status(db: Session = Depends(get_db)):
    db_status = "connected" if db is not None else "not configured"
    return {
        "status": "ok", 
        "database": db_status,
        "message": "API is running smoothly"
    }
