from langchain_community.retrievers import WikipediaRetriever


#initialize the retriever(optionl:set language and top_k)
retriever = WikipediaRetriever(top_k_results=2,lang="en")

#Define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

#Get relevant wikipedia documents
docs = retriever.invoke(query)









from langchain_community.retrievers import WikipediaRetriever

print("Program started")

retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

print("Retriever created")

query = "the geopolitical history of india and pakistan from the perspective of a chinese"

docs = retriever.invoke(query)

print("Documents found:", len(docs))

for i, doc in enumerate(docs, 1):
    print(f"\nDocument {i}")
    print(doc.metadata)
    print(doc.page_content[:500])