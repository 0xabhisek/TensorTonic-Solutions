import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.array(x)
    mu = np.mean(x)
    s = np.std(x, ddof = 1)
    return s**2, s