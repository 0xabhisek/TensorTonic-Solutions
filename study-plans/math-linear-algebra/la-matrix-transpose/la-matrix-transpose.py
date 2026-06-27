import numpy as np

def matrix_transpose(A):
    """Returns: ndarray, the transpose of A."""
    A = np.asarray(A, dtype=float)
    return A.T
