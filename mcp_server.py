import sys
import json
from client import QuantumPhaseEstimator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "estimate":
        qubits = params.get("precision_qubits", 4)
        phase = params.get("phase", 0.25)
        estimator = QuantumPhaseEstimator(qubits)
        return estimator.estimate_phase(phase)
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
