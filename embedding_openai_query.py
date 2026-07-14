from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

result = embedding.embed_query("Delhi is the capital of India")

print(len(result))   # dimension check
print(result[:5])    # first 5 values
