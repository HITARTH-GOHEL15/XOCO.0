
from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.football import router as football_router


app = FastAPI(
    title="XOCO.0 AI Backend",
    description="AI-powered football analysis backend",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(football_router)
