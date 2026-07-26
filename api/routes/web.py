from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def read_root():
    html_path = Path("templates/index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    return HTMLResponse(content=html_content, status_code=200)
