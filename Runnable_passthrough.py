from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence ,RunnablePassthrough
import os


load_dotenv()

model1 = ChatGroq(
    model="llama-3.3-70b-versatile"
)

Prompt1 = PromptTemplate(
    template= 'write a joke about {topic}',
    input_variables=['topic']
)

parsr = StrOutputParser

Prompt2=PromptTemplate(
    template='Explain the following joke -{text}',
    input_variables=['text']
)
joke_gen_chain =RunnableSequence(Prompt1,model1,parsr)

parallel_chain = RunnableSequence({
    'joke':RunnablePassthrough(),
    'explanation': RunnableSequence(Prompt2,model1,parsr)

})

final_chain = RunnableSequence(joke_gen_chai ,parallel_chain)


print(final_chain.invoke({'topic':'cricket'}))