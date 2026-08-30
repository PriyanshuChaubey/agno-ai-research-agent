from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

import os


from agno.agent import Agent  # type: ignore
from agno.models.groq import Groq  # type: ignore

from agno.tools.duckduckgo import DuckDuckGoTools  # type: ignore
from agno.tools.yfinance import YFinanceTools  # type: ignore


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3.8-27b"),
        tools=[DuckDuckGoTools(), HackerNewsTools(), YFinanceTools(all=True)],
        markdown=True,
        description="You are a comprehensive investment analyst with access to all financial data functions.",
        instructions=[
            "Use any financial function as needed for investment analysis",
            "Format your response using markdown and use tables to display data",
            "Provide detailed analysis and insights based on the data",
            "Include relevant financial metrics and recommendations",
        ],
        add_datetime_to_context=True
    )

groq_agent = build_agent()

groq_agent.print_response("Share the NVDA stock price and recent historical performance")
