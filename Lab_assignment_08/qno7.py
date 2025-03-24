import numpy as np
from numpy import random

arr = random.randint(20,size=6)

print(f"Before sorting = {arr}")
print(f"after sorting : {np.sort(arr)}")
arr = arr.reshape(3,2)
print(arr)
