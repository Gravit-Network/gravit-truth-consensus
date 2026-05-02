# gravit/benchmarks/runner.py

import numpy as np

from gravit.sim.simulator import run_simulation
from gravit.benchmarks.baselines import (
    degroot_step,
    bayesian_average,
    geometric_median
)


def run_all(betas=[0.0, 0.1, 0.2, 0.3]):

    results = {
        "gravit": [],
        "degroot": [],
        "bayes_avg": [],
        "median": []
    }

    for b in betas:

        grav = run_simulation(beta=b)
        results["gravit"].append(grav[-1])

        # synthetic placeholder trajectories
        beliefs = np.random.rand(10, 10)

        results["degroot"].append(
            np.mean(degroot_step(np.ones((10,10))/10, beliefs))
        )

        results["bayes_avg"].append(
            np.mean(bayesian_average(beliefs))
        )

        results["median"].append(
            np.mean(geometric_median(beliefs))
        )

    return results
