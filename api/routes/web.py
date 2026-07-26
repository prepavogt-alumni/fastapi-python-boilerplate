from collections import Counter
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.routes import pages_data as pd

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/home.html",
        context={
            "latest_modules": pd._MODULES[:4],
            "total_modules": len(pd._MODULES),
            "tech_tags": pd._TECH_TAGS,
            "infra_essentials": pd._INFRA_ESSENTIALS,
            "tech_stack": pd._TECH_STACK,
            "environment": "Production",
        }
    )

@router.get("/modules", response_class=HTMLResponse)
def modules_page(request: Request):
    cat_counts = Counter(m["category"] for m in pd._MODULES)
    badge_counts = Counter(m["badge"] for m in pd._MODULES)
    
    return templates.TemplateResponse(
        request=request,
        name="pages/modules.html",
        context={
            "modules": pd._MODULES,
            "category_filters": sorted(cat_counts.items()),
            "badge_filters": [
                (pd._BADGE_ESS, badge_counts.get(pd._BADGE_ESS, 0)),
                (pd._BADGE_MID, badge_counts.get(pd._BADGE_MID, 0)),
                (pd._BADGE_ADV, badge_counts.get(pd._BADGE_ADV, 0)),
            ],
            "environment": "Production",
        }
    )

@router.get("/modules/{slug}", response_class=HTMLResponse)
def module_detail_page(request: Request, slug: str):
    module = pd._MODULES_BY_SLUG.get(slug)
    if not module:
        raise HTTPException(status_code=404, detail="Module non trouvé")
        
    return templates.TemplateResponse(
        request=request,
        name="pages/module_detail.html",
        context={
            "module": module,
            "all_modules": pd._MODULES,
            "environment": "Production",
        }
    )

@router.get("/apps", response_class=HTMLResponse)
def apps_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/apps.html",
        context={
            "auth_endpoints": pd._AUTH,
            "enterprise_endpoints": pd._ENTERPRISE,
            "accounts_endpoints": pd._ACCOUNTS,
            "tiers_endpoints": pd._TIERS,
            "accounting_endpoints": pd._ACCOUNTING,
            "treasury_endpoints": pd._TREASURY,
            "loans_endpoints": pd._LOANS,
            "shares_endpoints": pd._SHARES,
            "events_endpoints": pd._EVENTS,
            "portals_endpoints": pd._CLIENT_PORTAL + pd._MANAGER_PORTAL,
            "environment": "Production",
        }
    )

@router.get("/design-system", response_class=HTMLResponse)
def design_system_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/design_system.html",
        context={
            "colors_brand": pd._COLORS_BRAND,
            "colors_functional": pd._COLORS_FUNCTIONAL,
            "colors_surface": pd._COLORS_SURFACE,
            "shadows": pd._SHADOWS,
            "spacings": pd._SPACINGS,
            "environment": "Production",
        }
    )

@router.get("/documentation", response_class=HTMLResponse)
def docs_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/docs.html",
        context={
            "environment": "Production",
        }
    )

@router.get("/changelog", response_class=HTMLResponse)
def changelog_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/changelog.html",
        context={
            "changelog": pd._CHANGELOG,
            "environment": "Production",
        }
    )

@router.get("/demo", response_class=HTMLResponse)
def demo_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )
