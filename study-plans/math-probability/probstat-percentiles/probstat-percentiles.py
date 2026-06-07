import numpy as np

def percentiles(x, q):
    """
    Returns: numpy array of percentile values.
    """
    x = np.array(x, dtype = float)
    pct = np.percentile(x, q)

    return pct
