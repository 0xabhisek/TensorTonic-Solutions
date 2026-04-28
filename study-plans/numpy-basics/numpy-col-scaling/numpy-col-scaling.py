import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""
    a = np.array(data, dtype = np.float64)
    b = np.array(weights, dtype = np.float64)
    return a*b[np.newaxis,:]