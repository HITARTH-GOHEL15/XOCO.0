
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API keys
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FOOTBALL_DATA_API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")

# base URLs
API_FOOTBALL_BASE_URL = "https://v3.football.api-sports.io"
FOOTBALL_DATA_API_BASE_URL = "https://api.football-data.org/v4"
THE_SPORTS_DB_API_BASE_URL = "https://www.thesportsdb.com/api/v1/json/3"

# football-headers (API-FOOTBALL)
FOOTBALL_HEADERS = {
    "x-apisports-key": FOOTBALL_API_KEY
}
