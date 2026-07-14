from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv 

load_dotenv


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text_splitter = SemanticChunker(
   HuggingFaceEmbeddings(),breakpoint_threshold_type="standerd_deviation",
   breakpoint_threshold_amount=1
)

sample ="""
Farmers prepare fields and plant seeds for the next crop. The weather is nice with bright sunshine and fresh air. Cricket is very popular in India, and the IPL is a famous cricket league enjoyed by fans all over the world.

Farmers grow crops in the fields during good weather.
Cricket is very popular in India, and IPL is a famous league loved worldwide.




"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)