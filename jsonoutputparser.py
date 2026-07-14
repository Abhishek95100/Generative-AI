from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os 
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    api_key="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",
    model="llama-3.1-8b-instant"
)
parser = JsonOutputParser()
template = PromptTemplate(
    template="Give me 5 facts about {topic}\n{format_instruction}",
    input_variables=['topic'],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)


chain = template |model | parser

result = chain.invoke({'topic':'black hole'})


print(result)
