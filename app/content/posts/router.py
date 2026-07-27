from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.content.posts.services import PostService

router = APIRouter()

@router.get("/")
def list_posts(db: Session = Depends(get_db)):
    posts = PostService.get_all_posts(db)
    return {"status": "ok", "count": len(posts), "posts": posts}

@router.post("/")
def create_post(title: str, body: str, author: str = "Admin", db: Session = Depends(get_db)):
    post = PostService.create_post(db, title, body, author)
    if not post:
        return {"error": "Database not configured"}
    return {"status": "created", "post_id": post.id, "title": post.title}
