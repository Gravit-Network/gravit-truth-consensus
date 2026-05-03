from gravit.sim.experiment import run_full_experiment

def test_contraction():
    results = run_full_experiment(
        beta_list=[0.0],
        runs=3,
        homogeneous_scoring=True,
        complete_graph=True,
        T_override=600,
    )
    assert results[0]["mean_phi"] < 1e-6
    print("✓ KL contraction verified")
