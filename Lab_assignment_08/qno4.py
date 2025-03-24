import numpy  as np 
arr = np.arange(5)
print("Before modifing origanl array : ",arr)
arr1 = arr.view()
arr2 = arr.copy()

arr1[0] = 85

arr2[0] = 55

print("After modifiying view, orginal array = ",arr)
print("View array = ",arr1)
print("Copy array = ",arr2)
