from datetime import date

from fastapi import FastAPI
import requests

from app.core.config import API_FOOTBALL_BASE_URL, FOOTBALL_API_KEY, FOOTBALL_HEADERS, THE_SPORTS_DB_API_BASE_URL

app = FastAPI(title="XOCO.0")

# global - header for all fast API functions


@app.get("/")
def health():
    return {"status": "XOCO.0 Backend is running"}


@app.get("/football/live")
def live_football_matches():

    live_football_matches_url = f"{API_FOOTBALL_BASE_URL}/fixtures?live=all"

    try:
        # get live data from the API
        response = requests.get(
            live_football_matches_url, headers=FOOTBALL_HEADERS)

        if response.status_code == 200:
            return response.json()["response"]
        else:
            print("Something went wrong. Status code:", response.status_code)
    except Exception as e:
        print("Could not reach the API:", e)


@app.get("/football/upcoming")
def upcoming_football_matches():

    today = date.today().strftime("%Y-%m-%d")

    upcoming_football_matches_url = f"{API_FOOTBALL_BASE_URL}/fixtures?date={today}"

    try:
        # get live data from the API
        response = requests.get(
            upcoming_football_matches_url, headers=FOOTBALL_HEADERS)

        if response.status_code == 200:
            return response.json()["response"]
        else:
            print("Something went wrong. Status code:", response.status_code)
    except Exception as e:
        print("Could not reach the API:", e)


@app.get("/football/player-profile/{player_name}")
def football_player_details(
    player_name: str
):

    football_player_details_url = f"{THE_SPORTS_DB_API_BASE_URL}/searchplayers.php?p={player_name}"

    try:
        # get live data from the API
        response = requests.get(football_player_details_url)

        if response.status_code == 200:
            return response.json()["player"]
        else:
            print("Something went wrong. Status code:", response.status_code)
    except Exception as e:
        print("Could not reach the API:", e)


@app.get("/football/match/{fixture_id}")
def match_detail(
    fixture_id: int
):

    football_match_url = f"{API_FOOTBALL_BASE_URL}/fixtures?id={fixture_id}"

    lineups_url = f"{API_FOOTBALL_BASE_URL}/fixtures/lineups?fixture={fixture_id}"

    statistics_url = f"{API_FOOTBALL_BASE_URL}/fixtures/statistics?fixture={fixture_id}"

    events_url = f"{API_FOOTBALL_BASE_URL}/fixtures/events?fixture={fixture_id}"

    player_statistics_url = f"{API_FOOTBALL_BASE_URL}/fixtures/players?fixture={fixture_id}"

    try:
        # get live data from the API
        match = requests.get(football_match_url, headers=FOOTBALL_HEADERS)
        lineups = requests.get(lineups_url, headers=FOOTBALL_HEADERS)
        statistics = requests.get(statistics_url, headers=FOOTBALL_HEADERS)
        events = requests.get(events_url, headers=FOOTBALL_HEADERS)
        players = requests.get(player_statistics_url, headers=FOOTBALL_HEADERS)

        match.raise_for_status()
        lineups.raise_for_status()
        statistics.raise_for_status()
        events.raise_for_status()
        players.raise_for_status()

        return {
            "match": match.json()["response"],
            "lineups": lineups.json()["response"],
            "statistics": statistics.json()["response"],
            "events": events.json()["response"],
            "players": players.json()["response"]
        }

    except Exception as e:
        print("Could not reach the API:", e)
