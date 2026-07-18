from fastapi import APIRouter

from app.clients.football_api import football_player_details, live_football_matches, match_detail, upcoming_football_matches


router = APIRouter(
    prefix="/football",
    tags=["Football"]
)


@router.get("/live")
def get_live_matches():
    return live_football_matches()


@router.get("/upcoming")
def get_upcoming_matches():
    return upcoming_football_matches()


@router.get("/player-profile/{player_name}")
def get_player_profile(player_name: str):
    return football_player_details(player_name)


@router.get("/match/{fixture_id}")
def get_match_details(fixture_id: int):
    return match_detail(fixture_id)
