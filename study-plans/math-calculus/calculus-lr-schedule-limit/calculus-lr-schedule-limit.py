import numpy as np

def lr_schedule_analysis(alpha_0, k):
    """
    Returns: dict with 'limit' (float), 'sum_diverges' (bool), 'sum_sq_converges' (bool)
    """
    if k > 0:
        limit = 0.0
    else:
        limit = float(alpha_0)

    sd = alpha_0 > 0

    sc = (alpha_0 == 0) or (k > 0)

    return {
        'limit': limit,
        'sum_diverges': sd,
        'sum_sq_converges': sc,
    }
