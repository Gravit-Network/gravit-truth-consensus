# gravit/benchmarks/baselines.py

import numpy as np


def degroot_step(W, beliefs):
    return W @ beliefs

def push_sum_step(W, x, y):
    x_new = W @ x
    y_new = W @ y
    return x_new / (y_new + 1e-12)

def bayesian_average(beliefs):
    return np.mean(beliefs, axis=0)

def geometric_median(beliefs):
    return np.median(beliefs, axis=0)
