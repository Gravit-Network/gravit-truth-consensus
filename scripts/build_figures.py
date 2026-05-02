import numpy as np
import matplotlib.pyplot as plt
from gravit.sim.simulator import run_simulation
from gravit.benchmarks.runner import run_all


def fig1():
    betas = [0.0, 0.1, 0.2, 0.3]

    plt.figure()

    for b in betas:
        kl = run_simulation(beta=b)
        plt.plot(kl)

    plt.yscale("log")
    plt.title("KL Convergence")
    plt.savefig("figures/fig1_kl.png")


def fig2():
    xs = np.linspace(0, 0.5, 10)
    ys = []

    for b in xs:
        kl = run_simulation(beta=b)
        ys.append(kl[-1])

    plt.figure()
    plt.plot(xs, ys)
    plt.title("Phase Transition")
    plt.savefig("figures/fig2_phase_transition.png")


def fig3():
    res = run_all([0.0, 0.1, 0.2, 0.3])

    plt.figure()
    plt.plot(res["gravit"], label="Gravit")
    plt.plot(res["degroot"], label="DeGroot")
    plt.plot(res["bayes_avg"], label="Bayesian Avg")

    plt.legend()
    plt.title("Baseline Comparison")
    plt.savefig("figures/fig3_baselines.png")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
