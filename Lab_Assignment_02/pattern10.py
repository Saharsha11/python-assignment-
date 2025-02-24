n = 5
for i in range(1,6):
    print(" "*(n-i),end="")
    for y in range(1,i+1):
        print(i,end="")
    print()