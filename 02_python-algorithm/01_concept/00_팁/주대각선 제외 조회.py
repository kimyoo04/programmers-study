import numpy as np

matrix = np.arange(25).reshape(5,5)

print(matrix)

for i in range(5):
    print(matrix[i][:i], matrix[i][i+1:])