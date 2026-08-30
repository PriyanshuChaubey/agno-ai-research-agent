from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

import os


from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3.8-27b"),
        db = db,
        add_history_to_context = True,
        markdown=True,
    )

groq_agent = build_agent()

groq_agent.print_response("What is the capital of Australia?")
groq_agent.print_response("What is the best time to visit it?")
