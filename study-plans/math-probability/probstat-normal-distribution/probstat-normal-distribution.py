from scipy import stats
import numpy as np

def normal_distribution(mu, sigma, x):
    """
    Returns: dict with 'z_score', 'cdf', 'pdf', 'prob_within_1std' as floats.
    """
    z_score = round((x - mu)/sigma,4)
    cdf = round(stats.norm.cdf(x,mu,sigma),4)
    pdf = round(stats.norm.pdf(x,mu,sigma),4)
    p1 = round(stats.norm.cdf(sigma+mu,mu,sigma) - stats.norm.cdf(mu-sigma,mu,sigma),4)
    return {"z_score": z_score, "cdf": cdf, "pdf": pdf, "prob_within_1_std": round(p1,4)}