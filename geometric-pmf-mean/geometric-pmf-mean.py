import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    k = np.array(k)
    pmf = np.array([(1-p)**(i-1)*p for i in k])
    ex = float(1/p)
    return pmf,ex
    