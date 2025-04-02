import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original matrix: \n", matrix)

# Transpose
transpose = matrix.T
print("Transpose matrix: \n", transpose)


another_matrix = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(matrix)
print(another_matrix)
print("Addition: \n ", matrix + another_matrix)
print("Multiplication: \n", matrix * another_matrix)