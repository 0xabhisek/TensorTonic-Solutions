import numpy as np

def standard_errors(samples):
    """
    Returns: dict with 'standard_errors' (list of floats) and 'mean_se'.
    """
    ses = []

    for l in samples:
        l = np.asarray(l, dtype=float)

        n = len(l)

        s = np.std(l, ddof=1)

        se = round(float(s / np.sqrt(n)), 4)

        ses.append(se)

    mean_se = round(float(np.mean(ses)), 4)

    return {
        "standard_errors": ses,
        "mean_se": mean_se
    }