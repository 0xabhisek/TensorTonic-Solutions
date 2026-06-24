import numpy as np

def linear_regression(X, y, lr, epochs):
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    n, d = X.shape

    # initialize
    w = np.zeros(d, dtype=np.float64)
    b = 0.0

    for i in range(epochs):

        # predictions
        y_hat = X @ w + b

        # gradients
        w_grad = (2 / n) * (X.T @ (y_hat - y))
        b_grad = (2 / n) * np.sum(y_hat - y)

        # update
        w -= lr * w_grad
        b -= lr * b_grad

    # round and convert
    w = [round(float(x), 4) for x in w]
    b = round(float(b), 4)

    return (w, b)