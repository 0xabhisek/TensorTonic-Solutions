from scipy import stats

def normal_distribution(mu, sigma, x):
    """
    Returns: dict with 'z_score', 'cdf', 'pdf', 'prob_within_1std' as floats.
    """
    z = round((x - mu)/sigma, 4)
    pdf = round(float(stats.norm.pdf(x,mu,sigma)),4)
    cdf = round(float(stats.norm.cdf(x,mu,sigma)), 4)
    p1 = round(  float(stats.norm.cdf(mu + sigma ,mu,sigma)) - float(stats.norm.cdf(mu - sigma,mu,sigma)) , 4)
    return {"z_score" : z, "cdf" : cdf, "pdf": pdf, "prob_within_1_std" : p1}