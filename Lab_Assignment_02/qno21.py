print("Armstrong from 1 to 300")
for x in range(1,301):
    if x < 10:
        print(x)
        continue
    y = x
    sum = 0
    while (x != 0):
        rem = x%10
        sum = sum + rem**3
        x = x//10
    if y == sum:
        print(y)