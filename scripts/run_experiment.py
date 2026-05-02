from gravit.sim.simulator import run_simulation


def main():
    kl = run_simulation()
    print("Final KL:", kl[-1])


if __name__ == "__main__":
    main()
