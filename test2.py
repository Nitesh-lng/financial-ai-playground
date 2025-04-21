from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
import os

load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

test_agent=Agent(
    model=Groq(
        id="llama-3.3-70b-versatile"
    ),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        )],
    show_tool_calls=True,
    markdown=True,
    instructions="show me with tabels",
    debug_mode=True
)

test_agent.print_response("which stock is the best to invest in 2025")