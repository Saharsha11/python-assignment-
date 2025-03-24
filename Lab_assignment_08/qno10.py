import numpy as np

# Creating a 3D array of shape (3, 4, 5)
arr = np.arange(18).reshape(3, 2, 3)  
print("Original 3D Array:\n", arr)

# Extracting a 2D slice by selecting a specific index along axis 0
slice_2d = arr[1, :, :]  # Selecting the second "layer"

print("\nSliced 2D Array:\n", slice_2d)

scaler = 5
print("Multiplication : ",slice_2d*scaler)
