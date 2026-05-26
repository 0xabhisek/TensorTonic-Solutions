import numpy as np

def subgradient_analysis(x_points, w_init, lr, n_iters):
    """
    Returns: dict with 'abs_subgrad', 'relu_subgrad', 'w_trajectory' (lists) and 'w_final' (float)
    """
    x = np.asarray(x_points, dtype = np.float64)

    abs_subgrad = np.sign(x).tolist()
    relu_subgrad = np.where(x > 0, 1.0, 0.0).tolist()

    w = float(w_init)
    traj = [w]
    for i in range(n_iters):
        g = float(np.sign(w-3)) + w 
        w = w - lr * g
        traj.append(float(w))

    return {
        'abs_subgrad': abs_subgrad,
        'relu_subgrad': relu_subgrad,
        'w_trajectory': traj,
        'w_final': traj[-1]
    }


        
