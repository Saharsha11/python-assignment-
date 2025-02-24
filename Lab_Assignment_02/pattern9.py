a = "ABCDE"
l = len(a)
for i in range(l,0,-1):
    print(" "*(l-i),end="")
    print(a[i-1]*i)