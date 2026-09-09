from client import QuantumPhaseEstimator

def main():
    print("=== Quantum Phase Estimation (QPE) ===")
    # 4 qubits -> phase resolution 1/16 = 0.0625
    qpe = QuantumPhaseEstimator(precision_qubits=4)
    true_phase = 0.375 # exactly 6/16

    res = qpe.estimate_phase(true_phase)
    print("Estimation Result:", res)
    assert abs(res["estimated_phase"] - true_phase) < 1e-4
    assert res["peak_probability"] > 0.99

    print("Quantum Phase Estimation verified successfully!")

if __name__ == "__main__":
    main()
