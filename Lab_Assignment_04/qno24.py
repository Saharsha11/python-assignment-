def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return (num%10)*10 + sum_of_digits(num//10)
    
print("Sum of digits = ",sum_of_digits(523))