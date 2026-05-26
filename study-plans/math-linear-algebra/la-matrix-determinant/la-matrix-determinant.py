import numpy as np

def matrix_determinant(A):
    """
    Returns: float, the determinant of square matrix A.
    """
    A = np.asarray(A, dtype = float)
    return np.linalg.det(A)