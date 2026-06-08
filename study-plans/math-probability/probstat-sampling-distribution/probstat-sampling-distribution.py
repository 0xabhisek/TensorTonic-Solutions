from scipy import stats

def sampling_distribution(mu, sigma, n, threshold):
    """
    Returns: dict with 'mean', 'std_error', 'tail_probability' as floats.
    """
    r = lambda x: round(float(x),4)
    mean = r(mu)
    std_error = r(sigma/(n)**0.5)
    t = r(stats.norm.cdf(threshold,mu,std_error))

    return {"sampling_mean": mean, "sampling_std": std_error, "prob_below_threshold": t}