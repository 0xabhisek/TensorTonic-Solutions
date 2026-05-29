import numpy as np
from scipy import stats

def clt_confidence_interval(data, confidence):
    """
    Returns: [mean, std_error, ci_lower, ci_upper] as a list.
    """
    x = np.asarray(data, dtype = float) 
    mean = round(float(np.mean(x)),4)
    n = len(x)
    se = round(float(np.std(x,ddof = 1)/(n**0.5)),4)
    z = round(float(stats.norm.ppf((1 + confidence) / 2)), 4)
    ci_lower = round(mean - z * se, 4)
    ci_upper = round(mean + z * se, 4)
    return [mean, se, ci_lower, ci_upper]
    