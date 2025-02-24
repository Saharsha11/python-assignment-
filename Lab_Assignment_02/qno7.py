print("1.Addition")
print("2.Substraction")
print("3.Multiply")
print("4.Divide")
choose = int(input("Enter the choice = "))
a = int(input("Enter the first number = "))
b = int(input("Enter the Second number = "))
match choose:
    case 1:
        print(f"Addition = {a+b}")
    case 2:
        print(f"Substraction = {a-b}")
    case 3:
        print(f"Multiplication = {a*b}")
    case 4:
        print(f"Division = {a/b}")
    case _:
        print("Wrong input")