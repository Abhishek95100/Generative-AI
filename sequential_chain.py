from langchain_groq  import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

Prompt1 = PromptTemplate(
    template='Generateer a detailed report on {topic}',
    input_variables=['topic']

)

Prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n{text}',
    input_variables=['text']
)

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()

chain = Prompt1 | model | parser | Prompt2 | model | parser

result = chain.invoke({'topic': 'Unemployment in india'})

print(result)

chain.get_graph().print_ascii()
