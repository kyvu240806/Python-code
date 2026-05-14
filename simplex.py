import numpy as np

def simplex(c, A, b):
    """
    Giải bài toán:
    maximize c^T x
    subject to Ax <= b, x >= 0
    """

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    m, n = A.shape

    tableau = np.zeros((m + 1, n + m + 1))

    tableau[:m, :n] = A
    tableau[:m, n:n+m] = np.eye(m)
    tableau[:m, -1] = b

    tableau[-1, :n] = -c

    basis = list(range(n, n + m))

    while True:
        pivot_col = np.argmin(tableau[-1, :-1])

        if tableau[-1, pivot_col] >= 0:
            break

        ratios = []

        for i in range(m):
            if tableau[i, pivot_col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, pivot_col])
            else:
                ratios.append(np.inf)

        pivot_row = np.argmin(ratios)

        if ratios[pivot_row] == np.inf:
            raise Exception("Unbounded solution")

        pivot = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot

        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

        basis[pivot_row] = pivot_col

    solution = np.zeros(n + m)

    for i in range(m):
        solution[basis[i]] = tableau[i, -1]

    optimal_value = tableau[-1, -1]

    return solution[:n], optimal_value, tableau


c = [3, 5]

A = [
    [1, 0],
    [0, 2],
    [3, 2]
]

b = [4, 12, 18]

x, z, tableau = simplex(c, A, b)

print("Optimal solution:", x)
print("Maximum value:", z)