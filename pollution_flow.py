import numpy as np

T = np.array([[0.35, 0.65],[0.1, 0.9]])

x0 = np.array([1, 0])

n = 30

xn = x0 @ np.linalg.matrix_power(T, n)

print(xn)