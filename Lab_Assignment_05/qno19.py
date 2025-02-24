class Employee:
    all_employee = []
    @classmethod
    def add_employee(cls):
        n = int(input("Enter the number of employee to enter = "))
        for i in range(n):
            emp = input("Enter the name of employee = ")
            cls.all_employee.append(emp)
        
    @classmethod
    def remove_employee(cls):
        rem = input("Enter the name of employee to remove = ")
        if rem in cls.all_employee:
            cls.all_employee.remove(rem)
            print(f"{rem} has been removed.")
        else:
            print("No employee named " + rem)
        
    @classmethod 
    def display(cls):
        print("Total employee = ",len(cls.all_employee))
        print("Employee Details:")
        for name in cls.all_employee:
            print(f"Name = {name}")
        
Employee.add_employee()
Employee.display()
Employee.add_employee()
Employee.remove_employee()
Employee.display()
