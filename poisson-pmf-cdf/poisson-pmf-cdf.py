import numpy as np
from math import exp
from math import factorial

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    pmf = exp(-lam)*((lam)**k)/factorial(k)

    cdf = sum(exp(-lam)*((lam)**i)/factorial(i) for i in range(k+1))

    return float(pmf),float(cdf)
    