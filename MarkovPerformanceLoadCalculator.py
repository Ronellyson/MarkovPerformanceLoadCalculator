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

def read_table_data():
    table_data = {}
    nodes = int(input("Digite o número de nós na tabela de demandas de serviço: "))
    for i in range(nodes):
        node = input(f"Digite o nome do nó {i+1}: ")
        demand = float(input(f"Digite a demanda de serviço para o nó {node}: "))
        table_data[node] = demand
    
    return table_data

display_menu()

option = input("Digite o número da opção desejada: ")

if option == '1':
    print("\n--- Cálculo do Desempenho do Sistema ---")
    graph_data = read_graph_data()
    table_data = read_table_data()

    # Criação da matriz de desempenho
    performance_matrix = np.zeros((len(graph_data), len(graph_data)))
    for i, node in enumerate(graph_data):
        for j, neighbor in enumerate(graph_data):
            if neighbor in graph_data[node]:
                performance_matrix[i][j] = graph_data[node][neighbor]

    # Criação do vetor de demandas de serviço
    load_vector = np.zeros(len(graph_data))
    for i, node in enumerate(graph_data):
        if node in table_data:
            load_vector[i] = table_data[node]

    # Cálculo do desempenho do sistema
    performance = markov_model(performance_matrix, load_vector)
    print(f"O desempenho do sistema é: {performance}\n")

elif option == '2':
    print("\n--- Cálculo da Carga do Sistema ---")
    graph_data = read_graph_data()
    table_data = read_table_data()

    # Criação da matriz de desempenho
    performance_matrix = np.zeros((len(graph_data), len(graph_data)))
    for i, node in enumerate(graph_data):
        for j, neighbor in enumerate(graph_data):
            if neighbor in graph_data[node]:
                performance_matrix[i][j] = graph_data[node][neighbor]

    # Criação do vetor de demandas de serviço
    load_vector = np.zeros(len(graph_data))
    for i, node in enumerate(graph_data):
        if node in table_data:
            load_vector[i] = table_data[node]

    # Cálculo da carga do sistema
    load = markov_load(performance_matrix, load_vector)
    print(f"A carga do sistema é: {load}\n")

elif option == '0':
    print("Encerrando o programa...")
else:
    print("Opção inválida. Tente novamente.\n")
