import numpy as np
def discrete_moments(values, probabilities):
    """
    Returns: [E_X, E_X2, variance, std_dev] as a list.
    """
    r = lambda x : round(x,4)
    x = np.array(values,dtype = float)
    px = np.array(probabilities, dtype = float)
    E_X = r(x @ px)
    E_X2 = r((x**2) @ px)
    var = r(E_X2 - (E_X)**2)
    std_dev = r((var)**0.5)

    return [E_X,E_X2,var, std_dev]