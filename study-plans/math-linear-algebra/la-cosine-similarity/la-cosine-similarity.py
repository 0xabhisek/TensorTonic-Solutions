import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    x = np.asarray(a,dtype = float)
    y = np.asarray(b, dtype = float)
    m = np.dot(x,y)
    n = np.linalg.norm(x) * np.linalg.norm(y)
    if n < 1e-10:
        return 0.0
    
    return m/n