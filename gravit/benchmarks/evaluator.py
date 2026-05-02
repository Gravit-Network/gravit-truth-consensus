# gravit/benchmarks/evaluator.py

import numpy as np
from gravit.math.metrics import kl


class BenchmarkEvaluator:

    def __init__(self, K):
        self.K = K

    def evaluate(self, trajectory, truth):
        avg = np.mean(trajectory, axis=0)
        return {
            "kl": kl(avg, truth),
            "accuracy": np.argmax(avg) == np.argmax(truth)
        }
