import numpy as np

# Matrix 1:
Matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# Matrix 2:
Matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# Default Result:
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Iterating Result:
for i in range(len(Matrix1)):
    for j in range(len(Matrix1[0])):
        result[i][j] = Matrix1[i][j] + Matrix2[i][j]

# Printing Matrix 1 in Matrix Form:
print("Matrix 1:")
print(np.matrix(Matrix1))
# Leaving a Gap:
print(" ")
# Printing Matrix 2 in Matrix Form:
print("Matrix 2:")
print(np.matrix(Matrix2))
# Leaving a Gap:
print(" ")
# Printing the Result:
print("Result:")
for r in result:
    print(r)
