import matplotlib.pyplot as plt
import numpy as np
from gravit.sim.simulator import run


def generate_figures():

    betas = [0.0, 0.1, 0.2, 0.3]

    # FIGURE 1: KL convergence
    plt.figure()

    for b in betas:
        kl = run(beta=b)
        plt.plot(kl, label=f"β={b}")

    plt.yscale("log")
    plt.title("KL Divergence Convergence")
    plt.legend()
    plt.savefig("figs/fig1_kl.png")

    # FIGURE 2: accuracy vs beta
    plt.figure()

    xs = np.linspace(0, 0.5, 10)
    ys = []

    for b in xs:
        kl = run(beta=b)
        ys.append(kl[-1])

    plt.plot(xs, ys)
    plt.title("Final Error vs Byzantine Ratio")
    plt.savefig("figs/fig2_byzantine.png")


if __name__ == "__main__":
    generate_figures()
