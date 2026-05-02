# scripts/run_experiment.py

import matplotlib.pyplot as plt
from gravit.sim.simulator import run_simulation


def main():

    betas = [0.0, 0.1, 0.2, 0.3]

    plt.figure()

    for b in betas:
        kl = run_simulation(beta=b)
        plt.plot(kl, label=f"beta={b}")

    plt.yscale("log")
    plt.legend()
    plt.title("Gravit Truth Consensus - KL Convergence")
    plt.show()


if __name__ == "__main__":
    main()
