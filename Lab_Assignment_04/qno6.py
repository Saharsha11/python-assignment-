def describe_person(name:str,age,city):
    print(f"Name = {name}")
    print(f"Age = {age}")
    print(f"City = {city}")

n = input("Enter the name = ")
a = int(input("Enter the age  = "))
c = input("Enter the city = ")
describe_person(n,a,c)
