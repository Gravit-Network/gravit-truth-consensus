import numpy as np

def capital_weighted_consensus(p: np.ndarray, capitals: np.ndarray) -> np.ndarray:
    w = capitals / np.sum(capitals)
    return np.average(p, axis=0, weights=w)
