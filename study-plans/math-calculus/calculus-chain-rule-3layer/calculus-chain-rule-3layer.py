import numpy as np

def chain_rule_3layer(w1, w2, w3, x):
    """
    Returns: dict with 'factors' (list of 6 floats), 'analytical_gradient' (float), 'numerical_gradient' (float)
    """
    x = np.asarray(x, dtype = float)
    def s(z):
        return 1.0/(1.0 + np.exp(-z))

    #Forward pass
    z1 = w1 * x
    a1 = s(z1)
    z2 = w2 * a1
    a2 = s(z2)
    z3 = w3 * a2
    y = s(z3)

    #sigmoid derivatives at each layer
    sd1 = a1 * (1.0 - a1)
    sd2 = a2 * (1.0 - a2)
    sd3 = y * (1.0 - y)

    factors = [float(sd3), float(w3), float(sd2), float(w2), float(sd1), float(x)]

    an = 1.0
    for f in factors:
        an *= f

    h = 1e-5
    def forward(w1_val):
        a1d = s(w1_val*x)
        a2d = s(w2*a1d)
        return s(w3*a2d)

    n = float((forward(w1+h) - forward(w1-h))/(2*h))

    return {
        'factors': factors,
        'analytical_gradient': an,
        'numerical_gradient': n
    }
    






    
