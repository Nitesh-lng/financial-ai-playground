from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

test_agent=Agent(
    model=Groq(
        id="llama-3.3-70b-versatile"
    )
)

test_agent.print_response("who is the biggest player in the finance in the 2022")