import numpy as np
from math import comb

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    pmf = []
    x = np.array(x, dtype = float)
    n = len(x)
    pmf = np.where(x==1,p,1-p)
    mu = p
    var = p*(1-p)
    return pmf,mu,var

    