import numpy as np
from scipy import stats

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x, dtype = float)
    mean = np.mean(x)
    median = np.median(x)
    mode = stats.mode(x).mode

    return (mean,median,mode)