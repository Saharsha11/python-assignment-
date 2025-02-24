num = int(input("Enter a number = "))
n = num 
sum = 0
while n != 0:
    rem = n%10
    sum = sum + rem**3
    n = n//10
    
if sum == num:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")
    