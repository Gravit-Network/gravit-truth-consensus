import matplotlib.pyplot as plt
from gravit.sim.simulator import run_simulation


def main():

    kl = run_simulation(beta=0.2)

    plt.plot(kl)
    plt.yscale("log")
    plt.title("KL Convergence")
    plt.savefig("figures/fig1_kl.png")


if __name__ == "__main__":
    main()
