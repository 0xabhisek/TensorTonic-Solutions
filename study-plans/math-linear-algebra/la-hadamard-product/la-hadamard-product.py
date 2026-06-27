import numpy as np

def hadamard_product(A, B):
    """
    Returns: ndarray, the element-wise product A * B.
    """
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    return A*B