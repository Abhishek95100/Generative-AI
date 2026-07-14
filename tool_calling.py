from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,ToolMessage
import requests
import os
from dotenv import load_dotenv


os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6J6VeJcfIsbXZgB5uIo42FihRkSvb0zrgTd3uKnNQ6Iog"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)
#tool create

@tool
def multiply(a:int, b:int) -> int:
    """ Give 2 numbers a and b this tool returns their product"""
    return a*b

print(multiply.invoke({'a':3,'b':4}))

multiply.name
multiply.description
multiply.args

#tool binding

llm_with_tools = llm.bind_tools([multiply])

response = llm_with_tools.invoke('can you multiply 3 with 10')

print(response.tool_calls)      # list dekhne ke liye

tool_call = response.tool_calls[0]

print(tool_call["args"])   # {'a': 3, 'b': 10}

output = multiply.invoke(tool_call["args"])

print(output)


# ToolMessage add karo
tool_message = ToolMessage(
    content=str(output),
    tool_call_id=tool_call["id"]
)

print(tool_message)