import numpy as np

# Reshape array
arr = np.array([1,2,3,4,5,6,7,8,9])
reshaped = arr.reshape((3,3))
print(reshaped)

# Expand array. I.e. give new dimension for array
arr2 = np.array([1,2,3])
expanded = arr2[:, np.newaxis]
print(expanded)