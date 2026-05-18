import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    x = np.array(x, dtype = float)
    m = float(np.mean(x))
    md = float(np.median(x))
    cnt = Counter(x)
    mo = float(max(cnt, key = cnt.get))
    return {"mean" : m, 'median' : md, 'mode' : mo}