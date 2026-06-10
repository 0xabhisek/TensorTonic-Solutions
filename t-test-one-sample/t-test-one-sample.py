import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    x = np.array(x)
    xbar = np.mean(x)
    s = np.std(x,ddof = 1)
    t = (xbar - mu0)/(s/(len(x)**0.5))
    return t