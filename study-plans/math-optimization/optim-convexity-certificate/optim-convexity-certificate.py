import numpy as np

def convexity_certificate(H):
    """
    Returns: dict with 'is_convex' (bool) and 'min_eigenvalue' (float, rounded to 6 decimals)
    """
    H = np.asarray(H, dtype = np.float64)
    eigs = np.linalg.eigvalsh(H)
    min_eig = float(np.min(eigs))
    return {
        'is_convex': bool(min_eig >= -1e-6),
        'min_eigenvalue': round(min_eig, 6)
    }
