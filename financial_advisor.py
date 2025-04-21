from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.agent import Agent
import os
from dotenv import load_dotenv
from phi.storage.agent.sqlite import SqlAgentStorage

load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")


storage=SqlAgentStorage(
    table_name="financial_advisor",
    db_file="financial_advisor.db"
)

financial_agent=Agent(
    name='Financial Advisor',
    model=Groq(
        id="meta-llama/llama-4-maverick-17b-128e-instruct"
    ),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        )
    ],
    show_tool_calls=True,
    markdown=True,
    instructions="show me with tabels",
    debug_mode=True
)


web_researcher=Agent(
    name='Web Researcher',
    model=Groq(
        id="meta-llama/llama-4-maverick-17b-128e-instruct"
    ),
    tools=[
        DuckDuckGo()
    ],
    show_tool_calls=True,
    markdown=True,
    instructions="Always include the source of the data"
)


agent_team=Agent(
    team=[
        financial_agent,
        web_researcher  
    ],
    model=Groq(
        id="meta-llama/llama-4-maverick-17b-128e-instruct"
    ),
    show_tool_calls=True,
    markdown=True,
    instructions="Always include the source of the data and always show table for financial data",
    debug_mode=True
)


agent_team.print_response("NTPC stock in india good to buy or not?")