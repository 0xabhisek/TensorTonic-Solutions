import numpy as np
from scipy import stats

def correlation_analysis(x, y):
    """
    Returns: dict with 'r', 't_stat', 'p_value' (floats), 'reject' (bool).
    """
    x = np.array(x, dtype = float)
    y = np.array(y, dtype = float)
    n = len(y)
    r = round(float(np.corrcoef(x,y)[0,1]), 4)
    r2 = round(r**2,4)
    t_stat = round(r * ((n - 2)**0.5) / ((1 - r**2)**0.5), 4)
    p_val = round(2*stats.t.sf(abs(t_stat),n-2),4)
    return {"r": r, "r_squared": r2, "t_stat": t_stat, "p_value": p_val, "significant": p_val < 0.05}