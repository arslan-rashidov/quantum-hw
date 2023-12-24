import cirq


def apply_x_and_cx(circuit, qubits):
    circuit.append(cirq.X.on_each(*qubits[:3]))
    circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[3]))
    circuit.append(cirq.CX(qubits[2], qubits[3]))
    circuit.append(cirq.X.on_each(*qubits[:3]))


def create_main_circuit(qubits):
    main_circuit = cirq.Circuit()
    apply_x_and_cx(main_circuit, qubits)
    return main_circuit


def print_qubits(qubits):
    for qubit in qubits:
        print(qubit)


qubits = cirq.LineQubit.range(4)
main_circuit = create_main_circuit(qubits)

print_qubits(qubits)
print(main_circuit)