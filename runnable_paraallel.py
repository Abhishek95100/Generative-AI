from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core .runnables import RunnableSequence
import os


load_dotenv()

model1 = ChatGroq(
    model="llama-3.3-70b-versatile"
)
promt = PromptTemplate(
    template='generate a linkedin post about {topic}',
    input_variables=['topic']
)

parser =  StrOutputParser

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(promt,model1,parser),
    'linkedin':RunnableSequence(promt,model1,parser)
})

parallel_chain.invoke({'topic':'Ai'})

