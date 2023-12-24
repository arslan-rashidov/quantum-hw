import cirq
import numpy as np

def inverse_fourier_transform(qubits):
    n = len(qubits)
    circuit = cirq.Circuit()

    for i in range(n):
        circuit.append(cirq.H(qubits[i]))

    for control_qubit in range(n):
        for target_qubit in range(control_qubit + 1, n):
            angle = 2.0 * np.pi / (2 ** (target_qubit - control_qubit + 1))
            circuit.append(cirq.CZ(qubits[control_qubit], qubits[target_qubit]) ** angle)

    for i in range(n // 2):
        circuit.append(cirq.SWAP(qubits[i], qubits[n - i - 1]))

    return circuit

input_state = np.array([1, 0, 0, 0])
qubits = cirq.LineQubit.range(len(input_state))
circuit_input = cirq.Circuit()
for i, bit in enumerate(input_state):
    if bit:
        circuit_input.append(cirq.X(qubits[i]))
circuit_transform = inverse_fourier_transform(qubits)
simulator = cirq.Simulator()
result = simulator.simulate(circuit_input + circuit_transform)
output_state = result.final_state_vector
print("Входное состояние:", input_state)
print("Выходное состояние после обратного преобразования Фурье:", output_state)