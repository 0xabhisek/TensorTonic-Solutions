def quadratic_minimum(a, b, c):
    """
    Returns: dict with 'x_star' and 'f_min' (floats), each rounded to 6 decimals
    """
    xd = -b/(2*a)
    fmin = c - (b*b)/(4*a)

    return {"x_star": xd,
           "f_min": fmin}
