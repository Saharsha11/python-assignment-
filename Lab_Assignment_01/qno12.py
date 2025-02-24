name = input("Enter the name = ")
english = int(input("Enter the marks in english = "))
nepali = int(input("Enter the marks in nepali = "))
science = int(input("Enter the marks in science = "))
computer = int(input("Enter the marks in computer  = "))
maths = int(input("Enter the marks in maths ="))
total_marks = english+nepali+science+computer+maths
percentage = (total_marks/500)*100
print(name,"obtained percentage = ",percentage)