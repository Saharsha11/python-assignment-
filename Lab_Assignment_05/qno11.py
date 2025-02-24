class Student:
    def __init__(self, id= 1, marks=100):
        self.id = id
        self.marks = marks

    # Constructor that takes another Student object
    def __init__(self, other_student=None):
        if other_student is not None:
            self.id = other_student.id
            self.marks = other_student.marks
        else:
            self.id = 1
            self.marks = 100

    def display(self):
        print(f"ID: {self.id}, Marks: {self.marks}")

# Creating an object with default values
p1 = Student()
p1.display()

# Creating an object with specific values
p2 = Student()
p2.id = 25
p2.marks = 75
p2.display()

# Creating an object using another object
p3 = Student(p2)  # Copying values from p2
p3.display()
