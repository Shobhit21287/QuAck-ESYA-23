import nbimporter
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import QuAcK_Lab as QuAcK

# Colors
BOLD = "\033[1m"
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"
RESET = "\033[0m"


# Functions

ket_to_bra = QuAcK.ket_to_bra
is_unitary = QuAcK.is_unitary
Z_gate = QuAcK.Z_gate
expectation = QuAcK.expectation
tensor_product = QuAcK.tensor_product
CNOT_Cirq = QuAcK.CNOT_Cirq
FFT_pointgen = QuAcK.FFT_pointgen
binary_to_decimal = QuAcK.binary_to_decimal
qpe_circuit1 = QuAcK.qpe_circuit
qpe_circuit2 = QuAcK.qpe_circuit
classical_shor = QuAcK.classical_shor
decode = QuAcK.decode


# Question 1
print(BOLD + CYAN + "\nQuestion 1" + RESET)
kets = [[1+1j, 2+5j, 3+2j], [1+1j, 2+5j, 3-2j]]
ans = [[[1-1j], [2-5j], [3-2j]], [[1-1j], [2-5j], [3+2j]]]

for i in range(len(kets)):
    try:
        bra = ket_to_bra(kets[i])
        if len(bra) != len(ans[i]):
            print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
            continue
        for j in range(len(ans[i])):
            if ans[i][j] != bra[j]:
                print(RED + BOLD + "[Failed] " +
                      RESET + "Test Case " + str(i+1))
                break
        else:
            print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
    except:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Question 2
print(BOLD + CYAN + "\nQuestion 2" + RESET)
matrices = [[[1, 0], [0, 1]]]
ans = [True]
for i in range(len(matrices)):
    try:
        sol = is_unitary(matrices[i])
        if type(sol) != bool:
            print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
        elif (sol == ans[i]):
            print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
        else:
            print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
    except:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Question 3
print(BOLD + CYAN + "\nQuestion 3" + RESET)
qc = QuantumCircuit(1)
qc.h(0)
qc.x(0)
qc.h(0)

i = 0
ans = Z_gate()

try:
    if ans == qc:
        print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
    else:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
except:
    print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Question 4
print(BOLD + CYAN + "\nQuestion 4" + RESET)
eigenvalues = [[0+8j, 6], [1+9j, 12]]
ans = [6, 12]

for i in range(len(eigenvalues)):
    try:
        sol = expectation(eigenvalues[i])
        if sol == ans[i]:
            print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
        else:
            print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
    except:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Question 5
print(BOLD + CYAN + "\nQuestion 5" + RESET)
arr1 = [[1, 2, 3]]
arr2 = [[1, 2, 3]]

ans = [[1, 2, 3, 2, 4, 6, 3, 6, 9]]

for i in range(len(arr1)):
    try:
        sol = tensor_product(arr1[i], arr2[i])
        if sol == ans[i]:
            print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
        else:
            print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
    except:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Question 6
print(BOLD + CYAN + "\nQuestion 6" + RESET)
qc = QuantumCircuit(2, 1)
qc.h(0)
qc.cx(0, 1)
qc.measure(1, 0)

sol = CNOT_Cirq()

i = 0
try:
    if qc == sol:
        print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
    else:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
except:
    print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Quetsion 7
print(BOLD + CYAN + "\nQuestion 7" + RESET)
order_px = [1]
order_qx = [1]

def FFT_pointgen_sol(order_px,order_qx) : 
    n = order_px + order_qx + 1
    a = np.power(np.e,1j*2*np.pi/n)
    return a

for i in range(len(order_px)):
    try:
        sol = FFT_pointgen(order_px[i], order_qx[i])
        if sol == FFT_pointgen_sol(order_px[i], order_qx[i]):
            print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
        else:
            print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
    except:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Question 8
print(BOLD + CYAN + "\nQuestion 8" + RESET)
binary = ["0.11", "0.1", "0.101"]
ans = [0.75, 0.5, 0.625]
for i in range(len(binary)):
    try:
        sol = binary_to_decimal(binary[i])
        assert sol == ans[i]
        print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
    except:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Question 9
print(BOLD + CYAN + "\nQuestion 9" + RESET)


def qft_dagger(qc, n):
    """n-qubit QFTdagger the first n qubits in circ"""
    # Don't forget the Swaps!
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            qc.cp(-np.pi/float(2**(j-m)), m, j)
        qc.h(j)


def qpe_circuit1_sol(n):
    qpe = QuantumCircuit(n, n - 1)
    for qubit in range(n - 1):
        qpe.h(qubit)

    for i in range(n - 1):
        for j in range(2**i):
            qpe.cp(2*np.pi/7*j, n - 1, i)

    qft_dagger(qpe, n)

    for i in range(n - 1):
        qpe.measure(i, i)

    return qpe


def qpe_circuit2_sol(n):
    qpe = QuantumCircuit(n, n - 1)
    for qubit in range(n - 1):
        qpe.h(qubit)

    for i in range(n - 1):
        for j in range(2**i):
            qpe.cp(2*np.pi/7, n - 1, i)

    qft_dagger(qpe, n)

    for i in range(n - 1):
        qpe.measure(i, i)

    return qpe


inputs = [4, 5, 6]
ans1 = [qpe_circuit1_sol(i) for i in inputs]
ans2 = [qpe_circuit2_sol(i) for i in inputs]

for i in range(len(inputs)):
    try:
        assert qpe_circuit1(inputs[i]) == ans1[i]
        print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
        continue
    except:
        try:
            assert qpe_circuit2(inputs[i]) == ans2[i]
            print(GREEN + BOLD + "[Passed] " + RESET +
                "Test Case " + str(i+1))
        except:
            print(RED + BOLD + "[Failed] " + RESET +
                "Test Case " + str(i+1))
            
        

    


# Question 10
print(BOLD + CYAN + "\nQuestion 10" + RESET)
inputs = [391]
ans = [[17, 23]]

for i in range(len(inputs)):
    try:
        assert ans[i] == classical_shor(inputs[i])
        print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
    except:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))


# Quesiton 11
print(BOLD + CYAN + "\nQuestion 11" + RESET)
input1 = [65]
input2 = [5]
input3 = [41]

ans = [9]

for i in range(len(input1)):
    try:
        assert ans[i] == decode(input1[i], input2[i], input3[i])
        print(GREEN + BOLD + "[Passed] " + RESET + "Test Case " + str(i+1))
    except:
        print(RED + BOLD + "[Failed] " + RESET + "Test Case " + str(i+1))
