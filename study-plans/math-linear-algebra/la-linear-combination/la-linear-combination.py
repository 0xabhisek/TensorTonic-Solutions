import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """
    v = np.array(vectors, dtype = np.float64)
    c = np.array(coefficients, dtype = np.float64)

    return c.dot(v)