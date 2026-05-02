import matplotlib.pyplot as plt
from gravit.sim.simulator import run


def main():
    betas = [0.0, 0.1, 0.2, 0.3]

    plt.figure()

    for b in betas:
        kl = run(beta=b)
        plt.plot(kl, label=f"beta={b}")

    plt.yscale("log")
    plt.legend()
    plt.title("KL Convergence")
    plt.show()


if __name__ == "__main__":
    main()
