from langchain_groq  import ChatGroq
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model1 = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser =StrOutputParser()

class Feedback(BaseModel):

    sentiment:Literal['positive','negative'] =Field(description='Give the sentiment of the feedback')
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='classify the sentiment of the following feedback text into postive or negative \n{feedback} \n{format_instruction}',
    input_variables=['feedback'],
   partial_variables={
    'format_instruction': parser2.get_format_instructions()
}


)

classifier_chain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    template='Write an appropiate response to this  positive feedback \n{feedbasck}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropiate response to this  negative feedback \n{feedbasck}',
    input_variables=['feedback']
)

from langchain_core.runnables import RunnableBranch, RunnableLambda

branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "positive",
        prompt2 | model1 | parser
    ),
    (
        lambda x: x.sentiment == "negative",
        prompt3 | model1 | parser
    ),
    RunnableLambda(lambda x: "could not find sentiment")
)
 
chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'this is a beautiful phone'}))

chain.get_graph().print_ascii()