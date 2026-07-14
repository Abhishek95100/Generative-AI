from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text ="""
class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self .grade = grade # Grade is a float (like 8.5 or 9.5)
    
    def get_details(self):
        return self.name"

    def is_passing(self):
        return self.grade >=6.0

    #Example usage
    student1 = Student("Aarav",30,8.4)
    print(student1.get_details())
    
    if student1.is_passing():
        print("The student is passing.")
    else:
        print("The student is not passing.")

        """
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)
chuks = splitter.split_text(text)

print(len(chuks))
print(chuks[1])