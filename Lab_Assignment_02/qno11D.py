a = int(input("Enter the first number = "))
b = int(input("Enter the second number = "))
c = int(input("Enter the third number = "))
d = int(input("Enter the fourth number = "))
res = a if (a < b and a < c and a < d) else b if (b < c and b < d) else c if (c < d) else d
print(f"{res} is the smallest number")

