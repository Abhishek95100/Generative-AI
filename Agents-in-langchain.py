from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import requests
import os

# API Key
os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6JfaR0VJWSX8Z0Zj8U9ChYKFx4yIiNBoBJqT6-PUCKR0w"

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)
#search
search_tool = DuckDuckGoSearchRun()
# Invoke
results = search_tool.invoke('top news in india today')
print(results)









