from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field


load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    api_key="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",
    model="llama-3.1-8b-instant"
)

class person(BaseModel):
    name: str = Field(description='Name of the person')
    age: str = Field(gt=18,description='Age of the person')

    city: str = Field(description='name of the city the person belongs to')

paser = PydanticOutputParser(pydantic_object= person)
template = PromptTemplate(
    template="""
Generate the name, age and city of a fictional {place} person.

{format_instructions}
""",
    input_variables=["place"],
    
)
partial_variables={
    "format_instructions": paser.get_format_instructions()
}
chain = template|model|paser

final_result = chain.invoke({'place':'sri lankan'})

print(final_result)