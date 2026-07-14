from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence 
import os


load_dotenv()

model1 = ChatGroq(
    model="llama-3.3-70b-versatile"
)

Prompt = PromptTemplate(
    template= 'write a joke about {topic}',
    input_variables=['topic']
)

parsr = StrOutputParser

Prompt2=PromptTemplate(
    template='Explain the following joke -{text}',
    input_variables=['text']
)
chain = RunnableSequence(Prompt,model1,parsr,Prompt2,model1,parsr)

print(chain.invoke({'topic':'AI'}))