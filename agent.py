from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

import os


from agno.agent import Agent
from agno.models.groq import Groq

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3.8-27b"),
        tools=[DuckDuckGoTools(), HackerNewsTools()],
        markdown=True,
        instructions="You are a helpful research assistant.Use the available tools to find current and relevant information.When using web-based information, provide concise and useful answers.",
        add_datetime_to_context=True
    )

groq_agent = build_agent()

groq_agent.print_response("In 2026 which campany is going to hire more freshers in India in IT?")
