from scipy import stats

def z_test_one_sample(x_bar, mu_0, sigma, n, alpha):
    """
    Returns: [z_stat, p_value, reject] as a list.
    """
    r = lambda x: round(x,4)    
    z_stat = r((x_bar - mu_0)/(sigma/(n**0.5)))
    p = r(2 * stats.norm.cdf(-abs(z_stat)))
    return [z_stat,p,p<alpha]