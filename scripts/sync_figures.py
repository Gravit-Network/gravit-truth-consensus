# scripts/sync_figures.py

import os
from gravit.sim.simulator import run_simulation


def generate_all_figures():

    os.makedirs("figures", exist_ok=True)

    betas = [0.0, 0.1, 0.2, 0.3]

    kl_curves = []

    for b in betas:
        kl = run_simulation(beta=b)
        kl_curves.append(kl)

    # save data for latex rendering
    import numpy as np
    np.save("figures/kl_curves.npy", kl_curves)
