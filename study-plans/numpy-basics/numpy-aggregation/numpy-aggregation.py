import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    a = np.array(data, dtype = np.float64)
    r0 = np.mean(a, axis)
    r1 = np.std(a, axis)
    r2 = np.min(a, axis)
    r3 = np.max(a, axis)
    return np.stack([r0,r1,r2,r3])