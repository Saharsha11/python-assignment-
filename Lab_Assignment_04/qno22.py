def sum_to_n(n):
    if n==0:
        return 0
    elif n == 1 : 
        return 1
    else:
        return n + sum_to_n(n-1)
    
num = int(input("Enter a number = "))
print("Sum = ",sum_to_n(num))