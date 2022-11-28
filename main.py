import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt

def isConstant(counts):
    """
    Verifica entre las llaves de la función si esta es constante
    (Dict) -> String
    """
    if '0000' in counts.keys():
        print("Función Constante")
    else:
        print("Función Balanceada")

def main():
    #Funcion cruzada (0->1, 1-0)
    print("------------Algoritmo Deutsch------------")
    print("------------Funcion (0->1, 1->0)---------")
    # Prueba 00
    print("------------Prueba 00--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    #Entradas

    #Barrera
    circuit.barrier(0, 1)
    #Funcion
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)
    #Barrera
    circuit.barrier(0, 1)
    #Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion cruzada (0->1, 1-0)
    print("------------Funcion (0->1, 1->0)------------")
    # Prueba 01
    print("------------Prueba 01-----------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)

    #Entradas
    circuit.x(1)
    #Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)
    #Barrera
    circuit.barrier(0, 1)
    #Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion cruzada (0->1, 1-0)
    print("------------Funcion (0->1, 1->0)------------")
    # Prueba 10
    print("------------Prueba 10-----------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    #Entradas
    circuit.x(0)
    #Barrera
    circuit.barrier(0, 1)
    #Funcion
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)
    #Barrera
    circuit.barrier(0, 1)
    #Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion cruzada (0->1, 1-0)
    print("------------Funcion (0->1, 1->0)------------")
    # Prueba 11
    print("------------Prueba 11-----------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    #Entradas
    circuit.x(1)
    circuit.x(0)
    #Barrera
    circuit.barrier(0, 1)
    #Funcion
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)
    #Barrera
    circuit.barrier(0, 1)
    #Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion cruzada (0->1, 1-0)
    print("-----------Funcion (0->1, 1->0)------------")
    # Algoritmo Deutsch
    print("-----------Prueba Algoritmo Deutsch--------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)

    # Entradas
    circuit.x(1)
    #Barrera
    circuit.barrier(0,1)
    #Algoritmo Deutsch
    circuit.h(0)
    circuit.h(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)
    #Barrera
    circuit.barrier(0, 1)
    #Algoritmo Deutsch
    circuit.h(0)
    #Medicion
    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    #Funcion recta (0->0, 1->1)
    print("------------Algoritmo Deutsch------------")
    print("------------Funcion (0->0, 1->1)---------")
    # Prueba 00
    print("------------Prueba 00--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    #Entradas

    #Barrera
    circuit.barrier(0, 1)
    #Funcion
    circuit.cx(0, 1)
    #Barrera
    circuit.barrier(0, 1)
    #Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion recta (0->0, 1->1)
    print("------------Funcion (0->0, 1->1)---------")
    # Prueba 01
    print("------------Prueba 01--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.cx(0, 1)
    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion recta (0->0, 1->1)
    print("------------Funcion (0->0, 1->1)---------")
    # Prueba 10
    print("------------Prueba 10--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(0)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.cx(0, 1)
    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion recta (0->0, 1->1)
    print("------------Funcion (0->0, 1->1)---------")
    # Prueba 11
    print("------------Prueba 11--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(0)
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.cx(0, 1)
    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion (0->0, 1->1)
    print("-----------Funcion (0->0, 1->1)------------")
    # Algoritmo Deutsch
    print("-----------Prueba Algoritmo Deutsch--------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)

    # Entradas
    circuit.x(1)
    #barrera
    circuit.barrier(0, 1)
    #Algoritmo Deutsch
    circuit.h(0)
    circuit.h(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.cx(0, 1)
    #Barrera
    circuit.barrier(0, 1)
    #Algoritmo Deutsch
    circuit.h(0)
    #Medicion
    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion todas a 0 (0->0, 1->0)
    print("------------Funcion (0->0, 1->0)---------")
    # Prueba 00
    print("------------Prueba 00--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas

    # Barrera
    circuit.barrier(0, 1)
    # Funcion

    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion todas a 0 (0->0, 1->0)
    print("------------Funcion (0->0, 1->0)---------")
    # Prueba 01
    print("------------Prueba 01--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion

    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion todas a 0 (0->0, 1->0)
    print("------------Funcion (0->0, 1->0)---------")
    # Prueba 10
    print("------------Prueba 10--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(0)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion

    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()


    # Funcion todas a 0 (0->0, 1->0)
    print("------------Funcion (0->0, 1->0)---------")
    # Prueba 11
    print("------------Prueba 11--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(1)
    circuit.x(0)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion

    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion (0->0, 1->0)
    print("-----------Funcion (0->0, 1->0)------------")
    # Algoritmo Deutsch
    print("-----------Prueba Algoritmo Deutsch--------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)

    # Entradas
    circuit.x(1)
    #Barrera
    circuit.barrier(0, 1)
    # Algoritmo Deutsch
    circuit.h(0)
    circuit.h(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion

    # Barrera
    circuit.barrier(0, 1)
    # Algoritmo Deutsch
    circuit.h(0)
    # Medicion
    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion todas a 1 (0->1, 1->1)
    print("------------Funcion (0->1, 1->1)---------")
    # Prueba 00
    print("------------Prueba 00--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas

    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion todas a 1 (0->1, 1->1)
    print("------------Funcion (0->1, 1->1)---------")
    # Prueba 01
    print("------------Prueba 01--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion todas a 1 (0->1, 1->1)
    print("------------Funcion (0->1, 1->1)---------")
    # Prueba 10
    print("------------Prueba 10--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(0)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion todas a 1 (0->1, 1->1)
    print("------------Funcion (0->1, 1->1)---------")
    # Prueba 11
    print("------------Prueba 11--------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 2)
    # Entradas
    circuit.x(0)
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Medicion
    circuit.measure([0, 1], [1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    # Funcion (0->1, 1->1)
    print("-----------Funcion (0->1, 1->1)------------")
    # Algoritmo Deutsch
    print("-----------Prueba Algoritmo Deutsch--------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)

    # Entradas
    circuit.x(1)
    # barrera
    circuit.barrier(0, 1)
    # Algoritmo Deutsch
    circuit.h(0)
    circuit.h(1)
    # Barrera
    circuit.barrier(0, 1)
    # Funcion
    circuit.x(1)
    # Barrera
    circuit.barrier(0, 1)
    # Algoritmo Deutsch
    circuit.h(0)
    # Medicion
    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    # Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    print()

    print("------------Algoritmo Deutsch-Jozsa--------------")

    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)
    #Funcion
    circuit.cx(0, 3)
    #Medicion
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("-------------------------------------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)
    #Funcion
    circuit.cx(1, 4)
    #Medicion
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    #Impresion
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("-------------------------------------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)
    #Funcion
    circuit.cx(3, 4)
    #Medicion
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    #Impresion
    counts = result.get_counts(circuit)
    isConstant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("-------------------------------------------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)
    #Funcion
    circuit.cx(0,4)
    #Medicion
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    #Impresion
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("--------------Pruebas Algoritmo Deutsch Jozsa--------------")
    print("--------------Primera funcion--------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)
    #Entradas
    circuit.x(4)
    #Barrera
    circuit.barrier()
    #Algoritmo Deutsch Jozsa
    for i in range(0, 5):
        circuit.h(i)
    #Barrera
    circuit.barrier()
    #Funcion
    circuit.cx(0, 3)
    #Barrera
    circuit.barrier()
    # Algoritmo Deutsch Jozsa
    for i in range(0, 4):
        circuit.h(i)
    circuit.barrier()
    #Medicion
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    isConstant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("--------------Segunda funcion--------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)
    #Entradas
    circuit.x(4)
    #Barrera
    circuit.barrier()
    #Algoritmo Deutsch Jozsa
    for i in range(0, 5):
        circuit.h(i)
    #Barrera
    circuit.barrier()
    #Funcion
    circuit.cx(1, 4)
    #Barreara
    circuit.barrier()
    # Algoritmo Deutsch Jozsa
    for i in range(0, 4):
        circuit.h(i)
    #Barrera
    circuit.barrier()
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    isConstant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    # Algoritmo Deutsch Jozsa
    print("--------------Tercera funcion--------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)
    #Entradas
    circuit.x(4)
    #Barrera
    circuit.barrier()
    #Algoritmo Deutsch Jozsa
    for i in range(0, 5):
        circuit.h(i)
    #Barrera
    circuit.barrier()
    #Funcion
    circuit.cx(2, 4)
    #Barrera
    circuit.barrier()
    #Algoritmo Deutsch Jozsa
    for i in range(0, 4):
        circuit.h(i)
    #Barrera
    circuit.barrier()
    #Medicion
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    isConstant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    print("--------------Cuarta funcion--------------")
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 4)
    #Entradas
    circuit.x(4)
    #Barrera
    circuit.barrier()
    # Algoritmo Deutsch Jozsa
    for i in range(0, 5):
        circuit.h(i)
    #Barrera
    circuit.barrier()
    #Funcion
    circuit.cx(0,4)
    #Barrera
    circuit.barrier()
    # Algoritmo Deutsch Jozsa
    for i in range(0, 4):
        circuit.h(i)
    #Barrera
    circuit.barrier()
    #Medicion
    circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    #Impresion
    result = job.result()
    counts = result.get_counts(circuit)
    isConstant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()
main()

