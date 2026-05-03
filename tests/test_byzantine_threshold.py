from gravit.sim.experiment import run_full_experiment

def test_byzantine_threshold():
    # Homogeneous honest scores plus a dense graph admit near-consensus without
    # Byzantines; higher beta inflates divergence (Σ_i KL(P_i || mean)).
    results = run_full_experiment(
        beta_list=[0.0, 0.15, 0.25, 0.35],
        runs=12,
        homogeneous_scoring=True,
        complete_graph=True,
        T_override=600,
    )
    phi0, phi_mid, phi_high = (
        results[0]["mean_phi"],
        results[2]["mean_phi"],
        results[3]["mean_phi"],
    )
    assert phi0 < 1e-5
    assert phi_mid < phi_high, "Higher Byzantine fraction should increase divergence"
    assert phi_high > phi0 * 25.0, "Large gap between Byzantine-free and corrupted runs"
    print("✓ Byzantine phase transition verified")
