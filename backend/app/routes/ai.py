
from fastapi import APIRouter
from pydantic import BaseModel

from app.clients.gemini import generate_ai_assistant, generate_match_analysis, generate_player_analysis
from app.routes.football import (
    get_live_matches,
    get_match_details,
    get_player_profile,
    get_upcoming_matches,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


class PlayerAnalysisRequest(BaseModel):
    fixture_id: int
    player_name: str


class MatchAnalysisRequest(BaseModel):
    fixture_id: int


class AiAssistantRequest(BaseModel):
    question: str


@router.post("/player-analysis")
async def player_analysis(request: PlayerAnalysisRequest):

    player_profile = get_player_profile(request.player_name)

    match_data = get_match_details(request.fixture_id)

    return generate_player_analysis(
        player_profile=player_profile,
        match=match_data["match"],
        statistics=match_data["statistics"],
        player_stats=match_data["players"],
        events=match_data["events"],
        lineups=match_data["lineups"],
    )


@router.post("/match-analysis")
async def match_analysis(request: MatchAnalysisRequest):

    match_data = get_match_details(request.fixture_id)

    return generate_match_analysis(
        match_data
    )


@router.post("/ai-assistant")
async def ai_assistant(request: AiAssistantRequest):

    question = request.question

    return generate_ai_assistant(
        question
    )
