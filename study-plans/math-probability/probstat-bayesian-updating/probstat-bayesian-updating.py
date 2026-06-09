def bayesian_update(prior_alpha, prior_beta, successes, failures):
    """Returns: dict with 'posterior_alpha', 'posterior_beta', 'prior_mean', 'posterior_mean' as floats."""
    post_a = prior_alpha + successes
    post_b = prior_beta + failures
    prior_mean = round(prior_alpha / (prior_alpha + prior_beta), 4)
    post_mean = round(post_a / (post_a + post_b), 4)
    return {"posterior_alpha": post_a, "posterior_beta": post_b, "prior_mean": prior_mean, "posterior_mean": post_mean}

    