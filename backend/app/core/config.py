
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API keys
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# base URLs
API_FOOTBALL_BASE_URL = "https://v3.football.api-sports.io"
