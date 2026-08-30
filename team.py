from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

import os

from agno.team import Team
from agno.agent import Agent  # type: ignore
from agno.models.groq import Groq  # type: ignore


eng_agent = Agent(name="English Agent", role="You are a helpful assistant that speaks English.")
chinese_agent = Agent(name="Chinese Agent", role="You are a helpful assistant that speaks Chinese.")
hindi_agent = Agent(name="Hindi Agent", role="You are a helpful assistant that speaks Hindi.")

team = Team(
    name = "Answer & Translate Team",
    members = [eng_agent, chinese_agent, hindi_agent],
    model = Groq(id="qwen/qwen3.8-27b"),
    markdown = True,
    show_members_responses = True,
    instructions = "You are a team of agents that answer questions and translate the answers into multiple languages.Do not just call one agent to answer the question, but rather have all agents answer the question and then translate the answers into their respective languages."
)




team.print_response("What is the capital of India?")
