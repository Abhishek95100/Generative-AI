from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGroq(
    model ="llama-3.3-70b-versatile"
)

#schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary:str = Field(description="A brief summary of the review")
    sentiment: Literal["pos","neg"] = Field(description=" Return sentiment of the reivew either negative ,postitive or neutral")
    pros: Optional[list[str]] = Field(default=None ,description="Write down all the cons inside a list")
    cons: Optional [list[str]] = Field(default=None,description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None,description="Write the name of the reviewer")



structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The Samsung Galaxy S24 Ultra delivers exceptional performance with its powerful Snapdragon processor, excellent battery life, and versatile camera system. The 200MP camera produces impressive photos, especially in low-light conditions, while the S-Pen adds productivity features that many users find valuable. However, the phone is quite large and heavy, making one-handed use less comfortable. Additionally, Samsung's One UI still includes unnecessary pre-installed apps, and the premium price may be difficult to justify for some buyers.

Sentiment

Mixed Positive

Pros
Outstanding performance for gaming, multitasking, and productivity
Excellent 200MP camera with strong zoom capabilities
Long-lasting battery with fast charging
Useful S-Pen functionality
Premium build quality
                                 
Review by Abhishek                             
""")


print(result)