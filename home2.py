import cirq


def apply_balanced_oracle(qubits):
    circuit = cirq.Circuit()
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))
    circuit.append(cirq.X(qubits[2]))
    circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[3]))
    circuit.append(cirq.CX(qubits[2], qubits[3]))
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))
    circuit.append(cirq.X(qubits[2]))
    return circuit


def apply_const_oracle(qubits):
    circuit = cirq.Circuit(cirq.X(qubits[3]))
    return circuit


def create_deutsch_jozsa_circuit(oracle):
    qubits = cirq.LineQubit.range(4)
    dj_circuit = cirq.Circuit()
    dj_circuit.append(cirq.H(q) for q in qubits[:-1])
    dj_circuit.append(cirq.X(qubits[-1]))
    dj_circuit.append(cirq.H(qubits[-1]))
    dj_circuit.append(oracle(qubits))
    dj_circuit.append(cirq.H(q) for q in qubits[:-1])
    dj_circuit.append(cirq.measure(*qubits[:-1], key='result'))
    return dj_circuit


def run_deutsch_jozsa_algorithm(oracle):
    dj_circuit = create_deutsch_jozsa_circuit(oracle)
    simulator = cirq.Simulator()
    result = simulator.run(dj_circuit)
    return result


def print_results(balanced_result, const_result):
    print("Balanced Oracle Result:", balanced_result.measurements['result'])
    print("Constant Oracle Result:", const_result.measurements['result'])


qubits = cirq.LineQubit.range(4)
balanced_result = run_deutsch_jozsa_algorithm(apply_balanced_oracle)
const_result = run_deutsch_jozsa_algorithm(apply_const_oracle)

print_results(balanced_result, const_result)
print(apply_balanced_oracle(qubits))
print(apply_const_oracle(qubits))
