import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x =  np.array(x)
    p = np.percentile(x,q, method = 'linear')
    return p