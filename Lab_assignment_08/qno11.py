from numpy import random
import numpy as np

arr = random.randint(1,101,size=20)

print(arr)

print("Mean = ",np.mean(arr))
print("median = ",np.median(arr))
print("Standard Deviation = ",np.std(arr))
print("Variance = ",np.var(arr))
print("Sum of all elements = ",np.sum(arr))
print("Min value = ",np.min(arr))
print("Max value = ",np.max(arr))
print("25th percentitle = ",np.percentile(arr,25))
print("75th percentitle = ",np.percentile(arr,75))