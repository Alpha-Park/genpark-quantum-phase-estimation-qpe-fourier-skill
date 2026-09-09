import math
import cmath

class QuantumPhaseEstimator:
    """Quantum Phase Estimation (QPE) simulator for unitary operators."""
    def __init__(self, precision_qubits: int):
        self.precision_qubits = precision_qubits
        self.num_states = 1 << precision_qubits

    def qft(self, vector: list[complex], inverse: bool = False) -> list[complex]:
        """Direct Quantum Fourier Transform implementation."""
        N = len(vector)
        result = [0.0 + 0.0j] * N
        sign = -1.0 if inverse else 1.0
        norm = 1.0 / math.sqrt(N)
        for k in range(N):
            acc = 0.0 + 0.0j
            for j in range(N):
                angle = sign * 2.0 * math.pi * j * k / N
                acc += vector[j] * cmath.exp(1j * angle)
            result[k] = acc * norm
        return result

    def estimate_phase(self, true_phase: float) -> dict:
        """
        true_phase: float in [0, 1), representing eigenvalue e^(2*pi*i*theta)
        """
        # Create registering statevector after controlled-U operations
        register = [0.0 + 0.0j] * self.num_states
        for j in range(self.num_states):
            angle = 2.0 * math.pi * true_phase * j
            register[j] = cmath.exp(1j * angle) / math.sqrt(self.num_states)

        # Apply Inverse Quantum Fourier Transform (IQFT)
        measured_state = self.qft(register, inverse=True)

        probabilities = [abs(amp) ** 2 for amp in measured_state]
        best_index = max(range(self.num_states), key=lambda i: probabilities[i])
        estimated_phase = best_index / self.num_states
        error = abs(estimated_phase - true_phase)

        return {
            "precision_qubits": self.precision_qubits,
            "register_states": self.num_states,
            "true_phase": round(true_phase, 5),
            "estimated_phase": round(estimated_phase, 5),
            "phase_error": round(error, 6),
            "peak_probability": round(probabilities[best_index], 4)
        }
