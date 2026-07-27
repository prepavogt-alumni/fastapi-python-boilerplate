from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class ProjectConfig(Base):
    __tablename__ = "project_configs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, default="FastAPI + Postgres Boilerplate")
    subtitle = Column(String, default="Production Serverless Boilerplate · Neon PostgreSQL · Vercel")
    description = Column(Text, default="Boilerplate moderne et modulaire avec FastAPI, Neon PostgreSQL et Jinja2 SSR")
    environment = Column(String, default="Production")
    tech_tags = Column(JSON, default=list)

class DesignToken(Base):
    __tablename__ = "design_tokens"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)  # brand, functional, surface, shadow, spacing
    name = Column(String, nullable=False)   # e.g., "Primary", "--shadow-sm", "--spacing-md"
    value = Column(String, nullable=False)  # e.g., "#0070f3", "0 1px 2px ...", "1rem"
    label = Column(String)                  # e.g., "--primary-color · #0070f3", "16px"

class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    tagline = Column(String)
    description = Column(Text)
    category = Column(String, index=True)  # Core, Data, Frontend, Ops
    badge = Column(String)                # Essentiel, Intermédiaire, Avancé
    badge_class = Column(String)          # badge-primary, badge-warning...
    version = Column(String, default="v1.0")
    status = Column(String, default="Production Ready")
    maintainer = Column(String)
    compatibility = Column(String)
    doc_intro = Column(Text)
    install_snippet = Column(Text)
    config_snippet = Column(Text)
    note = Column(Text)

    endpoints = relationship("Endpoint", back_populates="module", cascade="all, delete-orphan")

class Endpoint(Base):
    __tablename__ = "endpoints"

    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=True)
    category = Column(String, index=True)
    method = Column(String, nullable=False)   # GET, POST, PATCH, etc.
    path = Column(String, nullable=False)     # /api/v1/auth/login
    summary = Column(String)                  # "Connexion"

    module = relationship("Module", back_populates="endpoints")

class ChangelogRelease(Base):
    __tablename__ = "changelog_releases"

    id = Column(Integer, primary_key=True, index=True)
    version = Column(String, nullable=False)
    date_str = Column(String)
    tag = Column(String)
    tag_class = Column(String)
    changes = Column(JSON, default=list)

class TechStackItem(Base):
    __tablename__ = "tech_stack_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    version = Column(String)
    description = Column(Text)

class InfraItem(Base):
    __tablename__ = "infra_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tag = Column(String)
    description = Column(Text)
