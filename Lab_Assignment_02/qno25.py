n = int(input("Enter a number = "))
c = 0 
i=2
while i < n:
    if n % i == 0:
        print(f"{n} is not a prime number.")
        break
    i += 1
else:
    print(f"{n} is a prime number.")