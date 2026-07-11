from fastapi import APIRouter


router = APIRouter(
    prefix="/football",
    tags=["Football"]
)


@router.get("/live")
async def get_live_matches():
    return {
        "message": "Live matches endpoint"
    }


@router.get("/upcoming")
async def get_upcoming_matches():
    return {
        "message": "Upcoming matches endpoint"
    }


@router.get("/player-profile/{player_name}")
async def get_player_profile(player_name: str):
    return {
        "player_name": player_name
    }


@router.get("/match/{fixture_id}")
async def get_match_details(fixture_id: int):
    return {
        "fixture_id": fixture_id
    }
