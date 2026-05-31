import numpy as np

def mle_normal(data):
    """
    Returns: dict with 'mu_hat' and 'sigma_hat' as floats (MLE estimates).
    """
    x = np.array(data, dtype = float)
    mu_hat = round(np.mean(x),4)

    sigma_hat = round((np.mean((x - mu_hat)**2))**0.5 , 4 )
    return { "mu_mle": mu_hat, "sigma_mle": sigma_hat}