import cirq


def add_one_mod_four(qubits):
    circuit = cirq.Circuit()
    circuit.append(cirq.CNOT(qubits[1], qubits[0]))
    circuit.append(cirq.X(qubits[1]))
    print("Result (+1, %4):")
    print(circuit)
    sim = cirq.Simulator()
    result = sim.simulate(circuit)
    print(result)


def is_equals_two(qubits):
    circuit = cirq.Circuit()
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[2]))
    print("Result (== 2):")
    print(circuit)
    sim = cirq.Simulator()
    result = sim.simulate(circuit)
    print(result)


def grover_search(oracle, grover_circuit, num_iterations, qubits):
    for _ in range(num_iterations):
        grover_circuit.append(oracle)
        grover_circuit.append(cirq.H.on_each(qubits))
        grover_circuit.append(cirq.X.on_each(qubits))
        grover_circuit.append(cirq.H.on(qubits[1]))
        grover_circuit.append(cirq.CNOT(qubits[0], qubits[1]))
        grover_circuit.append(cirq.H.on(qubits[1]))
        grover_circuit.append(cirq.X.on_each(qubits))
        grover_circuit.append(cirq.H.on_each(qubits))
        grover_circuit.append(oracle)
        grover_circuit.append(cirq.H.on(qubits[1]))
        grover_circuit.append(cirq.CNOT(qubits[0], qubits[1]))
        grover_circuit.append(cirq.H.on(qubits[1]))
        grover_circuit.append(cirq.X.on_each(qubits))
        grover_circuit.append(cirq.H.on_each(qubits))

    return grover_circuit


def oracle(qubits):
    return cirq.Circuit(cirq.X(qubits[0]), cirq.CCX(qubits[0], qubits[1], qubits[2]), cirq.X(qubits[0]))


def is_equals_two_by_grover(qubits):
    grover_circuit = cirq.Circuit()
    grover_circuit = grover_search(oracle=oracle(qubits), grover_circuit=grover_circuit, num_iterations=1,
                                   qubits=qubits)
    grover_circuit.append(cirq.measure(qubits[0], key='result'))
    simulator = cirq.Simulator()
    result = simulator.run(grover_circuit, repetitions=1000)
    print("Результаты:", result.histogram(key='result'))


qubits_add_one = [cirq.LineQubit(i) for i in range(2)]
qubits_equals_two = [cirq.LineQubit(i) for i in range(3)]

add_one_mod_four(qubits_add_one)
is_equals_two(qubits_equals_two)

is_equals_two_by_grover(qubits_equals_two)
