import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    x = np.array(a, dtype = np.float64)
    y = np.array(b, dtype = np.float64)
    p = np.clip(x,lo,hi)
    q = np.clip(y,lo,hi)
    i = (p-lo)/(hi-lo)
    j = (q-lo)/(hi-lo)
    return np.abs(i - j)