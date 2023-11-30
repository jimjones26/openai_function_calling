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
