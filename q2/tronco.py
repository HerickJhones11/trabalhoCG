import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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


def plot_tronco(base, topo, height, ax, scale, angle, rotation_axis, translation):
    # Definir vértices do tronco de pirâmide
    vertices = np.array([
        [-base, -base, 0],  # Vértice 0
        [base, -base, 0],   # Vértice 1
        [base, base, 0],    # Vértice 2
        [-base, base, 0],   # Vértice 3
        [-topo, -topo, height],    # Vértice 4
        [topo, -topo, height],     # Vértice 5
        [topo, topo, height],      # Vértice 6
        [-topo, topo, height]      # Vértice 7
    ])

    translated_vertices = vertices + translation

    scale_matrix = np.diag(scale)
    scaled_vertices = np.dot(translated_vertices, scale_matrix)

    rotation_matrix = rotation_matrix_3d(rotation_axis, angle)
    rotated_vertices = np.dot(scaled_vertices, rotation_matrix)

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
        x = rotated_vertices[face, 0]
        y = rotated_vertices[face, 1]
        z = rotated_vertices[face, 2]
        ax.plot(x, y, z, color='green')






def tronco(ax):
    base = 2.0  # Comprimento da base inferior do tronco de pirâmide
    topo = 1.0     # Comprimento da base superior do tronco de pirâmide
    height = 3.0              # Altura do tronco de pirâmide
    scale = [1, 0.5, 0.25]
    angle = np.pi/3  # Ângulo de rotação (45 graus)
    rotation_axis = [1, 0, 0]  # Eixo de rotação (z-axis)
    translation = [-7, -5, 1]

    plot_tronco(base, topo, height, ax, scale, angle, rotation_axis, translation)
    return