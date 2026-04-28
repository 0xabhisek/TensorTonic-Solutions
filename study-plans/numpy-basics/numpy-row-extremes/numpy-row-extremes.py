import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    arr = np.array(data, dtype = np.float64)
    max = np.max(arr, axis = 1)
    min = np.min(arr, axis = 1)
    maxin = np.argmax(arr, axis = 1)
    minin = np.argmin(arr, axis = 1)
    return np.stack([max,maxin,min,minin])