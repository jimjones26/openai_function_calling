# ------------------------------------------------------------------
# Import modules
# ------------------------------------------------------------------

import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from datetime import datetime, timedelta
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage

# ------------------------------------------------------------------
# Load opeaai api key from .env file
# ------------------------------------------------------------------

load_dotenv()


# ------------------------------------------------------------------
# Ask ChatGPT a question
# ------------------------------------------------------------------

completetion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "What is the next flight from Amsterdam to New York?",
        }
    ],
)

output = completetion.choices[0].message.content
print(output)

# ------------------------------------------------------------------
# Use OpenAI's function calling feature
# ------------------------------------------------------------------

function_descriptions = [
    {
        "name": "get_flight_info",
        "description": "Get flight information between two locations.",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure airport, e.g. DUS",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination airport, e.g. HAM",
                },
            },
            "required": ["loc_origin", "loc_destination"],
        },
    }
]

user_prompt = "What is the next flight from Amsterdam to New York?"

completetion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[{"role": "user", "content": user_prompt}],
    functions=function_descriptions,
    function_call="auto",
)

output = completetion.choices[0].message
print(output)
