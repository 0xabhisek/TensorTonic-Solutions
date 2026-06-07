import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    x = np.array(x, dtype = float)
    s = np.std(x, ddof = 1)
    var = s*s
    return {'variance': var, 'std_dev': s}