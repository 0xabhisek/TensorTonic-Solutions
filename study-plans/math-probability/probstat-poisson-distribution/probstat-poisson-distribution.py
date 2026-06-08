from math import factorial, exp

def poisson_distribution(lam, max_k):
    """
    Returns: [pmf_list, cdf_at_max_k, p_zero] as a list.
    """
    n = max_k
    pmf = [round((lam**k * exp(-lam))/factorial(k),4) for k in range(n+1)]
    cdf = round(sum(pmf[:max_k + 1]),4)
    p0 = round(pmf[0],4)

    return[pmf,cdf,p0]

    