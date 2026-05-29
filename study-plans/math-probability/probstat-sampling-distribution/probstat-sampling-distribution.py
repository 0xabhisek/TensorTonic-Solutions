from scipy import stats

def sampling_distribution(mu, sigma, n, threshold):
    """
    Returns: dict with 'mean', 'std_error', 'tail_probability' as floats.
    """
    m = round(float(mu),4)
    se = round(float(sigma/(n**0.5)),4)
    pt = round(float(stats.norm.cdf(threshold,mu, se)),4)
    return {"sampling_mean": m, "sampling_std": se, "prob_below_threshold": pt}