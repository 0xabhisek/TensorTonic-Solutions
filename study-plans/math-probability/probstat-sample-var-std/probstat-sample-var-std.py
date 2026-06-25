import numpy as np

def sample_var_std(x):
    """Returns: dict with 'variance' and 'std_dev' as floats."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    mean = np.mean(x)
    variance = float(np.sum((x - mean) ** 2) / (n - 1))
    std_dev = float(np.sqrt(variance))
    return {"variance": variance, "std_dev": std_dev}
