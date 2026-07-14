from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='llama-3.1-8b-instant', temperature=1.5,max_completion_tokens = 10)

result = model.invoke("write a 10 line poem on cricket")

print(result.content)
