import numpy as np

def activation_continuity_analysis(x):
    """
    Returns: dict mapping 'relu', 'leaky_relu', 'gelu' to lists of non-differentiable x values
    """
    x = np.asarray(x, dtype = np.float64)
    h = 1e-7
    tol = 1e-5

    def relu(z):
        return np.maximum(0,z)

    def leaky_relu(z, alpha = 0.01):
        return np.where(z >= 0, z, alpha * z)

    def gelu(z):
        return (0.5*z*(1 + np.tanh(((2/np.pi)** 0.5)*(z + 0.044715*(z**3)))))

    result = {}

    for name,fn in [('relu', relu),('leaky_relu', leaky_relu),('gelu', gelu)]:
        ld = (fn(x) - fn(x-h))/h
        rd = (fn(x+h) - fn(x))/h
        non_diff_mask = np.abs(ld - rd) >= tol
        result[name] = x[non_diff_mask].tolist()
    return result






    
