import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_cubo(edge_length, ax, translation, angle, rotation_axis, scale):

    vertices = np.array([
        [0, 0, 0],
        [edge_length, 0, 0],
        [0, edge_length, 0],
        [edge_length, edge_length, 0],
        [0, 0, edge_length],
        [edge_length, 0, edge_length],
        [0, edge_length, edge_length],
        [edge_length, edge_length, edge_length]
    ])

    # Aplicar translação nos vértices

    scale_matrix = np.diag(scale)
    scaled_vertices = np.dot(vertices, scale_matrix)

    rotation_matrix = rotation_matrix_3d(rotation_axis, angle)
    rotated_vertices = np.dot(scaled_vertices, rotation_matrix)

    translated_vertices = rotated_vertices + translation


    # Definir as arestas do cubo
    edges = [
        [0, 1], [1, 3], [3, 2], [2, 0],
        [4, 5], [5, 7], [7, 6], [6, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    # Plotar as arestas do cubo
    for edge in edges:
        x = [translated_vertices[edge[0]][0], translated_vertices[edge[1]][0]]
        y = [translated_vertices[edge[0]][1], translated_vertices[edge[1]][1]]
        z = [translated_vertices[edge[0]][2], translated_vertices[edge[1]][2]]
        ax.plot(x, y, z, color='k')


# Função para criar a matriz de rotação 3D
def rotation_matrix_3d(axis, angle):
    x, y, z = axis
    c = np.cos(angle)
    s = np.sin(angle)
    C = 1 - c

    rotation_matrix = np.array([
        [x*x*C + c, x*y*C - z*s, x*z*C + y*s],
        [y*x*C + z*s, y*y*C + c, y*z*C - x*s],
        [x*z*C - y*s, y*z*C + x*s, z*z*C + c]
    ])

    return rotation_matrix


def cubo(ax):
    edge_length = 2.0
    translation = [6, -5, 1]
    angle = np.pi/4  # Ângulo de rotação (45 graus)
    rotation_axis = [0, 1, 1]  # Eixo de rotação (z-axis)
    scale = [2, 1, 0.5]
    plot_cubo(edge_length, ax, translation, angle, rotation_axis, scale)
