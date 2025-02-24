def sum_all(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum

print(f"Sum of all = {sum_all(1,5,10,25)}")