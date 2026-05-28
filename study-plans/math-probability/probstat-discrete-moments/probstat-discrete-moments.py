def discrete_moments(values, probabilities):
    """
    Returns: [E_X, E_X2, variance, std_dev] as a list.
    """
    ex = round(sum((x*p) for x,p in zip(values , probabilities)), 4)
    ex2 = round(sum(x*x*p for (x,p) in zip(values , probabilities)), 4)
    var = round(ex2 - (ex ** 2), 4)
    std = round((var ** 0.5), 4)

    return [ex, ex2, var, std]