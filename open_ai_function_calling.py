# ------------------------------------------------------------------
# Import modules
# ------------------------------------------------------------------

import os
import json
import openai

from datetime import datetime, timedelta
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage

# ------------------------------------------------------------------
# Load opeaai api key from .env file
# ------------------------------------------------------------------

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
