# n = int(input("Enter a number = "))
# print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")

#wap to find greatest amoung 3 num

a = int(input("Enter the first number = "))
b = int(input("Enter the second number = "))
c = int(input("Enter the third number = "))
res = a if a > b and a > c else b if b > c else c
print(f"{res} is the greatest number")