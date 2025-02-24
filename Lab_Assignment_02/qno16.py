odd = 0
even = 0
for i in range(1,101):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print (f"Sum of all odd = {odd}")
print (f"Sum of all even = {even}")