from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """Space exploration has advanced scientific knowledge and driven technological innovations.
Discoveries from missions to the Moon and Mars have not only improved our understanding of the universe but also produced practical technologies like satellite communication, GPS, and medical imaging that benefit people on Earth.
"""

# initialize the splitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=20
)
chuks = splitter.split_text(text)

print(len(chuks))
print(chuks)