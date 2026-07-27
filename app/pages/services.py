from sqlalchemy.orm import Session
from app.pages import models
from app.pages import data as pd

def get_project_config(db: Session = None):
    if db is not None:
        try:
            cfg = db.query(models.ProjectConfig).first()
            if cfg:
                return {
                    "title": cfg.title,
                    "subtitle": cfg.subtitle,
                    "description": cfg.description,
                    "environment": cfg.environment,
                    "tech_tags": cfg.tech_tags or pd._TECH_TAGS
                }
        except Exception:
            pass

    return {
        "title": "FastAPI + Postgres Boilerplate",
        "subtitle": "Production Serverless Boilerplate · Neon PostgreSQL · Vercel",
        "description": "Boilerplate moderne et modulaire avec FastAPI, Neon PostgreSQL et Jinja2 SSR",
        "environment": "Production",
        "tech_tags": pd._TECH_TAGS
    }

def get_design_tokens(db: Session = None):
    if db is not None:
        try:
            tokens = db.query(models.DesignToken).all()
            if tokens:
                brand = [(t.name, t.value, t.label) for t in tokens if t.category == "brand"]
                functional = [(t.name, t.value, t.label) for t in tokens if t.category == "functional"]
                surface = [(t.name, t.value, t.label) for t in tokens if t.category == "surface"]
                shadows = [(t.name, t.value) for t in tokens if t.category == "shadow"]
                spacings = [(t.name, t.value, t.label) for t in tokens if t.category == "spacing"]

                return {
                    "colors_brand": brand,
                    "colors_functional": functional,
                    "colors_surface": surface,
                    "shadows": shadows,
                    "spacings": spacings
                }
        except Exception:
            pass

    return {
        "colors_brand": pd._COLORS_BRAND,
        "colors_functional": pd._COLORS_FUNCTIONAL,
        "colors_surface": pd._COLORS_SURFACE,
        "shadows": pd._SHADOWS,
        "spacings": pd._SPACINGS
    }

def get_modules_data(db: Session = None):
    if db is not None:
        try:
            db_modules = db.query(models.Module).all()
            if db_modules:
                res = []
                for m in db_modules:
                    endpoints = [(e.method, e.path, e.summary) for e in m.endpoints]
                    res.append({
                        "slug": m.slug,
                        "name": m.name,
                        "tagline": m.tagline,
                        "description": m.description,
                        "category": m.category,
                        "badge": m.badge,
                        "badge_class": m.badge_class,
                        "version": m.version,
                        "status": m.status,
                        "maintainer": m.maintainer,
                        "compatibility": m.compatibility,
                        "doc_intro": m.doc_intro,
                        "install_snippet": m.install_snippet,
                        "config_snippet": m.config_snippet,
                        "note": m.note,
                        "endpoint_count": len(endpoints),
                        "endpoints": endpoints
                    })
                return res
        except Exception:
            pass

    return pd._MODULES

def get_changelog_data(db: Session = None):
    if db is not None:
        try:
            releases = db.query(models.ChangelogRelease).all()
            if releases:
                return [{
                    "version": r.version,
                    "date": r.date_str,
                    "tag": r.tag,
                    "tag_class": r.tag_class,
                    "changes": r.changes
                } for r in releases]
        except Exception:
            pass

    return pd._CHANGELOG

def get_tech_stack_data(db: Session = None):
    if db is not None:
        try:
            stack = db.query(models.TechStackItem).all()
            if stack:
                return [{"name": s.name, "version": s.version, "description": s.description} for s in stack]
        except Exception:
            pass

    return pd._TECH_STACK

def get_infra_data(db: Session = None):
    if db is not None:
        try:
            infra = db.query(models.InfraItem).all()
            if infra:
                return [{"name": i.name, "tag": i.tag, "description": i.description} for i in infra]
        except Exception:
            pass

    return pd._INFRA_ESSENTIALS
