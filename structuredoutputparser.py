from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    api_key="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",
    model="llama-3.1-8b-instant"
)

class Facts(BaseModel):
    fact_1: str = Field(description="fact 1 about the topic")
    fact_2: str = Field(description="fact 2 about the topic")
    fact_3: str = Field(description="fact 3 about the topic")

parser = PydanticOutputParser(pydantic_object=Facts)

template = PromptTemplate(
    template="""
Give 3 facts about {topic}.

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = template | model |parser

result = chain.invoke({'topic':'black hole'})

print (result)
