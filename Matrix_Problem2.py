import numpy as np

# Number of Rows in Matrix:
R = int(input("Enter the number of rows for Matrix: "))
# Number of Columns in Matrix:
C = int(input("Enter the number of columns for Matrix: "))

# Entering the values for the Matrix:
print("Enter the entries in a single line (separated by space): ")

# Converting values in Matrix Form:
entries = list(map(int, input().split()))

# Printing Matrix 1:
print("Matrix:")
matrix = np.array(entries).reshape(R, C)
print(matrix)
print("")

# Calculating sum of each row of the matrix:
for i in range(0, R):
    sumRow = 0
    for j in range(0, C):
        sumRow = sumRow + matrix[i][j]
    print("Sum of " + str(i + 1) + " Row: " + str(sumRow))

# Leaving a Line between:
print("")

# Calculating sum of each column of the matrix:
for i in range(0, R):
    sumCol = 0
    for j in range(0, C):
        sumCol = sumCol + matrix[j][i]
    print("Sum of " + str(i + 1) + " Column: " + str(sumCol))

# Leaving a Line between:
print("")

# Calculating sum of each Diagonal of the matrix:
Dia1 = 0
Dia2 = 0
for i in range(R):
    Dia1 += matrix[i][R - i - 1]
    Dia2 += matrix[i][i]
print("The sum of 1st Diagonal is", Dia1)
print("The sum of 2nd Diagonal is", Dia2)
