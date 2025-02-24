sum = 0
count = 0
for i in range(100,201):
    if (i % 7 == 0) and not(i%5==0):
        sum = sum + i
        count += 1
print("Number of integer from 100 t0 200 divisible by 7 and not divisible by 5 = ",count)
print("Sum of all integer = ",sum)