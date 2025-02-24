num = int(input("Enter a number = "))
n = num 
pal = 0
while n != 0:
    rem = n%10
    pal = pal*10 + rem
    n = n//10
    
if pal == num:
    print(f"{num} is a palindrom number.")
else:
    print(f"{num} is not a palindrom number.")
    