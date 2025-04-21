from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.agent import Agent
import os
from phi.storage.agent.sqlite import SqlAgentStorage
from dotenv import load_dotenv
from phi.playground import Playground , serve_playground_app

load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")


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
    instructions=["show me with tabels"],
    storage=SqlAgentStorage(
        table_name="financial_advisor",
        db_file="financial_advisor.db"),
    debug_mode=True,
    add_history_to_messages=True
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
    instructions=["Always include the source of the data"],
    storage=SqlAgentStorage(
        table_name="web_researcher",
        db_file="web_researcher.db"),
    add_history_to_messages=True,
)



app=Playground(
    agents=[
        financial_agent,
        web_researcher
    ]
).get_app()


if __name__ ==  "__main__":
    serve_playground_app("playground:app",reload=True)