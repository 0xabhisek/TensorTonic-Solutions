import numpy as np

def matrix_vector_multiply(A, x):
    """
    Returns: 1-D float64 array, the product A @ x.
    """
    x = np.asarray(x, dtype = np.float64)
    A = np.asarray(A, dtype = np.float64)
    return A@x
        