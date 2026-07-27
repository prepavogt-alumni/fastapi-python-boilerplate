from sqlalchemy.orm import Session
from app.content.posts.models import PostContent
from app.content.models import ContentType

class PostService:
    @staticmethod
    def get_all_posts(db: Session):
        if db is not None:
            try:
                return db.query(PostContent).all()
            except Exception:
                pass
        return []

    @staticmethod
    def create_post(db: Session, title: str, body_markdown: str, author: str = "Admin"):
        if db is None:
            return None
        slug = title.lower().replace(" ", "-")
        post = PostContent(
            title=title,
            slug=slug,
            type=ContentType.POST,
            body_markdown=body_markdown,
            author=author
        )
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
