from math import comb

def binomial_distribution(n, p, threshold):
    """
    Returns: dict with 'pmf' (list), 'mean', 'variance', 'prob_at_least'
    """

    pmfr = [
        comb(n, k) * (p**k) * ((1-p)**(n-k))
        for k in range(n+1)
    ]

    pmf = [round(x, 4) for x in pmfr]

    m = round(n * p, 4)

    var = round(n * p * (1-p), 4)

    tp = round(sum(pmf[threshold:]), 4)

    return {
        'pmf': pmf,
        'mean': m,
        'variance': var,
        'prob_at_least': tp
    }