import os
from dotenv import load_dotenv

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

# Load .env
load_dotenv()

# Gemini API Key

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Search Tool
search_tool = DuckDuckGoSearchRun()

# Weather Tool
@tool
def get_weather_data(city: str) -> str:
    """Returns the current weather of a city."""
    # Yahan actual weather API laga sakte ho
    return f"Weather information for {city} is not available right now."

# Prompt
prompt = hub.pull("hwchase17/react")

# Create Agent
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

# Agent Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

# Run Agent
response = agent_executor.invoke(
    {
        "input": "Find the capital of Madhya Pradesh, then find its current weather condition."
    }
)

print(response["output"])