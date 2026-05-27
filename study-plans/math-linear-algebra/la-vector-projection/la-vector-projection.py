import numpy as np

def vector_projection(u, v):
    """
    Returns: float64 array, the projection of u onto v.
    """
    u = np.asarray(u, dtype = np.float64)
    v = np.asarray(v, dtype = np.float64)
    return (u@v) * v/(v@v)