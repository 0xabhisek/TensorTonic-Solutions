import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    v = np.asarray(v, dtype = np.float64)
    l1 = np.sum(np.abs(v))
    l2 = (np.sum(v*v))**0.5
    l3 = np.linalg.norm(v, ord = np.inf)

    return np.array([l1,l2,l3])
    