from math import exp

def exponential_distribution(lam, t):
    """
    Returns: dict with 'pdf', 'cdf', 'survival', 'mean', 'variance' as floats.
    """
    rep = lambda x : float(round(x,4))
    pdf = rep(lam * exp(-lam * t))
    cdf = rep(1 - exp(-lam * t) )
    sf = rep(exp(-lam * t))
    m = rep(1/lam)
    v = rep(1/(lam**2))
    return {"pdf": pdf, "cdf": cdf, "survival": sf, "mean": m, "variance": v}