a = [1,2,3,4,5,6]
b = []
c = []
for i in range(len(a)):
    if i % 2 ==0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b,c)