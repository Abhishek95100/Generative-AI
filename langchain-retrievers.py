from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers.multi_query import MultiQueryRetriever

# Documents
all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression."),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity."),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation."),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity."),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy."),
]

# Embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector DB
vectorstore = FAISS.from_documents(all_docs, embedding_model)

# Retriever 1: similarity
similarity_retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

# LLM (required for MultiQueryRetriever)
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Retriever 2: multi-query
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm=llm
)

# Query
query = "How to improve energy levels and maintain balance?"

# RESULTS (MISSING IN YOUR CODE)
similarity_results = similarity_retriever.invoke(query)
multiquery_results = multiquery_retriever.invoke(query)

# Print
for i, doc in enumerate(similarity_results):
    print(f"\n--- Similarity Result {i+1} ---")
    print(doc.page_content)

print("*" * 100)

for i, doc in enumerate(multiquery_results):
    print(f"\n--- MultiQuery Result {i+1} ---")
    print(doc.page_content)