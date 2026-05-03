import numpy as np
def T(p, s, W):
    P_hat = p * s
    P_hat /= P_hat.sum(axis=1, keepdims=True) + 1e-12
    return W @ P_hat
