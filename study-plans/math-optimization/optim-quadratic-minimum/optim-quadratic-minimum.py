def quadratic_minimum(a, b, c):
    x_star = -b / (2.0 * a)
    f_min = c - (b * b) / (4.0 * a)
    return {
        "x_star": round(float(x_star), 6),
        "f_min": round(float(f_min), 6),
    }
