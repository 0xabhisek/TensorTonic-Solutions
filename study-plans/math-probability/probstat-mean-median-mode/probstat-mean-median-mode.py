import numpy as np
from collections import Counter
from scipy import stats

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    x = np.array(x,dtype = float)
    mean = np.mean(x)
    median = np.median(x)
    mode = stats.mode(x).mode
    return {'mean': mean, 'median': median, 'mode': mode}
    