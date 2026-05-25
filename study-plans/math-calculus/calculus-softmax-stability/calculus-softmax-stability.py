import numpy as np

def softmax_stability_analysis(z):
    """
    Returns: dict with 'naive', 'stable' (lists of floats) and 'naive_has_issues' (bool)
    """
    z = np.asarray(z, dtype = np.float64)
    exp_z = np.exp(z)
    naive = exp_z/np.sum(exp_z)
    m = np.max(z)
    exp_s = np.exp(z - m)
    stable = exp_s/np.sum(exp_s)

    issues = bool(np.any(np.isnan(naive)) or np.any(np.isinf(naive)))

    return {
        'naive': naive.tolist(),
        'stable': stable.tolist(),
        'naive_has_issues': issues
    }