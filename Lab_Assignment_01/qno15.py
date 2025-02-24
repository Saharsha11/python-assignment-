import math
a = int(input("Enter the side of triangle = "))
b = int(input("Enter the side of triangle = "))
c = int(input("Enter the side of triangle = "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle = ",area)