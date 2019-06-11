#!/usr/bin/env python

'''
  Superdense code
    A quantum communication protocol to transmit two classical bits of information, by sending only one qubit.

'''

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute

# IBM Q
from qiskit import IBMQ
from qiskit.providers.ibmq import least_busy
IBMQ.load_accounts()

