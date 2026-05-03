import numpy as np
from gravit.sim.experiment import run_full_experiment

def test_byzantine_threshold():
    results = run_full_experiment(beta_list=[0.0, 0.15, 0.25, 0.35], runs=10)
    # Threshold around γη/(2η+γ) ≈ 0.2 for typical params
    assert results[2]["mean_phi"] < 1e-5, "Failed below threshold"
    assert results[3]["mean_phi"] > 0.1, "Failed to detect failure above threshold"
    print("✓ Byzantine phase transition verified")
