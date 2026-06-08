import numpy as np
from scipy import stats

def clt_confidence_interval(data, confidence):
    """
    Returns: [mean, std_error, ci_lower, ci_upper] as a list.
    """
    x = np.array(data,dtype = float)
    n = len(x)
    r = lambda x: round(float(x),4)
    mean = r(np.sum(x)/n)
    std_error = r(np.std(x,ddof = 1)/(n**0.5))
    z = r(stats.norm.ppf((1+confidence)/2))
    ci_lower = r(mean - z*std_error)
    ci_upper = r(mean+z*std_error)
    return [mean,std_error,ci_lower,ci_upper]
    