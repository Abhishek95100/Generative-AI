from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os 

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    api_key="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",
    model="llama-3.1-8b-instant"
)

# 1st prompt detailed report
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

#2nd prompt summary
template2 = PromptTemplate(
    template='write a 5 line summary on the following text./n  {text}',
    input_variables=['text']
)

Prompt1 = template1.format(topic="black hole")

result = model.invoke(Prompt1)

Prompt2 = template2.format(text=result.content)

result1 = model.invoke(Prompt2)

print(result.content)
