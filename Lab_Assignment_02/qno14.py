n = int(input("Enter a number = "))
fact = 1
print("Using for loop")
for i in range(1,n+1):
    fact = fact * i
print(f"Factorial = {fact}") 

print()

print("Using while loop")
x = n 
fact = 1
while x!=0:
    fact = fact * x
    x -= 1
print(f"Factorial = {fact}")