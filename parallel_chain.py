from langchain_groq  import ChatGroq
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(
    model="llama-3.3-70b-versatile"
)

model2 = ChatGroq(
    model="llama-3.1-8b-instant"
)

Prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

Prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n{text}',

    input_variables=['text']
)

Prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes-> {notes} \n quiz-> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': Prompt1 | model1 | parser,
    'quiz': Prompt2 | model2 | parser
})


merge_chain = Prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Support Vector Machine (SVM)

Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It works by finding an optimal hyperplane that separates data points belonging to different classes with the maximum possible margin. The data points that are closest to the hyperplane are called support vectors, and they play a crucial role in defining the decision boundary. SVM is highly effective for high-dimensional datasets and is widely used in applications such as text classification, image recognition, spam detection, handwriting recognition, and bioinformatics. By using kernel functions such as Linear, Polynomial, Radial Basis Function (RBF), and Sigmoid, SVM can also handle non-linear classification problems efficiently. Its ability to generalize well on unseen data makes it one of the most powerful machine learning algorithms.

Short Version

Support Vector Machine (SVM) is a supervised learning algorithm used for classification and regression. It identifies the optimal boundary (hyperplane) that best separates different classes of data. SVM is widely used in text classification, image recognition, spam filtering, and pattern recognition tasks due to its high accuracy and effectiveness in high-dimensional data.
"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()