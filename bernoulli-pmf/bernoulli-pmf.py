import numpy as np
from math import comb

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    pmf = []
    x = np.array(x, dtype = float)
    n = len(x)
    for j in x:
        if j == 1:
            pmf.append(p)
        else:
            pmf.append(1-p)

    pmf = np.array(pmf)
    mu = p
    var = p*(1-p)
    return pmf,mu,var

    