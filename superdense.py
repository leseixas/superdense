#!/usr/bin/env python

'''
  Superdense code
    A quantum communication protocol to transmit two classical bits of information, by sending only one qubit.

'''

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute

# QASM simulator
from qiskit import Aer
backend = Aer.get_backend('qasm_simulator')

# IBM Q
#from qiskit import IBMQ
#from qiskit.providers.ibmq import least_busy
#IBMQ.load_accounts()
#large_enough_devices = IBMQ.backends(filters=lambda x: x.configuration().n_qubits > 3 and not x.configuration().simulator)
#backend = least_busy(large_enough_devices)

print("Backend:",backend)

# Preparation (Bell state)
qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)

# Encoding
# 00 = id
# 10 = Z
# 01 = X
# 11 = Z*X

#qc.x(0) # 10
#qc.y(0) # 11 # equal to X*Z
#qc.z(0) # 01


# Decoding

qc.cx(0,1)
qc.h(0)

qc.measure([0,1],[0,1])

job = execute(qc, backend, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print(counts)

