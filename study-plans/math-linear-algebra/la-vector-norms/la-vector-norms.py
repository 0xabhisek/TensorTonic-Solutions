import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    v = np.array(v)
    v1 = np.sum(np.abs(v))
    v2 = np.linalg.norm(v)
    v3 = np.max(np.abs(v))
    return np.array([v1,v2,v3])