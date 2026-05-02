# scripts/generate_figures.py

import numpy as np
import matplotlib.pyplot as plt
from gravit.sim.simulator import run_simulation


def main():

    xs = np.linspace(0, 0.5, 8)
    ys = []

    for b in xs:
        kl = run_simulation(beta=b)
        ys.append(kl[-1])

    plt.plot(xs, ys)
    plt.title("Error vs Byzantine ratio")
    plt.savefig("fig_byzantine.png")


if __name__ == "__main__":
    main()
