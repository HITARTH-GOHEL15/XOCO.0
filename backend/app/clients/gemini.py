import json

from google import genai

from app.core.config import GEMINI_API_KEY
from app.prompts.player_prompt import build_player_analysis_prompt
from app.prompts.match_prompt import build_match_analysis_prompt
from app.prompts.assistant_prompt import build_assistant_prompt

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# player analysis function
def generate_player_analysis(
    player_profile,
    match,
    statistics,
    player_stats,
    events,
    lineups,
):

    prompt = build_player_analysis_prompt(
        player_profile,
        match,
        statistics,
        player_stats,
        events,
        lineups,
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0.4,
            },
        )
        if not response.text:
            return "The model returned an empty response. Please try again"
        return json.loads(response.text)

    except Exception as e:
        return f"Sorry, couldn't generate a response right now. ({e})"


# match analysis function
def generate_match_analysis(
        match_data
):

    prompt = build_match_analysis_prompt(
        match_data
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0.4,
            },
        )
        if not response.text:
            return "The model returned an empty response. Please try again"
        return json.loads(response.text)

    except Exception as e:
        return f"Sorry, couldn't generate a response right now. ({e})"


# ai-assistant function
def generate_ai_assistant(
        question
):

    prompt = build_assistant_prompt(
        question
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0.4,
            },
        )
        if not response.text:
            return "The model returned an empty response. Please try again"
        return json.loads(response.text)

    except Exception as e:
        return f"Sorry, couldn't generate a response right now. ({e})"
