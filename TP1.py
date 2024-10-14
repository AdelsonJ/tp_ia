import math
import random
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import sys

# Funcao que le o arquivo texto
def read_cities():
    with open("instancia.txt", 'r') as file:
        lines = file.readlines()
    
    num_cities = int(lines[0].strip())
    coordinates = []
    for i in range(1, num_cities + 1):
        x, y = map(float, lines[i].strip().split())
        coordinates.append((x, y))
    
    return num_cities, coordinates

# Funcao que calcula a distancia euclidiana entre duas posicoes
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cria um grafo com a distancia entre todas as posicoes
def build_graph(num_cities, coordinates):
    graph = [[0] * num_cities for _ in range(num_cities)]
    
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                graph[i][j] = calculate_distance(coordinates[i], coordinates[j])
    
    return graph

# Determina a distancia total entre as cidades
def fitness(path, graph):
    total_distance = 0
    num_cities = len(path)
    for i in range(num_cities):
        total_distance += graph[path[i]][path[(i + 1) % num_cities]]
    return total_distance

# Funcao de mutacao que troca duas cidades, aleatorias, entre si
def swap_mutation(path):
    idx1, idx2 = random.sample(range(len(path)), 2)
    path[idx1], path[idx2] = path[idx2], path[idx1]
    return path

# Classe que representa a particula 
class Particle:
    def __init__(self, path):
        self.position = path
        self.velocity = []
        self.best_position = list(path)
        self.best_score = float('inf')

# Funcao que inicializa as particulas
def initialize_particles(num_particles, num_cities):
    particles = []
    for _ in range(num_particles):
        path = list(range(num_cities))
        random.shuffle(path)
        particles.append(Particle(path))
    return particles

# Cria a valocidade baseado no pBest e gBest
def create_velocity(path1, path2):
    velocity = []
    temp_path = list(path1)
    # Se a posicao for diferente da procurada, inverte os index. Repete até estar igual
    for i in range(len(path1)):
        if temp_path[i] != path2[i]:
            swap_index = temp_path.index(path2[i])
            velocity.append((i, swap_index))
            temp_path[i], temp_path[swap_index] = temp_path[swap_index], temp_path[i]
    return velocity

# Aplica a velocidade e retorna o novo individuo
def apply_velocity(path, velocity):
    new_path = list(path)
    for (i, j) in velocity:
        new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

# Funcao que plota o grafo
def plot_graph(num_iterations, best_score):
    # Cria um vetor crescente do tamanho do numero de interacoes
    iterections = list(range(num_iterations))

    # Plota o grafico
    plt.plot(iterections, best_score,  linestyle='', marker='o', color='blue')
    plt.title('Caixeiro Viajante com PSO')
    plt.xlabel('Iteracoes')
    plt.ylabel('Melhor resultado')
    plt.grid(True)
    plt.legend()
    plt.show() 


# Funcao do PSO
def pso_tsp(graph, num_particles, num_iterations):
    # Inicializadores
    num_cities = len(graph)
    particles = initialize_particles(num_particles, num_cities)
    global_best_position = None
    global_best_score = float('inf')
    mutation_rate = 0.1
    gbs_array = []
    gbp_array = []
    
    # Executa o PSO de acordo com o numero de iteracoes
    for _ in range(num_iterations):
        # Analisa as particulas
        for particle in particles:
            score = fitness(particle.position, graph)
            # Atribui novo pBest ou gBest caso o novo resultado seja menor
            if score < particle.best_score:
                particle.best_score = score
                particle.best_position = list(particle.position)
            if score < global_best_score:
                global_best_score = score
                global_best_position = list(particle.position)
        gbs_array.append(global_best_score)
        gbp_array.append(global_best_position)
            
        # Usa as velocidades para atrubuir novos elementos
        for particle in particles:
            personal_velocity = create_velocity(particle.position, particle.best_position)
            global_velocity = create_velocity(particle.position, global_best_position)
            
            new_velocity = personal_velocity + global_velocity
            particle.velocity = new_velocity
            new_position = apply_velocity(particle.position, new_velocity)
            
            # Faz uma mutacao das particulas
            """ if random.random() < mutation_rate:
                new_position = swap_mutation(new_position) """
                
            particle.position = new_position
    
    return gbp_array, gbs_array

#  Configurações do PSO
num_particles = int(sys.argv[1])
num_iterations = int(sys.argv[2])
plot = int(sys.argv[3])

# Le a instancia no arquivo testo  e cria o grafo
num_cities, coordinates = read_cities()
graph = build_graph(num_cities, coordinates)

# Chama a funcao do PSO e guarda os melhores valores encontrados para em seguida imprimir
best_path, best_score = pso_tsp(graph, num_particles, num_iterations)
print("Melhor caminho encontrado:", best_path[-1])
print("Distância total:", best_score[-1])

with open('saida.txt', 'w') as arquivo:
    for score in best_score:
        arquivo.write(f"{score}\n")

if(plot):
    plot_graph(num_iterations, best_score)


