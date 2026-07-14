from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key='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'
)

prompt = PromptTemplate(
    template="Write a summary for the following poem:\n{poem}",
    input_variables=["poem"]
)


Parser = StrOutputParser()
loader = TextLoader('cricket.text',encoding='utf-8')

docs = loader.load()
print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | Parser

print(chain.invoke({'poem':docs[0].page_content}))