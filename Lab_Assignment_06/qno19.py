class Student:
    def readRoll(self,roll_no):
        self. roll_no = roll_no

    def displayRoll(self):
        print("Roll no = ",self.roll_no)
    
class Test(Student):
       
    def readMarks(self,marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def displayMarks(self):
        print("Marks of subject 1 = ",self.marks1)
        print("Marks of subject 2 = ",self.marks2)

class Result(Test):
    def readResult(self):
        self.result = self.marks1 + self.marks2
    
    def disResult(self):
        print("Result = ",self.result)

r = Result()
r.readRoll(11)
r.displayRoll()
r.readMarks(75,90)
r.displayMarks()
r.readResult()
r.disResult()
