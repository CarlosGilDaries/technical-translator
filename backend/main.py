"""
Main entry point for the AI Technical Translator Pro backend.

Responsibilities: create the FastAPI app, register routers, configure middleware.
Do NOT add endpoints, business logic, or Pydantic models here.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.health import router as health_router
from api.routes.translation import router as translation_router

app = FastAPI(
    title="AI Technical Translator Pro",
    description="Translates technical text into easy-to-understand language.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(translation_router)

