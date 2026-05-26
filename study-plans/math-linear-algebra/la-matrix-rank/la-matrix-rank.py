import numpy as np

def matrix_rank(A):
    """
    Returns: int, the rank of matrix A.
    """
    return int(np.linalg.matrix_rank(np.array(A)))