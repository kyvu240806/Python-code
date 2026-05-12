import numpy as np
import matplotlib.pyplot as plt
import json

data = [[2, 2], [4, 8], [7, 12]]

size = len(data)
y = [0 for _ in range(4*(size-1))]

y[0] = data[0][1]
y[2*size-3] = data[size-1][1]

j = 1
for i in range(1, 2*size-3, 2):
    y[i] = data[j][1]
    y[i+1] = data[j][1]
    j += 1

A = [[0 for _ in range(4*(size-1))] for _ in range(4*(size-1))]

k = 0
j = 0
for i in range(0, 2*(size-1), 2):
    A[i][k] = data[j][0]**3
    A[i][k+1] = data[j][0]**2
    A[i][k+2] = data[j][0]
    A[i][k+3] = 1

    A[i+1][k] = data[j+1][0]**3
    A[i+1][k+1] = data[j+1][0]**2
    A[i+1][k+2] = data[j+1][0]
    A[i+1][k+3] = 1

    j += 1
    k += 4

j = 1
k = 0
for i in range(2*(size-1), 4*size-6, 2):
    A[i][k] = 3*data[j][0]**2
    A[i][k+1] = 2*data[j][0]
    A[i][k+2] = 1
    A[i][k+4] = -3*data[j][0]**2
    A[i][k+5] = -2*data[j][0]
    A[i][k+6] = -1

    A[i+1][k] = 6*data[j][0]
    A[i+1][k+1] = 2
    A[i+1][k+4] = -6*data[j][0]
    A[i+1][k+5] = -2

    j += 1
    k += 4

A[-2][0] = 6*data[0][0]
A[-2][1] = 2
A[-1][-4] = 6*data[-1][0]
A[-1][-3] = 2

x = np.linalg.solve(A, y)

print(x)
