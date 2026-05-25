import numpy as np

def convex_set_membership(A, b, x):
    """
    Returns: dict with 'in_set' (bool) and 'max_violation' (float, rounded to 6 decimals)
    """
    A_ = np.asarray(A, dtype=np.float64)
    b_ = np.asarray(b, dtype=np.float64)
    x_ = np.asarray(x, dtype=np.float64)
    r = A_@x_ - b_
    max_violation = float(np.max(r))
    return {
        'in_set': bool(max_violation <= 1e-6),
        'max_violation': round(max_violation,6)
    }
