def bayesian_update(prior_alpha, prior_beta, successes, failures):
    """
    Returns: dict with 'posterior_alpha', 'posterior_beta', 'prior_mean', 'posterior_mean' as floats.
    """
    posterior_alpha = round(prior_alpha + successes, 4)
    posterior_beta = round(prior_beta + failures,4)

    prior_mean = round(prior_alpha /(prior_alpha + prior_beta),4)
    posterior_mean = round(posterior_alpha/(posterior_alpha + posterior_beta),4)

    return {"posterior_alpha": posterior_alpha, "posterior_beta": posterior_beta, "prior_mean": prior_mean, "posterior_mean": posterior_mean}
    