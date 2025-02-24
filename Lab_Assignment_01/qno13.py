principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
times_compounded = int(input("Enter the number of times interest is compounded per year: "))
rate = rate/100
compound = principal*(1+(rate/times_compounded))**(times_compounded*time)
print("Compound Interest = ",compound)