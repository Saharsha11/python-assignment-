import numpy as np

list1 = [2,5,88,10,15,78,20,69,77,100]

arr1 = np.array(list1)
arr2 = arr1.astype(np.float32)
arr3 = arr2.reshape(2,5)
print(arr2 ,arr2.dtype) 
print(arr3)