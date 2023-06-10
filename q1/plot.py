from matplotlib import pyplot as plt
import numpy as np


def plot_cone(center, radius, height, top_radius_ratio=0.5, num_slices=0, num_points=10):


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Coordenadas z dos círculos
    z = np.linspace(center[2], center[2] + height, num_slices)

    angle = np.pi/4
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                            [np.sin(angle), np.cos(angle), 0],
                            [0, 0, 1]])

    # Desenha os círculos em cada fatia
    for i in range(num_slices):
        theta = np.linspace(0, 2 * np.pi, num_points) # de 0 até 2pi
        r = radius * (1 - (i/num_slices) * (1 - top_radius_ratio))  # Reduz o raio para formar o cone com a tampa superior

        x = center[0] + r * np.cos(theta)
        y = center[1] + r * np.sin(theta)
        z_val = np.full_like(theta, z[i])  # Cria um array com o mesmo tamanho de theta com o valor de z correspondente
        ax.plot(x, y, z_val, color="blue")
        if i == 0:
            x_start = x
            y_start = y
            z_start = z_val
        if i == (num_slices - 1):
            x_end = x
            y_end = y
            z_end = z_val

    
    for i in range(0, len(x_start)):
        ax.plot([x_start[i], x_end[i]], [y_start[i], y_end[i]], [z_start[i], z_end[i]], color="blue")

        

    # Define os limites dos eixos x, y e z
    ax.set_xlim(center[0] - radius, center[0] + radius)
    ax.set_ylim(center[1] - radius, center[1] + radius)
    ax.set_zlim(center[2], center[2] + height)

    # Define os rótulos dos eixos
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    plt.title('Cone de Círculos')
    plt.grid(True)  # Ativa a grade de fundo
    plt.show()  # Mostra o gráfico

def plot_esfera(radius):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect("equal")

    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = radius * np.cos(u) * np.sin(v)
    y = radius * np.sin(u) * np.sin(v)
    z = radius * np.cos(v)
    ax.plot_surface(x, y, z, color="w", edgecolor="r")
    plt.show()

def plot_cubo(edge_length):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Definir os vértices do cubo
    vertices = [
        [0, 0, 0],
        [edge_length, 0, 0],
        [0, edge_length, 0],
        [edge_length, edge_length, 0],
        [0, 0, edge_length],
        [edge_length , 0, edge_length],
        [0, edge_length, edge_length],
        [edge_length, edge_length, edge_length]
    ]

    # Definir as arestas do cubo
    edges = [
        [0, 1], [1, 3], [3, 2], [2, 0],
        [4, 5], [5, 7], [7, 6], [6, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    # Plotar as arestas do cubo
    for edge in edges:
        x = [vertices[edge[0]][0], vertices[edge[1]][0]]
        y = [vertices[edge[0]][1], vertices[edge[1]][1]]
        z = [vertices[edge[0]][2], vertices[edge[1]][2]]
        ax.plot(x, y, z, color='k')

    # Definir limites dos eixos
    ax.set_xlim(0, edge_length)
    ax.set_ylim(0, edge_length)
    ax.set_zlim(0, edge_length)

    # Mostrar o gráfico
    plt.show()

def plot_tronco(base, topo, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Definir vértices do tronco de pirâmide
    vertices = np.array([
        [-base/2, -base/2, 0],  # Vértice 0
        [base/2, -base/2, 0],   # Vértice 1
        [base/2, base/2, 0],    # Vértice 2
        [-base/2, base/2, 0],   # Vértice 3
        [-topo/2, -topo/2, height],    # Vértice 4
        [topo/2, -topo/2, height],     # Vértice 5
        [topo/2, topo/2, height],      # Vértice 6
        [-topo/2, topo/2, height]      # Vértice 7
    ])

    # Definir faces do tronco de pirâmide
    faces = [
        [0, 1, 5, 4],  # Base inferior
        [1, 2, 6, 5],  # Lateral
        [2, 3, 7, 6],  # Base superior
        [3, 0, 4, 7],  # Lateral
        [4, 5, 6, 7]   # Lateral
    ]

    # Plotar as faces do tronco de pirâmide
    for face in faces:
        x = vertices[face, 0]
        y = vertices[face, 1]
        z = vertices[face, 2]
        ax.plot(x, y, z, color='k')

    # Definir limites dos eixos
    max_dim = max(base, topo, height)
    ax.set_xlim(-max_dim, max_dim)
    ax.set_ylim(-max_dim, max_dim)
    ax.set_zlim(0, height)

    # Mostrar o gráfico
    plt.show()


    # Mostrar o gráfico
    plt.show()
