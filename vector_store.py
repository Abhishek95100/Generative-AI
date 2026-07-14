from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

#your source documents

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models.")
]

# intialize embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#creat chrom vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name ="my_collection"
)

#convertt vectorstore into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k":2})

query ="what is chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n---Result {i+1}---")
    print(doc.page_content)

