# scripts/benchmark_plot.py

import matplotlib.pyplot as plt
import numpy as np
from gravit.benchmarks.runner import run_all


def main():

    betas = [0.0, 0.1, 0.2, 0.3]
    res = run_all(betas)

    plt.plot(betas, res["gravit"], label="Gravit")
    plt.plot(betas, res["degroot"], label="DeGroot")
    plt.plot(betas, res["bayes_avg"], label="Bayesian Avg")
    plt.plot(betas, res["median"], label="Geometric Median")

    plt.title("Byzantine Robustness Comparison")
    plt.legend()
    plt.savefig("benchmark_comparison.png")


if __name__ == "__main__":
    main()
