from langchain_community.document_loaders import WebBaseLoader

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key='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'
)

prompt = PromptTemplate(
    template="Answer the folloeing question \n{question} from the following text-\n{text}",
    input_variables=["question","text"]
)


Parser = StrOutputParser()

url ='https://www.flipkart.com/apple-macbook-neo-a18-pro-2026-pro-8-gb-256-gb-ssd-tahoe-mhfa4hn-a/p/itm9fce39e65bd7e?pid=COMHH8C57Y6W6NZU&lid=LSTCOMHH8C57Y6W6NZUASDOLA&marketplace=FLIPKART&q=Apple+mackbook&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=b49952aa-aade-424d-b3dd-3524a0b0eef0.COMHH8C57Y6W6NZU.SEARCH&ppt=sp&ppn=sp&ssid=1x1gi7x8xc0000001782466652708&qH=ae6b714c227b6726&ov_redirect=true'


loader = WebBaseLoader(url)


docs = loader.load()

chain =prompt | model | Parser 

print(chain.invoke({"question": "What is the peak brightness of this product that we are talking about?", "text": docs[0].page_content}))
