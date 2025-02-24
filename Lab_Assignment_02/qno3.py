num = int(input("Enter a 4 digit number = "))
sum = 0
rev = 0
square = 0
print("Individiual digits : ")
while num != 0:
    rem = num%10
    print(rem)
    sum += rem 
    rev = rev*10+rem
    square = square + rem**2
    num = num//10
print("Sum of digit = ",sum) 
print("Reverse of digit = ",rev) 
print("Sum of square of digit = ",square)