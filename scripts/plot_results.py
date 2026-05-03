import json
import matplotlib.pyplot as plt

with open("results/experiment_results.json") as f:
    data = json.load(f)

betas = [d["beta"] for d in data]
phis = [d["phi"] for d in data]

plt.figure(figsize=(8, 5))
plt.plot(betas, phis, marker='o')
plt.xlabel("Byzantine fraction β")
plt.ylabel("Final Φ (KL Lyapunov)")
plt.title("Phase Transition at Byzantine Threshold")
plt.grid(True)
plt.savefig("results/phase_transition.png")
plt.show()
