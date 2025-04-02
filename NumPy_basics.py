import numpy as np 

# Create an array from list
arr = np.array([1,2,3,4])
print(arr)


# Create a matrix using numpy built in function
zeros = np.zeros((3,3))
print(zeros)

# All one matrix with the given row and column
ones = np.ones((2,4))
print(ones)

# Ranging and array with the given space. 
range_array = np.arange(1,10,2)
print(range_array)

# Evenly spaced array. start, end, and number elements needed
linspace_array = np.linspace(1,100,4)
print(linspace_array)