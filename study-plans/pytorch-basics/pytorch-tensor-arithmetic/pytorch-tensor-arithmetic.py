import torch
import numpy as np

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    X = torch.tensor(x)
    Y = torch.tensor(y)
    if op == 'add':
        return torch.add(X,Y).tolist()
    elif op == 'matmul':
        return torch.matmul(X,Y).tolist()
    elif op == 'multiply':
        return torch.mul(X,Y).tolist()
    elif op == 'power':
        return np.power(X,Y).tolist()
    else:
        return torch.max(X,Y).tolist()
    