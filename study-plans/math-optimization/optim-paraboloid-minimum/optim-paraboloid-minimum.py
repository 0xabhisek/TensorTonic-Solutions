def paraboloid_minimum(a, b, c, d, e):
    """
    Returns: dict with 'x_star', 'y_star', 'f_min' (floats), each rounded to 6 decimals
    """
    xd = -c/(2*a)
    yd = -d/(2*b)
    f_min = a*(xd**2) + b*(yd**2) +c*(xd) + d*(yd) + e

    return {'x_star': round(float(xd),6),
           'y_star': round(float(yd),6),
           'f_min': round(float(f_min),6)}
