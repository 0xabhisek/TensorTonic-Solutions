import numpy as np
from math import comb

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    pmf = []
    x = np.array(x, dtype = float)
    n = len(x)
    pmf = [ p if j == 1 else (1 - p) for j in x]

    pmf = np.array(pmf)
    mu = p
    var = p*(1-p)
    return pmf,mu,var

    