import numpy as np

def markov_model(performance_matrix, load_vector):
    stationary_dist = np.linalg.solve(performance_matrix.T - np.eye(len(performance_matrix)), np.zeros(len(performance_matrix)))
    performance = np.dot(stationary_dist, load_vector)
    return performance

def markov_load(performance_matrix, load_vector):
    stationary_dist = np.linalg.solve(performance_matrix.T - np.eye(len(performance_matrix)), np.zeros(len(performance_matrix)))
    load = np.dot(stationary_dist, np.dot(performance_matrix, load_vector))
    return load

def display_menu():
    print("===== Modelo de Desempenho e Carga de Markov =====")
    print("1. Calcular o desempenho do sistema")
    print("2. Calcular a carga do sistema")
    print("0. Sair")

display_menu()

option = input("Digite o número da opção desejada: ")

if option == '1':
    print("\n--- Cálculo do Desempenho do Sistema ---")
    # Implementação do cálculo do desempenho
elif option == '2':
    print("\n--- Cálculo da Carga do Sistema ---")
    # Implementação do cálculo da carga
elif option == '0':
    print("Encerrando o programa...")
else:
    print("Opção inválida. Tente novamente.\n")
