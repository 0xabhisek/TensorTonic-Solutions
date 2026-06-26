import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    e = 1e-6
    a = np.array(a)
    b = np.array(b)
    norma = np.linalg.norm(a)
    normb = np.linalg.norm(b)
    if norma < e or normb < e:
        return 0.0
    coss = np.dot(a,b)/(norma*normb)
    return coss