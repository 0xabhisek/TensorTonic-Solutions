def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    """
    Returns: float, the posterior probability P(A|B).
    """
    pa_b = round((p_b_given_a*p_a)/(p_b_given_a*p_a + p_b_given_not_a*(1 - p_a))  ,4)
    return pa_b