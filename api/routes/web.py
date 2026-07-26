from collections import Counter
from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.database import get_db
from services import pages_service as ps
from api.routes import pages_data as pd

router = APIRouter()

templates = Jinja2Templates(directory="templates")

def _get_base_context(db: Session):
    config = ps.get_project_config(db)
    return {
        "project_config": config,
        "environment": config.get("environment", "Production")
    }

@router.get("/", response_class=HTMLResponse)
def home_page(request: Request, db: Session = Depends(get_db)):
    context = _get_base_context(db)
    modules = ps.get_modules_data(db)
    tech_stack = ps.get_tech_stack_data(db)
    infra_essentials = ps.get_infra_data(db)

    context.update({
        "latest_modules": modules[:4],
        "total_modules": len(modules),
        "tech_tags": context["project_config"].get("tech_tags", []),
        "infra_essentials": infra_essentials,
        "tech_stack": tech_stack,
    })

    return templates.TemplateResponse(request=request, name="pages/home.html", context=context)

@router.get("/modules", response_class=HTMLResponse)
def modules_page(request: Request, db: Session = Depends(get_db)):
    context = _get_base_context(db)
    modules = ps.get_modules_data(db)
    cat_counts = Counter(m["category"] for m in modules)
    badge_counts = Counter(m["badge"] for m in modules)
    
    context.update({
        "modules": modules,
        "category_filters": sorted(cat_counts.items()),
        "badge_filters": [
            (pd._BADGE_ESS, badge_counts.get(pd._BADGE_ESS, 0)),
            (pd._BADGE_MID, badge_counts.get(pd._BADGE_MID, 0)),
            (pd._BADGE_ADV, badge_counts.get(pd._BADGE_ADV, 0)),
        ],
    })

    return templates.TemplateResponse(request=request, name="pages/modules.html", context=context)

@router.get("/modules/{slug}", response_class=HTMLResponse)
def module_detail_page(request: Request, slug: str, db: Session = Depends(get_db)):
    context = _get_base_context(db)
    modules = ps.get_modules_data(db)
    module = next((m for m in modules if m["slug"] == slug), None)
    if not module:
        raise HTTPException(status_code=404, detail="Module non trouvé")
        
    context.update({
        "module": module,
        "all_modules": modules,
    })

    return templates.TemplateResponse(request=request, name="pages/module_detail.html", context=context)

@router.get("/apps", response_class=HTMLResponse)
def apps_page(request: Request, db: Session = Depends(get_db)):
    context = _get_base_context(db)
    modules = ps.get_modules_data(db)
    context.update({
        "modules": modules,
    })
    return templates.TemplateResponse(request=request, name="pages/apps.html", context=context)

@router.get("/design-system", response_class=HTMLResponse)
def design_system_page(request: Request, db: Session = Depends(get_db)):
    context = _get_base_context(db)
    tokens = ps.get_design_tokens(db)
    
    context.update({
        "colors_brand": tokens["colors_brand"],
        "colors_functional": tokens["colors_functional"],
        "colors_surface": tokens["colors_surface"],
        "shadows": tokens["shadows"],
        "spacings": tokens["spacings"],
    })

    return templates.TemplateResponse(request=request, name="pages/design_system.html", context=context)

@router.get("/documentation", response_class=HTMLResponse)
def docs_page(request: Request, db: Session = Depends(get_db)):
    context = _get_base_context(db)
    return templates.TemplateResponse(request=request, name="pages/docs.html", context=context)

@router.get("/changelog", response_class=HTMLResponse)
def changelog_page(request: Request, db: Session = Depends(get_db)):
    context = _get_base_context(db)
    changelog = ps.get_changelog_data(db)
    context.update({"changelog": changelog})
    return templates.TemplateResponse(request=request, name="pages/changelog.html", context=context)

@router.get("/demo", response_class=HTMLResponse)
def demo_page(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})
