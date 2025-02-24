from functools import reduce

def product(a,b):
    return a*b
number = [1,2,3,4,5]
ans = reduce(product,number)
print(ans)