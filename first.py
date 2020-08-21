# %%
import qiskit as qk

q = qk.QuantumRegister(2)
c = qk.ClassicalRegister(2)

circuit = qk.QuantumCircuit(q, c)

circuit.h(q[0])
circuit.cx(q[0], q[1])
circuit.measure(q, c)
circuit.draw(output='mpl')


# %%
circ = qk.QuantumCircuit(3)
circ.h(0)
circ.x(1)
circ.cx(0, 1)
circ.cx(1, 2)
circ.draw()

# %%
