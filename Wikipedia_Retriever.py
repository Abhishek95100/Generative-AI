from langchain_community.retrievers import WikipediaRetriever


#initialize the retriever(optionl:set language and top_k)
retriever = WikipediaRetriever(top_k_results=2,lang="en")

#Define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

#Get relevant wikipedia documents
docs = retriever.invoke(query)


#print retriver content 
for i,doc in enumerate(docs):
    print(f"\n---Result{i+1}---")
    print(f"content\n{doc.page_content}...")