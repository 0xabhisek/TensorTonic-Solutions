import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    a = np.array(data, dtype = np.float64)

    r = np.round(a,decimals)
    f = np.floor(a)
    c = np.ceil(a)

    rp = np.pad(r,pad_width,mode = 'constant')
    fp = np.pad(f,pad_width, mode = 'constant')
    cp = np.pad(c, pad_width, mode = 'constant')

    return np.stack([rp,fp,cp])