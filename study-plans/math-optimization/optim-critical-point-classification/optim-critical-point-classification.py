import numpy as np

def classify_critical_point(H):
    """
    Returns: one of 'local_min', 'local_max', 'saddle', 'degenerate'
    """
    eigs = np.linalg.eigvalsh(np.asarray(H, dtype = np.float64))
    tol = 1e-6
    if bool(np.any(np.abs(eigs) <= 1e-6)):
        return 'degenerate'
    if bool(np.all(eigs > tol)):
        return 'local_min'
    if bool(np.all(eigs < -tol)):
        return 'local_max'
    return 'saddle'