import argparse
from gravit.sim.experiment import run_full_experiment

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", nargs="+", type=float, default=[0.0, 0.1, 0.2, 0.3])
    args = parser.parse_args()
    run_full_experiment(beta_list=args.beta)
    print("Done.")
