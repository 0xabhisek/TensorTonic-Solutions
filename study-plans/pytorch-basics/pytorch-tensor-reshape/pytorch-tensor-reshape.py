import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x = torch.tensor(x, dtype = torch.float32)
    if op == 'flatten':
        return x.reshape(-1)

    elif op == 'squeeze':
        return torch.squeeze(x)
    else:
        return x.T
        
