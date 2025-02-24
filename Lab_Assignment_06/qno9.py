class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
class Teacher:
    def __init__(self,subject):
        self.subject = subject
    
class Tutor(Person,Teacher):

    def __init__(self, name, age,subject):
        Person.__init__(self,name, age)
        Teacher.__init__(self,subject)
    
    def display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Subject = {self.subject}")

t = Tutor("Aarosh",69,"Sex Education")
t.display()
        
        