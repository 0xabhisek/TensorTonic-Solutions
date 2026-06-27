import numpy as np

def matrix_trace(A):
    A = np.asarray(A, dtype=float)
    return np.trace(A)