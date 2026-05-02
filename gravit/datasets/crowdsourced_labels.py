# gravit/datasets/crowdsourced_labels.py

import numpy as np


class CrowdSourcedDataset:
    """
    Simulates real-world annotation disagreement:
    - multiple annotators
    - noisy labeling
    - latent true label
    """

    def __init__(self, N_samples=1000, K=5, noise=0.2):
        self.N = N_samples
        self.K = K
        self.noise = noise

        self.truth = np.random.randint(K, size=N_samples)

    def get_annotations(self, n_annotators=10):
        annotations = []

        for i in range(n_annotators):
            labels = self.truth.copy()

            noise_mask = np.random.rand(self.N) < self.noise
            labels[noise_mask] = np.random.randint(0, self.K, noise_mask.sum())

            annotations.append(labels)

        return np.array(annotations), self.truth
