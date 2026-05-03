import numpy as np
EPS = 1e-12
def compute_phi(P, p_star):
    return np.sum(P * np.log(P / (p_star + EPS) + EPS))
def compute_avg_distance(P, p_star):
    return np.mean(np.linalg.norm(P - p_star, axis=1, ord=1))
def entropy(p):
    return -np.sum(p * np.log(p + EPS))
