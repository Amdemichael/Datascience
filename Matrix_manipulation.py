import numpy as np

# Reshape array
arr = np.array([1,2,3,4,5,6,7,8,9])
reshaped = arr.reshape((3,3))
print(reshaped)

# Expand array. I.e. give new dimension for array
arr2 = np.array([1,2,3])
expanded = arr2[:, np.newaxis]
print(expanded)

# Element wise operation
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)
print(a - b)
print(a * b)
print(a/b)

# Mathematical operations
ar = np.array([4,16,25])
print(np.sqrt(ar))
print(np.sum(ar))
print(np.mean(ar))
print(np.max(ar))

# Array Indexing, Slicing, and Reshaping
arr3 = np.array([10,20,30,40,50,60])
print(arr3[2])
print(arr3[-1])

print(arr3[1:4])
print(arr3[:3])
print(arr3[3:])

resshape = arr3.reshape((2,3))