import numpy as np

def loss_curvature_analysis(y_hat, y, delta):
    """
    Returns: dict with 'mse', 'ce', 'huber' keys, each containing 'dL' and 'd2L' lists
    """
    y_hat = np.asarray(y_hat, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)

    # MSE: L = (y - y_hat)^2
    mse_dL = (2.0 * (y_hat - y)).tolist()
    mse_d2L = (np.full_like(y_hat, 2.0)).tolist()

    # Cross-Entropy: L = -[y*ln(y_hat) + (1-y)*ln(1-y_hat)]
    ce_dL = (-y / y_hat + (1.0 - y) / (1.0 - y_hat)).tolist()
    ce_d2L = (y / y_hat**2 + (1.0 - y) / (1.0 - y_hat)**2).tolist()

    # Huber: piecewise based on |y - y_hat| vs delta
    residual = y - y_hat
    abs_r = np.abs(residual)
    in_quad = abs_r <= delta

    huber_dL = np.where(in_quad, y_hat - y, np.sign(y_hat - y) * delta).tolist()
    huber_d2L = np.where(in_quad, 1.0, 0.0).tolist()

    return {
        "mse": {"dL": mse_dL, "d2L": mse_d2L},
        "ce": {"dL": ce_dL, "d2L": ce_d2L},
        "huber": {"dL": huber_dL, "d2L": huber_d2L},
    }
