import numpy as np 

arr = np.linspace(10,20,num=5)
print(arr)

median = np.median(arr)
sd = np.std(arr)
print(f"Median = {median}")
print(f"Standard Deviation = {sd}")