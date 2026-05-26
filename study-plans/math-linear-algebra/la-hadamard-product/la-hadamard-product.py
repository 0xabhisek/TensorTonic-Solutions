import numpy as np

def hadamard_product(A, B):
    """
    Returns: ndarray, the element-wise product A * B.
    """
    A = np.asarray(A)
    B = np.asarray(B)
    m = len(A)
    n = len(A[0])
    x = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            x[i][j] = A[i][j] * B[i][j]

    return x
            