import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

for x in arr:
    print(x)
result = np.where(arr == 4)
print(result)