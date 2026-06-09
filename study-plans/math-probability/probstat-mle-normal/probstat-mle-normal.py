import numpy as np

def mle_normal(data):
    """
    Returns: dict with 'mu_hat' and 'sigma_hat' as floats (MLE estimates).
    """
    x = np.array(data, dtype = float)
    n = len(x)
    mu = round(float((1/n)*(np.sum(x))),4)
    sig = round(float((1/n)*(np.sum((x - mu)**2)))**0.5,4)

    return {"mu_mle": mu, "sigma_mle": sig }