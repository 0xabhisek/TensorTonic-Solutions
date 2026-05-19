def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    """
    Returns: float, the posterior probability P(A|B).
    """
    p_b = round(float(p_a*p_b_given_a + (1-p_a)*p_b_given_not_a) , 4)
    pa_b = round(float(p_b_given_a*p_a/p_b),4)
    return pa_b