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

def read_graph_data():
    graph_data = {}
    nodes = int(input("Digite o número de nós no grafo: "))
    for i in range(nodes):
        node = input(f"Digite o nome do nó {i+1}: ")
        graph_data[node] = {}
        
        connections = int(input(f"Digite o número de conexões para o nó {node}: "))
        for j in range(connections):
            neighbor = input(f"Digite o nome do nó vizinho {j+1}: ")
            probability = float(input(f"Digite a probabilidade de transição para o nó vizinho {neighbor}: "))
            graph_data[node][neighbor] = probability
    
    return graph_data

display_menu()

option = input("Digite o número da opção desejada: ")

if option == '1':
    print("\n--- Cálculo do Desempenho do Sistema ---")
    graph_data = read_graph_data()
    # Implementação do cálculo do desempenho com base nos dados do grafo
elif option == '2':
    print("\n--- Cálculo da Carga do Sistema ---")
    # Implementação do cálculo da carga
elif option == '0':
    print("Encerrando o programa...")
else:
    print("Opção inválida. Tente novamente.\n")
