import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x, dtype = float)
    p = np.array(p, dtype = float)
    ex = np.sum(x*p)
    if x.shape != p.shape:
        raise ValueError
    if abs(p.sum() - 1.0) > 1e-6:
        raise ValueError
    return float(np.sum(x * p))
